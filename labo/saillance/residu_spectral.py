"""Saillance par résidu spectral (Hou et Zhang, CVPR 2007, « Saliency Detection: A Spectral Residual Approach »).
Image réduite à 64 px de large, log-amplitude moins sa moyenne locale 3x3, reconstruction avec la phase, carré, flou gaussien.
Usage : python3 residu_spectral.py plan1.png plan3.png  -> position du pic de saillance du plan 1, saillance moyenne
dans la zone de l'anomalie (différence plan1/plan3) rapportée à la saillance moyenne de l'image, rang centile de la zone."""
import sys, json, numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter, gaussian_filter, zoom
def saillance(path, w=64):
    im = Image.open(path).convert("L"); W, H = im.size
    a = np.asarray(im.resize((w, round(w * H / W)), Image.BILINEAR), float)
    F = np.fft.fft2(a); L = np.log(np.abs(F) + 1e-9); P = np.angle(F)
    S = np.abs(np.fft.ifft2(np.exp((L - uniform_filter(L, 3, mode="nearest")) + 1j * P))) ** 2
    S = gaussian_filter(S, 2.5)  # sigma ~ 8 px à 64 px, comme dans l'article
    S = zoom(S, (H / S.shape[0], W / S.shape[1]), order=1)[:H, :W]
    mh, mw = int(0.06 * H), int(0.06 * W)  # bords : artefact de périodicité de la FFT, exclus
    S[:mh] = S[-mh:] = 0; S[:, :mw] = S[:, -mw:] = 0
    return S / S.max()
a = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float); b = np.asarray(Image.open(sys.argv[2]).convert("RGB"), float)
m = np.abs(a - b).max(2) > 10
S = saillance(sys.argv[1]); h, w = S.shape
py, px = np.unravel_index(np.argmax(S), S.shape); ys, xs = np.nonzero(m)
zone = S[m].mean(); interieur = S > 0
print(json.dumps({"pic": [int(px), int(py)], "dist_pic_anomalie_pct_diag": round(100 * np.hypot(xs.mean() - px, ys.mean() - py) / np.hypot(w, h), 1),
                  "saillance_zone_sur_moyenne": round(float(zone / S[interieur].mean()), 2),
                  "centile_zone": round(float((S[interieur] < zone).mean() * 100), 1)}))
