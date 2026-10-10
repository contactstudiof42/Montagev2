"""Pièce 20 v5 : structure de l'examen n°8 corrigée, avec son. python3 -I v5.py OUT_DIR
Coups sur noires pointées (17,6 images), trou d'une mesure, tête d'affiche tenue une mesure ; nom noir dans le coup puis
inversé ; bande son synthétique (kick 128 BPM, relais à chaque coup, impact sur la tête d'affiche, trou sans kick)."""
import os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.argv = [sys.argv[0], "v4", "/dev/null"] + sys.argv[1:]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "piece.py")).read().split("POS = [")[0])  # scène et compo
OUT = sys.argv[3]; os.makedirs(OUT, exist_ok=True)

V6 = "--v6" in sys.argv; NOM = "v6" if V6 else "v5"
BIG = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 54)
BAR = 4 * BEAT                                                   # 46,9 images
coups = [(0, "NUIT BASSE", (60, 150), FONT, 18)]
k = 0; f = BAR
while f < 3 * BAR - 1:                                           # mesures 2-3 : noires pointées
    coups.append((int(round(f)), NOMS[k + 1] if V6 else NOMS[k], [(30, 120), (150, 220), (40, 300), (120, 90), (60, 180), (170, 140)][k % 6], FONT, 15))
    k += 1; f += 1.5 * BEAT
TROU = (int(round(3 * BAR)), int(round(4 * BAR)))                # mesure 4 : noir total, lasers coupés
coups.append((int(round(4 * BAR)), "OKAPI\nSOUND", (40, 110), BIG, N))   # tête d'affiche : tenue jusqu'à la fin

frames = []
for n in range(N):
    c = max((c for c in coups if c[0] <= n), key=lambda c: c[0])
    age = n - c[0]
    lit_n = 8 if (V6 and c[1].startswith("OKAPI\n")) else 3          # v6 : coup de la tête d'affiche tenu 8 images (1 seul flash)
    b, _ = scene(c[0], strobe=(age < lit_n))
    _, l = scene(n)
    if TROU[0] <= n < TROU[1]:
        b = np.zeros_like(b) + [0.004, 0.002, 0.008]; l = l * 0
        frames.append(compo(b, l)); continue
    img = compo(b, l)
    alpha = 1.0 if age < 3 else max(0.0, 1 - max(0, age - c[4]) / 6)
    im = Image.fromarray(img); d = ImageDraw.Draw(im)
    d.multiline_text(c[2], c[1], font=c[3], fill=(20, 18, 22) if age < lit_n else (int(255 * alpha),) * 3)
    frames.append(np.array(im))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r",
                str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", os.path.join(OUT, NOM + "_muet.mp4")],
               input=np.stack(frames).tobytes(), check=True)

SR = 48000; L = N * SR // FPS; a = np.zeros(L); r = np.random.default_rng(3)
def at(fr): return int(round(fr * SR / FPS))                     # image → échantillon (R5)
for i in range(int(N / BEAT) + 1):                               # kick : sinus glissant 120 → 45 Hz
    s0 = at(i * BEAT)
    if TROU[0] <= i * BEAT < TROU[1] or s0 >= L: continue
    t = np.arange(int(0.25 * SR)) / SR
    kick = np.sin(2 * np.pi * np.cumsum(45 + 75 * np.exp(-t * 30)) / SR) * np.exp(-t * 9) * 0.8
    a[s0:s0 + len(kick)] += kick[:L - s0]
for j, c in enumerate(coups):                                    # relais : bruit 12-25 ms passe-haut, durée variée
    s0 = at(c[0]); d = int(SR * (0.012 + 0.013 * ((j * 7) % 5) / 4))
    nz = np.diff(r.standard_normal(d + 1)) * np.exp(-np.arange(d) / d * 4) * 0.25
    a[s0:s0 + d] += nz[:L - s0]
s0 = at(coups[-1][0]); t = np.arange(int(1.2 * SR)) / SR          # impact : sub 40 Hz + transitoire
a[s0:s0 + len(t)] += (np.sin(2 * np.pi * 40 * t) * np.exp(-t * 3) * 0.9 + r.standard_normal(len(t)) * np.exp(-t * 60) * 0.4)[:L - s0]
a[at(TROU[0] + 3 * BEAT):at(TROU[0] + 3 * BEAT) + 600] += np.diff(r.standard_normal(601)) * 0.2   # le relais seul dans le trou
pcm = (np.clip(a / np.abs(a).max() * 0.7, -1, 1) * 32767).astype("<i2").tobytes()
wav = os.path.join(OUT, NOM + ".raw"); open(wav, "wb").write(pcm)
mp4 = os.path.join(OUT, NOM + ".mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(OUT, NOM + "_muet.mp4"), "-f", "s16le", "-ar", str(SR), "-ac", "1",
                "-i", wav, "-af", "loudnorm=I=-14:TP=-3:LRA=11,aresample=48000", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-shortest", mp4], check=True)
print([c[0] for c in coups], TROU)
