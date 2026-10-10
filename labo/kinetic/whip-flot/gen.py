"""Génère des coupes whip pan synthétiques avec vérité terrain (numpy + OpenCV, sans Blender).
python3 gen.py SORTIE     -> SORTIE/<cas>/A/f_01..12.png, B/f_01..12.png, verite.json

Principe : une « caméra » 320×180 balaie une grande texture (bruit multi-échelle coloré + rectangles + traits).
Plan A : accélère de 0 à vmax px/image (profil quadratique) ; plan B (autre texture = autre lieu) part de vmax et décélère.
Flou de bougé : moyenne de 16 sous-images sur un obturateur de 0,5 image (180°), positions calculées en continu,
donc l'animation est « prolongée au-delà des bords » (règle 1 du labo whip) — sauf le cas `bord_net`.
La direction donnée est celle du DÉFILEMENT DE L'IMAGE (contenu), en degrés : 0 = vers la droite, 90 = vers le bas."""
import sys, os, json, numpy as np, cv2

W, H, N, SUB = 320, 180, 12, 16
rng = np.random.default_rng(42)

def texture(seed, taille=2400, rayures=False):
    r = np.random.default_rng(seed)
    t = np.zeros((taille, taille, 3), np.float32)
    for s, a in [(3, .25), (11, .35), (41, .5), (151, .6)]:
        n = r.random((taille // s + 2, taille // s + 2, 3)).astype(np.float32)
        t += a * cv2.resize(n, (taille, taille), interpolation=cv2.INTER_CUBIC)[:taille, :taille]
    t = (t - t.min()) / (t.max() - t.min())
    for _ in range(500):  # rectangles colorés (structures nettes)
        x, y = r.integers(0, taille - 60, 2); w, h = r.integers(6, 60, 2)
        t[y:y + h, x:x + w] = r.random(3)
    if rayures:  # piège : texture périodique (barres de 24 px) -> ambiguïté de correspondance
        x = np.arange(taille); bar = ((x // 12) % 2).astype(np.float32)
        t = 0.15 * t + 0.85 * bar[None, :, None]
    return (t * 255).astype(np.float32)

def position(v_de_t, t):  # intégrale numérique de la vitesse (px/image) de 0 à t
    ts = np.linspace(0, t, 200); return np.trapezoid([v_de_t(u) for u in ts], ts) if t > 0 else 0.0

def plan(tex, angle, vprofil, bord_net=False, bruit=2.0):
    d = np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))])
    c0 = np.array([tex.shape[1] / 2, tex.shape[0] / 2])
    imgs = []
    for f in range(1, N + 1):
        acc = np.zeros((H, W, 3), np.float32)
        for k in range(SUB):
            t = f + (k + .5) / SUB * .5 - .25           # obturateur 180° centré sur l'image
            if bord_net: t = min(max(t, 1), N)            # animation figée hors des clés 1..12
            p = c0 - d * position(vprofil, t)             # le contenu défile dans +d => la fenêtre recule
            M = np.float32([[1, 0, p[0] - W / 2], [0, 1, p[1] - H / 2]])
            acc += cv2.warpAffine(tex, M, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP)
        img = acc / SUB + rng.normal(0, bruit, acc.shape)
        imgs.append(np.clip(img, 0, 255).astype(np.uint8))
    return imgs

def sortie(vmax): return lambda t: vmax * (np.clip(t, 0, N) / N) ** 2
def entree(vmax): return lambda t: vmax * (1 - (np.clip(t, 1, N + 1) - 1) / N) ** 2

# (nom, angle A, angle B, vmax, verite, options)
CAS = [
    ("meme_sens_30",    0,   0,  30, "raccord", {}),
    ("meme_sens_60",    0,   0,  60, "raccord", {}),
    ("meme_sens_100",   0,   0, 100, "raccord", {}),
    ("meme_sens_gauche",180, 180, 60, "raccord", {}),
    ("diag_30deg",      0,  30,  60, "raccord", {}),
    ("inverse_30",      0, 180,  30, "inverse", {}),
    ("inverse_60",      0, 180,  60, "inverse", {}),
    ("inverse_100",   180,   0, 100, "inverse", {}),
    ("vert_horiz_60",   0,  90,  60, "cassure", {}),
    ("horiz_vert_60", 270, 180,  60, "cassure", {}),
    ("diag_60deg",      0,  60,  60, "cassure", {}),
    ("controle_fixe",   0,   0,   0, "statique", {}),
    ("bord_net_60",     0,   0,  60, "raccord", {"bord_net": True}),
    ("rayures_60",      0,   0,  60, "raccord", {"rayures": True}),
    ("rayures_inv_60",  0, 180,  60, "inverse", {"rayures": True}),
]

if __name__ == "__main__":
    out = sys.argv[1]; verite = {}
    for i, (nom, aA, aB, v, vt, o) in enumerate(CAS):
        tA = texture(100 + i, rayures=o.get("rayures", False)); tB = texture(200 + i, rayures=o.get("rayures", False))
        for lettre, tex, ang, prof in [("A", tA, aA, sortie(v)), ("B", tB, aB, entree(v))]:
            d = f"{out}/{nom}/{lettre}"; os.makedirs(d, exist_ok=True)
            for j, im in enumerate(plan(tex, ang, prof, o.get("bord_net", False))):
                cv2.imwrite(f"{d}/f_{j + 1:02d}.png", im[:, :, ::-1])
        verite[nom] = {"angle_A": aA, "angle_B": aB, "vmax": v, "verite": vt, **o}
        print(nom, flush=True)
    json.dump(verite, open(f"{out}/verite.json", "w"), indent=1)
