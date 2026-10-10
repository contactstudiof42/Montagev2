"""Paroles mot à mot en ASS (libass via ffmpeg) : chaque mot apparaît-il à l'image prévue ? (session 14)
python3 -I ass_mot_a_mot.py <dossier_sortie> [cadence, ex. 25 ou 30000/1001]
Un vers de 8 mots, temps d'apparition volontairement hors de la grille des images (centisecondes ASS).
Mode : karaoké \\k avec SecondaryColour transparente = le mot est invisible avant son temps, plein après.
Mesure : sur chaque image rendue, on compte les mots visibles (projection des colonnes, mots séparés par
leurs blancs sur l'image finale) et on compare l'image d'apparition à ceil(t × cadence)."""
import sys, os, subprocess, math
from fractions import Fraction
import numpy as np
from PIL import Image
out = sys.argv[1]; fps = Fraction(sys.argv[2] if len(sys.argv) > 2 else "25"); os.makedirs(out, exist_ok=True)
MOTS = ["Les", "vitrines", "me", "rendent", "un", "type", "que", "je"]
DEBUTS = [0.50, 0.63, 0.97, 1.11, 1.53, 1.67, 1.99, 2.13]   # secondes ; 0,63 = 15,75 images à 25 i/s, etc.
FIN = 3.5
def cs(t): return round(t * 100)
ligne = "".join(("{\\k%d}" % (cs(DEBUTS[0]) - cs(0.40)) if i == 0 else "") + "{\\k%d}%s " % (
    (cs(DEBUTS[i + 1]) if i + 1 < len(MOTS) else cs(FIN)) - cs(DEBUTS[i]), m) for i, m in enumerate(MOTS))
# l'événement commence à 0,40 s ; le premier \k (vide) attend jusqu'au premier mot
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Vers,Inter Medium,50,&H00FFFFFF,&HFF000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,2,40,40,700,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.40,0:00:{FIN:05.2f},Vers,,0,0,0,,{ligne.strip()}
"""
open(f"{out}/vers.ass", "w").write(ass)
n = math.ceil(4 * fps)
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", f"color=black:s=1080x1920:r={fps}:d=4",
                "-vf", f"ass={out}/vers.ass", "-frames:v", str(n), f"{out}/f%03d.png"], check=True)
def colonnes(i):
    a = np.asarray(Image.open(f"{out}/f{i:03d}.png").convert("L"))[1100:1300]   # bande du vers (MarginV 700 en bas)
    return (a > 128).any(axis=0)
# segmentation des mots sur l'image la plus pleine (tous les mots visibles)
plein = colonnes(math.floor(3.0 * float(fps)) + 1); xs = np.flatnonzero(plein); segs, deb = [], xs[0]
for a, b in zip(xs[:-1], xs[1:]):
    if b - a > 12: segs.append((deb, a)); deb = b   # blanc > 12 px = espace entre mots (l'approche interne est < 12 px à 50 px de corps)
segs.append((deb, xs[-1])); assert len(segs) == len(MOTS), f"{len(segs)} segments pour {len(MOTS)} mots"
apparition = [None] * len(MOTS)
for i in range(1, n + 1):
    c = colonnes(i)
    for k, (a, b) in enumerate(segs):
        if apparition[k] is None and c[a:b + 1].any(): apparition[k] = i - 1   # image n° (0 = t=0)
ok = 0
for k, m in enumerate(MOTS):
    att = math.ceil(DEBUTS[k] * fps - Fraction(1, 10**6)); ecart = apparition[k] - att; ok += ecart == 0
    print(f"{m:10s} t={DEBUTS[k]:.2f}s  attendu image {att:3d}  vu image {apparition[k]:3d}  écart {ecart:+d}")
print(f"cadence {fps} : {ok}/{len(MOTS)} mots à l'image attendue")
