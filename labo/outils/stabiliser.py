# stabiliser.py VIDEO DEBUT_S FIN_S --mode fixe|rail [--fenetre 1.0] [--ref 0.5] [--json sortie.json] [--png courbe.png]
# Après Gyroflow (qui ne corrige que la rotation de la caméra et le rolling shutter), corrige ce que la main a ajouté :
# translation, échelle (va-et-vient avant / arrière) et rotation résiduelle. Deux intentions du cadreur (Diego, 2026-10-11) :
#   fixe : il voulait un plan fixe sans trépied (lettres K-O-R-E, packshot posé) -> le sujet est épinglé sur l'image `--ref`
#          (fraction de la plage, 0,5 = milieu) ;
#   rail : il voulait un mouvement (travelling avant / arrière, glissement) -> on garde le trajet lissé (gaussienne de
#          `--fenetre` s, 1,0 par défaut, comme un rail), on retire seulement les à-coups. Jamais fixe.
# Mesure : points suivis (Lucas-Kanade) + similitude robuste (RANSAC) entre images consécutives, en coordonnées centrées,
# composées en une transformation cumulée (échelle s, rotation a, translation t, en px d'une image de 1080 de large).
# Sortie JSON, une entrée par image source dans [DEBUT-0,2 s, FIN+0,2 s] (marge pour les poignées), prête pour un Transform
# Fusion (Pivot au centre) : Size = base * s_cible / s, Angle = -(a_cible - a), Center = 0.5 + base * (T_cible - s_cible/s * R t)
# normalisé (x / largeur, y / hauteur, y vers le haut). `base` = zoom minimal pour qu'aucun bord noir n'entre (calculé).
# Image 0 du JSON = image source au temps DEBUT_S (image 0 de la composition du plan si son point d'entrée est DEBUT_S).
# Lancer avec .venv/bin/python -I.
import sys, json, subprocess, numpy as np, cv2

def lire(video, t0, t1, larg=540):
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                        "stream=width,height,r_frame_rate:stream_side_data=rotation", "-of", "json", video],
                       capture_output=True, text=True)
    s = json.loads(p.stdout)["streams"][0]
    w, h = s["width"], s["height"]
    if any(abs(int(d.get("rotation", 0))) == 90 for d in s.get("side_data_list", [])): w, h = h, w
    a, b = s["r_frame_rate"].split("/"); fps = float(a) / float(b)
    H = int(round(larg * h / w / 2)) * 2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(max(0, t0)), "-i", video, "-t", str(t1 - max(0, t0)),
                          "-vf", f"scale={larg}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, larg), fps, w, h

def cumul(fr):
    H, W = fr[0].shape; c = np.array([W / 2, H / 2])
    A = np.eye(3); out = [A.copy()]
    for i in range(1, len(fr)):
        p0 = cv2.goodFeaturesToTrack(fr[i - 1], 400, 0.01, 6)
        M = None
        if p0 is not None and len(p0) >= 12:
            p1, st, _ = cv2.calcOpticalFlowPyrLK(fr[i - 1], fr[i], p0, None, winSize=(21, 21), maxLevel=3)
            m = st.ravel() == 1
            if m.sum() >= 10:
                M, inl = cv2.estimateAffinePartial2D(p0[m] - c, p1[m] - c, method=cv2.RANSAC, ransacReprojThreshold=1.0)
        if M is None:
            M = np.array([[1, 0, 0], [0, 1, 0]], float)
        A = np.vstack([M, [0, 0, 1]]) @ A
        out.append(A.copy())
    k = 1080.0 / W
    s = np.array([np.hypot(a[0, 0], a[1, 0]) for a in out])
    ang = np.degrees(np.array([np.arctan2(a[1, 0], a[0, 0]) for a in out]))
    t = np.array([[a[0, 2] * k, a[1, 2] * k] for a in out])
    return s, ang, t

def lisser(x, sig):
    r = int(3 * sig); g = np.exp(-np.arange(-r, r + 1) ** 2 / (2 * sig ** 2)); g /= g.sum()
    x2 = x if x.ndim > 1 else x[:, None]
    pad = np.pad(x2, ((r, r), (0, 0)), mode="reflect" if len(x2) > r else "edge")
    y = np.stack([np.convolve(pad[:, j], g, mode="valid") for j in range(x2.shape[1])], axis=1)
    return y if x.ndim > 1 else y[:, 0]

if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda n, d=None: (a[a.index(n) + 1] if n in a else d)
    video, t0, t1 = a[0], float(a[1]), float(a[2])
    mode = opt("--mode", "rail"); fen = float(opt("--fenetre", 1.0)); ref = float(opt("--ref", 0.5))
    m0 = min(0.2, t0); fr, fps, W, H = lire(video, t0 - m0, t1 + 0.2)
    s, ang, t = cumul(fr)
    if mode == "fixe":
        i = int(round(m0 * fps + ref * (t1 - t0) * fps)); i = min(max(i, 0), len(s) - 1)
        sc, ac, tc = np.full_like(s, s[i]), np.full_like(ang, ang[i]), np.tile(t[i], (len(t), 1))
    else:
        sig = max(1.0, fen * fps / 2.0)
        sc, ac, tc = np.exp(lisser(np.log(s), sig)), lisser(ang, sig), lisser(t, sig)
    # normaliser : l'image de référence (milieu) garde son cadrage d'origine
    j = len(s) // 2; ns, na, nt = sc[j] / s[j], ac[j] - ang[j], tc[j] - t[j]
    sc, ac, tc = sc / ns, ac - na, tc - nt
    rs = sc / s; ra = ac - ang; Hp = 1080.0 * H / W
    R = lambda d: np.array([[np.cos(np.radians(d)), -np.sin(np.radians(d))], [np.sin(np.radians(d)), np.cos(np.radians(d))]])
    off = np.array([tc[k] - rs[k] * (R(ra[k]) @ t[k]) for k in range(len(s))])   # T / base, px centrés, y vers le bas
    def sans_bord(base):   # chaque coin de l'image de sortie doit venir de l'intérieur de l'image source
        for k in range(len(s)):
            Ri = R(-ra[k])
            for q in ((540, Hp / 2), (-540, Hp / 2), (540, -Hp / 2), (-540, -Hp / 2)):
                p_ = Ri @ (np.array(q) / base - off[k]) / rs[k]
                if abs(p_[0]) > 540 or abs(p_[1]) > Hp / 2: return False
        return True
    lo, hi = 1.0, 1.6
    if not sans_bord(lo):
        for _ in range(30):
            mid = (lo + hi) / 2
            if sans_bord(mid): hi = mid
            else: lo = mid
        lo = hi
    base = round(float(lo) * 1.003, 4)
    cles = []
    for k in range(len(s)):
        T = base * off[k]
        # Fusion : Angle positif = sens inverse des aiguilles d'une montre, Y vers le haut
        cles.append(dict(image=k - int(round(m0 * fps)), Size=round(float(base * rs[k]), 5), Angle=round(float(-ra[k]), 4),
                         X=round(0.5 + float(T[0]) / 1080.0, 6), Y=round(0.5 - float(T[1]) / Hp, 6)))
    ecart = np.hypot(*(t - tc).T)
    res = dict(video=video.split("/")[-1], mode=mode, fps=fps, images=len(s), base=base,
               main_px_moy=round(float(ecart.mean()), 2), main_px_pic=round(float(ecart.max()), 2),
               echelle_main_pct=round(float(100 * np.abs(s / sc - 1).max()), 2), rotation_main_deg=round(float(np.abs(ang - ac).max()), 3))
    print(json.dumps(res, ensure_ascii=False))
    if opt("--json"): json.dump(dict(res, cles=cles), open(opt("--json"), "w"))
    if opt("--png"):
        from PIL import Image, ImageDraw
        Wd, Hd = 900, 360; im = Image.new("RGB", (Wd, Hd), (20, 20, 20)); dr = ImageDraw.Draw(im); n = len(s)
        X = lambda i: 40 + i * (Wd - 60) / max(1, n - 1)
        for y0, series, lab in ((90, [t[:, 0], tc[:, 0], t[:, 1], tc[:, 1]], "x / y (px) : brut, cible"), (270, [100 * (s - 1), 100 * (sc - 1)], "échelle (%) : brute, cible")):
            e = max(1e-6, max(np.abs(z - z[0]).max() for z in series))
            for z, col in zip(series, [(255, 120, 120), (255, 255, 255), (120, 160, 255), (200, 200, 200)]):
                dr.line([(X(i), y0 - (z[i] - z[0]) / e * 70) for i in range(n)], fill=col, width=2)
            dr.text((44, y0 - 85), f"{lab} — ±{e:.1f}", fill=(230, 230, 230))
        im.save(opt("--png"))
