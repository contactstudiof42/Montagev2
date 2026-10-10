#!/usr/bin/env python3
"""Planche par version : pour chaque coupe, la paire « dernière image avant / première après ».
Usage : python3 planche.py RENDUS VERSION SORTIE.png"""
import json, subprocess, sys, io
from PIL import Image, ImageDraw, ImageFont
R, V, OUT = sys.argv[1:4]
ev = json.load(open(f"{R}/{V}-events.json"))
FPS = 25
def img_at(t):
    b = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", f"{R}/{V}.mp4", "-frames:v", "1",
                        "-vf", "scale=240:-1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(b)).convert("RGB")
paires = [(e["t"] - 1.5 / FPS, e["t"] + 0.5 / FPS, e["type"]) for e in ev["detail"]]
tw, th = 240, 135
fnt = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 13)
sheet = Image.new("RGB", (2 * tw + 140, (th + 4) * len(paires) + 30), (20, 20, 20))
d = ImageDraw.Draw(sheet)
d.text((6, 6), f"{V} : {ev['evenements']} év. / {ev['duree_s']} s = {ev['par_minute']}/min", font=fnt, fill=(240, 240, 240))
for k, (ta, tb, typ) in enumerate(paires):
    y = 30 + k * (th + 4)
    sheet.paste(img_at(ta), (0, y)); sheet.paste(img_at(tb), (tw + 4, y))
    d.text((2 * tw + 10, y + 50), f"{tb:.2f} s\n{typ}", font=fnt, fill=(240, 220, 120))
sheet.save(OUT, optimize=True)
