"""Rendu Gyroflow d'une plage avec une synchronisation IMPOSÉE et vérifiée (V5 Sony, 2026-10-11).
L'autosynchronisation de la ligne de commande ne laisse aucune trace (aucun point de synchro dans le projet, rien au journal) :
on mesure le décalage gyroscope / image avec `gyro_sync.py`, on l'impose dans le projet, on rend, puis on vérifie que le
décalage résiduel est proche de 0 (preuve écrite en JSON).
Convention vérifiée sur C6507 : décalage Gyroflow (ms) = - décalage mesuré par gyro_sync.py (-34 ms mesurés -> +34 imposés
-> 4 ms résiduels).

Usage : python gyro_rendu.py RUSH.MP4 DEBUT_S FIN_S OFFSET_MS SORTIE_DIR SUFFIXE
Sorties : SORTIE_DIR/<rush>_<suffixe>.mov (ProRes HQ, zoom fixe 115 %, lissage par défaut), <rush>_<suffixe>.gyroflow,
          <rush>_<suffixe>_preuve.json (décalage imposé, résiduel, corrélations).
"""
import sys, os, json, subprocess
G = os.path.expanduser("~/Applications/Gyroflow-GitHub.app/Contents/MacOS/gyroflow")
HERE = os.path.dirname(os.path.abspath(__file__))
rush, d, f, off, out, suf = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5], sys.argv[6]
os.makedirs(out, exist_ok=True)
base = os.path.splitext(os.path.basename(rush))[0]
preset = "{ 'version': 2, 'stabilization': { 'adaptive_zoom_window': -1.0, 'max_zoom': 115.0 }, 'trim_ranges_ms': [[%.1f, %.1f]] }" % (d * 1000, f * 1000)
subprocess.run([G, rush, "--export-project", "3", "-p", "{ 'output_folder': 'file://%s/' }" % out, "--preset", preset], capture_output=True)
proj = os.path.join(out, base + ".gyroflow")
p = json.load(open(proj))
p["offsets"] = {str(int((d + f) / 2 * 1e6)): off}
p["output"]["output_folder"] = "file://" + out + "/"
p["output"]["output_filename"] = f"{base}_{suf}.mov"
p["output"]["codec"] = "ProRes"; p["output"]["codec_options"] = "HQ"; p["output"]["audio"] = False; p["output"]["use_gpu"] = True
pp = os.path.join(out, f"{base}_{suf}.gyroflow")
json.dump(p, open(pp, "w")); os.remove(proj)
# vérification : métadonnées du projet décalé -> décalage résiduel
meta = os.path.join(out, f"{base}_{suf}_meta.json")
subprocess.run([G, pp, "--export-metadata", f"3:{meta}"], capture_output=True)
v = subprocess.run([sys.executable, "-I", os.path.join(HERE, "gyro_sync.py"), rush, str(d), str(f), "--meta", meta], capture_output=True, text=True)
res = json.loads(v.stdout.strip().splitlines()[-1])
# rendu
r = subprocess.run([G, pp, "-t", "_" + suf], capture_output=True, text=True)
sortie = os.path.join(out, f"{base}_{suf}.mov")
preuve = {"rush": base, "plage_s": [d, f], "offset_impose_ms": off, "residuel": res, "sortie": sortie, "existe": os.path.exists(sortie),
          "gyro": p["gyro_source"].get("detected_source"), "objectif": p["calibration_data"].get("lens_model"),
          "lissage": p["stabilization"].get("smoothing_params", [{}])[0], "zoom_fixe": p["stabilization"].get("adaptive_zoom_window") == -1.0}
json.dump(preuve, open(os.path.join(out, f"{base}_{suf}_preuve.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: preuve[k] for k in ("rush", "plage_s", "offset_impose_ms", "existe")}, ensure_ascii=False),
      "résiduel", res.get("decalage_ms"), res.get("correlation_xy"))
