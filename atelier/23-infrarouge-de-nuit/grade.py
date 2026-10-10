"""Pièce 23 — deux étalonnages d'une même image IR : python3 -I grade.py RENDUS_DIR OUT.png
surveillance : teinte verte, contraste dur, bruit vidéo coloré gros grain (bloc 2 px), vignette nulle.
neutre       : monochrome légèrement froid, courbe douce (noir protégé à ~6 %), grain fin mono, vignette légère."""
import sys, numpy as np
from PIL import Image, ImageDraw
R, OUT = sys.argv[1:3]
NOIR = 0.03 if "nuit3" in sys.argv else 0.06; rng = np.random.default_rng(1)


def surveillance(y):
    y = np.clip((y - 0.05) * 1.6, 0, 1)
    n = rng.normal(0, 0.07, (y.shape[0] // 2, y.shape[1] // 2, 3)).repeat(2, 0).repeat(2, 1)
    return np.clip(np.stack([y * 0.55, y * 1.0, y * 0.5], -1) + n * [0.6, 1, 0.6], 0, 1)


def neutre(y):
    y = NOIR + (0.96 - NOIR) * (y ** 0.85)                         # noir posé (6 % en v1-v2, 3 % en v3), pas de clip
    h, w = y.shape; yy, xx = np.mgrid[0:h, 0:w]; v = 1 - 0.25 * (((xx - w / 2) / w) ** 2 + ((yy - h / 2) / h) ** 2) * 2
    y = np.clip(y * v + rng.normal(0, 0.018, y.shape), 0, 1)
    return np.stack([y * 0.96, y * 0.98, y * 1.0], -1)


tiles = []
for m in sys.argv[3:] or ("axe", "decale"):
    y = np.asarray(Image.open(f"{R}/{m}.png").convert("L")).astype(float) / 255
    for f in (surveillance, neutre):
        im = Image.fromarray((f(y) * 255).astype(np.uint8)); ImageDraw.Draw(im).text((6, 4), f"{m} / {f.__name__}", fill=(255, 80, 80))
        tiles.append(im)
o = Image.new("RGB", (960, 270 * ((len(tiles) + 1) // 2)))
for k, t in enumerate(tiles): o.paste(t, ((k % 2) * 480, (k // 2) * 270))
o.quantize(128).save(OUT, optimize=True)   # planche < 500 Ko
