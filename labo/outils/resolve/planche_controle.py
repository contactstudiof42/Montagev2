"""Planche des images de contrôle exportées par Resolve (ExportCurrentFrameAsStill).

Usage : planche_controle.py sortie.jpg image1.png image2.png ... [--largeur 480]
Chaque vignette porte le nom du fichier. Sortie JPEG légère, pour la regarder, pas pour juger la couleur fine.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

args = sys.argv[1:]
largeur = 480
if "--largeur" in args:
    i = args.index("--largeur")
    largeur = int(args[i + 1])
    del args[i:i + 2]
sortie, fichiers = args[0], args[1:]
vignettes = []
for f in fichiers:
    im = Image.open(f).convert("RGB")
    h = round(im.height * largeur / im.width)
    im = im.resize((largeur, h), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, largeur, 18], fill=(0, 0, 0))
    d.text((4, 3), Path(f).stem, fill=(255, 255, 0))
    vignettes.append(im)
cols = min(4, len(vignettes))
rows = (len(vignettes) + cols - 1) // cols
hmax = max(v.height for v in vignettes)
planche = Image.new("RGB", (cols * (largeur + 4), rows * (hmax + 4)), (40, 40, 40))
for k, v in enumerate(vignettes):
    planche.paste(v, ((k % cols) * (largeur + 4), (k // cols) * (hmax + 4)))
planche.save(sortie, quality=80)
print(sortie, planche.size)
