#!/usr/bin/env python3
"""Calage des coupes sur la musique d'une séquence (phase 2, Whiplash). Compare les coupes aux temps (beat_track)
et aux attaques fortes (pics de l'enveloppe d'onsets au-dessus d'un percentile), contre un hasard mesuré :
les mêmes coupes décalées au hasard dans la séquence (2 000 tirages), ce qui garde leur nombre et leur densité.
Usage : calage.py DOSSIER DEBUT FIN [tolérance_images=2] [percentile=90]   (DEBUT/FIN en h:mm:ss ; lit DOSSIER/proxy.mp4
et DOSSIER/coupes.json ; lancer avec .venv/bin/python -I). Sortie : tempo, part des coupes à ± tolérance d'une attaque
forte ou d'un temps, et la même part attendue au hasard (moyenne, 5e et 95e centiles : sous le 5e = les coupes ÉVITENT les attaques).
Limite : sur un tempo très rapide (> 200 BPM), un temps tombe toutes les 5-6 images : le calage « au temps » ne prouve
rien ; seule la comparaison aux attaques fortes (accents) et au hasard compte."""
import sys, json, os, subprocess, numpy as np, librosa
D, a, b = sys.argv[1:4]; tol_i = int(sys.argv[4]) if len(sys.argv) > 4 else 2; pc = float(sys.argv[5]) if len(sys.argv) > 5 else 90
sec = lambda s: sum(float(x) * 60**i for i, x in enumerate(reversed(s.split(':'))))
A, B = sec(a), sec(b); fps = 24000 / 1001; tol = tol_i / fps
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(A), "-t", str(B - A), "-i", os.path.join(D, "proxy.mp4"),
                      "-vn", "-ac", "1", "-ar", "22050", "-f", "f32le", "-"], capture_output=True).stdout
y = np.frombuffer(raw, np.float32); sr = 22050
env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=256)
tempo, beats = librosa.beat.beat_track(onset_envelope=env, sr=sr, hop_length=256, units='time')
pk = librosa.util.peak_pick(env, pre_max=3, post_max=3, pre_avg=10, post_avg=10, delta=0, wait=4)
pk = pk[env[pk] >= np.percentile(env, pc)]; fort = librosa.frames_to_time(pk, sr=sr, hop_length=256)
c = np.array([t for t in json.load(open(os.path.join(D, "coupes.json")))["coupes"] if A + 0.5 < t < B - 0.5]) - A
def part(cs, ref): return float(np.mean([np.min(np.abs(ref - x)) <= tol for x in cs])) if len(cs) and len(ref) else 0
rng = np.random.default_rng(0); L = B - A
def hasard(ref):
    v = [part(np.mod(c + rng.uniform(0, L), L), ref) for _ in range(2000)]; return np.mean(v), np.percentile(v, 95), np.percentile(v, 5)
hf, hb = hasard(fort), hasard(beats)
print(f"{a}-{b} : {len(c)} coupes, tempo {float(np.atleast_1d(tempo)[0]):.0f} BPM, {len(fort)} attaques fortes (>{pc:.0f}e centile), tolérance ±{tol_i} images")
print(f"  sur une attaque forte : {part(c, fort):.0%} (hasard {hf[0]:.0%}, 5e-95e centile {hf[2]:.0%}-{hf[1]:.0%})")
print(f"  sur un temps          : {part(c, beats):.0%} (hasard {hb[0]:.0%}, 5e-95e centile {hb[2]:.0%}-{hb[1]:.0%})")
