"""Le « pop » mot à mot (échelle 70 % -> 100 % en 120 ms, \\t par mot) fait-il glisser la ligne ? (session 14)
python3 -I ass_pop.py <dossier_sortie> [mode]  ; mode = ligne (un seul événement, mots centrés ensemble)
ou calques (un événement par mot, position \\pos calculée une fois sur la ligne finale, comme un monteur AE).
Mesure : bord gauche du premier mot, image par image : s'il bouge, toute la ligne « respire » à chaque mot."""
import sys, os, subprocess
import numpy as np
from PIL import Image, ImageFont
out = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else "ligne"; os.makedirs(out, exist_ok=True)
MOTS = ["Les", "vitrines", "me", "rendent", "un", "type", "que", "je"]; T = [0.5, 0.63, 0.97, 1.11, 1.53, 1.67, 1.99, 2.13]
ms = lambda t: round(t * 1000)
tete = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Vers,Inter Medium,50,&H00FFFFFF,&HFF000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,2,40,40,700,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
if mode == "ligne":
    # chaque mot : transparent jusqu'à son temps, puis apparaît à 70 % et grandit à 100 % (temps relatifs au début, 0,40 s)
    txt = " ".join("{\\alpha&HFF&\\fscx70\\fscy70\\t(%d,%d,\\alpha&H00&)\\t(%d,%d,\\fscx100\\fscy100)}%s" % (
        ms(t - 0.4), ms(t - 0.4) + 1, ms(t - 0.4), ms(t - 0.4) + 120, m) for m, t in zip(MOTS, T))
    ev.append(f"Dialogue: 0,0:00:00.40,0:00:03.50,Vers,,0,0,0,,{txt}")
else:
    f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Medium.otf", 50); esp = f.getlength(" ")
    larg = [f.getlength(m) for m in MOTS]; x = (1080 - sum(larg) - esp * (len(MOTS) - 1)) / 2
    for m, t, w in zip(MOTS, T, larg):   # \an2 : point d'ancrage en bas au centre du mot, l'échelle part de ce point
        ev.append("Dialogue: 0,0:00:%05.2f,0:00:03.50,Vers,,0,0,0,,{\\an2\\pos(%.1f,1220)\\fscx70\\fscy70\\t(0,120,\\fscx100\\fscy100)}%s" % (t, x + w / 2, m))
        x += w + esp
open(f"{out}/pop.ass", "w").write(tete + "\n".join(ev) + "\n")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "color=black:s=1080x1920:r=25:d=3.4", "-vf", f"ass={out}/pop.ass", f"{out}/f%03d.png"], check=True)
bords = []
for i in range(13, 80):
    a = np.asarray(Image.open(f"{out}/f{i + 1:03d}.png").convert("L"))[1100:1300]; xs = np.flatnonzero((a > 128).any(axis=0))
    bords.append(int(xs[0]) if len(xs) else -1)
v = [b for b in bords if b >= 0]
print(mode, "bord gauche du 1er mot, images 13-79 :", sorted(set(v))[:12], f"... amplitude {max(v) - min(v)} px, {len(set(v))} positions")
