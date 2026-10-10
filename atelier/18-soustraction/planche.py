"""Planche de la pièce 18 : python3 -I planche.py <dossier_rendus> <sortie.png> <ligne1> [<ligne2> ...]
Chaque ligne = liste de noms d'images séparés par des virgules (ex. e7,lf5,lf3,lf1).
Chaque vignette à 320 px (taille téléphone) ; imprime luminance moyenne et nombre de taches lumineuses
comptées à cette taille (seuil 200/255, composantes connexes) — ce qu'un œil peut compter au téléphone."""
import sys
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import label
d, out, lignes = sys.argv[1], sys.argv[2], [l.split(",") for l in sys.argv[3:]]
tw, th = 320, 180
pl = Image.new("RGB", (tw * max(map(len, lignes)), th * len(lignes)))
for r, ligne in enumerate(lignes):
    prec = None
    for c, nom in enumerate(ligne):
        im = Image.open(f"{d}/{nom}.png").convert("RGB").resize((tw, th), Image.LANCZOS)
        a = np.asarray(im).astype(float); y = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
        n = label(y > 200)[1]; m = y.mean()
        baisse = "" if prec is None else f" ({100 * (m - prec) / prec:+.0f} %)"
        print(f"{nom}: luminance {m:.1f}{baisse}, taches comptables à 320 px : {n}")
        prec = m
        ImageDraw.Draw(im).text((4, 4), f"{nom}  L={m:.0f}{baisse}  taches={n}", fill=(255, 255, 0))
        pl.paste(im, (c * tw, r * th))
pl.save(out, optimize=True)
