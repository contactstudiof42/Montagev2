#!/usr/bin/env python3
"""Planche de spectrogrammes autour de coupes (session 8, OSS 117) : mixage à gauche, voix séparée à droite, ±0,6 s, trait blanc à la coupe,
0-4 kHz, chaque panneau normalisé (un panneau gris uniforme = silence amplifié). Sert à trancher à l'œil « pendant la parole / au bord / silence ».
Usage : spectro_coupes.py MIX.wav VOIX.wav coupes.json DEBUT_s FIN_s sortie.png [une coupe sur N=3]   (.venv/bin/python -I)"""
import sys, json, wave, numpy as np
from PIL import Image, ImageDraw
mixf, vocf, coupesf, A, B, out = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
pas = int(sys.argv[7]) if len(sys.argv) > 7 else 3
def lire(f):
    w = wave.open(f); sr = w.getframerate(); y = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float)
    if w.getnchannels() > 1: y = y.reshape(-1, w.getnchannels()).mean(1)
    return sr, y
srm, ym = lire(mixf); srv, yv = lire(vocf)
c = [t for t in json.load(open(coupesf))['coupes'] if A < t < B][::pas]
def spec(sr, y, t, W=0.6):
    a = int((t - W) * sr); s = y[a:a + int(2 * W * sr)]
    n = 512; h = 80; fr = [s[i:i + n] * np.hanning(n) for i in range(0, len(s) - n, h)]
    S = 20 * np.log10(np.abs(np.fft.rfft(fr, axis=1))[:, :int(4000 / (sr / n))] + 1e-3)
    S = np.clip((S - S.max() + 60) / 60, 0, 1)
    im = Image.fromarray((255 * S.T[::-1]).astype(np.uint8)).resize((300, 90))
    return im
rows = []
for i, t in enumerate(c):
    r = Image.new('L', (620, 200), 0); d = ImageDraw.Draw(r)
    r.paste(spec(srm, ym, t), (10, 15)); r.paste(spec(srv, yv, t), (310, 15))
    for x in (160, 460): d.line([(x, 15), (x, 105)], fill=255)
    d.text((10, 2), f"#{i} coupe {t:.2f} s  (gauche mix, droite voix)", fill=255)
    rows.append(r.crop((0, 0, 620, 110)))
cols = 2; H = (len(rows) + 1) // cols
P = Image.new('L', (620 * cols, 110 * H), 0)
for i, r in enumerate(rows): P.paste(r, ((i // H) * 620, (i % H) * 110))
P.save(out, optimize=True); print(len(c), [round(x, 2) for x in c])
