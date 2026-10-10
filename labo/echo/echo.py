#!/usr/bin/env python3
"""Labo 88 : écho de poses (Marey) — l'écart entre deux fantômes, mesuré en
largeurs de tête, décide-t-il de la lecture (traînée / trajectoire / écho / foule) ?
Un marcheur filiforme blanc sur noir, 6 poses, écarts 0.2 0.5 1 2 4 largeurs de tête.
Mesures : recouvrement de deux poses voisines (IoU), nombre de composantes
connexes de l'image composite (≈ nombre de silhouettes qu'on peut compter).
Usage : python3 echo.py SORTIE.png"""
import math, sys, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

W, H, HEAD = 900, 280, 26
UNIFORME = "--uniforme" in sys.argv  # largeur de tête en px
N = 6

def pose(img, x, phase, alpha):
    d = ImageDraw.Draw(img)
    c = int(255 * alpha)
    y0 = 60
    d.ellipse([x - HEAD / 2, y0, x + HEAD / 2, y0 + HEAD], fill=c)
    hip = (x, y0 + 110)
    d.line([(x, y0 + HEAD), hip], fill=c, width=9)
    a = 0.6 * math.sin(phase)
    for s in (1, -1):  # jambes et bras en opposition de phase
        knee = (hip[0] + 40 * math.sin(s * a), hip[1] + 45)
        d.line([hip, knee, (knee[0] + 25 * math.sin(s * a) - 5, hip[1] + 90)], fill=c, width=8)
        sh = (x, y0 + HEAD + 15)
        d.line([sh, (sh[0] - 35 * math.sin(s * a), sh[1] + 55)], fill=c, width=7)

def masque(x, phase):
    m = Image.new("L", (W, H)); pose(m, x, phase, 1.0)
    return np.array(m) > 127

res, rows = {}, []
for ecart in (0.2, 0.5, 1, 2, 4):
    dx = ecart * HEAD
    x0 = W / 2 - dx * (N - 1) / 2
    img = Image.new("L", (W, H))
    comp = np.zeros((H, W), bool)
    for k in range(N):
        x, ph = x0 + k * dx, k * 0.9
        pose(img, x, ph, 0.8 if UNIFORME else 0.35 + 0.65 * (k + 1) / N)  # la dernière pose la plus claire
        comp |= masque(x, ph)
    a, b = masque(x0, 0), masque(x0 + dx, 0.9)
    iou = (a & b).sum() / (a | b).sum()
    ncomp = ndimage.label(comp)[1]
    res[ecart] = {"iou_voisins": round(float(iou), 2), "silhouettes_separees": int(ncomp)}
    rows.append((ecart, img, iou, ncomp))

fnt = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 18)
sheet = Image.new("L", (W, len(rows) * (H + 30)))
d = ImageDraw.Draw(sheet)
for i, (e, img, iou, n) in enumerate(rows):
    sheet.paste(img, (0, i * (H + 30) + 30))
    d.text((8, i * (H + 30) + 4), f"écart {e} tête  |  IoU voisins {iou:.2f}  |  composantes {n}", font=fnt, fill=200)
sheet.convert("RGB").save(sys.argv[1], optimize=True)
json.dump(res, open(sys.argv[1].replace(".png", ".json"), "w"), indent=1)
print(res)
