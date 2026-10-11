# decalage.py DOSSIER : écart signé (en images) entre chaque coupe vue et l'attaque forte la plus proche (musique séparée et mix)
import sys, json, numpy as np, librosa
D = sys.argv[1]; c = json.load(open(f"{D}/coupes_oeil.json")); fps = c["fps"]; cuts = np.array(c["coupes"])
for src in ("sep/htdemucs/audio/no_vocals.wav", "audio.wav"):
    y, sr = librosa.load(f"{D}/{src}", sr=22050, mono=True); hop = 128
    env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    pk = librosa.util.peak_pick(env, pre_max=6, post_max=6, pre_avg=20, post_avg=20, delta=0, wait=8)
    f = librosa.frames_to_time(pk[env[pk] >= np.percentile(env, 90)], sr=sr, hop_length=hop)
    d = [(f[np.argmin(np.abs(f - t))] - t) * fps for t in cuts]
    print(src.split('/')[-1], "écarts (attaque - coupe, images ; + = l'attaque suit la coupe) :", " ".join(f"{x:+.1f}" for x in d))
    a = np.array(d); a = a[np.abs(a) <= 4]; print("   |écart|<=4 :", len(a), "/", len(d), " médiane", f"{np.median(a):+.1f}" if len(a) else "-")
