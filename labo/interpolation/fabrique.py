"""Vérité terrain pour l'interpolation d'images (ralenti, conversion de cadence).
Scène synthétique à 60 i/s, 320x180, 4 s : fond texturé qui panote lentement, un disque texturé rapide (translation),
une barre qui tourne (mouvement non linéaire), un carré qui passe devant le disque (occlusion), une coupe franche à 2,0 s
(autre fond, autre couleur). Sorties : verite60.mkv (FFV1, sans perte) et source30.mkv (une image sur deux).
Usage : python3 fabrique.py <dossier> [bruit|lisse]
« bruit » : textures aléatoires (cas hostile, objets camouflés) ; « lisse » : fond flou, disque en dégradé radial (plus proche d'une image filmée)."""
import os, subprocess, sys, numpy as np
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
STYLE = sys.argv[2] if len(sys.argv) > 2 else "bruit"
W, H, N = 320, 180, 240
rng = np.random.default_rng(1)
def texture(seed, h, w):
    r = np.random.default_rng(seed).random((h // 4 + 2, w // 4 + 2, 3))
    return np.kron(r, np.ones((4, 4, 1)))[:h, :w] * 0.6 + 0.2
fondA, fondB = texture(2, H, W + 200), texture(3, H, W + 200) * [0.4, 0.7, 1.2]
disque = texture(4, 40, 40)
if STYLE == "lisse":
    from scipy.ndimage import gaussian_filter
    fondA = gaussian_filter(fondA, (6, 6, 0)); fondB = gaussian_filter(fondB, (6, 6, 0))
    fondA = (fondA - fondA.mean()) * 4 + 0.5; fondB = (fondB - fondB.mean()) * 4 + 0.45
    r = np.hypot(*np.mgrid[-20:20, -20:20]) / 20
    disque = np.stack([1 - 0.6 * r, 0.6 - 0.4 * r, 0.2 + 0 * r], 2); disque[18:22, :] = 0.05  # une bande sombre : un détail

yy, xx = np.mgrid[0:H, 0:W]
frames = np.zeros((N, H, W, 3), np.float32)
for i in range(N):
    t = i / 60
    fond = fondA if t < 2.0 else fondB
    off = int(round(20 * t))  # pano lent : 20 px/s
    im = fond[:, off:off + W].copy()
    cx, cy = (20 + 600 * (t % 2.0) / 2.0 * 0.5 + 300 * (t % 2.0) / 2.0) % W, 70  # disque : ~225 px/s
    m = (xx - cx) ** 2 + (yy - cy) ** 2 < 18 ** 2
    im[m] = disque[(yy[m] - cy + 20).astype(int) % 40, (xx[m] - cx + 20).astype(int) % 40]
    a = 2 * np.pi * 0.8 * t  # barre : 0,8 tour/s autour de (240,130)
    d = (xx - 240) * np.sin(a) - (yy - 130) * np.cos(a); l = (xx - 240) * np.cos(a) + (yy - 130) * np.sin(a)
    im[(abs(d) < 3) & (abs(l) < 35)] = [1, 0.9, 0.2]
    qx = int(W - (t % 2.0) * 160)  # carré qui passe devant le disque, en sens inverse
    im[45:100, max(qx - 25, 0):max(qx + 25, 0)] = [0.85, 0.15, 0.15]
    frames[i] = im
u8 = (np.clip(frames, 0, 1) * 255).astype(np.uint8)
def ecrit(arr, fps, nom):
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps),
                          "-i", "-", "-c:v", "ffv1", "-pix_fmt", "yuv444p", f"{out}/{nom}"], stdin=subprocess.PIPE)
    p.stdin.write(arr.tobytes()); p.stdin.close(); p.wait()
ecrit(u8, 60, "verite60.mkv"); ecrit(u8[::2], 30, "source30.mkv")  # même noms : un dossier par style; print("ok", N, "images")
