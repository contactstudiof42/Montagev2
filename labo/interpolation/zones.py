"""PSNR restreint aux zones en mouvement (pixels où la vérité change entre i-1 et i+1), sur les images inventées,
hors coupe. Écrit aussi une planche : vérité / méthodes pour l'image i (ligne 1) et |erreur| x4 (ligne 2).
Usage : python3 zones.py <dossier> <i_planche> noms..."""
import sys, subprocess, numpy as np
from PIL import Image
R, ip, noms = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
W, H = 320, 180
lit = lambda f: np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                             capture_output=True).stdout, np.uint8).reshape(-1, H, W, 3).astype(float)
V = lit(f"{R}/verite60.mkv")
idx = [i for i in range(1, len(V) - 1, 2) if i not in (119,)]
mask = {i: (np.abs(V[i + 1] - V[i - 1]).max(2) > 10) for i in idx}
haut, bas = [V[ip]], [np.zeros_like(V[ip])]
for n in noms:
    X = lit(f"{R}/{n}.mkv")
    print(n, "images", len(X)); err = [((X[i] - V[i]) ** 2).mean(2)[mask[i]] for i in idx if i < len(X)]
    mse = np.concatenate(err).mean()
    print(n, "PSNR zones en mouvement", round(10 * np.log10(255 ** 2 / mse), 2), "dB ; part de l'image en mouvement",
          round(100 * np.mean([mask[i].mean() for i in idx]), 1), "%")
    haut.append(X[ip]); bas.append(np.clip(np.abs(X[ip] - V[ip]) * 4, 0, 255))
pl = np.concatenate([np.concatenate(haut, 1), np.concatenate(bas, 1)], 0).astype(np.uint8)
Image.fromarray(pl).resize((pl.shape[1] * 3 // 4, pl.shape[0] * 3 // 4)).save(f"planche-i{ip}.png", optimize=True)
