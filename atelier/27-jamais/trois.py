"""Pièce 27 v3 « Trois fois jamais » : règle de trois + silence-gag + tenue de la réaction finale.
Occurrences 1 et 2 : « X ? Jamais. » → coupe (écart 2 images) → il en mange, yeux plissés, « ting » de fourchette
à la 1re image, mastication, regard caméra à 0,6 s, tenue 1,5 s. Occurrence 3 (la trahison) : coupe → assiette vide,
chou-fleur intact, bras croisés, il regarde déjà la caméra, AUCUN ting (le son appris est retiré).
usage : python3 trois.py RENDUS TENUE_FINALE_S [--ting3] [--nom NOM]   (--ting3 = contre-épreuve : le ting reste)"""
import sys, json, wave, subprocess, math, numpy as np
from PIL import Image, ImageDraw
FPS, W, H, SR = 25, 640, 360, 22050
R, tenue3 = sys.argv[1], float(sys.argv[2]); ting3 = '--ting3' in sys.argv; V4 = '--v4' in sys.argv
nom = sys.argv[sys.argv.index('--nom')+1] if '--nom' in sys.argv else f"trois_t{tenue3:g}{'_ting3' if ting3 else ''}{'_v4' if V4 else ''}"
ALIM = [((70, 130, 60), (50, 100, 44)), ((40, 80, 40), (30, 64, 30)), ((244, 238, 214), (96, 140, 70))]  # brocoli, épinards, chou-fleur
def lire(p):
    w = wave.open(p); return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)/32768
def fin_parole(v):
    env = np.array([np.sqrt(np.mean(v[i:i+220]**2)+1e-12) for i in range(0, len(v)-220, 220)])
    return (np.where(20*np.log10(env) > -40)[0][-1]+1)*0.01
rng = np.random.default_rng(3)
segs, t = [], 0.0                                  # (debut_A, t_voix, fin_mot, coupe, fin_B, k)
for k in range(3):
    v = lire(f'{R}/l{k+1}.wav'); a0 = t; tv = a0 + 0.5
    fm = tv + fin_parole(v); tc = round(fm*FPS + 2)/FPS
    fb = tc + (1.5 if k < 2 else tenue3)
    segs.append(dict(a0=a0, tv=tv, fm=fm, tc=tc, fb=fb, k=k, v=v)); t = fb
duree = t; N = int(round(duree*FPS)); ns = int(duree*SR) + SR
audio = rng.normal(0, 10**(-52/20), ns)
def ajoute(t, x, g=1.0):
    k = int(t*SR); audio[k:k+len(x)] += g*x[:max(0, ns-k)]
def ting():
    n = np.arange(int(0.5*SR))/SR
    return (np.sin(2*np.pi*2630*n) + 0.6*np.sin(2*np.pi*3950*n)) * np.exp(-n*9) * 0.22
def craque():
    L = int(0.07*SR); b = rng.normal(0, 1, L)*np.exp(-np.linspace(0, 6, L)); return 0.25*np.convolve(b, np.ones(3)/3, 'same')
for s in segs:
    ajoute(s['tv'], s['v'][: int((s['tc']-s['tv'])*SR)])
    if s['k'] < 2 or ting3: ajoute(s['tc'], ting())
    if s['k'] < 2:
        x = s['tc'] + 0.12
        while x < s['tc'] + 0.55: ajoute(x, craque()); x += 1/3.2
if V4:
    L = int(0.3*SR); b = rng.normal(0, 1, L); b = np.convolve(b, np.ones(40)/40, 'same')*np.hanning(L)*0.9
    ajoute(segs[2]['tc'] + 1.3, b)
audio = np.clip(audio[:int(duree*SR)], -1, 1)
wf = wave.open(f'{R}/{nom}.wav', 'w'); wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
wf.writeframes((audio*32767).astype(np.int16).tobytes()); wf.close()
def niveau(s, t):
    k = int((t - s['tv'])*SR)
    return 0 if k < 0 or k >= len(s['v']) else min(1, np.sqrt(np.mean(s['v'][k:k+880]**2))*8)
def plan_a(s, t):
    im = Image.new('RGB', (W, H), (196, 172, 140)); d = ImageDraw.Draw(im); cx, cy = 300, 150
    d.rectangle([0, 250, W, H], fill=(150, 128, 104))
    d.rounded_rectangle([cx-70, cy+55, cx+70, H+20], 30, fill=(70, 92, 120)); d.rectangle([cx-75, cy+110, cx+75, cy+140], fill=(60, 80, 106))
    d.ellipse([cx-52, cy-60, cx+52, cy+55], fill=(232, 196, 160))
    d.ellipse([cx-24, cy-12, cx-14, cy-2], fill=(30, 30, 30)); d.ellipse([cx+14, cy-12, cx+24, cy-2], fill=(30, 30, 30))
    d.line([cx-30, cy-26, cx-10, cy-22], fill=(60, 40, 30), width=4); d.line([cx+10, cy-22, cx+30, cy-26], fill=(60, 40, 30), width=4)
    o = niveau(s, t)*14; d.ellipse([cx-14, cy+22-o/2, cx+14, cy+26+o/2], fill=(110, 40, 40))
    return im
def tas(d, k, bx, by, entame):
    c, f = ALIM[k]
    if k == 1:                                                     # épinards : un tas de feuilles sombres
        for j in range(6): d.ellipse([bx-60+j*18, by-30+(j % 2)*10, bx-20+j*18, by+10+(j % 2)*10], fill=c if j % 2 else f)
        return
    for a in (-1, 1): d.polygon([(bx, by+20), (bx+a*70, by-30), (bx+a*40, by+30)], fill=f)
    for j in range(7):
        ang = math.pi*(0.15 + j*0.12)
        d.ellipse([bx+60*math.cos(ang)-26, by-50*math.sin(ang)-22, bx+60*math.cos(ang)+26, by-50*math.sin(ang)+22], fill=c)
    d.ellipse([bx-30, by-40, bx+30, by+10], fill=c)
    if entame: d.polygon([(bx+20, by-50), (bx+60, by-20), (bx+30, by)], fill=(120, 112, 98))
def plan_b(s, t):
    t -= s['tc']; k = s['k']; im = Image.new('RGB', (W, H), (120, 112, 98)); d = ImageDraw.Draw(im); cx, cy = 320, 112
    trahison = k == 2; regard = trahison or t >= 0.6
    d.rounded_rectangle([cx-95, cy+60, cx+95, H+20], 34, fill=(70, 92, 120))
    if trahison: d.rectangle([cx-100, cy+118, cx+100, cy+150], fill=(60, 80, 106))       # bras croisés, comme au plan A
    d.rectangle([0, 268, W, H], fill=(90, 70, 52))
    pousse = 0
    if V4 and trahison: pousse = -50*min(1, max(0, (t-1.3)/0.3))
    if not (V4 and trahison): d.ellipse([cx+40, 262, cx+200, 300], fill=(214, 220, 226))                          # assiette
    d.ellipse([cx-62, cy-62, cx+62, cy+62], fill=(232, 196, 160))
    if regard:
        for sx in (-22, 22):
            d.ellipse([cx+sx-13, cy-22, cx+sx+13, cy+4], fill=(250, 250, 250)); d.ellipse([cx+sx-5, cy-14, cx+sx+5, cy-4], fill=(20, 20, 20))
    else:
        for sx in (-22, 22): d.arc([cx+sx-12, cy-14, cx+sx+12, cy+6], 200, 340, fill=(30, 30, 30), width=4)
    if trahison and V4:
        d.line([cx-40, cy-30, cx-12, cy-24], fill=(60, 40, 30), width=5); d.line([cx+12, cy-24, cx+40, cy-30], fill=(60, 40, 30), width=5)
    if trahison:
        d.line([cx-14, cy+34, cx+14, cy+34], fill=(110, 40, 40), width=4)                # bouche close, digne
        if not V4: d.line([cx+60, 282, cx+180, 270], fill=(190, 190, 196), width=6)  # fourchette posée, propre
    else:
        joue = 0 if regard else 5*abs(math.sin(t*math.pi*3.2))
        d.ellipse([cx-66-joue, cy+4, cx-26, cy+48], fill=(240, 184, 150)); d.ellipse([cx+26, cy+4, cx+66+joue, cy+48], fill=(240, 184, 150))
        d.ellipse([cx-10, cy+26, cx+10, cy+44], fill=(110, 40, 40))
        d.line([cx+70, cy+150, cx+4, cy+36], fill=(190, 190, 196), width=6); d.ellipse([cx-14, cy+22, cx+12, cy+46], fill=ALIM[k][0])
    if V4 and trahison:
        px = cx-150+pousse; d.ellipse([px-90, 262, px+90, 304], fill=(214, 220, 226)); tas(d, k, px, 268, False)
        if 1.2 < t < 1.7:                                                            # un bras sort du croisé, un doigt pousse
            d.line([cx-80, cy+134, px+92, 262], fill=(60, 80, 106), width=18); d.ellipse([px+78, 252, px+100, 274], fill=(232, 196, 160))
    else: tas(d, k, cx-150, 270, not trahison)
    return im
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-i', f'{R}/{nom}.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-shortest', f'{R}/{nom}.mp4'], stdin=subprocess.PIPE)
for f in range(N):
    t = f/FPS; s = next(x for x in segs if t < x['fb'] or x is segs[-1])
    p.stdin.write((plan_a(s, t) if t < s['tc'] else plan_b(s, t)).tobytes())
p.stdin.close(); p.wait()
json.dump(dict(nom=nom, duree=round(duree, 2), segs=[{k: round(v, 3) for k, v in s.items() if k != 'v'} for s in segs]), open(f'{R}/{nom}.json', 'w'))
print(nom, round(duree, 2), [(round(s['tc'], 2), round(s['fb'], 2)) for s in segs])
