# bande_rush.py DOSSIER_PROXY SORTIE.png RUSH[:debut:fin] ... : une rangée de 10 vignettes par rush (de debut à fin, en s),
# temps écrit sous chaque vignette, pour choisir un moment sans relire tout le dérush. Proxies 25p, temps = s depuis le début.
import sys, subprocess, json
from PIL import Image, ImageDraw
d, out, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
rows = []
for sp in specs:
    r, *ab = sp.split(":")
    f = f"{d}/{r}.mp4"
    dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",f],capture_output=True,text=True).stdout)
    a, b = (float(ab[0]), float(ab[1])) if ab else (0.0, dur - 0.05)
    tiles = []
    for k in range(10):
        t = a + (b - a) * k / 9
        p = subprocess.run(["ffmpeg","-v","error","-ss",f"{t:.2f}","-i",f,"-frames:v","1","-vf","scale=120:-2","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
        import io
        im = Image.open(io.BytesIO(p)).convert("RGB") if p else Image.new("RGB",(120,213))
        c = Image.new("RGB",(im.width, im.height+14),(0,0,0)); c.paste(im,(0,0))
        ImageDraw.Draw(c).text((2,im.height+1),f"{r} {t:.1f}",fill=(255,230,0)); tiles.append(c)
    row = Image.new("RGB",(sum(t.width for t in tiles), tiles[0].height)); x=0
    for t in tiles: row.paste(t,(x,0)); x+=t.width
    rows.append(row)
W = max(r.width for r in rows); im = Image.new("RGB",(W,sum(r.height for r in rows))); y=0
for r in rows: im.paste(r,(0,y)); y+=r.height
im.save(out)
