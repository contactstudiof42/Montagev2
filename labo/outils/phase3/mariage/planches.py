# planches.py DEBUT FIN [n=8] : planche de dérush (une ligne par rush, n images clés réparties), clips triés sur l'horloge du Zoom
# usage : planches.py 16:15 16:45  -> _travail/planches/p_1615-1645_XX.jpg (24 lignes par page)
import sys, json, os
from PIL import Image, ImageDraw
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
def sec(h): a, b = map(int, h.split(":")); return a*3600 + b*60 + (86400 if a < 12 else 0)
d0, d1 = sec(sys.argv[1]), sec(sys.argv[2]); n = int(sys.argv[3]) if len(sys.argv) > 3 else 8
r = [x for x in json.load(open(f"{T}/chrono.json")) if d0 <= x["t0"] < d1]
W, H, L = 192, 108, 150; rows = 24; os.makedirs(f"{T}/planches", exist_ok=True)
for p in range(0, len(r), rows):
    page = r[p:p+rows]; im = Image.new("RGB", (L + n*(W+2), len(page)*(H+2)), (20, 20, 20)); dr = ImageDraw.Draw(im)
    for j, x in enumerate(page):
        y = j*(H+2); v = f"{T}/vignettes/{x['nom']}"
        ks = sorted(f for f in os.listdir(v) if f.startswith("k_")) if os.path.isdir(v) else []
        try: ts = [float(t) for t in open(f"{v}/temps.txt").read().split()]
        except Exception: ts = []
        col = {"DIEGO": (255, 210, 80), "QUENTIN": (120, 200, 255)}.get(x["cam"], (255, 120, 200))
        dr.text((4, y+4), x["nom"].replace("20260604_", ""), fill=col); dr.text((4, y+20), f"{x['heure']}  {x['duree_s']:.0f}s", fill=(230, 230, 230))
        dr.text((4, y+36), (x.get("objectif") or "")[:22], fill=(150, 150, 150))
        if not ks: continue
        for i in range(n):
            k = round(i * (len(ks) - 1) / max(1, n - 1)) if len(ks) > 1 else 0
            t = Image.open(f"{v}/{ks[k]}").resize((W, H)); im.paste(t, (L + i*(W+2), y))
            if k < len(ts): dr.text((L + i*(W+2) + 3, y + H - 12), f"{ts[k]:.0f}s", fill=(255, 255, 0))
    out = f"{T}/planches/p_{sys.argv[1].replace(':','')}-{sys.argv[2].replace(':','')}_{p//rows+1:02d}.jpg"
    im.save(out, quality=80); print(out, len(page))
