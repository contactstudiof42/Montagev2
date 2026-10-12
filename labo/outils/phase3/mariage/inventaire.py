# inventaire.py : lit les XML Sony (sans ouvrir les médias) et écrit inventaire.json + .csv
import os, re, json, glob, sys
R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
OUT = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
rows = []
for cam in ["DIEGO", "QUENTIN", "ROMS 1", "ROMS 2"]:
    for mp4 in sorted(glob.glob(f"{R}/{cam}/**/*.MP4", recursive=True)):
        x = mp4[:-4] + "M01.XML"
        d = {"cam": cam, "fichier": os.path.relpath(mp4, R), "nom": os.path.basename(mp4)[:-4], "taille_go": round(os.path.getsize(mp4)/1e9, 2)}
        if os.path.exists(x):
            s = open(x, encoding="utf-8", errors="ignore").read()
            g = lambda p: (re.search(p, s) or [None, None])[1]
            d.update(images=int(g(r'<Duration value="(\d+)"') or 0), fps=g(r'captureFps="([^"]+)"'), format_fps=g(r'formatFps="([^"]+)"'),
                     date=g(r'<CreationDate value="([^"]+)"'), modele=g(r'modelName="([^"]+)"/>\s*<Lens') or g(r'<Device[^>]*modelName="([^"]+)"'),
                     objectif=g(r'<Lens modelName="([^"]+)"'), gamma=g(r'CaptureGammaEquation" value="([^"]+)"'),
                     gamut=g(r'CaptureColorPrimaries" value="([^"]+)"'), largeur=g(r'pixel="(\d+)"'), hauteur=g(r'numOfVerticalLine="(\d+)"'),
                     gyro="Gyroscope" in s, tc=g(r'LtcChange frameCount="0" value="(\d+)"'))
            fpsv = float(re.sub(r'[^0-9.]', '', d["format_fps"] or "50") or 50)
            d["duree_s"] = round(d["images"] / fpsv, 2)
        rows.append(d)
json.dump(rows, open(f"{OUT}/inventaire.json", "w"), indent=1, ensure_ascii=False)
import csv
keys = ["cam","nom","date","duree_s","images","fps","format_fps","largeur","hauteur","gamma","gamut","modele","objectif","gyro","taille_go","fichier"]
with open(f"{OUT}/inventaire.csv", "w", newline="") as f:
    w = csv.DictWriter(f, keys, extrasaction="ignore"); w.writeheader(); [w.writerow(r) for r in rows]
from collections import Counter
for cam in ["DIEGO","QUENTIN","ROMS 1","ROMS 2"]:
    rr = [r for r in rows if r["cam"]==cam]
    print(cam, len(rr), "clips", round(sum(r.get("duree_s",0) for r in rr)/60,1), "min",
          Counter((r.get("modele"),r.get("fps"),r.get("format_fps"),r.get("largeur"),r.get("hauteur"),r.get("gamma")) for r in rr).most_common(6),
          Counter(r.get("objectif") for r in rr).most_common(6), "gyro", sum(r.get("gyro",False) for r in rr),
          "de", min(r.get("date","") for r in rr), "à", max(r.get("date","") for r in rr))
