#!/usr/bin/env python3
"""Mesures de la pièce 26 : événements / 2,5 s, activité visuelle (YDIF / s), loudness momentané (LUFS / s).

Usage : mesure.py RENDUS_DIR OUT_DIR v1 [v2 v3 ...]
Écrit OUT_DIR/mesures.png (une bande par version) et OUT_DIR/mesures.json, et OUT_DIR/VERSION-planche.png.
"""
import json, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

COMPTES = {"coupe", "punch", "sfx", "caption", "porte"}
R, O, VERS = sys.argv[1], sys.argv[2], sys.argv[3:]
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)


def ydif(mp4):
    out = subprocess.run(["ffmpeg", "-i", mp4, "-vf", "signalstats,metadata=print:key=lavfi.signalstats.YDIF",
                          "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
    v = [float(x) for x in re.findall(r"YDIF=([\d.]+)", out)]
    return [sum(v[i:i + 24]) / len(v[i:i + 24]) for i in range(0, len(v), 24)]


def lufs(mp4):
    out = subprocess.run(["ffmpeg", "-i", mp4, "-af", "ebur128", "-vn", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    m = [(float(t), float(x)) for t, x in re.findall(r"t:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)", out)]
    res = {}
    for t, x in m:
        res.setdefault(int(t), []).append(x)
    return [max(res[k]) if k in res else -70 for k in range(max(res) + 1)]


def planche(mp4, png):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp4, "-vf",
                    "fps=1/5,scale=160:90,tile=8x5", "-frames:v", "1", png], check=True)


res = {}
for v in VERS:
    mp4 = f"{R}/{v}.mp4"
    j = json.load(open(f"{R}/{v}-evenements.json"))
    ev = [(t, k) for ex in j for t, k in ex["evenements"]]
    rel = [t for t, k in ev if k == "relance"]
    duree = j[-1]["debut"] + j[-1]["duree"]
    bins = [0] * int(duree / 2.5 + 1)
    for t, k in ev:
        if k in COMPTES:
            bins[int(t / 2.5)] += 1
    yd, lu = ydif(mp4), lufs(mp4)
    # autour de chaque relance : événements dans les 3 s avant vs moyenne des 8 s après
    autour = []
    for r in rel:
        av = sum(1 for t, k in ev if k in COMPTES and r - 3 <= t < r + 0.5)
        ap = sum(1 for t, k in ev if k in COMPTES and r + 0.5 <= t < r + 8.5) * 3.5 / 8
        autour.append({"t": r, "ev_3s_avant": av, "ev_3s_apres_moy": round(ap, 2),
                       "ydif_avant": round(sum(yd[int(r) - 3:int(r) + 1]) / 4, 2),
                       "ydif_apres": round(sum(yd[int(r) + 1:int(r) + 9]) / 8, 2),
                       "lufs_max_avant": max(lu[int(r) - 3:int(r) + 1]),
                       "lufs_moy_apres": round(sum(lu[int(r) + 1:int(r) + 9]) / 8, 1)})
    par_ex = []
    for ex in j:
        a, d = int(ex["debut"]), ex["duree"]
        par_ex.append({"extrait": ex["extrait"], "ev_par_min": round(sum(1 for t, k in ex["evenements"] if k in COMPTES) * 60 / d, 1),
                       "ydif_moy": round(sum(yd[a:a + d]) / d, 2), "lufs_moy": round(sum(lu[a:a + d]) / d, 1),
                       "ydif_min_10s": round(min(sum(yd[i:i + 10]) / 10 for i in range(a, a + d - 9)), 2)})
    res[v] = {"relances": autour, "extraits": par_ex}
    planche(mp4, f"{O}/{v}-planche.png")
    res[v]["_bins"], res[v]["_yd"], res[v]["_lu"], res[v]["_rel"], res[v]["_ex"] = bins, yd, lu, rel, [e["debut"] for e in j]

# figure : une bande par version
BW, BH = 1000, 150
img = Image.new("RGB", (BW, BH * len(VERS) + 20), (250, 250, 250))
dr = ImageDraw.Draw(img)
for n, v in enumerate(VERS):
    y0 = n * BH + 10
    r = res[v]
    sx = (BW - 60) / (len(r["_yd"]) or 1)
    for e in r["_ex"]:
        dr.line([50 + e * sx, y0, 50 + e * sx, y0 + BH - 20], fill=(200, 200, 200))
    for i, b in enumerate(r["_bins"]):
        x = 50 + i * 2.5 * sx
        dr.rectangle([x, y0 + BH - 20 - b * 12, x + 2.5 * sx - 1, y0 + BH - 20], fill=(120, 140, 200))
    pts = [(50 + i * sx, y0 + BH - 20 - min(yd, 25) * 4.4) for i, yd in enumerate(r["_yd"])]
    dr.line(pts, fill=(30, 150, 60), width=2)
    pl = [(50 + i * sx, y0 + BH - 20 - (max(l, -50) + 50) * 2.2) for i, l in enumerate(r["_lu"])]
    dr.line(pl, fill=(200, 120, 20), width=1)
    for t in r["_rel"]:
        dr.line([50 + t * sx, y0, 50 + t * sx, y0 + BH - 20], fill=(220, 30, 30), width=2)
    dr.text((4, y0 + 4), v, font=FONT, fill=(0, 0, 0))
dr.text((50, BH * len(VERS) + 4), "barres : événements / 2,5 s · vert : YDIF / s · orange : LUFS momentané · rouge : relances",
        font=FONT, fill=(60, 60, 60))
img.save(f"{O}/mesures.png")
json.dump({v: {k: x for k, x in res[v].items() if not k.startswith("_")} for v in VERS},
          open(f"{O}/mesures.json", "w"), indent=1, ensure_ascii=False)
for v in VERS:
    print(v)
    for e in res[v]["extraits"]:
        print("  ", e)
    for a in res[v]["relances"]:
        print("   R", a)
