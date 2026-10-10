"""Fabrique un faux rush de téléphone en cadence variable (VFR) avec une vérité terrain de synchro.
- 0-3 s : 30 i/s réguliers ; 3-8 s : « basse lumière », intervalles de 1/30 à 1/20 s avec gigue (moyenne ~24 i/s) ;
  8-10 s : 30 i/s. Un flash blanc sur l'image dont l'horodatage est le plus proche de 5,000 s, un clic audio à 5,000 s.
Sortie : vfr.mp4 (H.264 + AAC, horodatages conservés) et verite.json.  Usage : python3 fabrique_vfr.py <dossier_rendus>"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw
out = sys.argv[1]; os.makedirs(f"{out}/img", exist_ok=True)
rng = np.random.default_rng(3); t, ts = 0.0, []
while t < 10.0:
    ts.append(t)
    t += 1 / 30 if (t < 3 or t >= 8) else rng.uniform(1 / 30, 1 / 20)
ts = np.array(ts); iflash = int(np.argmin(abs(ts - 5.0)))
for i, x in enumerate(ts):
    im = Image.new("RGB", (320, 180), (255, 255, 255) if i == iflash else (30, 30, 40))
    ImageDraw.Draw(im).text((10, 10), f"{i:04d}  {x:.3f}s", fill=(200, 60, 60)); im.save(f"{out}/img/{i:04d}.png")
with open(f"{out}/liste.txt", "w") as f:  # concat : une durée par image = horodatages exacts
    f.write("ffconcat version 1.0\n")
    for i in range(len(ts)):
        f.write(f"file img/{i:04d}.png\noption framerate 90000\nduration {(ts[i + 1] if i + 1 < len(ts) else 10.0) - ts[i]:.6f}\n")
    f.write(f"file img/{len(ts) - 1:04d}.png\noption framerate 90000\n")
sr = 48000; a = np.zeros(sr * 10, np.float32); k = int(5.0 * sr); a[k:k + 480] = 0.8 * np.sin(2 * np.pi * 1000 * np.arange(480) / sr)
a.tofile(f"{out}/clic.f32")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{out}/liste.txt", "-f", "f32le", "-ar", str(sr), "-ac", "1",
                "-i", f"{out}/clic.f32", "-fps_mode", "vfr", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
                "-video_track_timescale", "90000", f"{out}/vfr.mp4"], check=True)
v = dict(n_images=len(ts), i_flash=iflash, t_flash=round(float(ts[iflash]), 4), t_clic=5.0,
         ecart_verite_ms=round(1000 * (float(ts[iflash]) - 5.0), 1), cadence_moyenne=round(len(ts) / 10, 2))
json.dump(v, open("verite.json", "w"), indent=1); print(v)
