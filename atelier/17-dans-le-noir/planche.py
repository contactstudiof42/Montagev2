"""Planche : 1 image par seconde (10 images, 5×2) + luminance moyenne. python3 planche.py dossier sortie.png"""
import sys, numpy as np
from PIL import Image, ImageDraw
d, out = sys.argv[1], sys.argv[2]; ims = []; lum = []
for k in range(10):
    im = Image.open(f"{d}/f_{1 + 12 * k:04d}.png").convert("RGB"); a = np.asarray(im, float) / 255
    lum.append(round(float((0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]).mean()), 3))
    t = im.resize((192, 108)); ImageDraw.Draw(t).text((4, 2), f"{k} s", fill=(255, 255, 160)); ims.append(t)
W = Image.new("RGB", (960, 216))
for k, t in enumerate(ims): W.paste(t, ((k % 5) * 192, (k // 5) * 108))
W.save(out, optimize=True); print("luminance moyenne par seconde :", lum)
