# gyro_jitter.py META.json T0 T1 [capteur_mm=35.9] : tremblement de la caméra d'après le gyroscope (indépendant des sujets qui bougent).
# Rotation image par image (org_quat), trajectoire angulaire cumulée (lacet, tangage, roulis), lissée sur 0,4 s ; reste = tremblement,
# converti en px pour une image de 1080 de large avec la focale enregistrée. Imprime moyenne et pic du reste (px), et la vitesse voulue (px/s).
import sys, json, numpy as np
from scipy.spatial.transform import Rotation as Rot
from scipy.ndimage import gaussian_filter1d
d = json.load(open(sys.argv[1])); t0, t1 = float(sys.argv[2]), float(sys.argv[3]); cap = float(sys.argv[4]) if len(sys.argv) > 4 else 35.9
fr = [f for f in d if t0 * 1000 <= f["timestamp_ms"] <= t1 * 1000]
q = np.array([f["org_quat"] for f in fr]); q = q[:, [1, 2, 3, 0]]                 # w,x,y,z -> x,y,z,w
R = Rot.from_quat(q); rel = R[:-1].inv() * R[1:]; rv = rel.as_rotvec()          # rotation entre deux images (rad)
traj = np.cumsum(rv, axis=0); fps = 1000 / np.median(np.diff([f["timestamp_ms"] for f in fr]))
lis = gaussian_filter1d(traj, sigma=0.4 * fps / 2.355, axis=0, mode="nearest"); reste = traj - lis
foc = np.median([f["focal_length"] for f in fr]); px = foc / cap * 1080                # px par radian (largeur 1080)
r = np.hypot(reste[:, 0], reste[:, 1]) * px + np.abs(reste[:, 2]) * 540 * 0.5         # x/y + roulis (bord à mi-largeur, pondéré)
v = np.hypot(np.diff(lis[:, 0]), np.diff(lis[:, 1])) * px * fps
print(json.dumps({"focale": round(float(foc), 1), "images": len(fr), "fps": round(float(fps), 1), "moyenne": round(float(r.mean()), 2), "pic": round(float(r.max()), 2), "vitesse_voulue_px_s": round(float(v.mean()), 1)}))
