"""Pièce 21 « L'objet qui change de rôle » : python3 -I piece.py VERSION VOIX.wav OUT.mp4   (VERSION = A | B | C)
Voix de synthèse (espeak-ng, fr, 150 mots/min) enregistrée AVANT l'animation (principe Kurzgesagt) ; débuts de phrases
mesurés par silencedetect (-40 dB, 0,25 s) : 0 ; 2,18 ; 3,59 ; 4,91 ; 6,37 s.
A : cinq illustrations séparées, coupe franche à chaque début de phrase (l'« explainer » à pictogrammes).
B : un seul cercle qui change de rôle (horloge → cadran de 24 h → nuit → reste → 3 h qui deviennent un écran),
    chaque transformation déclenchée au début de la phrase qui la nomme (principe Vox / Kurzgesagt).
C : même animation que B, mais les transformations tombent sur une grille fixe de 1,6 s (« sur le beat »), pas sur la voix.
640×360, 25 i/s, 9 s. Tout est dessiné (PIL), police DejaVu Sans Bold (licence libre)."""
import math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

V, VOIX, OUT = sys.argv[1:4]
V2 = "--v2" in sys.argv          # v2 : aiguilles au repos (sous le seuil de l'événement), « 13 h » nomme le reste après le départ des 3 h
W, H, FPS, N = 640, 360, 25, 225
FOND, NUIT, CHAUD, CLAIR, ECRAN = (14, 18, 38), (58, 72, 140), (255, 150, 40), (235, 235, 245), (90, 220, 255)
F = lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", s)
DEBUTS = [0, 2.18, 3.59, 4.91, 6.37]
if V == "C":
    DEBUTS = [0, 1.6, 3.2, 4.8, 6.4]                       # grille fixe
CX, CY, R = 250, 180, 110


def ease(u):
    u = min(1, max(0, u)); return u * u * (3 - 2 * u)


def k(t, i, d=0.45):
    """avancement (0→1) de la transformation i, déclenchée à DEBUTS[i], durée d."""
    return ease((t - DEBUTS[i]) / d)


def arc_pts(a0, a1, r, cx=CX, cy=CY, n=40):
    return [(cx + r * math.sin(a), cy - r * math.cos(a)) for a in np.linspace(a0, a1, n)]


def frame_B(t):
    im = Image.new("RGB", (W, H), FOND); d = ImageDraw.Draw(im)
    k1, k2, k3, k4 = (k(t, i) for i in range(1, 5))
    repos = 0.012 * math.sin(t * 2.1)                      # mouvement de repos : le cercle respire (±1,2 %)
    r = R * (1 + repos)
    # nuit : secteur 0 → 8/24, balayé pendant k1, s'efface pendant k3
    if k1 > 0 and k3 < 1:
        a1 = 2 * math.pi * 8 / 24 * k1
        col = tuple(int(c * (1 - k3) + f * k3) for c, f in zip(NUIT, FOND))
        d.polygon([(CX, CY)] + arc_pts(0, a1, r), fill=col)
    # reste : secteur 8/24 → 24/24, balayé pendant k2 ; ses 3 dernières heures partent pendant k4
    if k2 > 0:
        a0 = 2 * math.pi * 8 / 24; a1 = a0 + 2 * math.pi * 16 / 24 * k2
        a_cut = 2 * math.pi * 21 / 24
        d.polygon([(CX, CY)] + arc_pts(a0, min(a1, a_cut) if k4 > 0 else a1, r), fill=CHAUD)
        if a1 > a_cut and k4 < 1:                           # la part de 3 h, encore dans le cercle
            ox = 40 * k4; d.polygon([(CX + ox, CY)] + arc_pts(a_cut, a1, r, CX + ox), fill=CHAUD)
    # cadran : 12 graduations qui deviennent 24 (k1)
    for h in range(24):
        if h % 2 and k1 == 0: continue
        a = 2 * math.pi * h / 24; long = 12 if h % 2 == 0 else 7
        alpha = 1 if h % 2 == 0 else k1
        c = tuple(int(CLAIR[j] * alpha + FOND[j] * (1 - alpha)) for j in range(3))
        d.line([(CX + (r - long) * math.sin(a), CY - (r - long) * math.cos(a)), (CX + r * math.sin(a), CY - r * math.cos(a))], fill=c, width=3)
    d.ellipse([CX - r, CY - r, CX + r, CY + r], outline=CLAIR, width=4)
    # aiguilles : tournent doucement, disparaissent pendant k1
    if k1 < 1:
        c = tuple(int(CLAIR[j] * (1 - k1) + FOND[j] * k1) for j in range(3))
        for L, w, sp in (((0.55, 6, 0.02), (0.8, 4, 0.25)) if V2 else ((0.55, 6, 0.3), (0.8, 4, 3.6))):
            a = t * sp + 1.0
            d.line([(CX, CY), (CX + r * L * math.sin(a), CY - r * L * math.cos(a))], fill=c, width=w)
    # l'écran : la part de 3 h devient un téléphone à droite (k4)
    if k4 > 0:
        u = ease((t - DEBUTS[4] - 0.3) / 0.6)
        x0, y0 = 300 + 140 * u, 150 - 40 * u
        w, h = 60 + 40 * u, 60 + 120 * u
        d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=int(30 - 16 * u), fill=CHAUD if u < 0.5 else ECRAN)
        if u > 0.6: d.text((x0 + w / 2, y0 + h / 2), "3 h", font=F(28), fill=FOND, anchor="mm")
    lab = None
    if k2 > 0.5: lab = ("16 h", CHAUD)
    elif k1 > 0.5: lab = ("8 h", (150, 165, 230))
    elif t < DEBUTS[1]: lab = ("24 h", CLAIR)
    if V2 and k4 > 0.5:
        lab = ("13 h", CHAUD)
    if lab and (V2 or not (k4 > 0.5)): d.text((CX, CY + r + 26), lab[0], font=F(26), fill=lab[1], anchor="mm")
    return im


def frame_A(t):
    im = Image.new("RGB", (W, H), FOND); d = ImageDraw.Draw(im)
    i = max(j for j, s in enumerate(DEBUTS) if s <= t)
    if i == 0:                                              # horloge
        d.ellipse([CX - R, CY - R, CX + R, CY + R], outline=CLAIR, width=4)
        for h in range(12):
            a = 2 * math.pi * h / 12
            d.line([(CX + (R - 12) * math.sin(a), CY - (R - 12) * math.cos(a)), (CX + R * math.sin(a), CY - R * math.cos(a))], fill=CLAIR, width=3)
        d.line([(CX, CY), (CX + 50, CY - 30)], fill=CLAIR, width=6); d.line([(CX, CY), (CX - 20, CY - 85)], fill=CLAIR, width=4)
        d.text((CX, CY + R + 26), "24 h", font=F(26), fill=CLAIR, anchor="mm")
    elif i == 1:                                            # lune
        d.ellipse([CX - 80, CY - 80, CX + 80, CY + 80], fill=(150, 165, 230)); d.ellipse([CX - 40, CY - 100, CX + 110, CY + 50], fill=FOND)
        d.text((CX + 140, CY), "8 h", font=F(48), fill=(150, 165, 230), anchor="mm")
    elif i == 2:                                            # gros chiffre
        d.text((CX + 60, CY), "16 h", font=F(110), fill=CHAUD, anchor="mm")
    elif i == 3:                                            # 16 cases
        for j in range(16):
            x, y = 150 + (j % 8) * 46, 120 + (j // 8) * 70
            d.rounded_rectangle([x, y, x + 38, y + 58], radius=6, fill=CHAUD)
    else:                                                   # téléphone
        d.rounded_rectangle([CX - 50, CY - 95, CX + 50, CY + 95], radius=14, fill=ECRAN)
        d.text((CX, CY), "3 h", font=F(34), fill=FOND, anchor="mm")
    return im


frames = [np.array(frame_A(n / FPS) if V == "A" else frame_B(n / FPS)) for n in range(N)]
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                "-i", "-", "-i", VOIX, "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                "-af", "apad", "-t", str(N / FPS), OUT], input=np.stack(frames).tobytes(), check=True)
