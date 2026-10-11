"""Tempo, temps, mesures, énergie par mesure et ruptures d'une musique (pour la monter).
Usage : analyse_musique.py musique.mp3 dossier_sortie
"""
import sys, json
import numpy as np, librosa
from PIL import Image, ImageDraw
f, out = sys.argv[1], sys.argv[2]
y, sr = librosa.load(f, sr=22050, mono=True)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units="time")
tempo = float(np.atleast_1d(tempo)[0])
onset = librosa.onset.onset_strength(y=y, sr=sr)
on_t = librosa.onset.onset_detect(onset_envelope=onset, sr=sr, units="time", backtrack=False)
rms = librosa.feature.rms(y=y)[0]; t_rms = librosa.times_like(rms, sr=sr)
db = 20 * np.log10(rms + 1e-9)
# bandes : basses (<150 Hz) et aigus (>4 kHz)
S = np.abs(librosa.stft(y)); fr = librosa.fft_frequencies(sr=sr)
low = 20*np.log10(S[fr < 150].mean(0) + 1e-9); high = 20*np.log10(S[fr > 4000].mean(0) + 1e-9)
# ruptures : nouveauté sur le chroma + mfcc
feat = np.vstack([librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), librosa.feature.chroma_cqt(y=y, sr=sr)])
bounds = librosa.segment.agglomerative(feat, 12); b_t = librosa.frames_to_time(bounds, sr=sr)
bars = beats[::4]
rows = []
for i, b in enumerate(bars):
    e = bars[i+1] if i+1 < len(bars) else len(y)/sr
    m = (t_rms >= b) & (t_rms < e)
    rows.append(dict(mesure=i+1, debut=round(float(b), 3), db=round(float(db[m].mean()), 1),
                     basses=round(float(low[m].mean()), 1), aigus=round(float(high[m].mean()), 1)))
json.dump(dict(tempo=tempo, duree=len(y)/sr, temps=[round(float(x), 3) for x in beats],
               attaques=[round(float(x), 3) for x in on_t], ruptures=[round(float(x), 2) for x in b_t], mesures=rows),
          open(f"{out}/musique.json", "w"), indent=1)
print(f"tempo {tempo:.1f} BPM, {len(beats)} temps, durée {len(y)/sr:.1f} s")
print("ruptures :", [round(float(x), 1) for x in b_t])
for r in rows: print(r["mesure"], r["debut"], r["db"], r["basses"], r["aigus"], "#" * int(max(0, r["db"] + 40)))
# image : spectrogramme + RMS + mesures
D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=2048, hop_length=512)), ref=np.max)
Dm = librosa.feature.melspectrogram(S=np.abs(librosa.stft(y))**2, sr=sr, n_mels=128)
img = librosa.power_to_db(Dm, ref=np.max)[::-1]
img = ((img + 80) / 80 * 255).clip(0, 255).astype(np.uint8)
W = 1600; im = Image.fromarray(img).resize((W, 256)).convert("RGB")
c = Image.new("RGB", (W, 340), "black"); c.paste(im, (0, 0)); d = ImageDraw.Draw(c)
dur = len(y) / sr
pts = [(int(t / dur * W), 336 - int(max(0, v + 50) * 1.6)) for t, v in zip(t_rms[::10], db[::10])]
d.line(pts, fill=(255, 200, 0))
for i, b in enumerate(bars):
    x = int(b / dur * W); d.line([(x, 256), (x, 262)], fill="white")
    if i % 4 == 0: d.text((x + 1, 262), str(i + 1), fill="white")
for b in b_t:
    x = int(b / dur * W); d.line([(x, 0), (x, 256)], fill=(255, 0, 0))
for s in range(0, int(dur), 10):
    d.text((int(s / dur * W) + 1, 2), f"{s}s", fill="cyan")
c.save(f"{out}/musique.png")
