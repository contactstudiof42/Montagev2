# bande_rush.py SORTIE.jpg RUSH:DEBUT:FIN [RUSH:DEBUT:FIN ...] : vignettes (~1/s) des passages donnés, 10 par ligne, étiquetées.
import sys, os
from PIL import Image, ImageDraw, ImageFont
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/vignettes"
W, H, C = 256, 144, 10; font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
cases = []
for arg in sys.argv[2:]:
    n, a, b = arg.split(":"); a, b = float(a), float(b); v = f"{T}/{n}"
    ks = sorted(f for f in os.listdir(v) if f.startswith("k_")); ts = [float(t) for t in open(f"{v}/temps.txt").read().split()]
    sel = [(k, t) for k, t in zip(ks, ts) if a <= t <= b]
    for i in range(0, len(sel), C): cases.append([(f"{v}/{k}", f"{n.replace('20260604_','')} {t:.1f}") for k, t in sel[i:i+C]])
im = Image.new("RGB", (C*(W+2), len(cases)*(H+2)), (20, 20, 20)); dr = ImageDraw.Draw(im)
for j, l in enumerate(cases):
    for i, (f, lab) in enumerate(l):
        im.paste(Image.open(f).resize((W, H)), (i*(W+2), j*(H+2)))
        dr.rectangle([i*(W+2), j*(H+2), i*(W+2)+dr.textlength(lab, font=font)+6, j*(H+2)+18], fill=(0, 0, 0)); dr.text((i*(W+2)+3, j*(H+2)+1), lab, fill=(255, 220, 80), font=font)
im.save(sys.argv[1], quality=78); print(sys.argv[1], len(cases), "lignes")
