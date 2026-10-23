# planche.py DOSSIER_RENDUS SORTIE.png [COLONNES] : assemble les images de contrôle en planche, avec le cadre 2,39:1 tracé
# (les bandes hors du cadre livré sont assombries) et le nom de chaque image en légende.
import sys, os, glob
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]; ncol = int(sys.argv[3]) if len(sys.argv) > 3 else 4
fs = sorted(glob.glob(os.path.join(src, "*.png")))
ims = [Image.open(f).convert("RGB") for f in fs]; w, h = ims[0].size; lab = 18
sheet = Image.new("RGB", (ncol * w, ((len(ims) + ncol - 1) // ncol) * (h + lab)), (20, 20, 20))
for i, (f, im) in enumerate(zip(fs, ims)):
    ch = int(round(w / 2.39)); y0 = (h - ch) // 2
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rectangle([0, 0, w, y0], fill=(0, 0, 0, 140)); d.rectangle([0, y0 + ch, w, h], fill=(0, 0, 0, 140))
    d.line([0, y0, w, y0], fill=(255, 255, 0, 200)); d.line([0, y0 + ch, w, y0 + ch], fill=(255, 255, 0, 200))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    x, y = (i % ncol) * w, (i // ncol) * (h + lab)
    sheet.paste(im, (x, y + lab)); ImageDraw.Draw(sheet).text((x + 4, y + 3), os.path.basename(f)[:-4], fill=(230, 230, 230))
sheet.save(out, optimize=True); print(out, sheet.size)
