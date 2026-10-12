# planche_mariage.py SORTIE.jpg IMG1 IMG2 ... : grille 2 colonnes, 960 px de large par image, nom en haut
import sys
from PIL import Image, ImageDraw
out, fs = sys.argv[1], sys.argv[2:]; W = 960; ims = []
for f in fs:
    i = Image.open(f).convert("RGB"); ims.append(i.resize((W, int(W * i.height / i.width))))
H = max(i.height for i in ims); rows = (len(ims) + 1) // 2
g = Image.new("RGB", (2 * W + 6, rows * (H + 20)), (30, 30, 30)); d = ImageDraw.Draw(g)
for k, (f, i) in enumerate(zip(fs, ims)):
    x, y = (k % 2) * (W + 6), (k // 2) * (H + 20); g.paste(i, (x, y + 18)); d.text((x + 4, y + 3), f.split("/")[-1], fill=(255, 255, 0))
g.save(out, quality=88); print(out, g.size)
