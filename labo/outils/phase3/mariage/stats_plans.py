# stats_plans.py montage.json RENDU.mp4 : luma p2 / p50 / p98 de l'image du milieu de chaque plan (piste 1) sur le rendu -> stats_plans.json
import sys, json, subprocess, numpy as np
J = json.load(open(sys.argv[1])); V = sys.argv[2]; out = {}
for e in sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"]):
    t = e["rec"] + e["dur"] / 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", V, "-frames:v", "1", "-vf", "scale=480:270,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    y = np.frombuffer(raw, np.uint8).astype(float)
    if y.size == 0: continue
    k = f"{e['nom']}|{e['src']}"; out[k] = [float(np.percentile(y, p)) for p in (2, 50, 98)]
    print(f"{e['rec']:7.2f} {e['nom']:16s} {e['look']:8s} p2 {out[k][0]:4.0f} p50 {out[k][1]:4.0f} p98 {out[k][2]:4.0f}")
json.dump(out, open(sys.argv[1].replace("montage.json", "stats_plans.json"), "w"), indent=0)
