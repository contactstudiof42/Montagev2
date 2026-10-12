# musique.py FICHIER.wav : tempo, temps, sections (changements de timbre), courbe d'énergie par 2 s
import sys, numpy as np, librosa
y, sr = librosa.load(sys.argv[1], sr=22050, mono=True)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units="time")
rms = librosa.feature.rms(y=y, hop_length=512)[0]; t = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=512)
mf = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13); bounds = librosa.segment.agglomerative(mf, 10); bt = librosa.frames_to_time(bounds, sr=sr)
print(f"durée {len(y)/sr:.1f} s, tempo {float(np.atleast_1d(tempo)[0]):.1f}, {len(beats)} temps, premier temps {beats[0]:.2f} s, intervalle médian {np.median(np.diff(beats)):.3f} s")
print("sections :", " ".join(f"{b:.1f}" for b in bt))
db = 20 * np.log10(rms + 1e-6)
print("énergie par 4 s (dB) :", " ".join(f"{int(s)}:{db[(t>=s)&(t<s+4)].mean():.0f}" for s in range(0, int(len(y)/sr), 4)))
