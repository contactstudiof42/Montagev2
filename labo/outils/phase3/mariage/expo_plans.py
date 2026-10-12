# expo_plans.py montage.json : exposition plan par plan. Image du milieu de chaque plan (rush S-Log3), visages (MediaPipe FaceDetector,
# modèle local), recherche du décalage CDL (en S-Log3, 0,077 = 1 diaph) qui amène la luminance des visages à la cible du look
# (sans visage : la médiane de l'image), sous contrainte des hautes lumières (p99,5 <= 0,93). Écrit cdl.json {(nom,src): offset}.
import sys, json, subprocess, numpy as np
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/couleur")
from look_mariage import couleur, nb, COUL, NB
import mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
J = json.load(open(sys.argv[1])); R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
P = {"couleur": dict(COUL, expo=-0.85, epaule=0.62, pied=0.10, chroma=0.9, olive=0.035, olive_h=112),
     "nb": dict(NB, expo=-0.8, epaule=0.70, pied=0.06), "nuit": dict(COUL, expo=-0.6, epaule=0.62, pied=0.08, chroma=0.72, olive=0.0, peau_c=0.06),
     "photobooth": dict(COUL, expo=-1.25, epaule=0.62, pied=0.08, chroma=0.8, olive=0.0, peau_c=0.065)}
CIBLE_VISAGE = {"couleur": 0.50, "nb": 0.56, "nuit": 0.40}; CIBLE_MED = {"couleur": 0.36, "nb": 0.36, "nuit": 0.22}
det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(base_options=mpt.BaseOptions(model_asset_path="/Volumes/SSD FAST/Montage-IA/videos/_travail/modeles/blaze_face_short_range.tflite"), min_detection_confidence=0.5))
W, H = 960, 540
def image(e):
    t = max(0, e["src"]) + e["dur"] * e["vitesse"] / 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", f"{R}/{INV[e['nom']]['fichier']}", "-frames:v", "1", "-vf", f"scale={W}:{H},format=rgb48le", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535
def rend(x, look, off): return (couleur if look != "nb" else nb)(np.clip(x + off, 0, 1).reshape(-1, 3), P[look]).reshape(x.shape)
Y = np.array([0.2126, 0.7152, 0.0722]); out = {}
for e in sorted([e for e in J["video"] if e["piste"] == 1 and "KINETIC" not in e.get("note", "")], key=lambda e: e["rec"]):
    x = image(e); look = e["look"]
    # visages sur une version neutre (look sans décalage)
    base = (rend(x, look, 0) * 255).astype(np.uint8)
    faces = det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(base))).detections
    boites = [(f.bounding_box.origin_x, f.bounding_box.origin_y, f.bounding_box.width, f.bounding_box.height) for f in faces if f.bounding_box.width > 24]
    def mesure(off):
        im = rend(x, look, off); y = im @ Y
        if boites:
            v = np.concatenate([y[max(0, b[1] + b[3] // 4):b[1] + 3 * b[3] // 4, max(0, b[0] + b[2] // 4):b[0] + 3 * b[2] // 4].ravel() for b in boites])
            m = float(np.median(v)) if v.size else float(np.median(y)); cible = CIBLE_VISAGE[look]
        else: m = float(np.median(y)); cible = CIBLE_MED[look]
        return m, cible, float(np.percentile(y, 99.5))
    best = None
    for off in np.arange(-0.115, 0.116, 0.0193):      # -1,5 à +1,5 diaph par quart de diaph
        m, c, hi = mesure(off); err = abs(m - c) + (5 * (hi - 0.93) if hi > 0.93 else 0)
        if best is None or err < best[0]: best = (err, off, m, c, hi)
    m0, c0, h0 = mesure(0.0)
    out[f"{e['nom']}|{e['src']}"] = round(float(best[1]), 4)
    print(f"{e['rec']:7.2f} {e['nom']:16s} {look:8s} visages {len(boites)}  avant {m0:.2f} (h {h0:.2f}) -> décalage {best[1]/0.077:+.2f} diaph : {best[2]:.2f} cible {best[3]:.2f} h {best[4]:.2f}", flush=True)
json.dump(out, open(sys.argv[1].replace("montage.json", "cdl.json"), "w"), indent=0)
