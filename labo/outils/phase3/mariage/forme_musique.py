# forme_musique.py SORTIE.png F1.wav [F2.wav ...] : pour chaque morceau, forme d'onde (RMS), centroïde spectral, densité d'attaques, graduation en s
import sys, numpy as np, librosa
from PIL import Image, ImageDraw
out, fs = sys.argv[1], sys.argv[2:]; W, H = 1800, 150; rows = []
for f in fs:
    y, sr = librosa.load(f, sr=22050, mono=True); L = len(y) / sr
    rms = librosa.feature.rms(y=y, hop_length=512)[0]; cen = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=512)[0]
    on = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512); t = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=512)
    im = Image.new("RGB", (W, H), (15, 15, 15)); d = ImageDraw.Draw(im); px = W / L
    r = rms / rms.max(); c = np.clip(cen / 5000, 0, 1); o = on / np.percentile(on, 99)
    for i in range(0, len(t), 2):
        x = int(t[i] * px); h = int(r[i] * 60)
        d.line([(x, 70 - h), (x, 70 + h)], fill=(int(80 + 175 * c[i]), 160, int(255 - 175 * c[i])))
    k = int(sr / 512 * 2)
    for j in range(0, len(o) - k, k):
        x = int(t[j] * px); dens = o[j:j + k].mean(); d.line([(x, H - 5), (x, H - 5 - int(30 * min(dens, 1.5)))], fill=(230, 200, 0))
    for s in range(0, int(L), 10): d.text((int(s * px) + 2, 2), str(s), fill=(255, 255, 255)); d.line([(int(s * px), 0), (int(s * px), H)], fill=(60, 60, 60))
    d.text((W - 200, 2), f.split("/")[-1][:28], fill=(255, 255, 0)); rows.append(im)
g = Image.new("RGB", (W, H * len(rows))); [g.paste(im, (0, i * H)) for i, im in enumerate(rows)]; g.save(out); print(out)
