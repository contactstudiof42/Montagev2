# controle.py montage.json MAQUETTE.mp4 SORTIE.jpg [debut fin] : pour chaque plan de la piste 1 : première, milieu, dernière image + note
import sys, json, subprocess, io
from PIL import Image, ImageDraw
J = json.load(open(sys.argv[1])); V = sys.argv[2]; out = sys.argv[3]
D0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0; D1 = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
DV = float(subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=duration","-of","default=nw=1:nk=1",V],capture_output=True,text=True).stdout)
evs = [e for e in sorted(J["video"], key=lambda e: e["rec"]) if e["piste"] == 1 and D0 <= e["rec"] < D1]
W, H = 256, 144; g = Image.new("RGB", (3 * (W + 2) + 330, len(evs) * (H + 2)), (15, 15, 15)); d = ImageDraw.Draw(g)
def im(t):
    t = max(0, min(t, DV - 0.06))
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", V, "-frames:v", "1", "-vf", f"scale={W}:{H}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(r)).convert("RGB")
for j, e in enumerate(evs):
    for i, t in enumerate([e["rec"] + 0.04, e["rec"] + e["dur"] / 2, e["rec"] + e["dur"] - 0.08]):
        g.paste(im(t - (float(sys.argv[6]) if len(sys.argv) > 6 else 0)), (i * (W + 2), j * (H + 2)))
    x0 = 3 * (W + 2) + 6; y = j * (H + 2)
    d.text((x0, y + 4), f"{e['rec']:.2f}s  {e['dur']:.2f}s  {e['look']}", fill=(255, 255, 0))
    d.text((x0, y + 20), f"{e['nom'].replace('20260604_','')}  src {e['src']:.2f}" + (f"  v{e['vitesse']}" if e['vitesse'] != 1 else ""), fill=(200, 200, 200))
    n = e.get("note", ""); [d.text((x0, y + 36 + 14 * l), n[l*48:(l+1)*48], fill=(160, 220, 160)) for l in range(min(6, (len(n) + 47) // 48))]
g.save(out, quality=80); print(out, g.size)
