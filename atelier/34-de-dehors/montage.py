"""Pièce 34 : python3 montage.py VERSION(v1|v2|...) RENDUS  -> RENDUS/VERSION.mp4 + VERSION-evenements.json
Dialogue espeak-ng filtré « à travers la carrosserie », bruits synthétiques, plans fixes Blender (scene.py)."""
import sys, os, json, subprocess, wave, numpy as np
V, R = sys.argv[1], sys.argv[2]; SR = 48000
EVT = V != 'v1'                         # v2 et suivantes : événements internes (liseuse, phares)
DUREE, CUT = 112.0, 100.0
if V in ('v5', 'v6'): DUREE, CUT = 110.0, 999.0          # v5 = v4 sans la coupe dedans : la dernière réplique entendue à travers la buée
K = dict(v='fr+m3', p='25', s='135'); N = dict(v='fr+f2', p='55', s='150')
DIAL = [(2.5, K, "Quatre euros vingt. Pour deux heures. Tu te rends compte ?"), (8.5, N, "Papa."),
        (10.0, K, "Non mais je dis ça. La prochaine fois, je me gare dans la rue."),
        (15.0, N, "Papa. Je pars. Au Canada. En novembre."),
        (34.0, K, "Il fait froid, là-bas."), (37.0, N, "Oui."),
        (41.0, K, "Tu mettras le chauffage. Ici aussi il fait froid. Tu peux mettre le chauffage ?"),
        (51.0, N, "C'est un poste à Montréal. C'est bien, tu sais."), (56.0, K, "Je sais que c'est bien."),
        (66.0, K, "Les résultats, ils ont dit dix jours."), (71.0, N, "Je serai là."), (74.0, K, "Bien sûr que tu seras là."),
        (97.0, N, "Tu dis rien ?"), (101.0, K, "Là-bas aussi, ils ont des parkings à ce prix-là ?")]
LAMPE = [(3.0, 19.5), (99.5, None)] if EVT else []     # allumée pour lire le ticket ; éteinte juste après « je pars » ; rallumée avant la dernière réplique
PHARES = (24.0, 28.5) if EVT and V != 'v6' else None   # v6 : phares retirés (remplissage, voir CRITIQUE)
tmp = os.path.join(R, 'tmp'); os.makedirs(tmp, exist_ok=True)
def lire(f):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-ar', str(SR), '-ac', '1', '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def filtre(x, af):
    p = os.path.join(tmp, 'f.raw'); x.astype(np.float32).tofile(p)
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', p, '-af', af, '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
mix = np.zeros(int(DUREE * SR), np.float32); evts = []
def poser(x, t, g=1.0):
    i = int(t * SR); n = min(len(x), len(mix) - i); mix[i:i + n] += g * x[:n]
for i, (t, who, txt) in enumerate(DIAL):
    w = os.path.join(tmp, f'l{i}.wav'); subprocess.run(['espeak-ng', '-v', who['v'], '-p', who['p'], '-s', who['s'], '-w', w, txt], check=True)
    x = lire(w); x /= np.abs(x).max() + 1e-9
    dedans = t >= CUT
    if not dedans:                      # à travers la carrosserie : bande étroite, petite réverbération de boîte, loin
        x = filtre(x, ('highpass=f=200,lowpass=f=1800,' if V == 'v6' else 'highpass=f=220,lowpass=f=1000,') + 'aecho=0.8:0.5:12|19:0.35|0.25,volume=0.5')
    poser(x, t, 0.5)
    evts.append(dict(t=t, fin=t + len(x) / SR, type='replique', qui='K' if who is K else 'N', dedans=dedans))
t = np.arange(len(mix)) / SR; rng = np.random.default_rng(34)
led = 0.004 * (np.sin(2 * np.pi * 100 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)) * (1 + 0.3 * rng.standard_normal(len(t)).clip(-1, 1))
air = filtre(rng.standard_normal(len(t)).astype(np.float32) * 0.02, 'lowpass=f=350')
dehors = t < CUT; mix += np.where(dehors, led, led * 0.2) + np.where(dehors, air, air * 0.4)
# ventilation : il demande le chauffage, Nadia l'allume à 48 s (bruit large, plus présent dedans)
vent = filtre(rng.standard_normal(len(t)).astype(np.float32) * 0.03, 'bandpass=f=900:w=1200')
mix += np.where(t >= 48, np.where(dehors, 0.25, 1.0), 0) * vent * np.clip((t - 48) / 1.5, 0, 1); evts.append(dict(t=48.0, type='son', quoi='ventilation'))
def clic(tc):
    n = int(0.03 * SR); poser(np.exp(-np.arange(n) / (0.003 * SR)) * rng.standard_normal(n).astype(np.float32) * (0.15 if tc < CUT else 0.4), tc)
for a, b in LAMPE:
    clic(a); evts.append(dict(t=a, type='image', quoi='liseuse on'))
    if b: clic(b); evts.append(dict(t=b, type='image', quoi='liseuse off'))
if PHARES:
    a, b = PHARES; d = b - a; tt = np.clip((t - a) / d, 0, 1); env = np.sin(np.pi * tt) ** 2 * ((t >= a) & (t <= b))
    moteur = filtre(rng.standard_normal(len(t)).astype(np.float32) * 0.06, 'lowpass=f=180') * env; mix += moteur
    evts.append(dict(t=a, fin=b, type='image', quoi='phares'))
evts.append(dict(t=CUT, type='coupe', quoi='dedans'))
mix /= max(1.0, np.abs(mix).max() / 0.9)
wav = os.path.join(tmp, f'{V}.wav'); mix.astype(np.float32).tofile(wav + '.raw')
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', wav + '.raw', wav], check=True)
# image : base extérieure, calques liseuse / phares en fondu court, puis l'intérieur
P = lambda n: os.path.join(R, n)
inp = ['-loop', '1', '-t', str(CUT), '-i', P('ext.png'), '-loop', '1', '-t', str(CUT), '-i', P('ext_lampe.png'),
       '-loop', '1', '-t', str(CUT), '-i', P('ext_phares.png'), '-loop', '1', '-t', str(DUREE - CUT), '-i', P('int.png' if EVT else 'int_sans.png'), '-i', wav]
if EVT:                                  # fondus alpha courts (0,12 s : une lampe s'allume net) ; phares en cloche de 4,5 s
    (la, lb), (pa, pb), l2 = LAMPE[0], PHARES or (0.0, 1.0), LAMPE[1][0]; h = (pb - pa) / 2
    fc = (f"[1]format=rgba,fade=in:st={la}:d=0.12:alpha=1,fade=out:st={lb - 0.12}:d=0.12:alpha=1[l];"
          f"[1]format=rgba,fade=in:st={l2}:d=0.12:alpha=1[l2];"
          f"[2]format=rgba,fade=in:st={pa}:d={h}:alpha=1,fade=out:st={pa + h}:d={h}:alpha=1[p];"
          f"[0][l]overlay[x1];[x1][l2]overlay[x2];[x2][p]overlay,fps=25,format=yuv420p[e];")
else:
    fc = "[0]fps=25,format=yuv420p[e];"
fc += "[3]fps=25,format=yuv420p[i];[e][i]concat=n=2:v=1:a=0[v]"
if V in ('v3', 'v4', 'v5', 'v6'):                  # v4 = v3 + poussée lente de 100 s vers la voiture (images HD recadrées)                            # buée : image composée image par image (numpy), canal d'opacité de la buée b(t)
    from PIL import Image
    HD = V in ('v4', 'v5', 'v6'); Q = (lambda n: P(('hd/' if HD and n != 'int' else '') + n + '.png'))
    im = {n: np.asarray(Image.open(Q(n)).convert('RGB'), np.float32) for n in ('ext', 'ext_lampe', 'ext_phares', 'ext_buee', 'ext_buee_lampe', 'int')}
    def cadre(f, tt):                    # zoom 1 → 2,4 avec accélération douce (t/100)^1,6 ; centre glisse vers la voiture (760, 450 en HD)
        if not HD: return f
        u = min(1, tt / min(CUT, 100.0)) ** 1.6; z = 1 + (1.1 if V == 'v6' else 1.4) * u; w, h = 1280 / z, 540 / z
        cx, cy = 640 + ((800 if V == 'v6' else 760) - 640) * u, 270 + ((420 if V == 'v6' else 450) - 270) * u   # v6 : zoom 2,1 recentré, le mât reste dans le champ
        x0 = min(max(cx - w / 2, 0), 1280 - w); y0 = min(max(cy - h / 2, 0), 540 - h)
        return np.asarray(Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)).resize((640, 270), Image.BILINEAR, box=(x0, y0, x0 + w, y0 + h)), np.float32)
    def b(tt):                           # 0 → 0,6 à 48 s (ils respirent, il fait froid) ; le chauffage dégage à 0,15 en 8 s ; remonte à 1 à 97 s
        if tt < 48: return 0.6 * tt / 48
        if tt < 56: return 0.6 - 0.45 * (tt - 48) / 8
        return min(1.0, 0.15 + 0.85 * (tt - 56) / 41)
    def lam(tt): return 1.0 if (LAMPE[0][0] <= tt < LAMPE[0][1]) or tt >= LAMPE[1][0] else 0.0
    pa, pb = PHARES or (0, 0); H, W = im['int'].shape[:2]
    pr = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '25', '-i', '-', '-i', wav,
                           '-c:v', 'libx264', '-crf', '24', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-af', 'loudnorm=I=-23:TP=-2', '-c:a', 'aac', '-b:a', '128k', '-shortest', P(f'{V}.mp4')], stdin=subprocess.PIPE)
    for k in range(int(DUREE * 25)):
        tt = k / 25
        if tt >= CUT: f = im['int']
        else:
            bb, ll = b(tt), lam(tt)
            clair = im['ext'] * (1 - ll) + im['ext_lampe'] * ll; embue = im['ext_buee'] * (1 - ll) + im['ext_buee_lampe'] * ll
            f = clair * (1 - bb) + embue * bb
            if PHARES and pa <= tt <= pb: f = f + (im['ext_phares'] - im['ext']) * np.sin(np.pi * (tt - pa) / (pb - pa)) ** 2
            f = cadre(f, tt)
        pr.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    pr.stdin.close(); pr.wait()
    evts += [dict(t=0.0, fin=48.0, type='image', quoi='buée monte'), dict(t=48.0, fin=56.0, type='image', quoi='buée se dégage'), dict(t=56.0, fin=97.0, type='image', quoi='buée monte')]
else:
  subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *inp, '-filter_complex', fc, '-map', '[v]', '-map', '4:a', '-r', '25',
                '-c:v', 'libx264', '-crf', '24', '-preset', 'veryfast', '-af', 'loudnorm=I=-23:TP=-2', '-c:a', 'aac', '-b:a', '128k', '-t', str(DUREE), P(f'{V}.mp4')], check=True)
json.dump(sorted(evts, key=lambda e: e['t']), open(P(f'{V}-evenements.json'), 'w'), indent=1, ensure_ascii=False)
print('ok', P(f'{V}.mp4'))
