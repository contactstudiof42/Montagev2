# flashs_rush.py NOM T0 T1 : luminance moyenne par image (50p) et sauts > 8 % (flash de photographe, bande de volet roulant)
import sys, json, subprocess, numpy as np
R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"; INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
n, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(a), "-t", str(b - a), "-i", f"{R}/{INV[n]['fichier']}", "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
f = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(float)
bandes = f.reshape(len(f), 9, 10, 160).mean(axis=(2, 3))           # 9 bandes horizontales
d = np.abs(np.diff(bandes, axis=0)).max(1)
print("flashs (s) :", [float(round(a + (i + 1) / 50, 2)) for i in np.where(d > float(sys.argv[4]) * 255 if len(sys.argv) > 4 else d > 0.08 * 255)[0]])
