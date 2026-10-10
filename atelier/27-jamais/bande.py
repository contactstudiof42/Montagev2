"""Bande-film à l'image près autour de la coupe, une ligne par version, avec enveloppe du son.
usage : python3 bande.py RENDUS SORTIE.png NOM1 NOM2 ... [--avant 18 --apres 50]
Chaque colonne = une image (recadrage tête 120x120 réduit à 28 px). Repères : rouge = fin du mot-clé,
blanc = coupe, jaune = regard caméra. L'enveloppe (dB, -60..0) est tracée sous chaque ligne."""
import sys, json, wave, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
args = sys.argv[1:]; opt = lambda k, d: int(args[args.index(k)+1]) if k in args else d
avant, apres = opt('--avant', 18), opt('--apres', 50)
noms = [a for i, a in enumerate(args[2:]) if not a.startswith('--') and (i == 0 or not args[2:][i-1].startswith('--'))]
R, OUT = args[0], args[1]; C, FPS = 28, 25
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
lignes = []
for n in noms:
    m = json.load(open(f'{R}/{n}.json')); ref = int(round(m['image_fin_parole']))
    f0 = ref - avant; nf = avant + apres
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{R}/{n}.mp4', '-vf', f"select='between(n,{max(0,f0)},{f0+nf-1})',crop=140:140:250:60,scale={C}:{C}",
                          '-vsync', '0', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    imgs = np.frombuffer(raw, np.uint8).reshape(-1, C, C, 3)
    w = wave.open(f'{R}/{n}.wav'); sr = w.getframerate(); a = np.frombuffer(w.readframes(w.getnframes()), np.int16)/32768
    L = Image.new('RGB', (150 + nf*C, C + 34), (24, 24, 24)); d = ImageDraw.Draw(L)
    d.text((4, 4), n, fill=(230, 230, 230), font=font)
    d.text((4, 18), f"coupe {m['image_coupe']-ref:+d} im", fill=(170, 170, 170), font=font)
    for k, im in enumerate(imgs): L.paste(Image.fromarray(im), (150 + k*C, 0))
    for k in range(nf):
        f = f0 + k; s = a[int(f/FPS*sr): int((f+1)/FPS*sr)]
        db = 20*np.log10(np.sqrt(np.mean(s**2)) + 1e-6) if len(s) else -60
        h = int(max(0, (db + 60)/60) * 30); d.rectangle([150 + k*C + 2, C + 32 - h, 150 + k*C + C - 3, C + 32], fill=(110, 170, 210))
    for f, col in ((ref, (230, 60, 60)), (m['image_coupe'], (255, 255, 255)), (m['image_regard'], (240, 210, 60))):
        x = 150 + (f - f0)*C; d.line([x, 0, x, C + 34], fill=col, width=2)
    lignes.append(L)
P = Image.new('RGB', (max(l.width for l in lignes), sum(l.height + 4 for l in lignes)), (0, 0, 0))
y = 0
for l in lignes: P.paste(l, (0, y)); y += l.height + 4
P.save(OUT, optimize=True); print(OUT, P.size)
