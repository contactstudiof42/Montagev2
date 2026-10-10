#!/usr/bin/env python3
"""Planche d'une vidéo analysée : une vignette par plan (image du milieu), annotée
(n°, début, durée), puis sous la grille une ligne de temps commune : volume court terme
(LUFS, fenêtre 3 s), coupes (traits) et temps musicaux (librosa).

Usage : python -I planche.py <video> <mesures.json d'analyse_clip.py> <sortie.png> [colonnes]
Le PNG est réduit en palette pour rester sous 500 Ko (règle du dépôt)."""
import sys, json, subprocess, io, re, numpy as np
from PIL import Image, ImageDraw, ImageFont

def image_a(video, t, w=320):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", video, "-frames:v", "1",
                          "-vf", f"scale={w}:-2", "-f", "image2pipe", "-vcodec", "png", "-"],
                         capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(raw)).convert("RGB")

def volume_court_terme(video):
    """LUFS court terme (3 s) toutes les 100 ms, via le filtre ebur128."""
    log = subprocess.run(["ffmpeg", "-nostats", "-i", video, "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    pts = re.findall(r"t:\s*([\d.]+).*?S:\s*(-?[\d.]+|-inf)", log)
    return np.array([(float(t), float(s) if s != "-inf" else -70.0) for t, s in pts])

def temps_musicaux(video):
    import librosa
    wav = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", video, "-vn", "-ac", "1", "-ar", "22050",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    y = np.frombuffer(wav, np.float32)
    return librosa.frames_to_time(librosa.beat.beat_track(y=y, sr=22050)[1], sr=22050)

def main(video, mesures, sortie, cols=6):
    m = json.load(open(mesures)); dur = m["duree_s"]
    bords = [0.0] + m["coupes_s"] + [dur]
    plans = [(a, b) for a, b in zip(bords[:-1], bords[1:])]
    vign = [image_a(video, (a + b) / 2) for a, b in plans]
    w, h = vign[0].size; pad, leg = 6, 18
    rows = -(-len(vign) // cols); W = cols * (w + pad) + pad
    H_grille = rows * (h + leg + pad) + pad; H_courbe = 170
    img = Image.new("RGB", (W, H_grille + H_courbe), (18, 18, 18)); d = ImageDraw.Draw(img)
    try: f = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
    except OSError: f = ImageFont.load_default()
    for i, ((a, b), v) in enumerate(zip(plans, vign)):
        x = pad + (i % cols) * (w + pad); y = pad + (i // cols) * (h + leg + pad)
        img.paste(v, (x, y))
        d.text((x + 2, y + h + 2), f"{i+1}  {int(a)//60}:{a%60:05.2f}  ({b-a:.1f} s)", fill=(230, 230, 230), font=f)
    # ligne de temps
    x0, x1, y0, y1 = 40, W - 10, H_grille + 20, H_grille + H_courbe - 25
    X = lambda t: x0 + (x1 - x0) * t / dur
    lu = volume_court_terme(video)
    if len(lu):
        Y = lambda s: y1 - (y1 - y0) * (np.clip(s, -40, -5) + 40) / 35
        d.line([(X(t), Y(s)) for t, s in lu], fill=(90, 170, 255), width=2)
        for s in (-30, -20, -10):
            d.text((4, Y(s) - 7), f"{s}", fill=(120, 120, 120), font=f)
    for t in temps_musicaux(video):
        d.line([(X(t), y1 + 2), (X(t), y1 + 7)], fill=(140, 140, 140))
    for t in m["coupes_s"]:
        d.line([(X(t), y0), (X(t), y1)], fill=(255, 120, 60), width=1)
    for s in range(0, int(dur) + 1, 15):
        d.text((X(s) - 8, y1 + 9), f"{s//60}:{s%60:02d}", fill=(160, 160, 160), font=f)
    d.text((x0, H_grille + 3), "bleu : volume court terme (LUFS)   orange : coupes   gris : temps musicaux",
           fill=(200, 200, 200), font=f)
    for n in (128, 96, 64, 48):  # moins de couleurs jusqu'à passer sous 500 000 octets
        buf = io.BytesIO(); img.quantize(colors=n, method=Image.Quantize.MEDIANCUT).save(buf, "PNG", optimize=True)
        if buf.tell() < 500_000: break
    open(sortie, "wb").write(buf.getvalue())

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 6)
