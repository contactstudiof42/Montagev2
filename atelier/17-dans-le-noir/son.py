"""Son de la pièce 17 (synthétique, aucune licence tierce) : python3 son.py sortie.wav
0-3 s : pièce (souffle de fond très bas) + petits geignements du bébé (bruit filtré, rapides, irréguliers)
3 s   : un toucher d'écran (clic très doux) ; puis une voix lointaine figurée par un murmure filtré passe-bande (pas de mots)
3-10 s: le souffle du bébé ralentit avec le bercement (même loi de phase intégrée que l'image) ; geignements qui s'espacent puis cessent."""
import sys, numpy as np, wave
sr = 48000; T = 10.0; n = int(sr * T); t = np.arange(n) / sr; rng = np.random.default_rng(17)
def bruit_filtre(lo, hi, m):
    x = rng.standard_normal(m); X = np.fft.rfft(x); f = np.fft.rfftfreq(m, 1 / sr); X[(f < lo) | (f > hi)] = 0; y = np.fft.irfft(X, m); return y / (np.abs(y).max() + 1e-9)
out = np.zeros(n)
out += 0.02 * bruit_filtre(40, 400, n)                     # fond de pièce
# phase du bercement (identique à scene.py v3+) -> le souffle suit
aa = 1.6 / 4; ph = np.where(t <= 3.5, t / 1.6, 3.5 / 1.6 + np.log((1.6 + aa * np.clip(t - 3.5, 0, 4)) / 1.6) / aa + np.clip(t - 7.5, 0, None) / 3.2)
souffle = bruit_filtre(300, 2500, n) * (0.5 + 0.5 * np.sin(2 * np.pi * ph)) ** 3   # une inspiration par balancement
amp_s = np.where(t < 3.5, 0.10, 0.10 - 0.05 * np.clip((t - 3.5) / 4, 0, 1)); out += amp_s * souffle
# geignements : rapprochés avant 3 s, espacés ensuite, aucun après 6 s
for t0 in [0.4, 1.1, 1.6, 2.3, 2.7, 3.9, 5.2]:
    i0 = int(t0 * sr); m = int(0.35 * sr); env = np.sin(np.linspace(0, np.pi, m)) ** 2
    f0 = 420 + 60 * rng.random(); tt = np.arange(m) / sr; voix = np.sin(2 * np.pi * (f0 * tt + 30 * tt ** 2)) * 0.6 + 0.4 * bruit_filtre(500, 3000, m)
    out[i0:i0 + m] += (0.12 if t0 < 3 else 0.06) * env * voix
# toucher d'écran
i0 = int(3.0 * sr); m = int(0.02 * sr); out[i0:i0 + m] += 0.08 * bruit_filtre(1500, 6000, m) * np.exp(-np.linspace(0, 8, m))
# voix lointaine (murmure, 3,4-8 s), passe-bande téléphone 300-3400 Hz, modulée en syllabes lentes
i0, i1 = int(3.4 * sr), int(8.0 * sr); m = i1 - i0; tt = np.arange(m) / sr
syl = (0.5 + 0.5 * np.sin(2 * np.pi * 3.2 * tt + 2 * np.sin(2 * np.pi * 0.7 * tt))) ** 2 * np.clip(np.minimum(tt, (m / sr) - tt) / 0.4, 0, 1)
out[i0:i1] += 0.05 * syl * bruit_filtre(300, 3400, m)
out = out / np.abs(out).max() * 0.5
w = wave.open(sys.argv[1], "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out * 32767).astype("<i2").tobytes()); w.close()
