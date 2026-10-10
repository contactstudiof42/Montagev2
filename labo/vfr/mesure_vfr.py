"""Mesure un fichier : cadence (variable ou non), instant du flash (image la plus claire), instant du clic audio, décalage.
Usage : python3 mesure_vfr.py fichier.mp4 [...]  → une ligne JSON par fichier."""
import json, subprocess, sys
import numpy as np
def probe(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-f", "lavfi", "-i", f"movie={f},signalstats", "-show_entries",
                        "frame=pts_time:frame_tags=lavfi.signalstats.YAVG", "-of", "json"], capture_output=True, text=True)
    fr = json.loads(r.stdout)["frames"]
    t = np.array([float(x["pts_time"]) for x in fr]); y = np.array([float(x["tags"]["lavfi.signalstats.YAVG"]) for x in fr])
    s = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                   "stream=r_frame_rate,avg_frame_rate", "-of", "json", f], capture_output=True, text=True).stdout)["streams"][0]
    a = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-map", "0:a:0", "-f", "f32le", "-ac", "1", "-ar", "48000", "-"],
                                     capture_output=True).stdout, np.float32)
    d = np.diff(t)
    return dict(fichier=f.split("/")[-1], images=len(t), r_frame_rate=s["r_frame_rate"], avg_frame_rate=s["avg_frame_rate"],
                intervalle_min_ms=round(1000 * d.min(), 2), intervalle_max_ms=round(1000 * d.max(), 2),
                vfr=bool(d.max() - d.min() > 0.002), t_flash=round(float(t[y.argmax()]), 4),
                t_clic=round(float(np.argmax(abs(a) > 0.1) / 48000), 4),
                decalage_ms=round(1000 * (float(t[y.argmax()]) - np.argmax(abs(a) > 0.1) / 48000), 1),
                images_doublees=int((np.diff(y) == 0).sum()))
for f in sys.argv[1:]:
    print(json.dumps(probe(f)))
