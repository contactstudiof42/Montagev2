# fiches.py SORTIE.jpg NOM1 NOM2 ... : toutes les images clés (~1/s) de chaque rush, une ligne par rush (max 16 images, réparties)
import sys, os
from PIL import Image, ImageDraw
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/vignettes"; out, noms = sys.argv[1], sys.argv[2:]
W, H, N = 200, 112, 16; g = Image.new("RGB", (110 + N * (W + 2), len(noms) * (H + 2)), (20, 20, 20)); d = ImageDraw.Draw(g)
for j, n in enumerate(noms):
    v = f"{T}/{n}"; ks = sorted(f for f in os.listdir(v) if f.startswith("k_")); ts = [float(t) for t in open(f"{v}/temps.txt").read().split()]
    idx = sorted(set(round(i * (len(ks) - 1) / max(1, N - 1)) for i in range(N))) if len(ks) > N else range(len(ks))
    d.text((3, j * (H + 2) + 4), n.replace("20260604_", ""), fill=(255, 220, 80))
    for i, k in enumerate(idx):
        g.paste(Image.open(f"{v}/{ks[k]}").resize((W, H)), (110 + i * (W + 2), j * (H + 2)))
        if k < len(ts): d.text((110 + i * (W + 2) + 3, j * (H + 2) + H - 12), f"{ts[k]:.1f}", fill=(255, 255, 0))
g.save(out, quality=82); print(out, g.size)
