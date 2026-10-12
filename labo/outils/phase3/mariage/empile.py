# empile.py SORTIE.jpg IMG... : empile verticalement des images
import sys
from PIL import Image
ims = [Image.open(f) for f in sys.argv[2:]]; W = max(i.width for i in ims); H = sum(i.height + 6 for i in ims)
g = Image.new("RGB", (W, H)); y = 0
for i in ims: g.paste(i, (0, y)); y += i.height + 6
g.save(sys.argv[1], quality=75); print(sys.argv[1], g.size)
