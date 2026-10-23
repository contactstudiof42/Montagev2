# habiller_animatique.py DOSSIER_IMAGES SORTIE.mp4 : met les images de l'animatique au cadre livré (2,39:1, bandes noires),
# écrit le plan et le minutage en haut, les répliques et les sons faits en post en bas, ajoute 1 s de noir avec le titre,
# puis encode en H.264 (ffmpeg du système, sans drawtext : le texte est posé avec Pillow).
import sys, os, glob, subprocess
from PIL import Image, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]; FPS = 24
PLANS = [(0, "1", "large, fixe"), (5, "2a", "sur elle"), (8, "2b", "sur lui"), (11, "3", "sur lui, par-dessus son épaule"),
         (16, "4a", "sur elle"), (19, "4b", "sur lui"), (22, "5a", "sur elle"), (25, "5b", "sur lui"), (28, "6", "à deux"),
         (31, "7a", "à deux, la caméra monte avec lui"), (34, "7b", "sur lui, en pied"), (39, "8a", "ses mains"), (41, "8b", "elle, de profil")]
# (début, fin, texte) ; entre crochets : son fait en post ; « (hc) » : dit hors champ
TXT = [(0.3, 4.8, "[il siffle l'air, doucement]"), (5.6, 7.2, "[elle souffle : la flamme se couche]"), (7.6, 8.0, "LUI (hc) : No."),
       (8.0, 10.2, "LUI : That's how you blow out a candle."), (12.0, 13.3, "ELLE (hc) : Nuns don't whistle."),
       (14.3, 15.4, "LUI : Nobody'll hear."), (15.5, 16.0, "[son inspiration à elle]"), (16.5, 17.4, "[note grêle, cassée]"),
       (19.7, 22.4, "LUI : See? He didn't strike you down."), (23.2, 25.4, "ELLE : There's something I have to tell you…"),
       (26.7, 27.4, "LUI : Later."), (27.5, 28.4, "[bourdonnement de la serrure]"), (28.4, 29.2, "[le pêne claque] [lumière rouge du dôme]"),
       (31.0, 31.9, "[cliquetis du métal]"), (32.5, 33.7, "ELLE : I'll pray for you."), (34.3, 35.2, "[trois notes sifflées, tout bas]"),
       (35.2, 36.4, "[la porte s'ouvre : le bruit du couloir entre]"), (36.4, 38.6, "[la chaîne traîne]"),
       (39.0, 39.8, "[coupe sèche : silence]"), (40.5, 41.0, "[sa première note]"), (41.0, 45.8, "[elle siffle l'air, juste, jusqu'au bout]")]
def font(n):
    for p in ("/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/SFNS.ttf", "/Library/Fonts/Arial.ttf"):
        if os.path.exists(p): return ImageFont.truetype(p, n)
    return ImageFont.load_default()
fs = sorted(glob.glob(os.path.join(src, "f_*.png")))
w, h = Image.open(fs[0]).size; ch = int(round(w / 2.39)); y0 = (h - ch) // 2
f1, f2 = font(max(14, w // 48)), font(max(16, w // 40))
tmp = os.path.join(src, "_habille"); os.makedirs(tmp, exist_ok=True)
def plan_a(t): return [p for p in PLANS if p[0] <= t][-1]
n = 0
for i, f in enumerate(fs):
    t = i / FPS; im = Image.open(f).convert("RGB"); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w, y0], fill=(0, 0, 0)); d.rectangle([0, y0 + ch, w, h], fill=(0, 0, 0))
    p = plan_a(t); d.text((12, 10), f"PLAN {p[1]} · {p[2]}", fill=(235, 235, 235), font=f1)
    tc = f"{int(t // 60)}:{t % 60:05.2f}"; d.text((w - 12 - d.textlength(tc, font=f1), 10), tc, fill=(235, 235, 235), font=f1)
    lines = [x[2] for x in TXT if x[0] <= t < x[1]]
    for k_, s in enumerate(lines[:2]):
        col = (255, 214, 120) if s.startswith("[") else (255, 255, 255)
        d.text(((w - d.textlength(s, font=f2)) / 2, y0 + ch + 8 + k_ * (f2.size + 4)), s, fill=col, font=f2)
    im.save(os.path.join(tmp, f"g_{n:05d}.png")); n += 1
for j in range(FPS):          # 1 s de noir avec le titre
    im = Image.new("RGB", (w, h), (0, 0, 0)); d = ImageDraw.Draw(im); tt = "L'AIR"
    d.text(((w - d.textlength(tt, font=f2)) / 2, h / 2 - f2.size / 2), tt, fill=(230, 230, 230), font=f2)
    im.save(os.path.join(tmp, f"g_{n:05d}.png")); n += 1
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "g_%05d.png"), "-c:v", "libx264",
                "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], check=True)
print("ANIMATIQUE", out, n, "images")
