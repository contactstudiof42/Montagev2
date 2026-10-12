# synchro_audio.py REF.wav CIBLE.wav [debut_s fin_s] : où CIBLE commence dans REF (s), corrélation du flux spectral mel (100 Hz),
# fenêtre de recherche optionnelle dans REF ; netteté = 2e pic hors ±1 s / pic (bon < 0,6)
import sys, numpy as np, librosa
from scipy.signal import fftconvolve
SR, HOP = 16000, 160
def env(f, off=0, dur=None):
    y, _ = librosa.load(f, sr=SR, mono=True, offset=off, duration=dur)
    o = librosa.onset.onset_strength(y=y, sr=SR, hop_length=HOP, n_mels=64, fmax=7000)
    o = o - np.convolve(o, np.ones(50) / 50, mode="same"); return (o - o.mean()) / (o.std() + 1e-9)
off = float(sys.argv[3]) if len(sys.argv) > 4 else 0; dur = float(sys.argv[4]) - off if len(sys.argv) > 4 else None
a, b = env(sys.argv[1], off, dur), env(sys.argv[2])
c = fftconvolve(a, b[::-1], mode="full") / len(b); i = int(np.argmax(c)); lag = i - (len(b) - 1)
m = c.copy(); m[max(0, i - 100):i + 100] = -np.inf
print(f"{off + lag / 100:.2f} {c.max():.3f} {m.max() / c.max():.2f}")
