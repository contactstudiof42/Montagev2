"""Planches pour le directeur artistique : rangées d'images extraites de vidéos (ou d'images fixes), annotées.

Usage :
  planche_da.py spec.json
spec = {"sortie": "x.jpg", "hauteur": 540, "rangees": [[{"src": "film.mp4", "t": 12.3, "label": "V3b 0:12"} | {"img": "ref.jpg", "label": "..."}, ...], ...]}
Chaque image est mise à la hauteur commune (largeur selon son format) ; JPEG qualité 88.
"""
import json, subprocess, sys, io
from PIL import Image, ImageDraw, ImageFont

def frame(src, t, h):
    out = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", src, "-frames:v", "1",
                          "-vf", f"scale=-2:{h}:flags=lanczos", "-f", "image2pipe", "-vcodec", "png", "-"],
                         capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(out)).convert("RGB")

def charge(e, h):
    if "img" in e:
        im = Image.open(e["img"]).convert("RGB")
        return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    return frame(e["src"], e["t"], h)

def main(spec):
    h = spec.get("hauteur", 540)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", max(14, h // 22))
    except OSError:
        font = ImageFont.load_default()
    rangees = []
    for r in spec["rangees"]:
        ims = [(charge(e, h), e.get("label", "")) for e in r]
        w = sum(i.width for i, _ in ims) + 8 * (len(ims) - 1)
        rg = Image.new("RGB", (w, h), (20, 20, 20))
        x = 0
        for im, lab in ims:
            rg.paste(im, (x, 0))
            if lab:
                d = ImageDraw.Draw(rg)
                tw = d.textlength(lab, font=font)
                d.rectangle([x, 0, x + tw + 10, font.size + 8], fill=(0, 0, 0))
                d.text((x + 5, 3), lab, fill=(255, 220, 80), font=font)
            x += im.width + 8
        rangees.append(rg)
    W = max(r.width for r in rangees)
    H = sum(r.height for r in rangees) + 8 * (len(rangees) - 1)
    pl = Image.new("RGB", (W, H), (20, 20, 20))
    y = 0
    for r in rangees:
        pl.paste(r, (0, y)); y += r.height + 8
    pl.save(spec["sortie"], quality=88)
    print(spec["sortie"], pl.size)

if __name__ == "__main__":
    main(json.load(open(sys.argv[1])))
