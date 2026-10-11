#!/usr/bin/env python3
"""ÉCHEC DE CALIBRATION (2026-10-11) : sur 24 images de Mad Max, le pic de saillance ne tombe sur le sujet
qu'environ une fois sur trois, et les cinq films de la vague 1 donnent tous le même résultat (44-55 % au tiers central,
saut à la coupe = hasard). Ne pas citer ses chiffres. Utiliser echantillon_tiers.py et compter à l'œil.

Où est le sujet dans le cadre, et saute-t-il d'un plan à l'autre ? (phase 2, Mad Max, session 3)
Décode tout le proxy à 4 i/s en 96 px de large (gris), retire les bandes noires image par image, calcule une
saillance « spectral residual » (Hou & Zhang 2007), lissée, et garde son pic (x, y en fraction du cadre, 0 = centre,
±0,5 = bord). Pour chaque coupe dont les deux plans durent au moins 0,75 s : pic de la dernière image avant la coupe
et de la première image après. Sort :
  - centrage : médiane de |x| et part des pics dans le tiers central (|x| < 1/6), sur les images de milieu de plan ;
  - saut à la coupe : distance médiane entre le pic avant et le pic après, comparée au hasard (mêmes images,
    appariées au hasard dans le film, 200 tirages) ; rapport < 1 = l'œil retrouve le sujet là où il était.
Usage : centrage.py DOSSIER [DEBUT_s FIN_s]   (lancer avec .venv/bin/python -I). Écrit DOSSIER/centrage.json.
Limite : la saillance n'est pas le regard d'un spectateur (elle préfère les contrastes, ignore les visages et le
mouvement) ; c'est un indice, à confirmer à l'œil sur une planche."""
import sys, os, json, subprocess, numpy as np
D = sys.argv[1]; A = float(sys.argv[2]) if len(sys.argv) > 2 else 0; B = float(sys.argv[3]) if len(sys.argv) > 3 else 1e9
FPS, W = 4, 96
f = os.path.join(D, 'proxy.mp4')
w0, h0 = map(int, subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height",
                                  "-of", "csv=p=0", f], capture_output=True, text=True).stdout.strip().split(',')[:2])
H = int(round(W * h0 / w0 / 2) * 2)
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"fps={FPS},scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                     capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W)   # uint8 : 2 h à 4 i/s tient en 200 Mo

def blur(x, k=3):
    for ax in (0, 1):
        x = sum(np.roll(x, s, ax) for s in range(-k, k + 1)) / (2 * k + 1)
    return x

def pic(im):
    im = im.astype(np.float32) / 255
    rows = np.where(im.mean(1) > 0.04)[0]          # bandes noires (letterbox, IMAX qui change de format)
    if len(rows) < 8 or im.max() - im.min() < 0.08: return None   # image noire ou unie : pas de sujet
    y0, y1 = rows[0], rows[-1] + 1; im = im[y0:y1]
    F = np.fft.fft2(im); L = np.log(np.abs(F) + 1e-6); P = np.angle(F)
    R = L - blur(L, 1)
    S = np.abs(np.fft.ifft2(np.exp(R + 1j * P))) ** 2
    S = blur(S, 3); m = 3; S[:m] = S[-m:] = 0; S[:, :m] = S[:, -m:] = 0   # bords : artefacts de la FFT
    y, x = np.unravel_index(S.argmax(), S.shape)
    return (x + 0.5) / im.shape[1] - 0.5, (y + 0.5) / im.shape[0] - 0.5

J = json.load(open(os.path.join(D, 'coupes.json'))); c = [0.0] + J['coupes'] + [J['stats']['duree']]
idx = lambda t: min(len(fr) - 1, max(0, int(round(t * FPS))))
milieux, paires = [], []
for i in range(1, len(c) - 1):
    s0, cut, e1 = c[i - 1], c[i], c[i + 1]
    if not (A <= cut < B): continue
    m = pic(fr[idx((s0 + cut) / 2)])
    if m: milieux.append(m)
    if cut - s0 >= 0.75 and e1 - cut >= 0.75:
        p, q = pic(fr[idx(cut - 0.3)]), pic(fr[idx(cut + 0.3)])
        if p and q: paires.append((p, q))
M = np.array(milieux); ax = np.abs(M[:, 0])
Pa = np.array([p for p, q in paires]); Qa = np.array([q for p, q in paires])
d = np.hypot(*(Pa - Qa).T)
rng = np.random.default_rng(0)
dh = np.median([np.median(np.hypot(*(Pa - Qa[rng.permutation(len(Qa))]).T)) for _ in range(200)])
out = {"plans": len(M), "mediane_abs_x": round(float(np.median(ax)), 3), "tiers_central": round(float((ax < 1 / 6).mean()), 3),
       "mediane_abs_y": round(float(np.median(np.abs(M[:, 1]))), 3),
       "coupes_mesurees": len(d), "saut_median": round(float(np.median(d)), 3), "saut_hasard": round(float(dh), 3),
       "rapport": round(float(np.median(d) / dh), 3), "sauts_lt_0.15": round(float((d < 0.15).mean()), 3)}
print(json.dumps(out))
nom = 'centrage.json' if len(sys.argv) <= 2 else f'centrage-{int(A)}-{int(B)}.json'
json.dump(out, open(os.path.join(D, nom), 'w'))
