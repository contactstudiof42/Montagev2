"""Pièce 27 « Jamais » : un Gilligan cut à l'image près.
usage : python3 piece.py OUTDIR ECART_IMAGES TENUE_S [prelap_images] [--nom NOM]
Rend OUTDIR/NOM.mp4 (640x360, 25 i/s) + NOM.json (temps de coupe, fin de parole)."""
import sys, json, wave, subprocess, math, numpy as np
from PIL import Image, ImageDraw
FPS, W, H = 25, 640, 360
out, ecart, tenue = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
prelap = int(sys.argv[4]) if len(sys.argv) > 4 and not sys.argv[4].startswith('--') else 0
V2 = '--v2' in sys.argv
nom = sys.argv[sys.argv.index('--nom')+1] if '--nom' in sys.argv else f"e{ecart}_t{tenue:g}_p{prelap}"
SR = 22050
def lire(p):
    w = wave.open(p); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)/32768
    return x, w.getframerate()
voix, sr = lire(f"{out}/voix.wav"); assert sr == SR
# fin de parole : dernière fenêtre de 10 ms au-dessus de -40 dBFS
env = np.array([np.sqrt(np.mean(voix[i:i+220]**2)+1e-12) for i in range(0, len(voix)-220, 220)])
actif = np.where(20*np.log10(env) > -40)[0]
debut_p, fin_p = actif[0]*0.01, (actif[-1]+1)*0.01
lead = 0.6                                    # silence avant la réplique
t_fin = lead + fin_p                          # fin du mot-clé dans le film
t_coupe = round((t_fin)*FPS + ecart)/FPS      # coupe à l'image
duree = t_coupe + tenue
N = int(round(duree*FPS)); ns = int(duree*SR)
rng = np.random.default_rng(7)
audio = rng.normal(0, 10**(-52/20), ns)       # ambiance de pièce
i0 = int(lead*SR); seg = voix[: max(0, int(t_coupe*SR)-i0)]  # la coupe coupe aussi le son du plan A
audio[i0:i0+len(seg)] += seg
# mastication : craquements à 3,2 Hz dès la coupe (ou prelap images avant), s'arrête au regard caméra
t_regard = t_coupe + 0.6
def craque(t):
    k = int(t*SR); L = int(0.07*SR)
    if k+L > ns: return
    b = rng.normal(0, 1, L) * np.exp(-np.linspace(0, 6, L))
    b = np.convolve(b, np.ones(3)/3, 'same')
    audio[k:k+L] += 0.25*b
t = t_coupe - prelap/FPS
while t < t_regard - 0.05:
    craque(t); t += 1/3.2
audio = np.clip(audio, -1, 1)
wf = wave.open(f"{out}/{nom}.wav", 'w'); wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
wf.writeframes((audio*32767).astype(np.int16).tobytes()); wf.close()
def niveau(t):
    k = int((t-lead)*SR)
    if k < 0 or k >= len(voix): return 0
    return min(1, np.sqrt(np.mean(voix[k:k+880]**2))*8)
def plan_a(f):
    t = f/FPS; im = Image.new('RGB', (W, H), (196, 172, 140)); d = ImageDraw.Draw(im)
    d.rectangle([0, 250, W, H], fill=(150, 128, 104))                  # bas de mur
    if not V2: d.rectangle([420, 40, 560, 170], fill=(222, 214, 196))   # cadre au mur (v2 : retiré, il volait l'œil)
    cx, cy = 300, 150
    d.rounded_rectangle([cx-70, cy+55, cx+70, H+20], 30, fill=(70, 92, 120))   # torse
    d.rectangle([cx-75, cy+110, cx+75, cy+140], fill=(60, 80, 106))    # bras croisés
    d.ellipse([cx-52, cy-60, cx+52, cy+55], fill=(232, 196, 160))       # tête
    d.ellipse([cx-24, cy-12, cx-14, cy-2], fill=(30, 30, 30)); d.ellipse([cx+14, cy-12, cx+24, cy-2], fill=(30, 30, 30))
    d.line([cx-30, cy-26, cx-10, cy-22], fill=(60, 40, 30), width=4); d.line([cx+10, cy-22, cx+30, cy-26], fill=(60, 40, 30), width=4)
    o = niveau(t)*14; d.ellipse([cx-14, cy+22-o/2, cx+14, cy+26+o/2], fill=(110, 40, 40))
    d.chord([cx-14, cy+18, cx+14, cy+30], 0, 180, fill=(110, 40, 40)) if o < 2 else None
    return im
def plan_b1(f, tc):
    t = f/FPS - tc; im = Image.new('RGB', (W, H), (120, 112, 98)); d = ImageDraw.Draw(im)
    d.rectangle([0, 230, W, H], fill=(90, 70, 52))                      # table
    cx, cy = 320, 120
    d.ellipse([cx-62, cy-62, cx+62, cy+62], fill=(232, 196, 160))       # tête plus grande, penchée
    regard = t >= 0.6
    ey = cy-10 if regard else cy+4; ex = 0 if regard else 0
    d.ellipse([cx-28, ey-6, cx-16, ey+6], fill=(30, 30, 30)); d.ellipse([cx+16, ey-6, cx+28, ey+6], fill=(30, 30, 30))
    joue = 0 if regard else 6*abs(math.sin(t*math.pi*3.2))           # mastication
    d.ellipse([cx-58-joue, cy+10, cx-30, cy+44], fill=(226, 180, 150)); d.ellipse([cx+30, cy+10, cx+58+joue, cy+44], fill=(226, 180, 150))
    d.line([cx-12, cy+34, cx+12, cy+34], fill=(110, 40, 40), width=4)
    d.ellipse([cx-150, 200, cx+150, 330], fill=(210, 220, 228))         # saladier
    for k in range(9):                                                   # chou-fleur
        x = cx-110 + k*27; d.ellipse([x-20, 196+((k*7) % 3)*6, x+20, 236+((k*7) % 3)*6], fill=(244, 238, 214))
    fy = 150 + (0 if regard else 12*math.sin(t*math.pi*3.2))
    d.line([cx+90, fy+80, cx+40, fy], fill=(180, 180, 186), width=5)   # fourchette
    d.ellipse([cx+30, fy-14, cx+52, fy+8], fill=(244, 238, 214))
    return im
def plan_b(f, tc):
    if not V2: return plan_b1(f, tc)
    # v2 : même pull bleu (identité), chou-fleur reconnaissable (tête entière entamée + feuilles vertes),
    # fourchette dans la bouche, yeux plissés de plaisir (^ ^) puis grands ouverts sur la caméra : pris en flagrant délit
    t = f/FPS - tc; im = Image.new('RGB', (W, H), (120, 112, 98)); d = ImageDraw.Draw(im)
    cx, cy = 320, 112; regard = t >= 0.6
    d.rounded_rectangle([cx-95, cy+60, cx+95, H+20], 34, fill=(70, 92, 120))       # pull bleu
    d.rectangle([0, 268, W, H], fill=(90, 70, 52))                                   # table
    d.ellipse([cx-62, cy-62, cx+62, cy+62], fill=(232, 196, 160))
    if regard:
        for sx in (-22, 22):
            d.ellipse([cx+sx-13, cy-22, cx+sx+13, cy+4], fill=(250, 250, 250)); d.ellipse([cx+sx-5, cy-14, cx+sx+5, cy-4], fill=(20, 20, 20))
    else:
        for sx in (-22, 22): d.arc([cx+sx-12, cy-14, cx+sx+12, cy+6], 200, 340, fill=(30, 30, 30), width=4)
    joue = 0 if regard else 5*abs(math.sin(t*math.pi*3.2))
    d.ellipse([cx-66-joue, cy+4, cx-26, cy+48], fill=(240, 184, 150)); d.ellipse([cx+26, cy+4, cx+66+joue, cy+48], fill=(240, 184, 150))
    d.ellipse([cx-10, cy+26, cx+10, cy+44], fill=(110, 40, 40))
    d.line([cx+70, cy+150, cx+4, cy+36], fill=(190, 190, 196), width=6)            # fourchette dans la bouche
    d.ellipse([cx-14, cy+22, cx+12, cy+46], fill=(246, 240, 216))                   # bouquet sur la fourchette
    bx, by = cx-150, 270                                                             # chou-fleur entamé sur la table
    for a in (-1, 1): d.polygon([(bx, by+20), (bx+a*70, by-30), (bx+a*40, by+30)], fill=(96, 140, 70))
    for k in range(7):
        ang = math.pi*(0.15 + k*0.12); d.ellipse([bx+60*math.cos(ang)-26, by-50*math.sin(ang)-22, bx+60*math.cos(ang)+26, by-50*math.sin(ang)+22], fill=(244, 238, 214))
    d.ellipse([bx-30, by-40, bx+30, by+10], fill=(244, 238, 214))
    d.polygon([(bx+20, by-50), (bx+60, by-20), (bx+30, by)], fill=(120, 112, 98))   # la part mangée
    return im
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-i', f'{out}/{nom}.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-shortest', f'{out}/{nom}.mp4'], stdin=subprocess.PIPE)
fc = int(round(t_coupe*FPS))
for f in range(N):
    p.stdin.write((plan_a(f) if f < fc else plan_b(f, t_coupe)).tobytes())
p.stdin.close(); p.wait()
json.dump(dict(nom=nom, ecart=ecart, tenue=tenue, prelap=prelap, fin_parole=round(t_fin, 3), image_fin_parole=t_fin*FPS,
               image_coupe=fc, image_regard=int(round(t_regard*FPS)), duree=round(duree, 2)), open(f'{out}/{nom}.json', 'w'))
print(nom, 'coupe', fc, 'fin parole', round(t_fin*FPS, 1))
