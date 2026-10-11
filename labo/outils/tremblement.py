# tremblement.py VIDEO [debut_s] [fin_s] [--png sortie.png] [--fenetre 0.4] [--json reste.json]
# Mesure le tremblement d'un plan : déplacement global du décor image par image (corrélation de phase sur l'image
# en niveaux de gris, fenêtre de Hann), trajectoire cumulée de la caméra, trajectoire lissée (le mouvement voulu,
# moyenne glissante gaussienne de `fenetre` secondes), reste = tremblement. Résultats en pixels ramenés à une image
# de 1080 px de large (quelle que soit la taille du fichier lu). Imprime : moyenne |reste|, pic |reste|, vitesse
# voulue moyenne, et (option) une courbe PNG (trajectoire brute / lissée en x et y, reste dessous).
# Lancer avec .venv/bin/python -I. Seuils : voir montage-regard § « Voir le mouvement ».
import sys, subprocess, json, numpy as np, cv2

def lire(video, t0=None, t1=None, larg=360):
    args = ["ffmpeg", "-v", "error"]
    if t0 is not None: args += ["-ss", str(t0)]
    args += ["-i", video]
    if t1 is not None: args += ["-t", str(t1 - (t0 or 0))]
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height,r_frame_rate:stream_side_data=rotation",
                        "-of", "json", video], capture_output=True, text=True)
    s = json.loads(p.stdout)["streams"][0]
    w, h = s["width"], s["height"]
    rot = any(abs(int(d.get("rotation", 0))) == 90 for d in s.get("side_data_list", []))
    if rot: w, h = h, w
    a, b = s["r_frame_rate"].split("/"); fps = float(a) / float(b)
    H = int(round(larg * h / w / 2)) * 2
    raw = subprocess.run(args + ["-vf", f"scale={larg}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, larg).astype(np.float32)
    return fr, fps, w

def mesure(fr, fps, larg_src, fenetre=0.4):
    k = 1080.0 / fr.shape[2]          # ramène à 1080 px de large
    # Points suivis (Lucas-Kanade) puis similitude robuste (RANSAC) : la majorité des points = le décor, un sujet
    # qui bouge (geste, bras) est rejeté. Repli : corrélation de phase si trop peu de points.
    win = cv2.createHanningWindow(fr.shape[2:0:-1], cv2.CV_32F)
    u8 = [f.astype(np.uint8) for f in fr]
    d = [(0.0, 0.0)]
    for i in range(1, len(fr)):
        p0 = cv2.goodFeaturesToTrack(u8[i - 1], 300, 0.01, 6)
        ok = False
        if p0 is not None and len(p0) >= 12:
            p1, st, _ = cv2.calcOpticalFlowPyrLK(u8[i - 1], u8[i], p0, None, winSize=(21, 21), maxLevel=3)
            m = st.ravel() == 1
            if m.sum() >= 10:
                M, inl = cv2.estimateAffinePartial2D(p0[m], p1[m], method=cv2.RANSAC, ransacReprojThreshold=1.0)
                if M is not None and inl is not None and inl.sum() >= 8:
                    d.append((M[0, 2] * k, M[1, 2] * k)); ok = True
        if not ok:
            (dx, dy), _ = cv2.phaseCorrelate(fr[i - 1], fr[i], win)
            d.append((dx * k, dy * k))
    d = np.array(d); traj = np.cumsum(d, axis=0)
    sig = max(1.0, fenetre * fps / 2.0)
    r = int(3 * sig); x = np.arange(-r, r + 1); g = np.exp(-x ** 2 / (2 * sig ** 2)); g /= g.sum()
    pad = np.pad(traj, ((r, r), (0, 0)), mode="edge")
    lisse = np.stack([np.convolve(pad[:, j], g, mode="valid") for j in range(2)], axis=1)
    reste = traj - lisse
    amp = np.hypot(reste[:, 0], reste[:, 1])
    bord = min(r, len(amp) // 4)        # bords de la fenêtre moins fiables
    core = amp[bord:len(amp) - bord] if len(amp) > 2 * bord + 2 else amp
    vit = np.hypot(*np.diff(lisse, axis=0).T) * fps if len(lisse) > 1 else np.array([0])
    return dict(images=len(fr), fps=round(fps, 2), moyenne=round(float(core.mean()), 2), pic=round(float(core.max()), 2),
                vitesse_voulue_px_s=round(float(vit.mean()), 1)), traj, lisse, reste

def courbe(png, traj, lisse, reste, titre):
    from PIL import Image, ImageDraw
    W, H = 900, 420; im = Image.new("RGB", (W, H), (20, 20, 20)); dr = ImageDraw.Draw(im)
    n = len(traj); X = lambda i: 40 + i * (W - 60) / max(1, n - 1)
    def trace(y0, h, series, cols, ech=None):
        ech = ech or max(1e-6, max(np.abs(s).max() for s in series))
        dr.line([(40, y0), (W - 20, y0)], fill=(70, 70, 70))
        for s, c in zip(series, cols):
            dr.line([(X(i), y0 - s[i] / ech * h) for i in range(n)], fill=c, width=2)
        return ech
    e = trace(110, 90, [traj[:, 0] - traj[0, 0], lisse[:, 0] - traj[0, 0], traj[:, 1] - traj[0, 1], lisse[:, 1] - traj[0, 1]],
              [(255, 120, 120), (255, 255, 255), (120, 160, 255), (200, 200, 200)])
    dr.text((44, 6), f"{titre} — trajectoire x (rouge) y (bleu), lissée en blanc, échelle ±{e:.0f} px", fill=(230, 230, 230))
    amp = np.hypot(reste[:, 0], reste[:, 1])
    e2 = trace(380, 140, [amp], [(255, 210, 60)], ech=max(4.0, amp.max()))
    for s in (1, 2, 4):
        if s <= e2: dr.line([(40, 380 - s / e2 * 140), (W - 20, 380 - s / e2 * 140)], fill=(90, 60, 60)); dr.text((4, 374 - s / e2 * 140), f"{s} px", fill=(200, 120, 120))
    dr.text((44, 226), "tremblement |reste| (px, image 1080 de large)", fill=(255, 210, 60))
    im.save(png)

if __name__ == "__main__":
    a = [x for x in sys.argv[1:]]
    png = None; fen = 0.4
    if "--png" in a: i = a.index("--png"); png = a[i + 1]; del a[i:i + 2]
    if "--fenetre" in a: i = a.index("--fenetre"); fen = float(a[i + 1]); del a[i:i + 2]
    jout = None
    if "--json" in a: i = a.index("--json"); jout = a[i + 1]; del a[i:i + 2]
    v = a[0]; t0 = float(a[1]) if len(a) > 1 else None; t1 = float(a[2]) if len(a) > 2 else None
    fr, fps, w = lire(v, t0, t1)
    res, traj, lisse, reste = mesure(fr, fps, w, fen)
    print(json.dumps({"video": v.split("/")[-1], "debut": t0, "fin": t1, **res}, ensure_ascii=False))
    if png: courbe(png, traj, lisse, reste, v.split("/")[-1])
    if jout:   # reste image par image (px, image de 1080 de large ; y vers le bas) : sert à stabiliser en compensant
        json.dump({"fps": fps, "reste": np.round(reste, 2).tolist()}, open(jout, "w"))
