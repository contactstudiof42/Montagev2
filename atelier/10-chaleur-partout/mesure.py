"""Planche A/B/C + mesures : luminance moyenne, part de pixels chauds (R > B + 0,08) et froids (B > R + 0,08)."""
import json, sys
import numpy as np
from PIL import Image, ImageDraw
R = "/home/user/Montagev2/atelier/rendus/10"; vs = sys.argv[1:] or ["A", "B", "C"]
out, m = Image.new("RGB", (480 * len(vs), 290), (0, 0, 0)), {}
for i, v in enumerate(vs):
    im = Image.open(f"{R}/{v}/0001.png").convert("RGB"); a = np.asarray(im) / 255
    Y = a @ [.2126, .7152, .0722]
    m[v] = dict(luminance=round(float(Y.mean()), 3), chauds=round(float((a[..., 0] > a[..., 2] + .08).mean()), 3),
                froids=round(float((a[..., 2] > a[..., 0] + .08).mean()), 4))
    out.paste(im, (480 * i, 0)); ImageDraw.Draw(out).text((480 * i + 6, 274), f"{v} : {m[v]}", fill=(255, 255, 255))
out.save(f"planche-{''.join(vs)}.png"); json.dump(m, open(f"mesures-{''.join(vs)}.json", "w"), indent=1); print(m)
