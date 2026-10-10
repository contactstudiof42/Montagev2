"""PSNR Y restreint aux zones en mouvement (pixels où la luma vraie change de > 10 entre les deux images d'origine qui
encadrent l'image inventée), images inventées hors coupe et hors 2k dernières ; planche PNG : ligne 1 vérité + méthodes
pour l'image i, ligne 2 |erreur| x 4. Adapté de labo/interpolation/zones.py.
Usage : python3 zones-reel.py <dossier> <k> <i_planche> <png_sortie> <i_coupe|-> noms..."""
import sys, subprocess, numpy as np
from PIL import Image, ImageDraw
R, k, ip, png, ic = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]; noms = sys.argv[6:]
ic = None if ic == "-" else int(ic); W, H = 320, 180
def lit(f, fmt):
    c = 3 if fmt == "rgb24" else 1
    b = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "rawvideo", "-pix_fmt", fmt, "-"], capture_output=True).stdout
    return np.frombuffer(b, np.uint8).reshape(-1, H, W, c).astype(np.float32)
V = lit(f"{R}/verite.mkv", "gray")[..., 0]
idx = [i for i in range(1, len(V) - 2 * k) if i % k and i != ic]
mask = {i: np.abs(V[(i // k + 1) * k] - V[(i // k) * k]) > 10 for i in idx}
VR = lit(f"{R}/verite.mkv", "rgb24"); haut, bas = [VR[ip]], [np.zeros_like(VR[ip])]
for n in noms:
    X = lit(f"{R}/{n}.mkv", "gray")[..., 0]
    mse = np.concatenate([((X[i] - V[i]) ** 2)[mask[i]] for i in idx]).mean()
    print(n, "PSNR Y zones en mouvement", round(10 * np.log10(255 ** 2 / mse), 2), "dB ; part en mouvement",
          round(100 * np.mean([mask[i].mean() for i in idx]), 1), "%")
    XR = lit(f"{R}/{n}.mkv", "rgb24"); haut.append(XR[ip]); bas.append(np.clip(np.abs(XR[ip] - VR[ip]) * 4, 0, 255))
pl = np.concatenate([np.concatenate(haut, 1), np.concatenate(bas, 1)], 0).astype(np.uint8)
im = Image.fromarray(pl); d = ImageDraw.Draw(im)
for j, t in enumerate(["verite"] + noms): d.text((j * W + 4, 2), t, fill=(255, 255, 0))
im = im.resize((im.width * 3 // 4, im.height * 3 // 4), Image.LANCZOS)
im.convert("P", palette=Image.ADAPTIVE, colors=128).save(png, optimize=True)
