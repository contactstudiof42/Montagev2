"""Pièce 15 : erreur du ralenti interpolé (C) contre le ralenti vrai (D), images inventées seulement.
python3 mesure.py ralenti_interp.mkv ralenti_vrai.mkv planche.png"""
import sys, subprocess, numpy as np
from PIL import Image
def lire(p):
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    return np.frombuffer(r, np.uint8).reshape(-1, 180, 320, 3).astype(float)
c, d = lire(sys.argv[1]), lire(sys.argv[2]); n = min(len(c), len(d)); print("images", len(c), len(d))
Y = lambda a: a @ [0.299, 0.587, 0.114]
mvt = np.zeros((180, 320), bool)
for i in range(1, n): mvt |= np.abs(Y(d[i]) - Y(d[i - 1])) > 8
res = []
for i in range(n):
    if i % 3 == 0: continue
    e = (Y(c[i]) - Y(d[i]))[mvt]; mse = (e ** 2).mean()
    res.append((i, 10 * np.log10(255 ** 2 / mse) if mse > 0 else 99))
p = [r[1] for r in res]
print(f"zone en mouvement {100*mvt.mean():.1f} % ; PSNR images inventées : moyenne {np.mean(p):.1f} dB, pire {min(p):.1f} dB (image {res[int(np.argmin(p))][0]})")
w = res[int(np.argmin(p))][0]
err = np.clip(np.abs(c[w] - d[w]) * 4, 0, 255)
row = np.concatenate([d[w], c[w], err], 1).astype(np.uint8)
Image.fromarray(row).save(sys.argv[3]); print("planche", sys.argv[3], "image", w)
