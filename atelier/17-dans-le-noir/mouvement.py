"""Centroïde horizontal de la zone éclairée, image par image (pas de 2) : on voit le bercement et son apaisement.
python3 mouvement.py dossier -> amplitude crête à crête par fenêtre de 2 s après l'allumage"""
import sys, glob, numpy as np
from PIL import Image
fs = sorted(glob.glob(sys.argv[1] + "/f_*.png")); xs = []; ts = []
for f in fs:
    n = int(f[-8:-4]);
    if n % 2 == 0: continue
    a = np.asarray(Image.open(f).convert("L"), float); m = a > 60
    if m.sum() < 20: continue
    ys, xx = np.nonzero(m); xs.append(xx.mean()); ts.append((n - 1) / 12)
xs, ts = np.array(xs), np.array(ts)
for t0 in (3.5, 5.5, 7.5):
    w = (ts >= t0) & (ts < t0 + 2)
    if w.any(): print(f"{t0:.1f}-{t0+2:.1f} s : centroïde x crête à crête = {np.ptp(xs[w]):.2f} px ; changements de sens = {int((np.diff(np.sign(np.diff(xs[w]))) != 0).sum())}")
