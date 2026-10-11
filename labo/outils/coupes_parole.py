#!/usr/bin/env python3
"""Où tombent les coupes par rapport à la parole (phase 2, Le Dîner de cons). Parole = énergie RMS sur 20 ms au-dessus
d'un seuil (percentile bas + marge), trous de moins de 150 ms bouchés. Pour chaque coupe : pendant la parole (coupe « sur
la phrase », réaction ou chevauchement) ou dans un silence ; dans ce cas, temps depuis la fin de la parole et jusqu'à la reprise.
Usage : coupes_parole.py DOSSIER DEBUT FIN [marge_dB=10]   (lit DOSSIER/audio16k.wav et DOSSIER/coupes.json ; .venv/bin/python -I)
Limite : musique et bruits comptent comme de la parole ; à réserver aux scènes de dialogue sans musique."""
import sys, json, os, numpy as np, wave
D, a, b = sys.argv[1:4]; marge = float(sys.argv[4]) if len(sys.argv) > 4 else 10
sec = lambda s: sum(float(x) * 60**i for i, x in enumerate(reversed(s.split(':'))))
A, B = sec(a), sec(b)
w = wave.open(os.path.join(D, 'audio16k.wav')); sr = w.getframerate(); w.setpos(int(A * sr))
y = np.frombuffer(w.readframes(int((B - A) * sr)), np.int16).astype(float)
h = int(0.02 * sr); n = len(y) // h; e = 20 * np.log10(np.sqrt((y[:n*h].reshape(n, h) ** 2).mean(1)) + 1e-6)
p = e > np.percentile(e, 20) + marge
k = 0
while k < n:                                   # boucher les trous < 150 ms
    if not p[k]:
        j = k
        while j < n and not p[j]: j += 1
        if j - k < 8 and k > 0 and j < n: p[k:j] = True
        k = j
    else: k += 1
c = [t - A for t in json.load(open(os.path.join(D, 'coupes.json')))['coupes'] if A < t < B]
pend, apres, avant = 0, [], []
for t in c:
    i = min(int(t / 0.02), n - 1)
    if p[i]: pend += 1; continue
    j = i
    while j > 0 and not p[j]: j -= 1
    k = i
    while k < n - 1 and not p[k]: k += 1
    apres.append((i - j) * 0.02); avant.append((k - i) * 0.02)
print(f"{a}-{b} : {len(c)} coupes ; parole {p.mean():.0%} du temps ; coupes pendant la parole : {pend/len(c):.0%}")
if apres:
    q = lambda v: ' / '.join(f'{x:.2f}' for x in np.percentile(v, [25, 50, 75]))
    print(f"  coupes dans un silence ({len(apres)}) : depuis la fin de la parole {q(apres)} s ; jusqu'à la reprise {q(avant)} s (quartiles)")
    print(f"  coupe avant le milieu du silence : {np.mean(np.array(apres) < np.array(avant)):.0%}")
