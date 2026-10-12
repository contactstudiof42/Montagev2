# fenetres_v4.py montage_V4.json : une « fenêtre » douce par plan (DA appel 4 : pas de vignettage uniforme, l'œil guidé vers les visages).
# Image de multiplication 1920x1080 : 1 sur les visages détectés (ellipse visage + haut du corps, bord très fondu), le reste baissé de
# `a` (N&B 0,30 ; jour 0,18 ; soir 0,28) ; sans visage, une ellipse centrale large. Extérieur de jour avec un ciel clair et peu saturé
# en haut du cadre : dégradé qui densifie le ciel (jusqu'à -22 %), sans le noircir.
# Sortie : _travail/fenetres_v4/f_<rec>.mov (ProRes Proxy, durée du plan) et fenetres.json {rec: fichier} ; aperçu PNG pour les planches.
import sys, json, os, subprocess, numpy as np
from PIL import Image, ImageFilter
J = json.load(open(sys.argv[1])); MD = os.path.dirname(os.path.abspath(sys.argv[1]))
C = json.load(open(f"{MD}/cdl_V4.json")); O = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/fenetres_v4"; os.makedirs(O, exist_ok=True)
CH = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/chrono.json"))}
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
W, H = 1920, 1080; yy, xx = np.mgrid[0:H, 0:W] / np.array([H, W])[:, None, None]
def heure(nom): return CH[nom]["t0"] % 86400
def ciel_clair(e):
    # haut du cadre clair et peu saturé sur l'image du milieu du rush (S-Log3 lu tel quel : un ciel couvert y est clair et neutre)
    t = max(0, e["src"]) + e["dur"] * e["vitesse"] / 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", f"/Volumes/SSD FAST/MARIAGE JO/RUSH/{INV[e['nom']]['fichier']}", "-frames:v", "1", "-vf", "scale=160:90", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(90, 160, 3).astype(float) / 255; top = a[:20]
    return top.mean() > 0.62 and (top.max(-1) - top.min(-1)).mean() < 0.08
# visages que le détecteur ne trouve pas (tête baissée, profil) : boîte posée à la main, vérifiée sur l'image (x, y, l, h en fraction)
MAIN = {"20260604_C3686|153.216": [[0.20, 0.10, 0.14, 0.30]]}
out = {}
for e in sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"]):
    c = C.get(f"{e['nom']}|{e['src']}", {}); boites = c.get("boites", []) or MAIN.get(f"{e['nom']}|{e['src']}", [])
    h = heure(e["nom"]); soir = h >= 21 * 3600 + 600 or h < 6 * 3600
    a = 0.30 if e["look"] == "V4_nb" else (0.28 if soir else 0.18)
    lum = np.zeros((H, W))
    if boites:
        for bx, by, bw, bh in boites:
            cx, cy = bx + bw / 2, by + bh * 0.9; rx, ry = max(bw * 2.2, 0.13), max(bh * 3.0, 0.26)
            lum = np.maximum(lum, np.clip(1 - (((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2), 0, 1))
    else:
        lum = np.clip(1 - (((xx - 0.5) / 0.55) ** 2 + ((yy - 0.52) / 0.62) ** 2), 0, 1)
    lum = np.asarray(Image.fromarray((lum * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(W * 0.06)), float) / 255
    lum = np.clip(lum * 1.6, 0, 1) ** 0.8
    m = 1 - a * (1 - lum)
    if e["look"] == "V4_couleur" and not soir and h < 18 * 3600 + 3600 and ciel_clair(e):
        m = m * (1 - 0.22 * np.clip((0.40 - yy) / 0.40, 0, 1) ** 1.2)
    import hashlib
    arr = (np.stack([m] * 3, -1) * 255).astype(np.uint8); n = max(1, round(e["dur"] * 25))
    hsh = hashlib.md5(arr.tobytes() + str(n).encode()).hexdigest()[:8]     # nom unique : Resolve garde en mémoire un fichier remplacé sous le même nom
    png = f"{O}/f_{e['rec']:07.2f}_{hsh}.png"; Image.fromarray(arr).save(png)
    mov = f"{O}/f_{e['rec']:07.2f}_{hsh}.mov"
    if os.path.exists(mov): out[f"{e['rec']:.3f}"] = {"mov": mov, "png": png, "a": a, "visages": len(boites)}; continue
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", png, "-frames:v", str(n + 2), "-r", "25", "-c:v", "prores_ks", "-profile:v", "0", "-pix_fmt", "yuv422p10le", mov], check=True)
    out[f"{e['rec']:.3f}"] = {"mov": mov, "png": png, "a": a, "visages": len(boites)}
    print(f"{e['rec']:7.2f} {e['nom']:16s} a={a:.2f} visages={len(boites)}", flush=True)
json.dump(out, open(f"{O}/fenetres.json", "w"), indent=1)
