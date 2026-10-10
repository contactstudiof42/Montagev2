"""Pièce 20 v8 : écho (v7) + noires pointées + 20 noms hiérarchisés. python3 -I v8.py OUT_DIR [--uniforme]
20 s, 9:16, 25 i/s, 128 BPM. Structure par mesures (1 mesure = 46,9 images) :
  m1 coup-titre | m2-4 : 7 noms « niveau 2 » un par coup, tailles et places qui changent | m5-6 : 12 noms « niveau 3 »
  par paquets de 3 (colonne), 4 coups | m7 trou (noir total) | m8 tête d'affiche tenue 8 images | m9-10 carton-liste.
--uniforme : témoin, les 19 noms traités pareil (même taille, même place, un par coup), pour juger la hiérarchie."""
import os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.argv = [sys.argv[0], "v4", "/dev/null", "1"] + sys.argv[1:]   # piece.py lit argv[3] = SUB
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "piece.py")).read().split("POS = [")[0])  # scène et compo
OUT = sys.argv[4]; os.makedirs(OUT, exist_ok=True)
UNI = "--uniforme" in sys.argv
NOM = "v8-uniforme" if UNI else "v8"
N8 = 500
F = lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", s)
TETE = "OKAPI\nSOUND"
N2 = ["LUNE VIVE", "DJ TARMAC", "FERRAILLE", "SOFIA K", "NOVA ROUGE", "VELOURS", "HALOGÈNE"]
N3 = ["BRUME", "LES QUAIS", "ATELIER 9", "MARIN B", "KHÔL", "PORT-SEC", "ZONE 3", "CRISTAL", "ARGILE", "MÉTRO 12",
      "SAULE", "JADE O."]
tous = [TETE.replace("\n", " ")] + N2 + N3
assert len(tous) == 20 and len(set(tous)) == 20, "doublon dans les noms"        # leçon v5

BAR = 4 * BEAT
coups = [(0, "NUIT BASSE", (60, 150), F(30), 18)]                  # (image, texte, position, police, durée d'affichage)
if UNI:
    noms = N2 + N3; f = BAR
    for k, t in enumerate(noms):                                   # un nom par noire pointée, toujours pareil
        coups.append((int(round(f)), t, (40, 160), F(30), 12)); f += 1.5 * BEAT
    TROU = (int(round(f)), int(round(f + BAR)))
    coups.append((TROU[1], TETE, (40, 110), F(54), 9999))
else:
    places2 = [((30, 110), 44), ((140, 230), 30), ((24, 270), 38), ((110, 80), 30), ((20, 170), 46), ((170, 130), 30), ((40, 220), 40)]
    f = BAR
    for t, (p, s) in zip(N2, places2):                             # m2-4 : niveau 2, rupture de forme (taille et place)
        coups.append((int(round(f)), t, p, F(s), 12)); f += 1.5 * BEAT
    f = 4 * BAR
    for j in range(4):                                             # m5-6 : niveau 3, paquets de 3 en colonne
        coups.append((int(round(f)), "\n".join(N3[3 * j:3 * j + 3]), [(24, 90), (200, 120), (24, 160), (200, 80)][j], F(20), 12))
        f += 1.5 * BEAT
    TROU = (int(round(6 * BAR)), int(round(7 * BAR)))
    coups.append((TROU[1], TETE, (40, 110), F(54), 9999))
FIN_TETE = TROU[1] + 72                                             # tête d'affiche ~2,9 s puis carton-liste
cache = {}


def echo(n0, lit):
    """pose tenue avec écho : moyenne de 8 poses entières (SUB 1) = poses fantômes discrètes (v7)."""
    if (n0, lit) not in cache:
        cache[(n0, lit)] = np.mean([scene(n0 + j, strobe=lit)[0] for j in range(8)], axis=0)
    return cache[(n0, lit)]


frames = []
for n in range(N8):
    if n >= FIN_TETE:                                               # carton-liste : statique, sans flash (recherche du nom)
        im = Image.new("RGB", (W, H), (6, 4, 10)); d = ImageDraw.Draw(im)
        d.text((24, 60), "OKAPI SOUND", font=F(36), fill=(240, 240, 240))
        d.multiline_text((24, 120), "\n".join(N2), font=F(22), fill=(220, 220, 220), spacing=8)
        d.multiline_text((24, 360), "\n".join(N3[:6]), font=F(16), fill=(170, 170, 170), spacing=6)
        d.multiline_text((190, 360), "\n".join(N3[6:]), font=F(16), fill=(170, 170, 170), spacing=6)
        d.text((24, 580), "NUIT BASSE · 14-15 MARS", font=F(18), fill=(240, 240, 240))
        frames.append(np.array(im)); continue
    if TROU[0] <= n < TROU[1]:
        frames.append(compo(np.zeros((H, W, 3)) + [0.004, 0.002, 0.008], np.zeros((H, W)))); continue
    c = max((c for c in coups if c[0] <= n), key=lambda c: c[0])
    age = n - c[0]
    lit_n = 8 if c[1] == TETE else 3                                # sommet plus long, pas plus fort (leçon v6)
    b = echo(c[0], age < lit_n)
    _, l = scene(n)                                                 # les lasers continuent
    img = compo(b, l)
    alpha = 1.0 if age < lit_n else max(0.0, 1 - max(0, age - c[4]) / 6)
    im = Image.fromarray(img); d = ImageDraw.Draw(im)
    d.multiline_text(c[2], c[1], font=c[3], fill=(20, 18, 22) if age < lit_n else (int(255 * alpha),) * 3, spacing=6)
    frames.append(np.array(im))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r",
                str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", os.path.join(OUT, NOM + ".mp4")],
               input=np.stack(frames).tobytes(), check=True)
print(NOM, [c[0] for c in coups], TROU, FIN_TETE)
