# expo_v4.py montage_V4.json : exposition et balance plan par plan pour la conversion V4 (look_mariage_v4).
# Trois images par plan (début, milieu, fin : l'exposition se règle sur tout le mouvement), visages (MediaPipe, local).
# Exposition : visages amenés à la cible du look (sans visage : la médiane), sous contrainte des hautes lumières sur les trois images
# (p99,5 de la luminance affichée <= 0,92 : la robe et le ciel gardent leur matière). Balance (couleur seulement) : gris moyen des
# blancs réels du plan (robe, costumes) ramenés à 70 % vers le neutre, ±1/3 de diaph au plus par canal.
# Sortie : cdl_V4.json {"nom|src": {"slope","offset","power","sat","diaph","balance"}} ; offsets en S-Log3 (0,07695 = 1 diaph).
import sys, json, subprocess, numpy as np
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/couleur")
from look_mariage_v4 import scene, couleur_lin, nb_lin, COUL, NB
from oklab import vers_lch
import mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
J = json.load(open(sys.argv[1])); R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
CIBLE_VISAGE = {"V4_couleur": 0.50, "V4_nb": 0.52}; CIBLE_MED = {"V4_couleur": 0.38, "V4_nb": 0.35}
CIBLE_NUIT = 0.20; HAUT = 0.92; DIAPH = 0.07695
CH = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/chrono.json"))}
def soir(nom): h = CH[nom]["t0"] % 86400; return h >= 21 * 3600 + 10 * 60 or h < 6 * 3600     # dîner et nuit : règle de Diego, visages sombres
det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(base_options=mpt.BaseOptions(model_asset_path="/Volumes/SSD FAST/Montage-IA/videos/_travail/modeles/blaze_face_short_range.tflite"), min_detection_confidence=0.5))
W, H = 640, 360; Y = np.array([0.2126, 0.7152, 0.0722])
def image(e, t):
    f = e["stab"]["fichier"] if e.get("stab") else f"{R}/{INV[e['nom']]['fichier']}"
    t = t - (e["stab"]["debut_plage"] if e.get("stab") else 0)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(0, t):.2f}", "-i", f, "-frames:v", "1", "-vf", f"scale={W}:{H},format=rgb48le", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535
def rend(lin, look): return (couleur_lin if look != "V4_nb" else nb_lin)(lin.reshape(-1, 3)).reshape(lin.shape)
SOIR_SEUL = "--soir" in sys.argv
# exceptions vues sur le rendu de contrôle (2026-10-12) : C4008, les lettres lumineuses jaunes prises pour du blanc → pas de balance
SANS_BALANCE = {"20260604_C4008"}
# DA avant livraison : blancs à caler sur ceux du bloc B (baiser, fin, salle d'Ornella, danse) → neutralisation complète comme le soir
FORT = {("FX30.5635", 570, 600), ("20260604_C3697", 0, 20), ("20260604_C3695", 160, 175), ("20260604_C3813", 0, 60), ("20260604_C3894", 80, 110), ("20260604_C3957", 0, 90), ("FX30.5838", 0, 40)}
def fort(e): return any(e["nom"] == n and a <= e["src"] <= b for n, a, b in FORT)
out = json.load(open(sys.argv[1].replace("montage_V4.json", "cdl_V4.json"))) if SOIR_SEUL else {}
for e in sorted([e for e in J["video"] if e["piste"] == 1 and (not SOIR_SEUL or soir(e["nom"]))], key=lambda e: e["rec"]):
    s0 = max(0, e["src"]); d = 0.04 if e.get("gel") else e["dur"] * e["vitesse"]
    xs = [scene(image(e, s0 + d * f)) for f in (0.05, 0.5, 0.95)]
    look = e["look"]; lin = xs[1]
    # balance (couleur) : sur les blancs réels du plan (robe, costumes, nappes : clairs et peu saturés), 70 % vers le neutre,
    # plafonnée à ±1/3 de diaph par canal (une lumière chaude reste chaude) ; sans blanc fiable, aucune correction
    gains = np.ones(3); bal = "—"
    if look == "V4_couleur" and e["nom"] not in SANS_BALANCE:
        y = lin @ Y; mx = lin.max(-1); mn = lin.min(-1); sat = (mx - mn) / np.maximum(mx, 1e-6)
        m = (y > np.percentile(y, 80)) & (y < np.percentile(y, 99.7)) & (sat < (0.65 if soir(e["nom"]) or fort(e) else 0.30))   # le soir, les blancs sont teintés par la LED
        if m.sum() > 300:
            moy = np.array([np.median(lin[..., c][m]) for c in range(3)]); g = (moy @ Y) / np.maximum(moy, 1e-6)
            k = (1.0, 1.5) if soir(e["nom"]) or fort(e) else (0.8, 2 / 3)       # DA appel 4 : même crème sur tous les plans couleur ; le soir, chemise = point blanc
            gains = np.clip(g ** k[0], 2 ** (-k[1]), 2 ** k[1]); gains /= (gains @ Y)
            bal = " ".join(f"{v:.2f}" for v in gains)
    base = (np.clip(rend(lin * gains, look), 0, 1) * 255).astype(np.uint8)
    faces = det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(base))).detections
    boites = [(f.bounding_box.origin_x, f.bounding_box.origin_y, f.bounding_box.width, f.bounding_box.height) for f in faces if f.bounding_box.width > 16]
    nuit = "nuit" in e.get("note", "") or "violet" in e.get("note", "")
    def mesure(st):
        ims = [rend(x * gains * 2 ** st, look) @ Y for x in xs]; yy = ims[1]
        if boites:
            v = np.concatenate([yy[max(0, b[1] + b[3] // 4):b[1] + 3 * b[3] // 4, max(0, b[0] + b[2] // 4):b[0] + 3 * b[2] // 4].ravel() for b in boites])
            m = float(np.median(v)) if v.size else float(np.median(yy)); c = CIBLE_VISAGE[look] - (0.11 if soir(e["nom"]) else 0)
        else: m = float(np.median(yy)); c = CIBLE_NUIT if nuit else CIBLE_MED[look] - (0.08 if soir(e["nom"]) else 0)
        return m, c, max(float(np.percentile(i, 99.5)) for i in ims)
    best = None
    for st in np.arange(-3.0, (0.51 if look == "V4_nb" else 1.51), 0.25):     # N&B : pas plus d'un demi-diaph d'éclaircissement (mur blanchi)
        m, c, hi = mesure(st); err = abs(m - c) + (4 * (hi - HAUT) if hi > HAUT else 0)
        if best is None or err < best[0]: best = (err, st, m, c, hi)
    _, st, m, c, hi = best
    off = st * DIAPH + np.log2(gains) * DIAPH
    out[f"{e['nom']}|{e['src']}"] = {"slope": "1.0 1.0 1.0", "offset": " ".join(f"{o:.4f}" for o in off), "power": "1.0 1.0 1.0", "sat": "1.0",
                                     "diaph": round(float(st), 2), "balance": bal, "visages": len(boites),
                                     "boites": [[round(b[0] / W, 3), round(b[1] / H, 3), round(b[2] / W, 3), round(b[3] / H, 3)] for b in boites]}
    print(f"{e['rec']:7.2f} {e['nom']:16s} {look:10s} visages {len(boites)}  {st:+.2f} diaph  mesure {m:.2f} (cible {c:.2f})  haut {hi:.2f}  balance {bal}", flush=True)
json.dump(out, open(sys.argv[1].replace("montage_V4.json", "cdl_V4.json"), "w"), indent=0)
