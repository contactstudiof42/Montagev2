"""Preuve qu'un plan est stabilisé avec les données gyroscopiques DE CE PLAN, et mesure de la synchronisation gyroscope / image
(retour de Diego du 2026-10-11 : « prouve, plan par plan, que chaque plan stabilisé l'est par Gyroflow avec les données
gyroscopiques, synchronisation comprise »).

1. Gyroscope : Gyroflow exporte les quaternions de la caméra image par image (`--export-metadata 3:…`, décalage 0) ;
   vitesse de rotation par image = conj(q_i) * q_i+1 (repère caméra), trois axes.
2. Image : sur l'original, points suivis (Shi-Tomasi + Lucas-Kanade) puis similitude par RANSAC entre images consécutives :
   déplacement x, y et rotation dans le plan, par image. Robuste aux motifs périodiques (tapis en carbone) qui trompent la
   corrélation de phase.
3. Pour chaque axe d'image, l'axe du gyroscope (et le signe) qui lui correspond le mieux ; puis le décalage temporel
   (de -120 à +120 ms, pas de 2 ms, interpolation) qui maximise la corrélation moyenne.
Une corrélation élevée (> 0,8) prouve que les données gyroscopiques décrivent bien le mouvement de ce plan ; le décalage
trouvé est la synchronisation (à reporter dans Gyroflow si elle n'est pas proche de 0).

Usage : python gyro_sync.py RUSH.MP4 DEBUT_S FIN_S [--json sortie.json]
"""
import sys, os, json, subprocess, argparse, tempfile
import numpy as np
import cv2

G = os.path.expanduser("~/Applications/Gyroflow-GitHub.app/Contents/MacOS/gyroflow")


def quat_mul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def rot_vec(q):
    q = q / np.linalg.norm(q)
    if q[0] < 0: q = -q
    ang = 2 * np.arccos(np.clip(q[0], -1, 1)); s = np.sqrt(max(1 - q[0] ** 2, 1e-12))
    return q[1:] / s * ang if ang > 1e-9 else np.zeros(3)


def gyro_rates(rush, d, f, meta=None):
    if meta:   # métadonnées déjà exportées (par exemple depuis un projet Gyroflow avec décalage imposé)
        m = json.load(open(meta))
    else:
        with tempfile.TemporaryDirectory() as td:
            out = os.path.join(td, "m.json")
            subprocess.run([G, rush, "--export-metadata", f"3:{out}"], capture_output=True)
            m = json.load(open(out))
    t = np.array([e["timestamp_ms"] for e in m]) / 1000
    q = np.array([e["org_quat"] for e in m])
    w = np.array([rot_vec(quat_mul(q[i] * np.array([1, -1, -1, -1]), q[i + 1])) for i in range(len(q) - 1)])
    tm = (t[:-1] + t[1:]) / 2
    return tm, w


def image_motion(rush, d, f, larg=540):
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height,r_frame_rate:stream_side_data=rotation",
                        "-of", "json", rush], capture_output=True, text=True)
    s = json.loads(p.stdout)["streams"][0]; w, h = s["width"], s["height"]
    num, den = map(int, s["r_frame_rate"].split("/")); fps = num / den
    if any(abs(int(x.get("rotation", 0))) == 90 for x in s.get("side_data_list", [])): w, h = h, w
    H = int(round(larg * h / w / 2)) * 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(d), "-i", rush, "-t", str(f - d), "-vf", f"scale={larg}:{H},format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    n = len(raw) // (larg * H)
    fr = [np.frombuffer(raw[i * larg * H:(i + 1) * larg * H], np.uint8).reshape(H, larg) for i in range(n)]
    mot = []
    for i in range(n - 1):
        pts = cv2.goodFeaturesToTrack(fr[i], 400, 0.01, 8)
        if pts is None or len(pts) < 12:
            mot.append([np.nan] * 3); continue
        nxt, st, _ = cv2.calcOpticalFlowPyrLK(fr[i], fr[i + 1], pts, None, winSize=(21, 21), maxLevel=3)
        ok = st[:, 0] == 1
        if ok.sum() < 12:
            mot.append([np.nan] * 3); continue
        M, inl = cv2.estimateAffinePartial2D(pts[ok], nxt[ok], method=cv2.RANSAC, ransacReprojThreshold=1.5)
        if M is None:
            mot.append([np.nan] * 3); continue
        cx, cy = larg / 2, H / 2   # déplacement du CENTRE de l'image (la translation de M est relative au coin : fausse dès qu'il y a zoom ou rotation)
        dx = M[0, 0] * cx + M[0, 1] * cy + M[0, 2] - cx; dy = M[1, 0] * cx + M[1, 1] * cy + M[1, 2] - cy
        mot.append([dx * 1080 / larg, dy * 1080 / larg, np.arctan2(M[1, 0], M[0, 0])])
    t = d + (np.arange(n - 1) + 1) / fps
    return t, np.array(mot), fps


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("rush"); ap.add_argument("debut", type=float); ap.add_argument("fin", type=float)
    ap.add_argument("--json"); ap.add_argument("--meta")
    a = ap.parse_args()
    tg, wg = gyro_rates(a.rush, a.debut, a.fin, a.meta)
    ti, mi, fps = image_motion(a.rush, a.debut, a.fin)
    good = ~np.isnan(mi).any(1)
    res = {"rush": os.path.basename(a.rush), "debut": a.debut, "fin": a.fin, "images": int(len(ti)), "images_valides": int(good.sum())}
    noms = ["x", "y", "rot"]
    # correspondance fixe des axes (ZV-E1 tenu vertical, rotation 90) : trouvée sur C6507 et C6723, les plans au mouvement
    # le plus ample : x image <-> gyro 0 (+), y image <-> gyro 1 (-), rotation dans le plan <-> gyro 2
    perm = (0, 1, 2)
    corr = lambda lag: [float(np.corrcoef(mi[good][:, i], np.interp(ti + lag, tg, wg[:, perm[i]])[good])[0, 1]) for i in range(3)]
    lags = np.arange(-0.12, 0.1201, 0.002)
    sc = [abs(c[0]) + abs(c[1]) for c in map(corr, lags)]   # pan / tilt : les axes que la main fait vraiment bouger
    lag = float(lags[int(np.argmax(sc))])
    cs, c0 = corr(lag), corr(0.0)
    amp = np.nanstd(mi[good][:, :2], 0)
    res.update({"decalage_ms": round(lag * 1000, 1), "correlation_xy": [round(c, 3) for c in cs[:2]], "correlation_rot": round(cs[2], 3),
                "correlation_xy_decalage_0": [round(c, 3) for c in c0[:2]],
                "amplitude_image_px_par_image": [round(float(x), 2) for x in amp]})
    print(json.dumps(res, ensure_ascii=False))
    if a.json:
        json.dump(res, open(a.json, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
