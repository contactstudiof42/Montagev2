# visages.py RENDU_1080p.mp4 montage.json SORTIE_DIR : visages image par image (une image sur deux) sur chaque plan 16:9, FaceLandmarker (modèle local),
# trois tuiles carrées (gauche, centre, droite) ; expressions à risque (yeux fermés, bouche tordue, grimace) > 0,6 ; bande des pires visages par plan.
import sys, json, subprocess, os, numpy as np
from PIL import Image
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
V, Jf, O = sys.argv[1], sys.argv[2], sys.argv[3]; os.makedirs(O, exist_ok=True)
RISQUE = ["eyeBlinkLeft", "eyeBlinkRight", "mouthPucker", "mouthFunnel", "mouthPressLeft", "mouthPressRight", "mouthRollLower", "mouthLeft", "mouthRight", "noseSneerLeft", "noseSneerRight", "mouthShrugUpper"]
det = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path="/Volumes/SSD FAST/Montage-IA/videos/_travail/modeles/face_landmarker.task"), output_face_blendshapes=True, num_faces=4, min_face_detection_confidence=0.5))
J = json.load(open(Jf)); res = []
for e in sorted([e for e in J["video"] if e["piste"] == 1], key=lambda e: e["rec"]):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{e['rec']:.3f}", "-t", f"{e['dur']:.3f}", "-i", V, "-vf", "fps=12.5,format=rgb24", "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, 1080, 1920, 3); pires = {}; nvis = 0; crops = []
    for n, im in enumerate(fr):
        for ox in (0, 420, 840):
            out = det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(im[:, ox:ox + 1080])))
            for fi, lm in enumerate(out.face_landmarks):
                xs = [p.x * 1080 + ox for p in lm]; ys = [p.y * 1080 for p in lm]
                if max(xs) - min(xs) < 70: continue
                nvis += 1; bs = {b.category_name: b.score for b in out.face_blendshapes[fi]}
                for k in RISQUE:
                    if bs.get(k, 0) > pires.get(k, (0, 0))[0]:
                        pires[k] = (round(bs[k], 2), round(e["rec"] + n / 12.5, 2))
                        if bs[k] > 0.6:
                            cx, cy, s = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, (max(xs) - min(xs)) * 0.8
                            crops.append(Image.fromarray(im).crop((int(cx - s), int(cy - s), int(cx + s), int(cy + s))).resize((160, 160)))
    alerte = {k: v for k, v in pires.items() if v[0] > 0.6}
    r = dict(rec=e["rec"], nom=e["nom"], src=e["src"], visages=nvis, alerte=alerte); res.append(r)
    if alerte:
        g = Image.new("RGB", (160 * min(8, len(crops)), 160)); [g.paste(c, (160 * i, 0)) for i, c in enumerate(crops[-8:])]
        g.save(f"{O}/{e['rec']:07.2f}_{e['nom']}.jpg"); print(f"{e['rec']:7.2f} {e['nom']} visages {nvis} {alerte}", flush=True)
json.dump(res, open(f"{O}/visages.json", "w"), indent=0)
print("plans sans visage :", [round(r["rec"], 1) for r in res if r["visages"] == 0])
