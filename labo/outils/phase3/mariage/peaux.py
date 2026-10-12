# peaux.py RENDU_1080p montage.json : teinte et chroma OkLCh de la peau (centre des visages détectés) à l'image du milieu de chaque plan couleur
import sys, json, subprocess, numpy as np
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/couleur"); from oklab import vers_lch
import mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(base_options=mpt.BaseOptions(model_asset_path="/Volumes/SSD FAST/Montage-IA/videos/_travail/modeles/blaze_face_short_range.tflite"), min_detection_confidence=0.6))
V = sys.argv[1]; J = json.load(open(sys.argv[2])); H = []
for e in sorted([e for e in J["video"] if e["piste"] == 1 and e["look"] != "nb" and "KINETIC" not in e["note"]], key=lambda e: e["rec"]):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{e['rec'] + e['dur'] / 2:.2f}", "-i", V, "-frames:v", "1", "-vf", "format=rgb24", "-f", "rawvideo", "-"], capture_output=True).stdout
    im = np.frombuffer(raw, np.uint8).reshape(1080, 1920, 3)
    for ox in (0, 420, 840):
        for f in det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(im[:, ox:ox + 1080]))).detections:
            b = f.bounding_box
            if b.width < 60: continue
            p = im[b.origin_y + b.height // 3: b.origin_y + 2 * b.height // 3, ox + b.origin_x + b.width // 4: ox + b.origin_x + 3 * b.width // 4].reshape(-1, 3) / 255
            L, C, h = vers_lch(p); m = (L > 0.35) & (L < 0.9)
            if m.sum() < 50: continue
            a = (C[m] * np.cos(np.radians(h[m]))).mean(); bb = (C[m] * np.sin(np.radians(h[m]))).mean()
            H.append((e["rec"], e["nom"], e["look"], float(np.degrees(np.arctan2(bb, a)) % 360), float(np.hypot(a, bb)), float(np.median(L[m]))))
for r in H: print(f"{r[0]:7.2f} {r[1]:16s} {r[2]:8s} teinte {r[3]:5.1f}°  chroma {r[4]:.3f}  L {r[5]:.2f}")
hs = np.array([r[3] for r in H if r[2] == "couleur"]); cs = np.array([r[4] for r in H if r[2] == "couleur"])
print(f"couleur : {len(hs)} visages, teinte médiane {np.median(hs):.1f}° (p10 {np.percentile(hs,10):.1f}, p90 {np.percentile(hs,90):.1f}), chroma médiane {np.median(cs):.3f}")
