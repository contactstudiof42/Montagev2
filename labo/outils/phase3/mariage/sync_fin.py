# sync_fin.py : décalage précis (à 10 ms) entre un rush et une référence (HF ou Zoom), par corrélation du flux spectral autour de l'estimation d'horloge.
# sync(nom, ref="HF"|"ZOOM") -> t_ref - t_rush (s) ; cache dans _travail/son/sync_fin.json
import json, os, subprocess, numpy as np, librosa
from scipy.signal import fftconvolve
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"; R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
HF0 = 63115.08
Z = [("040626-161726", 58646), ("040626-175038", 64238), ("040626-192350", 69830), ("040626-205702", 75422), ("040626-223014", 81014), ("050626-000326", 86606)]
CACHE = f"{T}/son/sync_fin.json"; SR = 16000
def env(y):
    o = librosa.onset.onset_strength(y=y, sr=SR, hop_length=160, n_mels=64, fmax=7000); o = o - np.convolve(o, np.ones(50) / 50, mode="same"); return (o - o.mean()) / (o.std() + 1e-9)
def sync(nom, ref="HF", fenetre=8.0):
    c = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    k = f"{nom}|{ref}"
    if k in c: return c[k]
    x = next(r for r in json.load(open(f"{T}/chrono.json")) if r["nom"] == nom)
    w = f"{T}/son/clips/{nom}.wav"
    if not os.path.exists(w): subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/{x['fichier']}", "-vn", "-ac", "1", "-ar", "16000", w])
    yb = librosa.load(w, sr=SR)[0]; b = env(yb)
    if ref == "HF":
        est = x["t0"] - HF0; off = max(0, est - fenetre); y = librosa.load(f"{T}/son/REC052_16k.wav", sr=SR, offset=off, duration=x["duree_s"] + 2 * fenetre)[0]; base = off
    else:
        n, s = max((z for z in Z if z[1] <= x["t0"]), key=lambda z: z[1]); est = x["t0"] - s; off = max(0, est - fenetre)
        y = librosa.load(f"{T}/son/{n}_16k.wav", sr=SR, offset=off, duration=x["duree_s"] + 2 * fenetre)[0]; base = s + off
    a = env(y); cc = fftconvolve(a, b[::-1], mode="full") / len(b); i = int(np.argmax(cc)); lag = (i - (len(b) - 1)) / 100
    m = cc.copy(); m[max(0, i - 100):i + 100] = -np.inf
    res = {"decalage": round(base + lag, 3), "pic": round(float(cc.max()), 3), "nettete": round(float(m.max() / cc.max()), 2)}
    c[k] = res; json.dump(c, open(CACHE, "w"), indent=0); return res
if __name__ == "__main__":
    import sys
    for n in sys.argv[2:]: print(n, sync(n, sys.argv[1]))
