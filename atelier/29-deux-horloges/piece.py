#!/usr/bin/env python3
"""Pièce 29 « Deux horloges » (montage alterné à deux vitesses de temps, principe d'Interstellar).
usage : python3 piece.py v1|v2|v3 DOSSIER   → DOSSIER/VERSION.mp4 (+ .edl pour labo/outils/coupes.py)"""
import sys, os, subprocess, wave, numpy as np
from PIL import Image, ImageDraw
V, D = sys.argv[1], sys.argv[2]; os.makedirs(D, exist_ok=True)
W, H, FPS = 480, 270, 25
N = 350 if V in ('v4', 'v5') else 300


def decoupage(v):
    """liste de (ligne, nb d'images) ; ligne 'A' ici, 'B' là-bas."""
    if v == 'v1':
        return [('A' if i % 2 == 0 else 'B', 30) for i in range(10)]
    if v == 'v5':   # chaque retour à là-bas tombe sur un tic (tics à k×31,25 images)
        return [('A', 62), ('B', 22), ('A', 41), ('B', 20), ('A', 43), ('B', 18), ('A', 13), ('B', 14), ('A', 17), ('B', 12), ('A', 19), ('B', 69)]
    # v2 / v3 : les plans d'ici raccourcissent vers la chute, ceux de là-bas restent courts ; fin = B tenu
    a = [62, 44, 32, 24, 18, 14]; b = [22, 20, 18, 16, 14]
    seq = []
    for i in range(len(a)):
        seq.append(('A', a[i]))
        if i < len(b):
            seq.append(('B', b[i]))
    seq.append(('B', N - sum(n for _, n in seq)))
    return seq


def ici(t, f_chute):
    """t = image globale. Goutte qui grossit jusqu'à f_chute puis tombe. v4 : macro (recadrage ×3 sur le bec)."""
    im = ici_large(t, f_chute)
    return im.crop((160, 40, 320, 130)).resize((W, H), Image.BICUBIC) if V in ('v4', 'v5') else im


def ici_large(t, f_chute):
    im = Image.new('RGB', (W, H), (22, 30, 42)); d = ImageDraw.Draw(im)
    d.rectangle([180, 0, 300, 70], fill=(120, 128, 138)); d.rectangle([215, 70, 265, 96], fill=(140, 148, 158))
    d.line([180, 0, 180, 70], fill=(180, 190, 200), width=2)
    if t < f_chute:
        r = 4 + 15 * (t / f_chute) ** 1.4; cy = 96 + r * 0.9
        d.ellipse([240 - r, cy - r, 240 + r, cy + r * 1.15], fill=(150, 185, 215))
        d.ellipse([240 - r * 0.35, cy - r * 0.6, 240 - r * 0.05, cy - r * 0.25], fill=(230, 240, 250))
    else:
        k = t - f_chute; y = 120 + 0.5 * 2.2 * k * k                     # chute libre
        if y < H + 30:
            d.ellipse([233, y - 9, 247, y + 11], fill=(150, 185, 215))
    return im


def labas(saut, k, gel=None):
    """saut = combien de temps a passé (0..1, semaines → années) ; k = image dans le plan (dérive lente de la lumière)."""
    jour = 0.5 + 0.5 * np.cos(saut * 37.0)                                 # moment de la journée, change à chaque saut
    lum = 0.55 + 0.45 * jour
    mur = tuple(int(c * lum) for c in (176, 140, 100))
    im = Image.new('RGB', (W, H), mur); d = ImageDraw.Draw(im)
    d.rectangle([0, 200, W, H], fill=tuple(int(c * lum) for c in (110, 80, 58)))      # sol
    ciel = tuple(int(c * (0.25 + 0.75 * jour)) for c in (150, 190, 230))
    d.rectangle([300, 40, 420, 150], fill=ciel); d.rectangle([300, 40, 420, 150], outline=(70, 50, 36), width=6)
    d.line([360, 40, 360, 150], fill=(70, 50, 36), width=4)
    sx = 280 - 200 * jour + k * 0.4                                     # tache de soleil au sol, dérive à peine
    if jour > 0.3:
        d.polygon([(sx, 205), (sx + 110, 205), (sx + 140, 262), (sx + 25, 262)], fill=tuple(min(255, int(c * 1.25)) for c in (176, 140, 100)))
    # plante : pousse puis se fane (au-delà de 0,7)
    h = 20 + 120 * min(saut, 0.7) / 0.7; vert = (60, 130, 60) if saut < 0.7 else (120, 110, 50) if saut < 0.9 else (90, 70, 45)
    d.rectangle([90, 200, 130, 232], fill=(150, 80, 50)); d.line([110, 200, 110, 200 - h], fill=vert, width=4)
    for j in range(int(h // 18)):
        y = 196 - j * 18; s = -1 if j % 2 else 1
        d.ellipse([110 + s * 4 - (12 if s < 0 else 0), y - 6, 110 + s * 4 + (12 if s > 0 else 0), y + 2], fill=vert)
    # bâtons au mur : un par semaine, barrés par cinq
    n = int((saut if gel is None else gel) * 70)          # v4 : au dernier retour, plus personne ne compte
    for i in range(n):
        g, r = divmod(i, 5); col, ligne = g % 9, g // 9
        x0, y0 = 30 + col * 28, 30 + ligne * 26
        if r < 4:
            d.line([x0 + r * 5, y0, x0 + r * 5, y0 + 16], fill=(60, 40, 30), width=2)
        else:
            d.line([x0 - 2, y0 + 12, x0 + 19, y0 + 3], fill=(60, 40, 30), width=2)
    return im


seq = decoupage(V)
f_chute = sum(n for _, n in seq[:-1]) - 4 if V != 'v1' else 270      # la goutte tombe juste avant le dernier retour
nb_b = sum(1 for l, _ in seq if l == 'B')
proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                         '-i', '-', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', f'{D}/{V}-img.mp4'], stdin=subprocess.PIPE)
t, ib, coupes = 0, 0, []
for ligne, n in seq:
    if t:
        coupes.append(t)
    if ligne == 'B':
        ib += 1
        # v1 : sauts constants ; v2/v3 : sauts qui grandissent (le dernier retour = années)
        saut = ib / nb_b if V == 'v1' else (ib / nb_b) ** 2.2
        if ib == nb_b and V != 'v1':
            saut = 1.0
        else:
            prec = saut
    for k in range(n):
        gel = prec if (V in ('v4', 'v5') and ib == nb_b) else None
        im = ici(t, f_chute) if ligne == 'A' else labas(saut, k, gel)
        if ligne == 'B' and ib == nb_b and V != 'v1':                     # dernier retour : la pièce est vide, le soir tombe
            im = Image.eval(im, lambda c: int(c * max(0.55, 1 - k / 120)))
        proc.stdin.write(im.tobytes()); t += 1
proc.stdin.close(); proc.wait()

# son
SR = 48000; a = np.zeros(N * SR // FPS); rng = np.random.default_rng(1)
t0 = 0
for ligne, n in seq:
    s0, s1 = t0 * SR // FPS, (t0 + n) * SR // FPS
    tt = np.arange(s1 - s0) / SR
    if ligne == 'A':
        a[s0:s1] += 0.04 * np.sin(2 * np.pi * 55 * tt)                        # bourdonnement froid d'ici
    else:
        a[s0:s1] += 0.03 * np.convolve(rng.standard_normal(s1 - s0), np.ones(40) / 40, 'same') * 6   # air, dehors
    t0 += n
if V in ('v3', 'v4', 'v5'):
    fin = f_chute * SR // FPS
    for s in np.arange(0, fin, int(1.25 * SR)):                               # le tic d'ici, entendu partout
        L = int(0.03 * SR); e = np.exp(-np.arange(L) / (0.004 * SR))
        a[s:s + L] += 0.5 * e * np.sin(2 * np.pi * 1800 * np.arange(L) / SR)
    c = f_chute * SR // FPS; L = int(0.25 * SR)                               # la goutte : un « plic » sourd
    a[c + int(0.2 * SR): c + int(0.2 * SR) + L] += 0.3 * np.exp(-np.arange(L) / (0.03 * SR)) * np.sin(2 * np.pi * 700 * np.exp(-np.arange(L) / SR * 3) * np.arange(L) / SR)
    a[coupes[-1] * SR // FPS:] *= 0.0                                         # silence sur le dernier retour
    a[coupes[-1] * SR // FPS:] += 0.004 * rng.standard_normal(len(a) - coupes[-1] * SR // FPS)
a = np.clip(a, -1, 1)
w = wave.open(f'{D}/{V}.wav', 'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((a * 32767).astype(np.int16).tobytes()); w.close()
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{D}/{V}-img.mp4', '-i', f'{D}/{V}.wav', '-c:v', 'copy', '-c:a', 'aac', '-shortest', f'{D}/{V}.mp4'], check=True)
tc = lambda f: f'{f//FPS//3600:02d}:{f//FPS//60%60:02d}:{f//FPS%60:02d}:{f%FPS:02d}'
e, r = [], 0
for i, (l, n) in enumerate(seq):
    e.append(f'{i+1:03d}  {l}LIGNE  V     C        {tc(0)} {tc(n)} {tc(r)} {tc(r+n)}'); r += n
e.append(f'* LOC: {tc(f_chute)} RED chute')
open(f'{D}/{V}.edl', 'w').write('\n'.join(e) + '\n')
print(V, 'plans', [n for _, n in seq], 'coupes', coupes, 'chute', f_chute)
