"""Contrôle du passage exact utilisé, plan par plan, sur un rendu (règle de Diego du 2026-10-11 : aucun plan de remplissage).

Pour chaque plan de la timeline (JSON [[piste, debut, fin, nom, ...], ...], images de timeline à 25 i/s) :
- première, milieu et dernière image du rendu ;
- netteté : variance du laplacien sur la tuile la plus nette (grille 4x6) et sur la médiane des tuiles, à pleine résolution ;
- exposition : luma p2, p50, p99,5, part de pixels >= 250 et <= 6 (8 bits plein) ;
- visages (toutes les images du plan) : FaceLandmarker de MediaPipe, blendshapes « à risque » (yeux mi-clos, bouche pincée,
  tordue, en cul de poule, grimace) ; bande des visages image par image pour juger à l'œil.
Sorties : <sortie>/planche_NN.jpg (12 plans par planche), <sortie>/visages/<plan>.jpg, <sortie>/controle.json.

Usage : python controle_plans.py RENDU.mp4 timeline.json SORTIE [--pistes 1,2,3] [--modele face_landmarker.task]
"""
import sys, os, json, subprocess, argparse
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

RISQUE = ["eyeBlinkLeft", "eyeBlinkRight", "eyeSquintLeft", "eyeSquintRight", "mouthPucker", "mouthFunnel",
          "mouthPressLeft", "mouthPressRight", "mouthRollLower", "mouthRollUpper", "mouthLeft", "mouthRight",
          "mouthStretchLeft", "mouthStretchRight", "jawOpen", "noseSneerLeft", "noseSneerRight", "browDownLeft", "browDownRight",
          "browOuterUpLeft", "browOuterUpRight", "browInnerUp", "mouthShrugLower", "mouthShrugUpper", "eyeWideLeft", "eyeWideRight"]


def lire_images(video, debut, fin, fps=25):
    """Images [debut, fin) du rendu, en RGB uint8, pleine résolution."""
    w, h = 1080, 1920
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{debut / fps:.4f}", "-i", video, "-frames:v", str(fin - debut),
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (w * h * 3)
    return [np.frombuffer(raw[i * w * h * 3:(i + 1) * w * h * 3], np.uint8).reshape(h, w, 3) for i in range(n)]


def nettete(img):
    g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype(np.float32)
    lap = cv2.Laplacian(g, cv2.CV_32F)
    h, w = g.shape
    v = []
    for i in range(6):
        for j in range(4):
            v.append(lap[i * h // 6:(i + 1) * h // 6, j * w // 4:(j + 1) * w // 4].var())
    v = np.array(v)
    return float(v.max()), float(np.median(v))


def expo(img):
    y = (0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2])
    return {"p2": float(np.percentile(y, 2)), "p50": float(np.percentile(y, 50)), "p995": float(np.percentile(y, 99.5)),
            "brule": float((y >= 250).mean() * 100), "bouche": float((y <= 6).mean() * 100)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rendu"); ap.add_argument("timeline"); ap.add_argument("sortie")
    ap.add_argument("--pistes", default="1")
    ap.add_argument("--modele", default=os.path.join(os.path.dirname(__file__), "../../videos/_travail/modeles/face_landmarker.task"))
    ap.add_argument("--sans-visages", action="store_true")
    a = ap.parse_args()
    os.makedirs(os.path.join(a.sortie, "visages"), exist_ok=True)
    pistes = {int(p) for p in a.pistes.split(",")}
    plans = [p for p in json.load(open(a.timeline)) if p[0] in pistes]
    det = None
    if not a.sans_visages:
        import mediapipe as mp
        from mediapipe.tasks.python import vision, BaseOptions
        det = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=a.modele), output_face_blendshapes=True, num_faces=3,
            min_face_detection_confidence=0.5))
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
    res, lignes = [], []
    for k, (piste, d, f, nom, *_) in enumerate(plans):
        imgs = lire_images(a.rendu, d, f)
        if not imgs:
            continue
        idx = [0, len(imgs) // 2, len(imgs) - 1]
        r = {"piste": piste, "debut": d, "fin": f, "nom": nom, "net_max": [], "net_med": [], "expo": []}
        for i in idx:
            m, md = nettete(imgs[i]); r["net_max"].append(round(m, 1)); r["net_med"].append(round(md, 1))
            r["expo"].append({kk: round(vv, 1) for kk, vv in expo(imgs[i]).items()})
        # visages, toutes les images
        visages, pires = [], {}
        if det is not None:
            import mediapipe as mp
            for n, im in enumerate(imgs):
                # le détecteur ramène l'image à un carré : on analyse trois tuiles carrées (haut, milieu, bas)
                vus, visages_tuile = [], []
                for oy in (0, 420, 840):
                    out = det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(im[oy:oy + 1080])))
                    for fi, lm in enumerate(out.face_landmarks):
                        xs = [p.x for p in lm]; ys = [(p.y * 1080 + oy) / 1920 for p in lm]
                        c = (sum(xs) / len(xs), sum(ys) / len(ys))
                        if any(abs(c[0] - v[0]) < 0.05 and abs(c[1] - v[1]) < 0.03 for v in vus):
                            continue
                        vus.append(c)
                        visages_tuile.append((xs, ys, out.face_blendshapes[fi]))
                for xs, ys, bsl in visages_tuile:
                    x0, x1 = max(0, min(xs)), min(1, max(xs)); y0, y1 = max(0, min(ys)), min(1, max(ys))
                    if (x1 - x0) * 1080 < 90:  # visage trop petit pour être jugé
                        continue
                    bs = {b.category_name: b.score for b in bsl}
                    for kk in RISQUE:
                        if bs.get(kk, 0) > pires.get(kk, (0, 0))[0]:
                            pires[kk] = (round(bs[kk], 2), d + n)
                    cx, cy, s = (x0 + x1) / 2 * 1080, (y0 + y1) / 2 * 1920, max((x1 - x0) * 1080, (y1 - y0) * 1920) * 0.75
                    crop = Image.fromarray(im).crop((int(cx - s), int(cy - s), int(cx + s), int(cy + s))).resize((160, 160))
                    visages.append((d + n, crop))
        r["visages_images"] = len(visages)
        r["pires_expressions"] = {kk: v for kk, v in sorted(pires.items(), key=lambda x: -x[1][0])[:6] if v[0] > 0.35}
        if visages:
            # une bande : toutes les images (max 40), numéro de l'image de timeline
            vs = visages[:40]
            band = Image.new("RGB", (160 * min(len(vs), 10), 190 * ((len(vs) + 9) // 10)), (0, 0, 0))
            dr = ImageDraw.Draw(band)
            for q, (fr, c) in enumerate(vs):
                band.paste(c, ((q % 10) * 160, (q // 10) * 190)); dr.text(((q % 10) * 160 + 4, (q // 10) * 190 + 162), str(fr), fill=(255, 255, 0), font=font)
            band.save(os.path.join(a.sortie, "visages", f"{d:04d}_{nom}.jpg"), quality=80)
        res.append(r)
        # ligne de planche
        th = [Image.fromarray(imgs[i]).resize((270, 480)) for i in idx]
        row = Image.new("RGB", (270 * 3 + 520, 480), (15, 15, 15))
        for q, t in enumerate(th):
            row.paste(t, (q * 270, 0))
        dr = ImageDraw.Draw(row)
        e = r["expo"]
        txt = [f"{d}-{f}  {nom}  (piste {piste})",
               "net max " + " / ".join(f"{x:.0f}" for x in r["net_max"]),
               "net med " + " / ".join(f"{x:.0f}" for x in r["net_med"]),
               "p2 " + " / ".join(f"{x['p2']:.0f}" for x in e),
               "p50 " + " / ".join(f"{x['p50']:.0f}" for x in e),
               "p99.5 " + " / ".join(f"{x['p995']:.0f}" for x in e),
               "brûlé % " + " / ".join(f"{x['brule']:.1f}" for x in e),
               f"visages : {len(visages)} img"]
        for kk, (sc, fr) in list(r["pires_expressions"].items())[:5]:
            txt.append(f"  {kk} {sc} @ {fr}")
        for q, t in enumerate(txt):
            dr.text((830, 10 + q * 30), t, fill=(235, 235, 235), font=font)
        lignes.append(row)
        print(d, f, nom, r["net_max"], [x["p2"] for x in e], [x["brule"] for x in e], r["pires_expressions"], flush=True)
    for s in range(0, len(lignes), 6):
        grp = lignes[s:s + 6]
        sh = Image.new("RGB", (grp[0].width, 480 * len(grp)), (0, 0, 0))
        for q, l in enumerate(grp):
            sh.paste(l, (0, q * 480))
        sh.save(os.path.join(a.sortie, f"planche_{s // 6:02d}.jpg"), quality=78)
    json.dump(res, open(os.path.join(a.sortie, "controle.json"), "w"), indent=1, ensure_ascii=False)


main()
