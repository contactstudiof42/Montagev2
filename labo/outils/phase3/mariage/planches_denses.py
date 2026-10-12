# planches_denses.py DEBUT FIN [pas=1] [prefixe] : toutes les vignettes (~1 image/s, ou une sur `pas`) des rushes d'une fenêtre,
# 10 par ligne, un rush commence toujours une nouvelle ligne ; étiquette = rush et seconde du rush. Pages de 14 lignes.
import sys, json, os
from PIL import Image, ImageDraw, ImageFont
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
def sec(h): a, b = map(int, h.split(":")); return a*3600 + b*60 + (86400 if a < 12 else 0)
d0, d1 = sec(sys.argv[1]), sec(sys.argv[2]); pas = int(sys.argv[3]) if len(sys.argv) > 3 else 1
pref = sys.argv[4] if len(sys.argv) > 4 else f"d_{sys.argv[1].replace(':','')}"
r = [x for x in json.load(open(f"{T}/chrono.json")) if d0 <= x["t0"] < d1]
W, H, C, RP = 256, 144, 10, 14
font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
lignes = []
for x in r:
    v = f"{T}/vignettes/{x['nom']}"
    if not os.path.isdir(v): continue
    ks = sorted(f for f in os.listdir(v) if f.startswith("k_"))[::pas]
    try: ts = [float(t) for t in open(f"{v}/temps.txt").read().split()][::pas]
    except Exception: ts = list(range(len(ks)))
    for i in range(0, len(ks), C):
        lignes.append([(f"{v}/{k}", f"{x['nom'].replace('20260604_','')} {ts[j] if j < len(ts) else 0:.0f}s {x['heure'] if i == 0 and j == 0 else ''}")
                       for j, k in list(enumerate(ks))[i:i+C]])
os.makedirs(f"{T}/denses", exist_ok=True)
for p in range(0, len(lignes), RP):
    page = lignes[p:p+RP]; im = Image.new("RGB", (C*(W+2), len(page)*(H+2)), (20, 20, 20)); dr = ImageDraw.Draw(im)
    for j, ligne in enumerate(page):
        for i, (f, lab) in enumerate(ligne):
            im.paste(Image.open(f).resize((W, H)), (i*(W+2), j*(H+2)))
            dr.rectangle([i*(W+2), j*(H+2), i*(W+2)+dr.textlength(lab, font=font)+6, j*(H+2)+18], fill=(0, 0, 0))
            dr.text((i*(W+2)+3, j*(H+2)+1), lab, fill=(255, 220, 80), font=font)
    out = f"{T}/denses/{pref}_{p//RP+1:02d}.jpg"; im.save(out, quality=78); print(out)
