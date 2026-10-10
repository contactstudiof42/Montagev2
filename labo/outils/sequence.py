#!/usr/bin/env python3
"""Planche d'une séquence d'un film (phase 2, passe fine) : une vignette par plan (image du milieu),
annotée (début, durée), sous-titre en cours sous la vignette, et en bas les durées de plans en barres
et la courbe LUFS court terme de la séquence. Lit DOSSIER/coupes.json, DOSSIER/ebur128.log, DOSSIER/proxy.mp4,
DOSSIER/st-en.srt (facultatif).
Usage : sequence.py DOSSIER DEBUT FIN SORTIE.png [colonnes=8] [largeur=200]   (DEBUT/FIN en h:mm:ss)
Variable LUFS=M pour la courbe momentanée (400 ms), utile pour comparer le son plan par plan.
PNG réduit en palette jusqu'à passer sous 500 000 octets."""
import sys, json, re, io, subprocess, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
D, a, b, out = sys.argv[1:5]; col = int(sys.argv[5]) if len(sys.argv) > 5 else 8; W0 = int(sys.argv[6]) if len(sys.argv) > 6 else 200
sec = lambda s: sum(float(x) * 60**i for i, x in enumerate(reversed(s.split(':'))))
hms = lambda t: f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:04.1f}"
A, B = sec(a), sec(b)
MOM = os.environ.get("LUFS", "S") == "M"   # LUFS=M : volume momentané (400 ms) au lieu du court terme (3 s)
F = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 11)
J = json.load(open(os.path.join(D, 'coupes.json'))); c = [0.0] + J['coupes'] + [J['stats']['duree']]
plans = [(s, e) for s, e in zip(c[:-1], c[1:]) if e > A and s < B]
st = []
if os.path.exists(os.path.join(D, 'st-en.srt')):
    for bl in open(os.path.join(D, 'st-en.srt'), encoding='utf-8', errors='replace').read().replace('\r', '').strip().split('\n\n'):
        l = bl.split('\n')
        if len(l) >= 3 and '-->' in l[1]:
            t0, t1 = [sec(x.replace(',', '.')) for x in l[1].split(' --> ')]; st.append((t0, t1, ' '.join(l[2:])))
def img(t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", os.path.join(D, 'proxy.mp4'), "-frames:v", "1",
                        "-vf", f"scale={W0}:-2", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(r)).convert('RGB')
vs = [img((max(s, A) + min(e, B)) / 2) for s, e in plans]
w, h = vs[0].size; HT = h + 30; rang = -(-len(vs) // col)
G = Image.new('RGB', (col * w, rang * HT + 150), (12, 12, 14)); d = ImageDraw.Draw(G)
for i, ((s, e), v) in enumerate(zip(plans, vs)):
    x, y = (i % col) * w, (i // col) * HT; G.paste(v, (x, y))
    d.text((x + 2, y + h + 1), f"{i+1}  {hms(s)}  {e-s:.1f}s", font=F, fill=(240, 220, 120))
    m = (s + e) / 2; txt = ' / '.join(t for t0, t1, t in st if t1 > s and t0 < e)
    d.text((x + 2, y + h + 15), txt[:int(w/5.5)], font=F, fill=(170, 170, 170))
# bas : durées + LUFS
y0 = rang * HT + 10; X = lambda t: 10 + (col * w - 20) * (t - A) / (B - A)
for s, e in plans:
    hh = 60 * min(e - s, 15) / 15; d.rectangle([X(max(s, A)) + 1, y0 + 60 - hh, X(min(e, B)) - 1, y0 + 60], fill=(230, 140, 60))
pts = []
for l in open(os.path.join(D, 'ebur128.log')):
    m = re.search(r't:\s*([\d.]+).*?M:\s*(-?[\d.]+)', l) if MOM else re.search(r't:\s*([\d.]+).*?S:\s*(-?[\d.]+)', l)
    if m and A <= float(m.group(1)) <= B: pts.append((X(float(m.group(1))), y0 + 135 - 65 * (min(max(float(m.group(2)), -50), -5) + 50) / 45))
if pts: d.line(pts, fill=(140, 220, 140))
d.text((10, y0 + 62), f"{a} → {b} · {len(plans)} plans · durée moyenne {np.mean([e-s for s,e in plans]):.2f} s · barres = durée (15 s max) · vert = LUFS {"M" if MOM else "S"} (-50..-5)", font=F, fill=(200, 200, 200))
n = 256
while True:
    buf = io.BytesIO(); (G if n > 256 else G.quantize(n)).save(buf, 'PNG', optimize=True)
    if buf.tell() < 500000 or n <= 16: break
    n = 128 if n == 256 else n // 2
open(out, 'wb').write(buf.getvalue()); print(out, buf.tell(), 'octets,', len(plans), 'plans')
