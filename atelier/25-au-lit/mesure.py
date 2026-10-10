#!/usr/bin/env python3
"""Mesures par tranche de 5 s (YAVG, LUFS court terme, fin de voix) + bande-film.
Usage : python3 mesure.py RENDUS V1,V2,... SORTIE.png"""
import json, re, subprocess, sys, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont
R, VS, OUT = sys.argv[1], sys.argv[2].split(","), sys.argv[3]
fnt = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 12)
rows, res = [], {}
for v in VS:
    f = f"{R}/{v}.mp4"
    y = subprocess.run(["ffprobe", "-v", "error", "-f", "lavfi", f"movie={f},signalstats", "-show_entries",
                        "frame_tags=lavfi.signalstats.YAVG", "-of", "csv=p=0"], capture_output=True, text=True).stdout.split()
    y = np.array([float(x.strip(",")) for x in y if x.strip(",")])
    yav = [round(float(y[i * 75:(i + 1) * 75].mean()), 1) for i in range(12)]  # 15 i/s × 5 s
    e = subprocess.run(["ffmpeg", "-nostats", "-i", f, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [(float(a), float(b)) for a, b in re.findall(r"t:\s*([\d.]+).*?S:\s*(-?[\d.]+)", e)]
    lufs = []
    for i in range(12):
        vals = [s for t, s in st if i * 5 + 4.5 <= t < i * 5 + 5.5]  # S (3 s) en fin de tranche
        lufs.append(round(vals[0], 1) if vals else None)
    res[v] = {"YAVG_par_5s": yav, "LUFS_S_par_5s": lufs}
    strip = Image.new("RGB", (12 * 107, 60))
    for i in range(12):
        b = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", str(i * 5 + 2.5), "-i", f, "-frames:v", "1",
                            "-vf", "scale=106:60", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
        strip.paste(Image.open(io.BytesIO(b)).convert("RGB"), (i * 107, 0))
    rows.append((v, strip, yav, lufs))
sheet = Image.new("RGB", (12 * 107 + 10, len(rows) * 175 + 10), (18, 18, 18))
d = ImageDraw.Draw(sheet)
for k, (v, strip, yav, lufs) in enumerate(rows):
    y0 = 10 + k * 175
    d.text((4, y0), f"{v}  (1 image toutes les 5 s ; courbe jaune = YAVG 0-120 ; bleue = LUFS S -40..-15)", font=fnt, fill=(230, 230, 230))
    sheet.paste(strip, (5, y0 + 16))
    def pts(vals, lo, hi):
        return [(5 + i * 107 + 53, y0 + 170 - 90 * ((x - lo) / (hi - lo))) for i, x in enumerate(vals) if x is not None]
    d.line(pts(yav, 0, 120), fill=(240, 210, 60), width=2)
    d.line(pts(lufs, -40, -15), fill=(90, 160, 240), width=2)
sheet.save(OUT, optimize=True)
json.dump(res, open(OUT.replace(".png", ".json"), "w"), indent=1)
for v in res: print(v, res[v])
