#!/usr/bin/env python3
"""Courbe de couleur d'un film entier à partir des vignettes de passe_globale.sh (une toutes les 10 s).
Usage : couleur_film.py DOSSIER [--marques "1:52:00=nom,..."]
Mesure par vignette (barres noires exclues : lignes moyennes < 20) : luminance moyenne (0-255),
saturation moyenne (HSV), chaleur (R - B moyen), part de pixels « rouges saturés » (teinte < 15° ou > 340°,
S > 0,5, V > 0,25), part de pixels « verts » (teinte 70-170°, S > 0,15).
Sortie : DOSSIER/couleur.png (bande de couleur moyenne éclaircie + 4 courbes lissées sur 1 min) et
DOSSIER/couleur.json (valeurs par minute)."""
import sys, glob, os, json, argparse, numpy as np
from PIL import Image, ImageDraw, ImageFont
ap = argparse.ArgumentParser(); ap.add_argument('d'); ap.add_argument('--marques', default=''); a = ap.parse_args()
F = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 11)
vs = sorted(glob.glob(os.path.join(a.d, 'vignettes', '*.jpg')))
rows = []
for v in vs:
    im = np.asarray(Image.open(v).convert('RGB')).astype(float)
    act = im.mean((1, 2)) > 20
    if act.sum() < 5: rows.append(None); continue
    px = im[act].reshape(-1, 3) / 255
    hsv = np.asarray(Image.fromarray((px.reshape(1, -1, 3) * 255).astype(np.uint8)).convert('HSV')).reshape(-1, 3) / 255.
    h, s, vv = hsv[:, 0] * 360, hsv[:, 1], hsv[:, 2]
    rouge = ((h < 15) | (h > 340)) & (s > .5) & (vv > .25)
    vert = (h > 70) & (h < 170) & (s > .15)
    rows.append(dict(rgb=(px.mean(0) * 255).tolist(), Y=float(px.mean() * 255), S=float(s.mean()),
                     chaud=float((px[:, 0] - px[:, 2]).mean() * 255), rouge=float(rouge.mean()), vert=float(vert.mean())))
n = len(rows); nmin = -(-n // 6)
def parmin(k):
    out = []
    for m in range(nmin):
        x = [r[k] for r in rows[m*6:(m+1)*6] if r]
        out.append(float(np.mean(x)) if x else None)
    return out
J = {k: parmin(k) for k in ('Y', 'S', 'chaud', 'rouge', 'vert')}
json.dump(J, open(os.path.join(a.d, 'couleur.json'), 'w'))
W, G = 1800, 60; H = 470
img = Image.new('RGB', (W, H), (18, 18, 20)); d = ImageDraw.Draw(img)
X = lambda i: G + (W - 2*G) * i / n
for i, r in enumerate(rows):
    if r: d.rectangle([X(i), 10, X(i+1), 60], fill=tuple(int(min(255, c * 2.2)) for c in r['rgb']))
d.text((4, 30), 'couleur\n(×2,2)', font=F, fill=(200, 200, 200))
pans = [('Y', 'luminance', 0, 120, (230, 230, 230)), ('S', 'saturation', 0, .6, (120, 190, 240)),
        ('chaud', 'chaleur R-B', -20, 50, (240, 160, 80)), ('rouge', 'rouge saturé', 0, .15, (240, 70, 70)), ('vert', 'vert', 0, .8, (120, 220, 120))]
hh = 70; y = 70
for k, nom, lo, hi, col in pans:
    vals = J[k]; d.text((4, y + 20), nom, font=F, fill=col)
    pts = [(G + (W - 2*G) * m / nmin, y + hh - hh * (min(max(v, lo), hi) - lo) / (hi - lo)) for m, v in enumerate(vals) if v is not None]
    d.line(pts, fill=col, width=2); d.line([G, y + hh, W - G, y + hh], fill=(60, 60, 65)); y += hh + 8
for m in range(0, nmin + 1, 10):
    xx = G + (W - 2*G) * m / nmin; d.line([xx, 62, xx, H - 14], fill=(55, 55, 60)); d.text((xx - 10, H - 13), f"{m//60}:{m%60:02d}", font=F, fill=(180, 180, 180))
for mq in filter(None, a.marques.split(',')):
    tc, nom = mq.split('='); p = [int(x) for x in tc.split(':')]; s = p[0]*3600 + p[1]*60 + (p[2] if len(p) > 2 else 0)
    xx = G + (W - 2*G) * s / (nmin * 60); d.line([xx, 62, xx, H - 14], fill=(240, 80, 80)); d.text((xx + 3, 64), nom, font=F, fill=(240, 120, 120))
img.save(os.path.join(a.d, 'couleur.png'), optimize=True)
print('ok', n, 'vignettes')
