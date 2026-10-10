"""Mesure à la coupe A|B : décalage horizontal par image (corrélation de phase) et indice de flou horizontal.
python3 mesure.py dossierA dossierB"""
import sys, glob, numpy as np
from PIL import Image
def lit(d): return [np.asarray(Image.open(f).convert("L"), float) for f in sorted(glob.glob(d + "/f_*.png"))]
def decalage(a, b):
    h = np.outer(np.hanning(a.shape[0]), np.hanning(a.shape[1])); a = (a - a.mean()) * h; b = (b - b.mean()) * h
    F = np.fft.fft2(a) * np.conj(np.fft.fft2(b)); r = np.fft.ifft2(F / (np.abs(F) + 1e-9)).real
    dy, dx = np.unravel_index(np.argmax(r), r.shape); dx = dx - a.shape[1] if dx > a.shape[1] // 2 else dx; return -dx
def flou(a): return np.abs(np.diff(a, axis=0)).mean() / (np.abs(np.diff(a, axis=1)).mean() + 1e-9)   # > 1 : flou horizontal
A, B = lit(sys.argv[1]), lit(sys.argv[2])
dA = [decalage(A[i], A[i + 1]) for i in range(len(A) - 4, len(A) - 1)]; dB = [decalage(B[i], B[i + 1]) for i in range(0, 3)]
print("décalage px/image  fin de A :", dA, " début de B :", dB)
print("flou horizontal par image (A 9-12 | B 1-3) :", " ".join("%.2f" % flou(x) for x in A[-4:]), "|", " ".join("%.2f" % flou(x) for x in B[:3]))
print("saut de vitesse à la coupe : %d px/image" % abs(dA[-1] - dB[0]))
