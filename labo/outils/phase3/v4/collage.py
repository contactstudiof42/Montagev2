# collage.py TYPE IMAGE.png [ALPHA.png] SORTIE.mov N_IMAGES : collage sur arrêt sur image (référence : captured-by-h ;
# demande de Diego sur la V3 : « collages avec arrêt sur image puis reprise du mouvement » au lieu d'un fond de couleur).
# L'image figée est déjà étalonnée (rendue par Resolve) : le collage est calculé ici en pleine définition (1080x1920),
# puis encodé en ProRes 4444 et posé sans LUT. Une seule chose bouge pendant l'arrêt (le saut d'échelle du sujet,
# puis un écho qui grandit lentement, ou la photo qui se pose).
#   A : fond monochrome orange (encre presque noire -> orange), grain de papier ; sujet en couleur, cerne blanc, ombre.
#   B : fond papier blanc cassé imprimé à l'encre noire ; sujet en couleur, ombre seule.
#   C : l'image devient une photo à bord blanc, posée de biais sur la même image inversée (cyan), assombrie.
import sys, subprocess, numpy as np, cv2
typ, src = sys.argv[1], sys.argv[2]
alpha_p = sys.argv[3] if typ in "AB" else None
out, N = sys.argv[-2], int(sys.argv[-1])
W, H = 1080, 1920
img = cv2.imread(src, cv2.IMREAD_UNCHANGED)[..., :3][..., ::-1].astype(np.float32) / 65535   # RVB 0-1
img = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
rng = np.random.default_rng(7)
lum = img @ np.array([0.2126, 0.7152, 0.0722], np.float32)
ease = lambda u: 1 - (1 - min(max(u, 0), 1)) ** 3            # départ vif, arrivée freinée

def papier(seed):
    g = np.random.default_rng(seed).normal(0, 1, (H // 2, W // 2)).astype(np.float32)
    g = cv2.resize(cv2.GaussianBlur(g, (0, 0), 0.8), (W, H)); return g * 0.018

def duotone(l, encre, teinte, gamma=1.0):
    l = np.clip((l - np.percentile(l, 2)) / (np.percentile(l, 98) - np.percentile(l, 2) + 1e-6), 0, 1) ** gamma
    return np.array(encre, np.float32) * (1 - l[..., None]) + np.array(teinte, np.float32) * l[..., None]

def place(calque, a, s, dx=0, dy=0, ang=0):          # échelle / rotation autour du centre, puis décalage
    M = cv2.getRotationMatrix2D((W / 2, H / 2), ang, s); M[0, 2] += dx; M[1, 2] += dy
    c = cv2.warpAffine(calque, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)
    m = cv2.warpAffine(a, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return c, np.clip(m, 0, 1)

def sur(fond, c, m): return fond * (1 - m[..., None]) + c * m[..., None]

frames = []
if typ in "AB":
    a = cv2.imread(alpha_p, cv2.IMREAD_UNCHANGED).astype(np.float32) / 65535; a = cv2.resize(a, (W, H))
    dur = (a > 0.5).astype(np.uint8)
    cerne = cv2.dilate(dur, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))).astype(np.float32)
    cerne = cv2.GaussianBlur(cerne, (0, 0), 1.0)
    ombre = cv2.GaussianBlur(cerne, (0, 0), 16) * 0.45
    if typ == "A":   # tirage orange : l'orange domine, la scène y est imprimée plus sombre
        l = np.clip((lum - np.percentile(lum, 2)) / (np.percentile(lum, 99) - np.percentile(lum, 2) + 1e-6), 0, 1) ** 0.8
        fond0 = np.array((0.86, 0.36, 0.10), np.float32) * (0.40 + 0.60 * l[..., None]); encre_echo = np.array([0.42, 0.14, 0.04], np.float32)
    else:            # papier millimétré blanc cassé (captured-by-h) : fines lignes tous les 36 px, plus marquées tous les 180 px
        fond0 = np.broadcast_to(np.array((0.91, 0.895, 0.86), np.float32), (H, W, 3)).copy()
        ys, xs = np.mgrid[0:H, 0:W]
        fin = ((xs % 36) < 1.5) | ((ys % 36) < 1.5); fort = ((xs % 180) < 2.5) | ((ys % 180) < 2.5)
        fond0[fin] = fond0[fin] * 0.93 + np.array((0.55, 0.62, 0.70)) * 0.07
        fond0[fort] = fond0[fort] * 0.85 + np.array((0.45, 0.55, 0.66)) * 0.15
        encre_echo = np.array([0.20, 0.19, 0.18], np.float32)
    for k in range(N):
        g = papier(100 + k)                                    # le grain du papier vit, l'image non
        f = np.clip(fond0 + g[..., None], 0, 1)
        e_s = 1.18 + 0.06 * k / max(1, N - 1)                  # écho : grandit lentement pendant tout l'arrêt
        ce, me = place(np.broadcast_to(encre_echo, (H, W, 3)).copy(), a, e_s)
        f = sur(f, ce, me * (0.30 if typ == "A" else 0.10) * ease(k / 3))
        s = 1.0 + 0.045 * ease(k / 4)                          # saut d'échelle du sujet, freiné, en 4 images
        so, mo = place(np.zeros((H, W, 3), np.float32), ombre, s, 0, 14 * ease(k / 4))
        f = sur(f, so, mo)
        if typ == "A":
            cc, mc = place(np.ones((H, W, 3), np.float32), cerne, s); f = sur(f, cc, mc)
        cs, ms = place(img, a, s); f = sur(f, cs, ms)
        frames.append(f)
else:
    inv = 1 - img; inv = cv2.GaussianBlur(inv, (0, 0), 3) * 0.42          # inversé (cyan), assombri : pas de flash
    bord = 22
    photo = cv2.copyMakeBorder(img, bord, bord, bord, bord, cv2.BORDER_CONSTANT, value=(0.95, 0.94, 0.92))
    photo = cv2.resize(photo, (W, H)); pa = np.ones((H, W), np.float32)
    for k in range(N):
        u = ease(k / 4)
        s = 0.70 + 0.06 * u; ang = 1.5 + 1.8 * u               # la photo se pose : grandit un peu, tourne de 3°
        f = inv + papier(200 + k)[..., None]
        so, mo = place(np.zeros((H, W, 3), np.float32), cv2.GaussianBlur(pa, (0, 0), 1) , s, 10, 22)
        f = sur(f, so, cv2.GaussianBlur(mo, (0, 0), 18) * 0.55)
        cp, mp_ = place(photo, pa, s, 0, 0, ang); f = sur(f, cp, mp_)
        frames.append(np.clip(f, 0, 1))
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", f"{W}x{H}", "-r", "25", "-i", "-",
                      "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuv444p12le",
                      "-vf", "scale=out_color_matrix=bt709:out_range=tv", "-colorspace", "bt709", "-color_primaries", "bt709",
                      "-color_trc", "bt709", "-color_range", "tv", out], stdin=subprocess.PIPE)
for f in frames: p.stdin.write((np.clip(f, 0, 1) * 65535 + 0.5).astype(np.uint16).tobytes())
p.stdin.close(); p.wait()
cv2.imwrite(out.rsplit(".", 1)[0] + "_apercu.png", (np.clip(frames[min(6, N - 1)][..., ::-1], 0, 1) * 255).astype(np.uint8))
print("écrit", out, N, "images")
