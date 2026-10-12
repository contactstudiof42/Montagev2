# bande.py NOM DEBUT FIN [ips=4] [nb|couleur] [cols=8] : images du passage (temps du rush), LUT de look, annotées ; sortie _travail/bandes/
import sys, json, subprocess, os, io
from PIL import Image, ImageDraw
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"; R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
nom, d0, d1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]); ips = float(sys.argv[4]) if len(sys.argv) > 4 else 4
mode = sys.argv[5] if len(sys.argv) > 5 else "couleur"; cols = int(sys.argv[6]) if len(sys.argv) > 6 else 8
x = next(r for r in json.load(open(f"{T}/inventaire.json")) if r["nom"] == nom)
lut = f"/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/P3/P3_mariage_{mode}.cube"
W, H = 320, 180
vf = f"fps={ips},scale={W}:{H},format=rgb48le,lut3d='{lut}',format=rgb24"
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(d0), "-t", str(d1 - d0), "-i", f"{R}/{x['fichier']}", "-vf", vf, "-f", "rawvideo", "-"], capture_output=True).stdout
n = len(raw) // (W * H * 3); rows = (n + cols - 1) // cols
g = Image.new("RGB", (cols * (W + 2), rows * (H + 2)), (0, 0, 0)); d = ImageDraw.Draw(g)
for k in range(n):
    im = Image.frombytes("RGB", (W, H), raw[k*W*H*3:(k+1)*W*H*3]); X, Y = (k % cols) * (W + 2), (k // cols) * (H + 2)
    g.paste(im, (X, Y)); d.text((X + 3, Y + 3), f"{d0 + k / ips:.2f}", fill=(255, 255, 0))
os.makedirs(f"{T}/bandes", exist_ok=True); out = f"{T}/bandes/{nom}_{d0:.0f}-{d1:.0f}.jpg"; g.save(out, quality=80); print(out, n)
