# stab_gyro.py NOM SRC DUR [lissage] : Gyroflow sur la plage [SRC-0.5, SRC+DUR+0.5] du rush, sortie dans _travail/stab/<NOM>_<SRC>/ (jamais dans le dossier source),
# nom <NOM>_stabilized_agent.mov ; puis tremblement avant / après sur la plage utilisée. Imprime une ligne JSON.
import sys, json, subprocess, os, glob
T = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"; R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
G = os.path.expanduser("~/Applications/Gyroflow-GitHub.app/Contents/MacOS/gyroflow"); PY = "/Volumes/SSD FAST/Montage-IA/.venv/bin/python"
nom, src, dur = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]); lis = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
x = next(r for r in json.load(open(f"{T}/inventaire.json")) if r["nom"] == nom); f = f"{R}/{x['fichier']}"
a = max(0.0, src - 0.5); b = min(x["duree_s"] - 0.05, src + dur + 0.5)
od = f"{T}/stab/{nom}_{src:.2f}_{lis}"; os.makedirs(od, exist_ok=True); out = f"{od}/{nom}_stabilized_agent.mov"
if not os.path.exists(out):
    p = "{ 'codec': 'ProRes', 'codec_options': 'HQ', 'use_gpu': true, 'audio': false, 'output_folder': 'file://" + od + "/' }"
    pr = ("{ 'version': 2, 'stabilization': { 'adaptive_zoom_window': -1.0, 'max_zoom': 115.0, 'method': 'Default', 'smoothing_params': [ { 'name': 'smoothness', 'value': " + str(lis) + " } ] }, "
          "'synchronization': { 'do_autosync': true, 'search_size': 3, 'max_sync_points': 3 }, 'trim_ranges_ms': [[" + f"{a*1000:.0f}, {b*1000:.0f}" + "]] }")
    r = subprocess.run([G, f, "-t", "_stabilized_agent", "-p", p, "--preset", pr], capture_output=True, text=True, timeout=900)
    cands = glob.glob(f"{od}/*.mov")
    if cands and cands[0] != out: os.rename(cands[0], out)
def mes(v, t0, t1, avant=None):
    args = [PY, "-I", "/Volumes/SSD FAST/Montage-IA/labo/outils/phase3/mariage/saccades.py", v, f"{t0:.2f}", f"{t1:.2f}"]
    try: return json.loads(subprocess.run(args, capture_output=True, text=True).stdout.strip().splitlines()[-1])
    except Exception as e: return {"erreur": str(e)}
res = {"nom": nom, "src": src, "dur": dur, "lissage": lis, "fichier": out if os.path.exists(out) else None, "debut_plage": a}
res["avant"] = mes(f, src, src + dur)
if res["fichier"]: res["apres"] = mes(out, src - a, src - a + dur)
print(json.dumps(res, ensure_ascii=False))
