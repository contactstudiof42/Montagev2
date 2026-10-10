"""Pièce 20 « La lumière écrit » : python3 -I piece.py VERSION OUT.mp4  (VERSION = v1 | v2 | v3)
Foule synthétique 25 i/s dans le noir, strobe libre, coups retimés par saccade, noms révélés. 360×640, 10 s."""
import subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

V, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, N = 360, 640, 25, 250
BEAT = 60 / 128 * FPS                                    # 11,72 images par noire
rng = np.random.default_rng(7)
xs = np.arange(W)[None, :]; ys = np.arange(H)[:, None]
heads = [(rng.uniform(0, W), rng.uniform(330, 560), rng.uniform(16, 30), rng.uniform(0, 6.28)) for _ in range(16)]
NOMS = ["OKAPI SOUND", "LUNE VIVE", "DJ TARMAC", "FERRAILLE", "SOFIA K", "BRUME", "LES QUAIS", "NOVA ROUGE",
        "ATELIER 9", "MARIN B", "KHÔL", "PORT-SEC", "VELOURS", "ZONE 3", "HALOGÈNE", "CRISTAL"]
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)


def scene(n, lasers_t=None, strobe=None):
    """image linéaire de la salle à l'image n ; lasers_t : temps des lasers (pour les faire bouger à part)."""
    t = n / FPS; tl = t if lasers_t is None else lasers_t
    lit = (np.floor(t * 7.7 + 0.5 / FPS * 7.7) > np.floor(t * 7.7)) if strobe is None else strobe
    base = np.zeros((H, W, 3)) + [0.012, 0.006, 0.025]
    crowd = np.zeros((H, W), bool)
    for (x0, y0, r, ph) in heads:
        y = y0 - 28 * max(0, np.sin(t * 2 * np.pi * 128 / 60 + ph))
        crowd |= ((xs - x0) ** 2 + (ys - y) ** 2) < r ** 2
        crowd |= (np.abs(xs - x0) < r * 1.8) & (ys > y + r * 0.8)
        crowd |= (np.abs(xs - (x0 + r * 1.2)) < 5) & (ys > y - 60 * max(0, np.sin(t * 4 + ph))) & (ys < y + r)  # bras
    if lit:
        base = base + [0.9, 0.9, 0.95]
        base[crowd] = [0.18, 0.16, 0.17]                              # corps révélés : gris chaud, contrastés
    else:
        base[crowd] = base[crowd] * 0.3
    lasers = np.zeros((H, W))
    for k, ang0 in enumerate((0.3, 1.2, 2.1)):
        a = ang0 + 0.6 * np.sin(tl * 0.9 + k)
        d = np.abs((xs - W / 2) * np.cos(a) + (ys - 40) * np.sin(a))
        lasers += np.exp(-(d / 2.5) ** 2) * 0.5
    lasers[crowd] *= 0.1
    return base, lasers


def compo(base, lasers, nom=None, alpha=0.0, encre=None):
    img = base + lasers[..., None] * [0.1, 1.0, 0.35]
    img = (np.clip(img, 0, 1) ** (1 / 2.2) * 255).astype(np.uint8)
    if nom and alpha > 0:
        im = Image.fromarray(img); d = ImageDraw.Draw(im)
        x, y = nom[1]
        d.text((x, y), nom[0], font=FONT, fill=encre if encre else (int(255 * alpha),) * 3)
        img = np.array(im)
    return img


POS = [(30, 120), (150, 200), (40, 260), (120, 90), (60, 180), (170, 140), (30, 230), (110, 110)]
frames = []
if V == "v1":                                           # saccade automatique : une image sur 12, tout figé
    k_nom = 0; cur = None
    for n in range(N):
        if n % 12 == 0:
            b, l = scene(n); held = (b, l, b[0, 0, 0] > 0.5)
            if held[2]:
                cur = (NOMS[k_nom % 16], POS[k_nom % 8]); k_nom += 1
        b, l, lit = held
        frames.append(compo(b, l, cur, 1.0 if cur else 0))
else:                                                   # coups choisis sur les noires
    beats = [int(round(i * BEAT)) for i in range(int(N / BEAT) + 1)]
    for n in range(N):
        i = max(j for j, bt in enumerate(beats) if bt <= n)
        n0 = beats[i]; age = n - n0
        b, l = scene(n0, strobe=(age < 3))              # coup allumé tenu 3 images, puis la même pose dans le noir
        if V in ("v3", "v4"):
            _, l = scene(n)                              # les lasers continuent de bouger en continu
        nom = (NOMS[i % 16], POS[i % 8]) if i >= 1 else ("NUIT BASSE", (60, 150))
        alpha = 1.0 if age < 3 else max(0.0, 1 - (age - 3) / 9)   # le nom persiste et s'éteint en 9 images
        encre = None
        if V == "v4" and age < 3:
            encre = (20, 18, 22)                         # v4 : le nom en noir dans le coup (image rémanente : il s'inverse ensuite)
        frames.append(compo(b, l, nom, alpha, encre))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r",
                str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", OUT],
               input=np.stack(frames).tobytes(), check=True)
