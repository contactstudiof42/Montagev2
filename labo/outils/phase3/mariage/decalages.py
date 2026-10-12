# decalages.py CAM N [fenetre_min=40] : décalage horloge caméra -> horloge Zoom sur N clips longs (>= 20 s), par corrélation du flux spectral
import sys, json, subprocess, os, numpy as np, librosa
from scipy.signal import fftconvolve
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"; R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
cam, N = sys.argv[1], int(sys.argv[2]); W = float(sys.argv[3]) * 60 if len(sys.argv) > 3 else 2400
Z = [("040626-161726", 16*3600+17*60+26), ("040626-175038", 17*3600+50*60+38), ("040626-192350", 19*3600+23*60+50),
     ("040626-205702", 20*3600+57*60+2), ("040626-223014", 22*3600+30*60+14), ("050626-000326", 24*3600+3*60+26)]
SR, HOP = 16000, 160
def env_y(y):
    o = librosa.onset.onset_strength(y=y, sr=SR, hop_length=HOP, n_mels=64, fmax=7000)
    o = o - np.convolve(o, np.ones(50) / 50, mode="same"); return (o - o.mean()) / (o.std() + 1e-9)
def zoom_segment(t0, t1):
    parts = []
    for n, s in Z:
        a, b = max(t0, s), min(t1, s + 5592.064 if n != "050626-000326" else s + 2305.576)
        if b > a: parts.append(librosa.load(f"{T}/son/{n}_16k.wav", sr=SR, offset=a - s, duration=b - a)[0])
    return np.concatenate(parts) if parts else None
r = [x for x in json.load(open(f"{T}/inventaire.json")) if x["cam"] == cam and x["duree_s"] >= 20]
idx = np.linspace(0, len(r) - 1, min(N, len(r))).astype(int)
os.makedirs(f"{T}/son/clips", exist_ok=True); out = []
for k in idx:
    x = r[k]; h, m, s = map(int, x["date"][11:19].split(":")); tc = h * 3600 + m * 60 + s
    if tc < 12 * 3600: tc += 24 * 3600
    w = f"{T}/son/clips/{x['nom']}.wav"
    if not os.path.exists(w): subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/{x['fichier']}", "-vn", "-ac", "1", "-ar", "16000", w])
    b = env_y(librosa.load(w, sr=SR)[0]); t0 = tc - W
    z = zoom_segment(t0, tc + W + x["duree_s"])
    if z is None: continue
    a = env_y(z); c = fftconvolve(a, b[::-1], mode="full") / len(b); i = int(np.argmax(c)); lag = (i - (len(b) - 1)) / 100
    mm = c.copy(); mm[max(0, i - 100):i + 100] = -np.inf
    off = t0 + lag - tc; out.append((x["nom"], x["date"][11:19], round(off, 2), round(float(c.max()), 3), round(float(mm.max() / c.max()), 2)))
    print(*out[-1], flush=True)
json.dump(out, open(f"{T}/son/decalages_{cam}.json", "w"))
