#!/usr/bin/env python3
"""Pièce 33 « Voix écrite après » (principe Varda) : 8 plans glanés dans les pièces 29-32 (rendus de la session 24),
montés d'abord, puis deux voix écrites après : A illustre, B relie. Mesure : durée de chaque phrase (espeak-ng, fr, 150 mots/min)
contre la durée du plan ; planche avec le texte sous chaque plan.  usage : python3 piece.py DOSSIER_RENDUS SORTIE.png"""
import sys, subprocess, wave, os, tempfile
from PIL import Image, ImageDraw, ImageFont
R, OUT = sys.argv[1], sys.argv[2]
P = 2.5                                                   # durée de chaque plan (s)
plans = [('29/v7.mp4', 1.5, 'goutte'), ('29/v7.mp4', 3.0, 'pièce, jour'), ('31/R1.png', 0, 'escalier froid'), ('32/F.mp4', 0.3, 'commode'),
         ('30/I.mp4', 2.45, 'torchon'), ('30/I.mp4', 7.5, 'plante'), ('31/R4b.png', 0, 'escalier chaud'), ('29/v7.mp4', 13.8, 'bâtons, soir')]
A = ['Une goutte au bord du robinet.', 'Une pièce au soleil.', 'Un escalier, le soir.', 'Une commode et son tiroir.',
     'Un torchon passe.', 'Une plante a poussé.', "L'escalier, au couchant.", 'Des bâtons sur un mur.']
B = ['Ici, rien ne bouge.', 'Là-bas, on attendait.', 'On montait sans y croire.', 'On fermait les choses doucement.',
     "Il suffit d'un geste", 'pour que tout ait changé.', 'Et on redescend autrement.', "Quelqu'un a cessé de compter."]
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
def duree(txt):
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, 'v.wav'); subprocess.run(['espeak-ng', '-v', 'fr', '-s', '150', '-w', f, txt], check=True)
        w = wave.open(f); return w.getnframes() / w.getframerate()
TW, TH = 160, 90
img = Image.new('RGB', (8 * (TW + 4), TH + 120), (16, 16, 16)); d = ImageDraw.Draw(img)
for i, (src, t, nom) in enumerate(plans):
    if src.endswith('.png'):
        im = Image.open(f'{R}/{src}').convert('RGB')
    else:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t), '-i', f'{R}/{src}', '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        import io; im = Image.open(io.BytesIO(raw)).convert('RGB')
    if im.height > im.width:                                # plans verticaux : bande centrale recadrée en 16:9
        h = int(im.width * 9 / 16); y0 = int(im.height * 0.42 - h / 2); im = im.crop((0, y0, im.width, y0 + h))
    img.paste(im.resize((TW, TH)), (i * (TW + 4), 0))
    for j, (lab, txt, col) in enumerate((('A', A[i], (200, 200, 200)), ('B', B[i], (240, 200, 120)))):
        dt = duree(txt); ok = dt <= P - 0.3
        y = TH + 6 + j * 56
        mots = txt.split(); l1 = ' '.join(mots[:len(mots) // 2 + 1]); l2 = ' '.join(mots[len(mots) // 2 + 1:])
        d.text((i * (TW + 4) + 4, y), f'{lab} {l1}', fill=col, font=font); d.text((i * (TW + 4) + 18, y + 14), l2, fill=col, font=font)
        d.text((i * (TW + 4) + 4, y + 30), f'{dt:.1f} s', fill=(120, 220, 120) if ok else (240, 90, 90), font=font)
        print(lab, i + 1, nom, f'{dt:.2f} s', 'OK' if ok else 'TROP LONG')
img.save(OUT, optimize=True)
