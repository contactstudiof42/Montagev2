#!/usr/bin/env python3
"""Détecteur de fondus enchaînés par linéarité : sur une fenêtre [a, b], si chaque image intérieure vaut
(1-α)·F[a] + α·F[b] avec α croissant de 0 à 1, c'est un fondu ; un mouvement ne se laisse pas décrire ainsi.
Usage : python3 linearite.py <video.mp4>"""
import json, subprocess, sys
import numpy as np
FPS = 25
TH = float(sys.argv[2]) if len(sys.argv) > 2 else 0.08
raw = subprocess.run(["ffmpeg", "-i", sys.argv[1], "-vf", "scale=80:45,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 45, 80).astype(float)
N = len(fr)
def score(a, b):
    A, B = fr[a].ravel(), fr[b].ravel(); D = B - A
    if np.abs(D).mean() < 8: return None, None          # extrémités trop semblables : pas une transition
    res, alphas = [], []
    for t in range(a + 1, b):
        al = np.clip(np.dot(fr[t].ravel() - A, D) / np.dot(D, D), 0, 1)
        res.append(np.abs(fr[t].ravel() - (A + al * D)).mean()); alphas.append(al)
    st = np.diff(alphas)
    L = len(alphas)
    # progressif : aucun saut > 2,5x le pas idéal (une coupe = un saut de 0 à 1 en une image)
    mono = np.all(st > -0.03) and alphas[0] < 0.35 and alphas[-1] > 0.65 and st.max() < max(0.25, 2.5 / (L + 1))
    # résidu rapporté à l'écart des extrémités : ~0 pour un fondu pur
    return (np.mean(res) / np.abs(D).mean()) if mono else None, alphas
trouves = []
for L in (6, 12, 25, 50):
    for a in range(0, N - L - 1):
        s, _ = score(a, a + L + 1)
        if s is not None and s < TH:
            trouves.append((a, a + L + 1, round(float(s), 3)))
# suppression des non-maxima : on garde la fenêtre au plus faible résidu, puis on écarte celles qui la recouvrent
trouves.sort(key=lambda x: x[2])
fus = []
for a, b, s in trouves:
    if all(b <= fa or a >= fb for fa, fb, _ in fus): fus.append((a, b, s))
fus.sort()
print(json.dumps([{"debut_s": round(a / FPS, 2), "fin_s": round(b / FPS, 2), "residu": s} for a, b, s in fus], indent=0))
