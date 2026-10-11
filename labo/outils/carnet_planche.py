"""Planche du carnet de goût : plusieurs images (rendu:temps ou fichier image), côte à côte, légendées, JPG < 200 Ko.
Usage : python carnet_planche.py sortie.jpg "video.mp4@12.3|légende" "image.png|légende" [...] [--h 900] [--crop x,y,w,h sur un élément: "video@t|légende|x,y,w,h"]
"""
import sys, subprocess, io, os
from PIL import Image, ImageDraw, ImageFont

def frame(video, t):
    out = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", video, "-frames:v", "1",
                          "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(out)).convert("RGB")

def main():
    args = sys.argv[1:]
    out = args.pop(0)
    H = 900
    if "--h" in args:
        i = args.index("--h"); H = int(args[i + 1]); del args[i:i + 2]
    tiles = []
    font = None
    for p in ["/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc"]:
        if os.path.exists(p):
            font = ImageFont.truetype(p, 26); break
    for a in args:
        parts = a.split("|")
        src, label = parts[0], (parts[1] if len(parts) > 1 else "")
        if "@" in src and not os.path.exists(src):
            v, t = src.rsplit("@", 1); im = frame(v, float(t))
        else:
            im = Image.open(src).convert("RGB")
        if len(parts) > 2 and parts[2]:
            x, y, w, h = map(int, parts[2].split(",")); im = im.crop((x, y, x + w, y + h))
        im = im.resize((round(im.width * H / im.height), H), Image.LANCZOS)
        canvas = Image.new("RGB", (im.width, H + 70), (20, 20, 20))
        canvas.paste(im, (0, 0))
        d = ImageDraw.Draw(canvas)
        d.text((12, H + 18), label, fill=(235, 235, 235), font=font)
        tiles.append(canvas)
    W = sum(t.width for t in tiles) + 8 * (len(tiles) - 1)
    sheet = Image.new("RGB", (W, H + 70), (0, 0, 0))
    x = 0
    for t in tiles:
        sheet.paste(t, (x, 0)); x += t.width + 8
    q = 88
    while True:
        b = io.BytesIO(); sheet.save(b, "JPEG", quality=q, optimize=True)
        if b.tell() < 195_000 or q <= 30:
            break
        q -= 6
        if q < 50:
            sheet = sheet.resize((int(sheet.width * 0.85), int(sheet.height * 0.85)), Image.LANCZOS)
    open(out, "wb").write(b.getvalue())
    print(out, sheet.size, b.tell(), "q", q)

main()
