# Pièce 01 v4 — design sonore synthétique (aucun média externe) : inspiration / rétention quasi silencieuse / expiration.
# python3 souffle_son.py <sortie.wav> [silence]   (« silence » : variante b, rétention sans grondement, simple air très bas)
import sys, wave, numpy as np
SR, D = 48000, 10.0
I, H = 3.0, 7.52                      # fin inspiration, fin rétention (cale sur l'image : 75 et 188 à 25 i/s)
rng = np.random.default_rng(42); n = int(SR*D); t = np.arange(n)/SR
def bande(lo, hi, pente=0.5):
    """bruit coloré (1/f^pente) limité à une bande lo-hi, par FFT"""
    X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1/SR); f[0] = 1
    X *= 1/f**pente; X *= np.exp(-0.5*((np.log(f)-np.log(np.sqrt(lo*hi)))/(np.log(hi/lo)/2))**2)
    x = np.fft.irfft(X, n); return x/np.max(np.abs(x))
inspi, expi, grave = bande(900, 4500), bande(250, 2200), bande(25, 110, 1.0)
env_i = np.where(t < I, (np.clip(t/I, 0, 1)**1.6) * np.clip((I-t)/0.18, 0, 1), 0)        # crescendo, arrêt net (on retient)
x = t - H
env_e = np.where(x > 0, np.clip(x/0.12, 0, 1) * np.exp(-np.clip(x, 0, None)*1.3), 0)    # attaque brève, longue décroissance
env_g = np.where((t > I) & (t < H+0.6), ((t-I)/(H-I)).clip(0, 1)**2 * np.clip((H+0.6-t)/0.6, 0, 1), 0)  # pression qui monte, coupée par l'expiration
if len(sys.argv) > 2 and sys.argv[2] == "silence":
    env_g = np.full(n, 0.12)                     # air de pièce constant, à peine audible : le silence n'est pas une panne
y = 0.55*env_i*inspi + 0.75*env_e*expi + 0.10*env_g*grave
y = y/np.max(np.abs(y))*0.5
st = np.stack([y, np.roll(y, 12)], 1)                                                   # micro-décalage = un peu d'air
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes())
