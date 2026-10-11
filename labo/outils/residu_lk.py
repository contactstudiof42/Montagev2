"""Tremblement résiduel d'un plan par points suivis (Lucas-Kanade + similitude RANSAC) : robuste aux motifs périodiques
(le tapis en carbone trompe la corrélation de phase de tremblement.py). Trajectoire cumulée x, y ; reste = trajectoire moins
sa version lissée (gaussienne de FENETRE s). Sort la moyenne et le pic du reste (px, image ramenée à 1080 de large).
Usage : python residu_lk.py VIDEO [DEBUT FIN] [--fenetre 0.4]"""
import sys, json, numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from gyro_sync import image_motion
from scipy.ndimage import gaussian_filter1d
a = [x for x in sys.argv[1:] if not x.startswith("--")]
fen = float(sys.argv[sys.argv.index("--fenetre") + 1]) if "--fenetre" in sys.argv else 0.4
v = a[0]; d = float(a[1]) if len(a) > 1 else 0.0; f = float(a[2]) if len(a) > 2 else 99.0
t, m, fps = image_motion(v, d, f)
m = np.nan_to_num(m[:, :2]); tr = np.cumsum(m, 0)
lis = gaussian_filter1d(tr, fen * fps, axis=0, mode="nearest"); reste = np.linalg.norm(tr - lis, axis=1)
print(json.dumps({"video": v.rsplit("/", 1)[-1], "debut": d, "fin": f, "moyenne": round(float(reste.mean()), 2), "pic": round(float(reste.max()), 2),
                  "vitesse_voulue_px_s": round(float(np.linalg.norm(np.diff(lis, axis=0), axis=1).mean() * fps), 1)}))
