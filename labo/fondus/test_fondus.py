#!/usr/bin/env python3
"""Labo : scdet rate-t-il les fondus ? Détecteur de fondus par différence moyenne image à image sur fenêtre.
Vérité terrain fabriquée : coupes franches, fondus enchaînés de 12 et 25 images, fondu au noir, plan à mouvement rapide.
Usage : python3 test_fondus.py <dossier_rendus>"""
import json, os, subprocess, sys
import numpy as np
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
FPS, W, H = 25, 320, 180
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-1500:])
srcs = [f"mandelbrot=s={W}x{H}:rate={FPS}", f"testsrc2=s={W}x{H}:rate={FPS}",
        f"cellauto=s={W}x{H}:rate={FPS}:rule=30", f"gradients=s={W}x{H}:rate={FPS}:speed=0.05",
        # plan à mouvement rapide (piège à faux positifs) : mire qui défile vite
        f"testsrc=s={W}x{H}:rate={FPS},scroll=h=0.04", f"life=s={W}x{H}:rate={FPS}:mold=5", f"smptehdbars=s={W}x{H}:rate={FPS}"]
for i, s in enumerate(srcs):
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", s, "-t", "3", "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "18", f"{OUT}/s{i}.mp4"])
# chaîne composée image par image en numpy : vérité terrain exacte par construction
def charge(i):
    raw = subprocess.run(["ffmpeg", "-i", f"{OUT}/s{i}.mp4", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(float)
S = [charge(i) for i in range(7)]
# (plan, transition vers le suivant : ("coupe",0) / ("fondu",n) / ("noir",n))
PLAN = [(0, ("coupe", 0)), (1, ("fondu", 12)), (2, ("fondu", 25)), (3, ("coupe", 0)), (4, ("noir", 24)), (5, ("fondu", 6)), (6, None)]
out, VERITE = [], {"coupes": [], "fondus": []}
for k, (p, tr) in enumerate(PLAN):
    clip = list(S[p])
    if out and PLAN[k - 1][1][0] != "coupe":   # le début de ce plan a déjà été mélangé dans la transition
        clip = clip[PLAN[k - 1][1][1]:]
    if tr is None or tr[0] == "coupe":
        out += clip
        if tr: VERITE["coupes"].append(round(len(out) / FPS, 2))
        continue
    n = tr[1]; nxt = S[PLAN[k + 1][0]]
    out += clip[:-n]; t0 = len(out)
    for j in range(n):
        al = (j + 1) / (n + 1)
        if tr[0] == "fondu": out.append((1 - al) * clip[-n + j] + al * nxt[j])
        else:  # fondu au noir puis ouverture : première moitié vers le noir, seconde depuis le noir
            out.append(clip[-n + j] * max(0, 1 - 2 * al) if al < 0.5 else nxt[j] * (2 * al - 1))
    VERITE["fondus"].append([round(t0 / FPS, 2), round(len(out) / FPS, 2), tr[0]])
pipe = subprocess.Popen(["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                         "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "18", f"{OUT}/chaine.mp4"],
                        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
pipe.communicate(np.clip(np.array(out), 0, 255).astype(np.uint8).tobytes())
# 1) scdet à plusieurs seuils
res = {"verite": VERITE, "scdet": {}}
for th in [4, 8, 12, 20]:
    r = subprocess.run(["ffmpeg", "-i", f"{OUT}/chaine.mp4", "-vf", f"scdet=threshold={th}", "-f", "null", "-"], capture_output=True, text=True).stderr
    res["scdet"][th] = [float(l.split("lavfi.scd.time:")[1].split()[0]) for l in r.splitlines() if "lavfi.scd.time:" in l]
# 2) détecteur maison : différence absolue moyenne image à image (luma 80x45)
raw = subprocess.run(["ffmpeg", "-i", f"{OUT}/chaine.mp4", "-vf", "scale=80:45,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 45, 80).astype(float)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))           # d[i] = différence entre image i et i+1
lum = fr.mean(axis=(1, 2))
med = np.median(d)
# coupe : pic isolé (> 6x la médiane locale et > 3x les voisins) ; fondu : >= 4 images consécutives au-dessus de 2x la médiane globale
# avec une variation de luminance ou de différence monotone, sans pic isolé
coupes, fondus = [], []
for i in range(1, len(d) - 1):
    loc = np.median(d[max(0, i - 12):i + 12])
    if d[i] > 6 * loc and d[i] > 3 * max(d[i - 1], d[i + 1]):
        coupes.append(round((i + 1) / FPS, 2))
au = d > 2.0 * med
i = 0
while i < len(d):
    if au[i]:
        j = i
        while j < len(d) and au[j]: j += 1
        if j - i >= 4:
            seg = d[i:j]
            if seg.max() < 3 * np.median(seg):   # pas un pic isolé : variation étalée
                fondus.append([round(i / FPS, 2), round(j / FPS, 2)])
        i = j
    else: i += 1
res["maison"] = {"coupes": coupes, "fondus": fondus, "mediane_diff": round(float(med), 2)}
res["diff_par_image"] = [round(float(x), 1) for x in d]
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resultats.json"), "w"), indent=0)
print(json.dumps({k: v for k, v in res.items() if k != "diff_par_image"}, indent=1))
