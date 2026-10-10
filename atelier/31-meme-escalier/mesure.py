#!/usr/bin/env python3
"""(Limite : la corrélation de contours n'a de sens qu'à cadre identique ; dès que la caméra bouge, juger à l'œil.)
Reconnaissance du lieu (corrélation des contours Sobel, normalisés) et transformation (Δ chroma a*b*, Δ L*) vs R1.
usage : python3 mesure.py DOSSIER R1 R2 ..."""
import sys, numpy as np
from PIL import Image
D, ref, autres = sys.argv[1], sys.argv[2], sys.argv[3:]
def charge(n):
    im = Image.open(f'{D}/{n}.png').convert('RGB')
    lab = np.asarray(im.convert('LAB')).copy()
    lab = np.dstack([lab[..., 0].astype(np.float32), lab[..., 1].view(np.int8).astype(np.float32), lab[..., 2].view(np.int8).astype(np.float32)])   # a*, b* signés
    g = lab[..., 0]
    gx = np.zeros_like(g); gy = np.zeros_like(g)
    gx[:, 1:-1] = g[:, 2:] - g[:, :-2]; gy[1:-1] = g[2:] - g[:-2]
    e = np.hypot(gx, gy); e = (e - e.mean()) / (e.std() + 1e-6)          # contours normalisés : insensibles au niveau
    return lab, e
L0, E0 = charge(ref)
for n in autres:
    L, E = charge(n)
    rec = float(np.mean(E0 * E))
    dab = float(np.mean(np.hypot(L[..., 1] - L0[..., 1], L[..., 2] - L0[..., 2])))
    dl = float(np.mean(L[..., 0]) - np.mean(L0[..., 0]))
    print(f'{n}: contours communs avec {ref} r={rec:.2f} ; Δchroma {dab:.1f} ; ΔL moyen {dl:+.1f} (0-255)')
