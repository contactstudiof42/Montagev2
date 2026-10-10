"""Son de la pièce 07 : uniquement les sons des objets, placés depuis la simulation (sim.json + evenements.json).
Roulement = bruit filtré dont l'amplitude suit la vitesse de la bille ; clics = contacts entre dominos ;
tasse = poussée (petit tintement), choc au sol (tintement inharmonique + coup sourd). Puis le silence (souffle de pièce).
Usage : python3 son.py sim.json evenements.json sortie.wav [duree_s]"""
import json, sys, wave, numpy as np
sim = json.load(open(sys.argv[1]))["rec"]; ev = json.load(open(sys.argv[2])); out = sys.argv[3]
SR, FPS = 48000, 25; dur = float(sys.argv[4]) if len(sys.argv) > 4 else 4.4
n = int(SR * dur); y = np.zeros(n); rng = np.random.default_rng(3)
t_of = lambda f: (f - 1) / FPS

def lp(x, a):  # passe-bas à un pôle
    o = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x): acc += a * (v - acc); o[i] = acc
    return o

# 1. Roulement : vitesse de la bille par image -> enveloppe, uniquement quand elle touche une surface (z bas)
pos = np.array([r["bille"][0] for r in sim]); v = np.r_[0, np.linalg.norm(np.diff(pos, axis=0), axis=1) * FPS]
contact = pos[:, 2] < 0.85  # sur le livre ou la table (en l'air au-dessus = rien)
env_f = np.where(contact, np.clip(v / 0.6, 0, 1), 0)
env = np.interp(np.arange(n) / SR, np.arange(len(env_f)) / FPS, env_f)
bruit = rng.standard_normal(n); roul = lp(bruit, 0.08) - lp(bruit, 0.01)  # bande grave-medium
roul *= 1 + 0.3 * np.sin(2 * np.pi * 9 * np.arange(n) / SR)  # petite irrégularité du roulement
y += 0.25 * roul * env

def burst(t, gain, f0, dec, bruit_part=0.5):
    i = int(t * SR); m = int(0.25 * SR); tt = np.arange(m) / SR
    s = (1 - bruit_part) * np.sin(2 * np.pi * f0 * tt) + bruit_part * lp(rng.standard_normal(m), 0.5)
    s *= np.exp(-tt / dec); j = min(n, i + m); y[i:j] += gain * s[:j - i]

# 2. Contacts : bille -> domino0, puis domino i -> i+1 (images "bouge"), et chaque domino qui se couche
doms = sorted(k for k in ev if k.startswith("domino") and k.endswith("_bouge"))
for k, kk in enumerate(doms):
    burst(t_of(ev[kk]), 0.5 if k == 0 else 0.32, 2600 + 90 * k, 0.012, 0.6)
for kk in (k for k in ev if k.endswith("_couche") and ev[k]):
    burst(t_of(ev[kk]), 0.18, 1500, 0.02, 0.8)
# 3. Tasse : poussée (tintement léger), puis choc au sol (partiels inharmoniques + coup sourd)
burst(t_of(ev["tasse_bouge"]), 0.2, 3100, 0.05, 0.2)
ts = t_of(ev["tasse_sol"]); i = int(ts * SR); m = int(1.2 * SR); tt = np.arange(m) / SR
ch = sum(a * np.sin(2 * np.pi * f * tt) * np.exp(-tt / d) for f, a, d in ((2140, .5, .35), (3410, .35, .22), (5230, .2, .12), (7100, .1, .06)))
ch += 0.9 * np.sin(2 * np.pi * 95 * tt) * np.exp(-tt / 0.05)  # le sol
j = min(n, i + m); y[i:j] += 0.6 * ch[:j - i]
# 4. Souffle de pièce, très bas, partout (un silence numérique se lit comme une panne)
y += 0.002 * lp(rng.standard_normal(n), 0.05)
y = y / np.max(np.abs(y)) * 10 ** (-3 / 20)
w = wave.open(out, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((y * 32767).astype(np.int16).tobytes()); w.close()
print("son", out, "contacts:", [ev[k] for k in doms], "tasse", ev["tasse_bouge"], ev["tasse_sol"])
