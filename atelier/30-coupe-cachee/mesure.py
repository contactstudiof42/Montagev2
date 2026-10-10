#!/usr/bin/env python3
"""Mesures de la pièce 30 : score scdet autour de la coupe, écart de raccord hors objet (avant/après le passage), planche.
usage : python3 mesure.py DOSSIER SORTIE.png A B C D"""
import sys, re, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
R, OUT, vs = sys.argv[1], sys.argv[2], sys.argv[3:]
W, H, COUPE = 270, 480, 62
IMS = [44, 52, 58, 61, 62, 64, 70, 80, 199]
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
def lire(v):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{R}/{v}.mp4', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
lignes = []
for v in vs:
    err = subprocess.run(['ffmpeg', '-i', f'{R}/{v}.mp4', '-vf', 'scdet=threshold=0', '-f', 'null', '-'], capture_output=True, text=True).stderr
    sc = {int(round(float(t) * 25)): float(s) for s, t in re.findall(r'lavfi\.scd\.score:\s*([\d.]+),\s*lavfi\.scd\.time:\s*([\d.]+)', err)}
    y = lire(v); m = np.ones((H, W), bool); m[200:345, 95:195] = False         # hors objet
    ecart = float(np.mean(np.abs(y[44] - y[80])[m]))
    temoin = float(np.mean(np.abs(y[20] - y[40])[m]))                       # même prise, 20 images d'écart : bruit + trotteuse
    zone = np.abs(y[44] - y[80]) * m; ys, xs = np.where(zone > 12)
    print(f'{v}: scdet à la coupe {sc.get(COUPE, 0):.1f} (max hors coupe {max(v_ for k, v_ in sc.items() if abs(k - COUPE) > 1):.1f}) ; '
          f'écart hors objet avant/après {ecart:.2f} (témoin même prise {temoin:.2f}) ; pixels > 12 : {len(ys)}')
    L = Image.new('RGB', (len(IMS) * 92 + 30, 172), (20, 20, 20)); d = ImageDraw.Draw(L); d.text((4, 4), v, fill=(240, 240, 240), font=font)
    for i, f in enumerate(IMS):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{R}/{v}.mp4', '-vf', f"select='eq(n,{f})',scale=90:160", '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        L.paste(Image.frombytes('RGB', (90, 160), raw), (30 + i * 92, 2))
        d.text((32 + i * 92, 160), str(f), fill=(255, 255, 255) if f == COUPE else (150, 150, 150), font=font)
    lignes.append(L)
P = Image.new('RGB', (lignes[0].width, len(lignes) * 176)); [P.paste(l, (0, i * 176)) for i, l in enumerate(lignes)]; P.save(OUT, optimize=True)
