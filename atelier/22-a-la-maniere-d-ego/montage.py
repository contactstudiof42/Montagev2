"""Pièce 22 — montage : python3 -I montage.py VERSION RENDUS_DIR VOIX_DIR OUT.mp4   (VERSION = A | B | B2 | B3)
Les images du recul (r000…r095, paramètre u régulier) sont reprises par une courbe temps → u propre à chaque version :
le même plan 3D, trois façons de le placer contre la voix.
A  : « explicatif » — voix continue, recul continu, chiffre affiché en grand, nappe musicale sans interruption.
B  : « à la manière d'EGO » — la voix s'arrête et la musique se coupe pendant le recul (3,5 s de vertige sans mots),
     le chiffre n'est que DIT, jamais écrit ; coupe sur la silhouette assise pour la dernière phrase.
B2 : B corrigé après critique (voir CRITIQUE.md).
Voix : espeak-ng fr, 135 mots/min, lignes l1…l6.wav. Musique : nappe synthétisée (ffmpeg aevalsrc), aucun média externe."""
import os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

V, R, VX, OUT = sys.argv[1:5]
FPS, W, H = 25, 480, 270
NR = len([f for f in os.listdir(R) if f.startswith("r")])
F = lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", s)
sm = lambda x: (lambda c: c * c * (3 - 2 * c))(min(1, max(0, x)))


def seg(t, pts):
    """interpolation lissée par morceaux de (temps, u)."""
    for (t0, u0), (t1, u1) in zip(pts, pts[1:]):
        if t0 <= t < t1: return u0 + (u1 - u0) * sm((t - t0) / (t1 - t0))
    return pts[-1][1]


if V == "A":
    VOIX = [0.3, 2.1, 3.6, 8.6, 11.9, 14.6]; DUR = 17.5; CUT = 14.4; MUS_TROU = None
    COURBE = [(0, 0), (1.5, 0), (14.4, 1)]
else:
    VOIX = [0.8, 3.0, 5.0, 10.4, 17.4, 21.2]; DUR = 25.0; CUT = 20.6; MUS_TROU = (13.6, 17.4)
    COURBE = [(0, 0), (4.5, 0), (10.0, 0.30), (13.6, 0.36), (17.2, 1.0)]
    if V == "B2":
        VOIX = [0.8, 3.0, 5.0, 10.4, 18.4, 22.2]; DUR = 26.0; CUT = 21.6; MUS_TROU = (13.6, 18.4)
        COURBE = [(0, 0), (4.5, 0), (10.0, 0.30), (13.6, 0.36), (18.0, 1.0)]
    if V == "B3":  # v3 : même placement que B2, mais la nappe MONTE pendant le recul (13,6 → 18,0) puis se coupe net
        VOIX = [0.8, 3.0, 5.0, 10.4, 18.4, 22.2]; DUR = 26.0; CUT = 21.6; MUS_TROU = None
        COURBE = [(0, 0), (4.5, 0), (10.0, 0.30), (13.6, 0.36), (18.0, 1.0)]

tmp = OUT + ".d"; os.makedirs(tmp, exist_ok=True)
final = Image.open(f"{R}/final.png").convert("RGB")
for i in range(int(DUR * FPS)):
    t = i / FPS
    if t >= CUT:
        im = final.copy()
    else:
        im = Image.open(f"{R}/r{round(seg(t, COURBE) * (NR - 1)):03d}.png").convert("RGB")
    if V == "A" and VOIX[4] <= t < CUT:                      # le chiffre écrit, à la manière d'un explicatif
        d = ImageDraw.Draw(im); a = sm((t - VOIX[4]) / 0.3)
        d.text((W / 2, H * 0.32), "117 000 000 000", font=F(40), fill=tuple(int(30 + 200 * (1 - a)) for _ in range(3)), anchor="mm")
    im.save(f"{tmp}/{i:04d}.png")

# bande son : voix posées aux temps VOIX, nappe (deux sinus graves + battement lent), trou de musique éventuel,
# souffle d'air très bas partout (le silence numérique sonne « coupé », pas « vide »)
ins, flt = [], []
for k, t0 in enumerate(VOIX):
    ins += ["-i", f"{VX}/l{k + 1}.wav"]
    flt.append(f"[{k + 1}:a]aresample=48000,adelay={int(t0 * 1000)}|{int(t0 * 1000)},apad[v{k}]")
vol = "0.10"
if MUS_TROU:
    a, b = MUS_TROU                                       # coupe franche à a, retour lent (2 s) à b
    vol = f"0.10*if(lt(t,{a}),1,if(lt(t,{b}),0,min(1,(t-{b})/2)))"
if V == "B3":                                         # crescendo ×2,5 sur le recul, coupe à 18,0 (la voix tombe dans le vide), retour 21,6
    vol = "0.10*if(lt(t,13.6),1,if(lt(t,18.0),1+1.5*(t-13.6)/4.4,if(lt(t,21.6),0,min(1,(t-21.6)/2))))"
nappe = (f"aevalsrc='({vol})*(sin(2*PI*55*t)+0.6*sin(2*PI*82.4*t)+0.3*sin(2*PI*110.3*t))*(0.8+0.2*sin(2*PI*0.25*t))'"
         f":s=48000:d={DUR}[m]")
air = f"anoisesrc=c=brown:a=0.004:d={DUR}:r=48000[n]"
mix = "".join(f"[v{k}]" for k in range(len(VOIX))) + f"[m][n]amix=inputs={len(VOIX) + 2}:normalize=0:duration=longest,atrim=0:{DUR}[a]"
fc = ";".join(flt + [nappe, air, mix])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}/%04d.png", *ins,
                "-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "160k", "-shortest", OUT], check=True)
