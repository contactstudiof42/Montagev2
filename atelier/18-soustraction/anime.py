"""Pièce 18 v4 : l'extinction montrée, animée par addition de passes linéaires.
python3 -I anime.py <dossier_exr> <config.ocio> <sortie>
Deux rendus Cycles EXR linéaires (cadre v3 serré) : e0100000 = lampadaire 1 allumé (41 % de la lumière du cadre),
e0000000 = éteint. La lumière est additive : L = avant - après ; image(t) = après + k(t) * teinte(t) * L,
puis vue AgX par OpenColorIO (config de Blender 4.2), comme le rendu direct.
Variantes (25 i/s, 100 images, événement à l'image 40) : A sèche, B fondu 1 s, C panne (clignotements),
D rallumage d'un sodium (montée lente, teinte qui vire du rose à l'orange) depuis le noir ;
v5 : E, le même rallumage sur un lampadaire lointain, virage placé dans la plage visible."""
import sys, os, subprocess
import numpy as np, OpenEXR, PyOpenColorIO as ocio
from PIL import Image, ImageDraw
d, cfg, out = sys.argv[1:4]; os.makedirs(out, exist_ok=True)
rd = lambda n: OpenEXR.File(f"{d}/{n}.exr").channels()["RGBA"].pixels[..., :3].astype(np.float32)
avant, apres = rd("e0100000"), rd("e0000000"); L = np.clip(avant - apres, 0, None)
LOIN = np.clip(rd("e0000100") - apres, 0, None)   # v5 : lampadaire 4, lointain (part 1,4x le fond contre 5,8x pour le 1)
proc = ocio.Config.CreateFromFile(cfg).getProcessor("Linear Rec.709", "sRGB", "AgX", ocio.TRANSFORM_DIR_FORWARD).getDefaultCPUProcessor()
LED = np.array([0.75, 0.85, 1.0], np.float32)
def vue(lin):
    x = np.ascontiguousarray(lin.copy()); proc.applyRGB(x); return (np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8)
N, EV = 100, 40
def seche(i): return (1.0 if i < EV else 0.0), LED
def fondu(i): return float(np.clip(1 - (i - EV) / 25, 0, 1)), LED
PANNE = {EV: 0, EV + 1: 0, EV + 2: 0.8, EV + 3: 1, EV + 4: 0, EV + 5: 0, EV + 6: 0, EV + 7: 0.5, EV + 8: 0}
def panne(i): return (1.0 if i < EV else PANNE.get(i, 0.0)), LED
def sodium(i):   # depuis le noir : rose faible (amorçage) -> orange plein, 3 s compressées (le vrai : plusieurs minutes)
    if i < 20: return 0.0, LED
    t = min(1.0, (i - 20) / 75); rose, orange = np.array([1.0, 0.35, 0.45]), np.array([1.0, 0.55, 0.15])
    return 0.04 + 0.96 * t ** 2.2, ((1 - t ** 0.7) * rose + t ** 0.7 * orange).astype(np.float32)
def sodium_vu(i):   # v5 : le virage de teinte placé dans la plage visible (départ à 25 %), sur le lointain
    if i < 20: return 0.0, LED
    t = min(1.0, (i - 20) / 75); rose, orange = np.array([1.0, 0.35, 0.45]), np.array([1.0, 0.55, 0.15])
    return 0.25 + 0.75 * t ** 1.5, ((1 - t) * rose + t * orange).astype(np.float32)
VAR = {"A_seche": seche, "B_fondu": fondu, "C_panne": panne, "D_sodium": sodium, "E_sodium_loin": sodium_vu}
SRC = {"E_sodium_loin": LOIN}
def Y(img): return float((0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2]).mean())
courbes = {}
for nom, f in VAR.items():
    od = f"{out}/{nom}"; os.makedirs(od, exist_ok=True); ys = []
    for i in range(N):
        k, col = f(i); img = vue(apres + k * (col / LED) * SRC.get(nom, L)); ys.append(Y(img.astype(float)))
        Image.fromarray(img).save(f"{od}/{i:03d}.png")
    courbes[nom] = ys
    fin = np.asarray(Image.open(f"{od}/{N - 1:03d}.png")).astype(float); yy = 0.2126 * fin[..., 0] + 0.7152 * fin[..., 1] + 0.0722 * fin[..., 2]
    print(f"  saillance du personnage en fin (boîte autour de l'ambre / moyenne du cadre) : {yy[214:294, 176:236].mean() / yy.mean():.1f}")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", "25", "-i", f"{od}/%03d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", f"{out}/{nom}.mp4"], check=True)
    print(nom, " ".join(f"{y:.0f}" for y in ys[::5]))
# planche : 4 lignes x 8 vignettes à 160 px + courbe de luminance par ligne
IM = {n: [38, 40, 41, 42, 43, 47, 52, 65] for n in ("A_seche", "B_fondu", "C_panne")}; IM["D_sodium"] = IM["E_sodium_loin"] = [19, 25, 35, 45, 55, 70, 85, 99]
W, H = 160, 90; pl = Image.new("RGB", (W * 8 + 220, (H + 20) * len(IM)), (20, 20, 20)); dr = ImageDraw.Draw(pl)
for r, (nom, ims) in enumerate(IM.items()):
    y0 = r * (H + 20); dr.text((4, y0 + 2), f"{nom}  (images {ims})", fill=(230, 230, 230))
    for c, i in enumerate(ims): pl.paste(Image.open(f"{out}/{nom}/{i:03d}.png").resize((W, H), Image.LANCZOS), (c * W, y0 + 16))
    ys = courbes[nom]; x0, gx = W * 8 + 10, 200 / N; m = max(max(v) for v in courbes.values())
    dr.line([(x0 + gx * i, y0 + 16 + H - H * v / m) for i, v in enumerate(ys)], fill=(255, 200, 80), width=2)
    for i in ims: dr.line([(x0 + gx * i, y0 + 16 + H - 4), (x0 + gx * i, y0 + 16 + H)], fill=(120, 120, 255))
pl.save(f"{out}/v5-planche.png", optimize=True)
