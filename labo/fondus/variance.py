#!/usr/bin/env python3
"""Labo fondus, méthode 2 (session 4) : écart au milieu + creux de variance, tolérants au mouvement.
Idée : au milieu d'un fondu de L images, l'image t ≈ moyenne des images t-h et t+h (h = L/2), alors que leurs
deux extrémités diffèrent beaucoup. Dans un plan qui bouge, la moyenne de t-h et t+h est un flou ≠ image t.
Et le mélange de deux images non corrélées a une variance spatiale plus faible que chacune (creux de variance).
  R(t,h) = |F_t - (F_{t-h}+F_{t+h})/2| / |F_{t-h} - F_{t+h}|   (petit = mélange)
Réglage retenu (session 4) : R < 0.3, |F_{t-h}-F_{t+h}| > 20, creux de variance DÉSACTIVÉ (hypothèse fausse, voir RESULTATS.md).
Usage : python3 variance.py <chaine.mp4>   (vérité terrain lue dans resultats.json de test_fondus.py)"""
import json, os, subprocess, sys
import numpy as np
FPS = 25; ICI = os.path.dirname(os.path.abspath(__file__))
raw = subprocess.run(["ffmpeg", "-i", sys.argv[1], "-vf", "scale=80:45,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, 45, 80).astype(float); N = len(F)
var = F.var(axis=(1, 2))
R_SEUIL, D_MIN, CREUX = float(os.environ.get("R", 0.3)), float(os.environ.get("DMIN", 20)), float(os.environ.get("CREUX", 1000))
hits = {}
for h in (3, 6, 12):   # demi-longueurs testées : fondus de ~6, ~12, ~24 images
    for t in range(h, N - h):
        a, b, m = F[t - h], F[t + h], F[t]
        den = np.abs(a - b).mean()
        if den < D_MIN: continue                      # extrémités semblables : rien à mélanger (plan fixe)
        R = np.abs(m - (a + b) / 2).mean() / den
        creux = var[t] < CREUX * min(var[t - h], var[t + h])
        if R < R_SEUIL and creux:
            hits.setdefault(t, []).append(h)
# fondu au noir : luminance moyenne quasi nulle, encadrée de rampes (détecteur séparé : le milieu n'est pas un mélange)
lum = F.mean(axis=(1, 2))
for t in range(N):
    if lum[t] < 3 and (t == 0 or lum[t - 1] >= 3 or t + 1 == N or lum[t + 1] >= 3): hits.setdefault(t, []).append("noir")
# regrouper les images détectées en segments
segs, prev = [], None
for t in sorted(hits):
    if prev is not None and t - prev <= 2: segs[-1][1] = t
    else: segs.append([t, t])
    prev = t
det = [[round(a / FPS, 2), round(b / FPS, 2)] for a, b in segs]
V = json.load(open(os.path.join(ICI, "resultats.json")))["verite"]
def touche(seg, ver): return seg[0] <= ver[1] + 0.12 and seg[1] >= ver[0] - 0.12
trouves = [v for v in V["fondus"] if any(touche(s, v) for s in det)]
faux = [s for s in det if not any(touche(s, v) for v in V["fondus"])]
res = {"R_seuil": R_SEUIL, "creux": CREUX, "detections": det, "fondus_trouves": f"{len(trouves)}/{len(V['fondus'])}",
       "manques": [v for v in V["fondus"] if v not in trouves], "faux_positifs": faux}
print(json.dumps(res))
