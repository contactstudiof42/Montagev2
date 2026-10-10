"""Pièce 12 : où est l'anomalie, quelle taille, est-elle dans la zone d'attention ?
Usage : python3 mesure.py L1.png L2.png
- aire du changement (% de l'image), boîte englobante
- différence hors zone (doit être ~0 : seul le détail change)
- saillance grossière : la zone la plus lumineuse/contrastée du plan 1 (fenêtre 48x27 px glissante)
  et la distance du changement à cette zone et au centre de l'image."""
import sys, json, numpy as np
from PIL import Image
a = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float) / 255
b = np.asarray(Image.open(sys.argv[2]).convert("RGB"), float) / 255
h, w, _ = a.shape
d = np.abs(a - b).max(2)
m = d > 0.04
ys, xs = np.nonzero(m)
box = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
cx, cy = xs.mean(), ys.mean()
# saillance : luminance locale x contraste local (écart type) sur fenêtres de 1/10 de l'image
L = a @ [0.2126, 0.7152, 0.0722]
bw, bh = w // 10, h // 10
best = None
for y in range(0, h - bh, bh // 3):
    for x in range(0, w - bw, bw // 3):
        p = L[y:y + bh, x:x + bw]; s = p.mean() * p.std()
        if best is None or s > best[0]:
            best = (s, x + bw / 2, y + bh / 2)
diag = (w * w + h * h) ** 0.5
r = {"aire_pct": round(100 * m.mean(), 3), "boite": box, "centre": [round(cx), round(cy)],
     "diff_hors_zone_max": round(float(d[~m].max()), 4),
     "zone_saillante": [round(best[1]), round(best[2])],
     "dist_saillance_pct_diag": round(100 * ((cx - best[1]) ** 2 + (cy - best[2]) ** 2) ** 0.5 / diag, 1),
     "dist_centre_pct_diag": round(100 * ((cx - w / 2) ** 2 + (cy - h / 2) ** 2) ** 0.5 / diag, 1)}
print(json.dumps(r))
