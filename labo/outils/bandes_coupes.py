#!/usr/bin/env python3
"""Vérifier une rafale : pour chaque coupe détectée entre DEBUT et FIN, une bande de 6 images consécutives (3 avant, 3 après).
Usage : bandes_coupes.py DOSSIER DEBUT_s FIN_s sortie.jpg [coupes_par_page=40]   (lancer avec .venv/bin/python -I)
DOSSIER contient proxy.mp4 et coupes.json (passe globale). Une page JPEG par tranche de coupes (sortie-1.jpg, sortie-2.jpg…).
Étiquette de chaque bande : temps de la coupe, durée du plan qui suit, et « r » = différence à la coupe / médiane des
différences voisines dans la bande. Une vraie coupe donne r élevé (souvent > 4) ; un plan porté flou, un écran dans le champ
ou un stroboscope donnent r proche de 1 à 2. r n'est qu'un indice, souvent faux (session 10 : sur « Fou-Rire », trois fausses
coupes ont r de 24 à 31 ; sur Joker, les vraies coupes ont r < 1 parce que la coupe tombe une ou deux images à côté du trait rouge,
PySceneDetect datant la coupe à ±2 images) : trancher sur les images. Pour vérifier les plans de moins de 0,6 s que la passe globale
fusionne, écrire dans un dossier à part un coupes.json des seules coupes nouvelles (`scenedetect -m 1`) avec un lien vers proxy.mp4."""
import sys, json, subprocess, numpy as np
from PIL import Image, ImageDraw
dos, a, b, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
par_page = int(sys.argv[5]) if len(sys.argv) > 5 else 40
video = f"{dos}/proxy.mp4"
coupes = json.load(open(f"{dos}/coupes.json"))["coupes"]
sel = [i for i, t in enumerate(coupes) if a <= t <= b]
n_, d_ = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=r_frame_rate",
                         "-of", "default=nw=1:nk=1", video], capture_output=True, text=True).stdout.strip().split("/")
fps = float(n_) / float(d_ or 1)
W, H = 112, 63
t0 = max(0.0, a - 0.5)
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t0), "-t", str(b - t0 + 1.0), "-i", video,
                      "-vf", f"scale={W}:{H},format=rgb24", "-f", "rawvideo", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
g = fr.mean(3)
def bande(t):
    k = int(round((t - t0) * fps))
    idx = [min(max(j, 0), len(fr) - 1) for j in range(k - 3, k + 3)]
    d = [np.abs(g[idx[j]] - g[idx[j - 1]]).mean() for j in range(1, 6)]
    r = d[2] / max(max(d[0], d[1], d[3], d[4]), 3.0)   # plancher : images dupliquées (session 10)
    return idx, r, d[2]
cols = 2
rows_par_page = (par_page + cols - 1) // cols
lab = 14
pages = [sel[i:i + par_page] for i in range(0, len(sel), par_page)]
resume = []
for p, page in enumerate(pages, 1):
    nrows = (len(page) + cols - 1) // cols
    im = Image.new("RGB", (cols * (6 * W + 10), nrows * (H + lab)), (0, 0, 0))
    dr = ImageDraw.Draw(im)
    for n, i in enumerate(page):
        t = coupes[i]
        duree = (coupes[i + 1] - t) if i + 1 < len(coupes) else 0
        idx, r, dc = bande(t)
        resume.append((t, duree, r))
        x0, y0 = (n % cols) * (6 * W + 10), (n // cols) * (H + lab)
        dr.text((x0 + 2, y0 + 1), f"{int(t // 60)}:{t % 60:05.2f}  plan suivant {duree:.2f} s  d={dc:.0f} r={r:.1f}", fill=(255, 255, 0))
        for j, f in enumerate(idx):
            im.paste(Image.fromarray(fr[f]), (x0 + j * W, y0 + lab))
        dr.line([(x0 + 3 * W, y0 + lab), (x0 + 3 * W, y0 + lab + H)], fill=(255, 0, 0), width=1)
    nom = out.replace(".jpg", f"-{p}.jpg")
    im.save(nom, quality=80)
    print(nom)
faibles = [x for x in resume if x[2] < 2.5]
print(f"{len(resume)} coupes ; r < 2,5 (suspectes) : {len(faibles)} :", " ".join(f"{t:.2f}" for t, _, _ in faibles))
