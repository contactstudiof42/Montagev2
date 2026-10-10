#!/usr/bin/env python3
"""Pièce 30 « Coupe cachée » (Short 9:16). usage : python3 piece.py A|B|C|D DOSSIER"""
import sys, os, subprocess, numpy as np
from PIL import Image, ImageDraw
V, D = sys.argv[1], sys.argv[2]; os.makedirs(D, exist_ok=True)
W, H, FPS, N = 270, 480, 25, 200
COUPE = 62                                   # image de coupe (milieu du passage du torchon)
large = V in ('A', 'G', 'H'); raccord = V in ('D', 'E'); torchon = V != 'B'


def scene(f, prise):
    """prise 1 = avant la coupe, prise 2 = après. f = image globale."""
    dl = 1.0 if (prise == 1 or raccord) else 1.06            # lumière qui a bougé entre les prises
    dx = 0 if (prise == 1 or raccord) else 2                  # pied de caméra effleuré
    # G : post = gain d'étalonnage qui rattrape la lumière de la prise 2 ; H : G + recadrage de 2 px (stabilisation)
    mur = tuple(int(c * dl) for c in (205, 196, 180))
    im = Image.new('RGB', (W + 8, H + 8), mur); d = ImageDraw.Draw(im)
    d.rectangle([150, 60, 250, 190], fill=tuple(min(255, int(c * dl)) for c in (215, 230, 245)), outline=(120, 100, 80), width=4)
    if not raccord:                                           # horloge murale à trotteuse
        cx, cy = 70, 110; d.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], fill=(245, 245, 240), outline=(40, 40, 40), width=3)
        s = f / FPS + (0 if prise == 1 else 37)               # la prise 2 est tournée 37 s plus tard
        a = 2 * np.pi * s / 60
        d.line([cx, cy, cx + 27 * np.sin(a), cy - 27 * np.cos(a)], fill=(200, 30, 30), width=2)
        d.line([cx, cy, cx + 15 * np.sin(0.6), cy - 15 * np.cos(0.6)], fill=(30, 30, 30), width=4)
    d.rectangle([0, 330, W + 8, H + 8], fill=(120, 84, 60))   # table
    if prise == 1:                                            # la tasse
        d.rectangle([110, 262, 160, 330], fill=(235, 235, 230)); d.arc([150, 275, 182, 310], -90, 90, fill=(235, 235, 230), width=7)
    else:                                                     # la plante
        d.polygon([(108, 330), (162, 330), (156, 290), (114, 290)], fill=(180, 90, 55))
        for ang, h in ((-0.5, 70), (0, 95), (0.45, 75), (-0.2, 55), (0.25, 60)):
            d.line([135, 290, 135 + h * np.sin(ang), 290 - h * np.cos(ang)], fill=(50, 130, 60), width=5)
            d.ellipse([135 + h * np.sin(ang) - 9, 290 - h * np.cos(ang) - 6, 135 + h * np.sin(ang) + 9, 290 - h * np.cos(ang) + 6], fill=(60, 150, 70))
    im = im.crop((4 + dx - (dx if V == 'H' else 0), 4, 4 + dx - (dx if V == 'H' else 0) + W, 4 + H))
    if prise == 2 and V in ('G', 'H'):
        im = Image.eval(im, lambda c: int(round(c / 1.06)))
    return im


def pose_torchon(im, f):
    """passage gauche → droite de COUPE-12 à COUPE+12 ; centré sur l'objet à COUPE."""
    k = (f - (COUPE - 12)) / 24
    if not torchon or not 0 <= k <= 1:
        return im
    lw = W * 1.4 if large else 120
    xc = -lw / 2 + k * (W + lw) if large else -60 + k * (W + 120) * 1.0
    if not large:                                             # centré sur la tasse (x=140) à la coupe
        xc = 140 + (k - 0.5) * (W + 160)
    d = ImageDraw.Draw(im)
    y0, y1 = (0, H) if large else ((150, 360) if V == 'E' else (200, 360))   # E : couvre l'union tasse + plante
    d.rectangle([xc - lw / 2, y0, xc + lw / 2, y1], fill=(60, 70, 110))
    for j in range(int(xc - lw / 2), int(xc + lw / 2), 14):
        d.line([j, y0, j, y1], fill=(75, 85, 128), width=3)
    return im


rng = np.random.default_rng(3)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', f'{D}/{V}.mp4'], stdin=subprocess.PIPE)
for f in range(N):
    im = pose_torchon(scene(f, 1 if f < COUPE else 2), f)
    a = np.asarray(im).astype(np.int16) + rng.normal(0, 3, (H, W, 1)).astype(np.int16)   # léger grain de capteur
    p.stdin.write(np.clip(a, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print(V, 'ok')
