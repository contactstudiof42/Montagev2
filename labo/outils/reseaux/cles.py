# cles.py VIDEO SORTIE.jpg "t1 t2 ..." [crop=w:h:x:y] [cols=2] [largeur=720] : images clés en pleine résolution, annotées
import sys, subprocess, numpy as np
from PIL import Image, ImageDraw
v, out, ts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3].split()]
crop = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] != "-" else None
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 2; W = int(sys.argv[6]) if len(sys.argv) > 6 else 720
ims = []
for t in ts:
    vf = (f"crop={crop}," if crop else "") + f"scale={W}:-2"
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",v,"-frames:v","1","-vf",vf,"-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    import io; im = Image.open(io.BytesIO(raw)).convert("RGB"); d = ImageDraw.Draw(im); d.text((6,6), f"{t:.2f}s", fill=(255,255,0)); ims.append(im)
h = ims[0].height; rows = (len(ims)+cols-1)//cols
g = Image.new("RGB", (cols*(W+4), rows*(h+4)))
for i, im in enumerate(ims): g.paste(im, ((i%cols)*(W+4), (i//cols)*(h+4)))
g.save(out, quality=88); print(out, g.size)
