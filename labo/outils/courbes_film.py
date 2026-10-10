#!/usr/bin/env python3
"""Courbes d'un film entier après passe_globale.sh (phase 2).
Usage : courbes_film.py DOSSIER [--titre T] [--marques "1:52:00=amarrage,..."]
Lit DOSSIER/*-Scenes.csv (PySceneDetect) et DOSSIER/ebur128.log.
Écrit DOSSIER/courbes.png (coupes par minute, durée médiane des plans par minute, LUFS court terme),
DOSSIER/coupes.json (temps des coupes, durées des plans, statistiques), et des planches de vignettes
DOSSIER/planche-XX.png (10 min chacune, une vignette / 10 s, 6 par ligne).
"""
import sys, csv, glob, json, re, os, argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser(); ap.add_argument('d'); ap.add_argument('--titre', default='')
ap.add_argument('--marques', default=''); a = ap.parse_args()
D = a.d
FONT = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 13)
PET = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 11)

def hms(t):
    t = int(t); return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}"

# coupes
f = glob.glob(os.path.join(D, '*-Scenes.csv'))[0]
rows = list(csv.reader(open(f)))
h = rows[1]; i0 = h.index('Start Time (seconds)'); i1 = h.index('End Time (seconds)')
plans = [(float(r[i0]), float(r[i1])) for r in rows[2:]]
duree = plans[-1][1]
coupes = [p[0] for p in plans[1:]]
L = np.array([e - s for s, e in plans])
# loudness
t, S = [], []
for ligne in open(os.path.join(D, 'ebur128.log')):
    m = re.search(r't:\s*([\d.]+).*?S:\s*(-?[\d.]+)', ligne)
    if m: t.append(float(m.group(1))); S.append(float(m.group(2)))
t, S = np.array(t), np.array(S)
integ = re.findall(r'I:\s+(-?[\d.]+) LUFS', open(os.path.join(D, 'ebur128.log')).read())
nmin = int(np.ceil(duree / 60))
cpm = np.histogram(coupes, bins=nmin, range=(0, nmin * 60))[0]
med = np.full(nmin, np.nan)
for k in range(nmin):
    sel = [e - s for s, e in plans if k * 60 <= (s + e) / 2 < (k + 1) * 60]
    if sel: med[k] = np.median(sel)
lufs_min = np.array([np.median(S[(t >= k*60) & (t < (k+1)*60)]) if np.any((t >= k*60) & (t < (k+1)*60)) else np.nan for k in range(nmin)])
stats = dict(duree=duree, plans=len(plans), asl=float(L.mean()), mediane=float(np.median(L)),
             lufs_integre=float(integ[-1]) if integ else None,
             histo={'<1': int((L<1).sum()), '1-2': int(((L>=1)&(L<2)).sum()), '2-4': int(((L>=2)&(L<4)).sum()),
                    '4-8': int(((L>=4)&(L<8)).sum()), '8-15': int(((L>=8)&(L<15)).sum()), '>=15': int((L>=15).sum())},
             plans_longs=[[hms(s), round(e-s, 1)] for s, e in plans if e - s >= 15])
json.dump(dict(stats=stats, coupes=coupes, cpm=cpm.tolist(), mediane_par_min=[None if np.isnan(x) else round(float(x),2) for x in med],
               lufs_par_min=[None if np.isnan(x) else round(float(x),1) for x in lufs_min]), open(os.path.join(D, 'coupes.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in stats.items() if k != 'plans_longs'}, indent=1), len(stats['plans_longs']), 'plans >= 15 s')

# graphique
W, H, G = 1800, 560, 60
img = Image.new('RGB', (W, H), (18, 18, 20)); dr = ImageDraw.Draw(img)
X = lambda s: G + (W - 2*G) * s / (nmin * 60)
dr.text((G, 8), f"{a.titre}  —  {len(plans)} plans, ASL {L.mean():.2f} s, médiane {np.median(L):.2f} s, {stats['lufs_integre']} LUFS intégrés", font=FONT, fill=(230,230,230))
# panneau 1 : coupes / min (barres)
y0, hh = 40, 170; mx = max(cpm.max(), 1)
dr.text((4, y0), f"coupes\n/min\n(max {mx})", font=PET, fill=(200,200,200))
for k, c in enumerate(cpm):
    dr.rectangle([X(k*60)+1, y0+hh - hh*c/mx, X((k+1)*60)-1, y0+hh], fill=(230,140,60))
# panneau 2 : médiane des plans (échelle log 0,5-30 s)
y1 = 230; hh2 = 130
dr.text((4, y1), "médiane\nplan (log)", font=PET, fill=(200,200,200))
for v in (1, 3, 10, 30):
    yy = y1 + hh2 - hh2 * (np.log(v) - np.log(0.5)) / (np.log(30) - np.log(0.5)); dr.line([G, yy, W-G, yy], fill=(50,50,55)); dr.text((G-22, yy-7), f"{v}s", font=PET, fill=(150,150,150))
for k, v in enumerate(med):
    if not np.isnan(v):
        yy = y1 + hh2 - hh2 * (np.log(min(max(v,.5),30)) - np.log(0.5)) / (np.log(30) - np.log(0.5))
        dr.rectangle([X(k*60)+1, yy-2, X((k+1)*60)-1, yy+2], fill=(120,190,240))
# panneau 3 : LUFS court terme (-50..-5)
y2 = 380; hh3 = 140
dr.text((4, y2), "LUFS S\n-50..-5", font=PET, fill=(200,200,200))
pts = [(X(tt), y2 + hh3 - hh3 * (min(max(s, -50), -5) + 50) / 45) for tt, s in zip(t[::10], S[::10])]
dr.line(pts, fill=(140,220,140), width=1)
for v in (-40, -30, -20, -10):
    yy = y2 + hh3 - hh3 * (v + 50) / 45; dr.line([G, yy, W-G, yy], fill=(50,50,55))
# graduations temps + marques
for m in range(0, nmin + 1, 10):
    dr.line([X(m*60), 36, X(m*60), H-30], fill=(70,70,75)); dr.text((X(m*60)-14, H-26), hms(m*60)[:-3], font=PET, fill=(180,180,180))
for mq in filter(None, a.marques.split(',')):
    tc, nom = mq.split('='); p = [int(x) for x in tc.split(':')]; s = p[0]*3600 + p[1]*60 + (p[2] if len(p) > 2 else 0)
    dr.line([X(s), 36, X(s), H-30], fill=(240,80,80)); dr.text((X(s)+3, 38), nom, font=PET, fill=(240,120,120))
img.save(os.path.join(D, 'courbes.png'), optimize=True)

# planches de vignettes (10 min chacune)
vig = sorted(glob.glob(os.path.join(D, 'vignettes', '*.jpg')))
if vig:
    w0, h0 = Image.open(vig[0]).size; col = 6
    for p in range(0, len(vig), 60):
        lot = vig[p:p+60]; rang = int(np.ceil(len(lot) / col))
        pl = Image.new('RGB', (col * w0, rang * (h0 + 14)), (0, 0, 0)); d2 = ImageDraw.Draw(pl)
        for j, v in enumerate(lot):
            x, y = (j % col) * w0, (j // col) * (h0 + 14)
            pl.paste(Image.open(v), (x, y)); d2.text((x + 2, y + h0), hms((p + j) * 10), font=PET, fill=(220,220,220))
        pl.save(os.path.join(D, f'planche-{p//60:02d}.jpg'), quality=80)
