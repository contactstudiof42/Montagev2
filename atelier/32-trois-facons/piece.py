#!/usr/bin/env python3
"""Pièce 32 « Trois façons ». usage : python3 piece.py F|K DOSSIER"""
import sys, os, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
V, D = sys.argv[1], sys.argv[2]; os.makedirs(D, exist_ok=True)
W, H, FPS, SEG = 270, 480, 25, 75
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 54)

def ouverture(seg, k):
    """ouverture du tiroir (0 fermé, 1 ouvert) dans le segment seg (0..2), image k."""
    if k < 15: return 1.0
    t = k - 15
    if seg == 0: return max(0.0, 1 - t / 25)                                    # doucement, 1 s
    if seg == 1: return max(0.0, 1 - t / 4)                                     # coup de hanche, 4 images
    if t < 3: return 1 - t / 3                                                  # claqué en 3 images...
    return min(1.6, 1.6 * (1 - np.exp(-(t - 3) / 3)))                           # ...rebondit plus ouvert qu'avant

def image(seg, k):
    o = ouverture(seg, k)
    tremble = (3 * np.sin(k * 2.5) * np.exp(-(k - 19) / 6)) if seg >= 1 and k >= 19 else 0
    im = Image.new('RGB', (W, H), (226, 220, 206)); d = ImageDraw.Draw(im)
    d.rectangle([0, 360, W, H], fill=(150, 120, 95))                             # sol
    x0 = 55 + tremble; d.rectangle([x0, 200, x0 + 160, 362], fill=(120, 82, 52))   # commode
    d.rectangle([x0 + 10, 210, x0 + 150, 270], fill=(105, 70, 44)); d.rectangle([x0 + 70, 236, x0 + 90, 244], fill=(200, 180, 120))
    p = 60 * o                                                                   # tiroir du bas, il sort vers la caméra (vu de 3/4 : vers le bas)
    d.polygon([(x0 + 10, 290), (x0 + 150, 290), (x0 + 150 + p * 0.3, 290 + p * 0.5), (x0 + 10 + p * 0.3, 290 + p * 0.5)], fill=(160, 115, 75))
    d.rectangle([x0 + 10 + p * 0.3, 290 + p * 0.5, x0 + 150 + p * 0.3, 350 + p * 0.5], fill=(105, 70, 44))
    d.rectangle([x0 + 70 + p * 0.3, 316 + p * 0.5, x0 + 90 + p * 0.3, 324 + p * 0.5], fill=(200, 180, 120))
    if k < 12:                                                                    # carton : le numéro (signature)
        d.text((W / 2 - 16, 70), str(seg + 1), fill=(40, 40, 40), font=font)
    if V == 'K':                                                                  # découpage « dynamique » : autre axe par segment, punch-in sur l'impact
        z = (1.0, 1.35, 1.2)[seg]; cx = (135, 175, 110)[seg]; cy = (280, 310, 300)[seg]
        if 15 + (25 if seg == 0 else 3) <= k < 15 + (25 if seg == 0 else 3) + 10: z *= 1.5
        cw, ch = W / z, H / z
        im = im.crop((cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)).resize((W, H), Image.BICUBIC)
        if seg == 1: im = im.transpose(Image.FLIP_LEFT_RIGHT)                    # contrechamp
    return im

p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', f'{D}/{V}.mp4'], stdin=subprocess.PIPE)
for seg in range(3):
    for k in range(SEG):
        p.stdin.write(image(seg, k).tobytes())
p.stdin.close(); p.wait(); print(V, 'ok')
