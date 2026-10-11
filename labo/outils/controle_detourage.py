"""Contrôle d'un détourage (règle de Diego du 2026-10-11 : un détourage se juge au bord, à 200 %).

Pour chaque masque : le masque seul, le sujet sur noir, sur blanc, sur magenta (vignettes), puis trois bords agrandis à 200 %
(point le plus haut du sujet = cheveux ; bords gauche et droit à mi-hauteur = épaules, bras) sur fond magenta.
Usage : python controle_detourage.py SOURCE.png SORTIE.jpg MASQUE1.png [MASQUE2.png ...] [--points x,y;x,y;x,y]
"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def main():
    args = sys.argv[1:]
    pts = None
    if "--points" in args:
        i = args.index("--points"); pts = [tuple(map(int, p.split(","))) for p in args[i + 1].split(";")]; del args[i:i + 2]
    src, out, masks = args[0], args[1], args[2:]
    im = np.asarray(Image.open(src).convert("RGB"), np.float32)
    H, W = im.shape[:2]
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
    except Exception:
        font = ImageFont.load_default()
    T = 360  # côté d'une vignette
    rows = []
    for mp in masks:
        m = np.asarray(Image.open(mp).convert("L"), np.float32)[..., None] / 255
        ys, xs = np.where(m[..., 0] > 0.5)
        if pts is None:
            ytop = ys.min(); xtop = int(np.median(xs[ys < ytop + 20]))
            ymid = int(ys.min() + (ys.max() - ys.min()) * 0.45)
            row = np.where(m[ymid, :, 0] > 0.5)[0]
            p = [(xtop, ytop + 60), (row.min(), ymid), (row.max(), ymid)]
        else:
            p = pts
        tiles = []
        sc = T / H * 2  # vignette pleine image : hauteur 2T
        def vign(arr):
            return Image.fromarray(arr.clip(0, 255).astype(np.uint8)).resize((int(W * sc), int(H * sc)), Image.LANCZOS)
        tiles.append(vign(np.repeat(m * 255, 3, 2)))
        for fond in ((0, 0, 0), (255, 255, 255), (255, 0, 255)):
            tiles.append(vign(im * m + np.array(fond, np.float32) * (1 - m)))
        comp = im * m + np.array((255, 0, 255), np.float32) * (1 - m)
        for (x, y) in p:
            s = T // 2  # 180 px source -> 360 px = 200 %
            x0, y0 = int(np.clip(x - s // 2 * 2, 0, W - 2 * s)), int(np.clip(y - s, 0, H - 2 * s))
            c = comp[y0:y0 + 2 * s, x0:x0 + 2 * s]
            c = Image.fromarray(c.clip(0, 255).astype(np.uint8)).resize((2 * T, 2 * T), Image.LANCZOS)
            tiles.append(c)
        hh = 2 * T
        rowim = Image.new("RGB", (sum(t.width for t in tiles) + 6 * len(tiles), hh + 40), (20, 20, 20))
        x = 0
        for t in tiles:
            rowim.paste(t, (x, 0)); x += t.width + 6
        ImageDraw.Draw(rowim).text((10, hh + 6), os.path.basename(mp), fill=(240, 240, 240), font=font)
        rows.append(rowim)
    Wt = max(r.width for r in rows)
    sheet = Image.new("RGB", (Wt, sum(r.height for r in rows)), (0, 0, 0))
    y = 0
    for r in rows:
        sheet.paste(r, (0, y)); y += r.height
    sheet.save(out, quality=82)
    print(out, sheet.size)


main()
