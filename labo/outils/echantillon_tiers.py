#!/usr/bin/env python3
"""Échantillon pour juger À L'ŒIL où est le sujet dans le cadre (phase 2, Mad Max, session 3).
Tire au hasard (graine fixe) N images de milieu de plan (plans > 1,5 s), trace les tiers verticaux en vert,
et les range en mosaïque 6 colonnes. On compte ensuite à l'œil les images dont le sujet principal (visage,
corps, véhicule suivi) est dans le tiers central. Remplace centrage.py, dont la saillance ne trouve pas le sujet.
Usage : echantillon_tiers.py DOSSIER SORTIE.png [N=24] [graine=1]   (lancer avec .venv/bin/python -I)
Résultats (2026-10-11, N=24, graine 1) : Mad Max ≈ 20/24, Interstellar ≈ 12/24, Joker ≈ 8/24."""
import sys, json, subprocess, io, numpy as np
from PIL import Image, ImageDraw
D, out = sys.argv[1:3]; N = int(sys.argv[3]) if len(sys.argv) > 3 else 24; G = int(sys.argv[4]) if len(sys.argv) > 4 else 1
c = json.load(open(f'{D}/coupes.json'))['coupes']; rng = np.random.default_rng(G)
ts = sorted(rng.choice([(a + b) / 2 for a, b in zip(c[:-1], c[1:]) if b - a > 1.5], N, replace=False))
tiles = []
for t in ts:
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", f"{D}/proxy.mp4", "-frames:v", "1", "-vf", "scale=240:-2",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    im = Image.open(io.BytesIO(r)).convert('RGB'); d = ImageDraw.Draw(im)
    for k in (1, 2): d.line([k * im.width / 3, 0, k * im.width / 3, im.height], fill=(0, 255, 0))
    tiles.append(im)
w, h = tiles[0].size; M = Image.new('RGB', (w * 6, h * ((N + 5) // 6)))
for i, im in enumerate(tiles): M.paste(im, ((i % 6) * w, (i // 6) * h))
M.save(out); print(out, [round(t) for t in ts])
