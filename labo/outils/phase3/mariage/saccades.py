# saccades.py VIDEO T0 T1 : mouvement image par image (corrélation de phase, centre 60 %, 640 px) ; « saccade » = moyenne |accélération|
# (variation du déplacement d'une image à l'autre, px ramenés à 1080 de large) : un mouvement régulier donne ~0, une main qui tremble beaucoup.
import sys, subprocess, json, numpy as np, cv2
v, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]); W = 640
raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t0), "-t", str(t1 - t0), "-i", v, "-vf", f"crop=iw*0.6:ih*0.6,scale={W}:-2,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
H = int(round(W * 9 / 16 / 2)) * 2; fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
win = cv2.createHanningWindow((W, H), cv2.CV_32F); d = []
for a, b in zip(fr[:-1], fr[1:]): (dx, dy), _ = cv2.phaseCorrelate(a, b, win); d.append((dx, dy))
d = np.array(d) * (1080 / (W / 0.6)); acc = np.diff(d, axis=0)
print(json.dumps({"images": len(fr), "saccade": round(float(np.hypot(acc[:, 0], acc[:, 1]).mean()), 3), "vitesse": round(float(np.hypot(d[:, 0], d[:, 1]).mean()), 3)}))
