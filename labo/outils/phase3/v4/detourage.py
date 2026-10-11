# detourage.py IMAGE.png PROFONDEUR.png SORTIE_ALPHA.png [decalage_seuil] [indices.json : {"fg": [[cx,cy,rx,ry],...], "bg": [...]}] : détourage d'une image figée en pleine résolution.
# Graine = carte de profondeur de Resolve (ResolveFX DepthMap, rendue en PNG) seuillée par Otsu (zones sûres / probables),
# contour par GrabCut sur l'image étalonnée, puis alpha doux par filtre guidé (suit les mèches, sans halo dur).
import sys, numpy as np, cv2
img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED); dep = cv2.imread(sys.argv[2], cv2.IMREAD_UNCHANGED)
d8 = lambda a: (a / 257).astype(np.uint8) if a.dtype == np.uint16 else a
img8 = d8(img)[..., :3]; dep = d8(dep); dep = dep[..., 0] if dep.ndim == 3 else dep
dec = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
t, _ = cv2.threshold(cv2.GaussianBlur(dep, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU); t = t + dec * 255
m = np.full(dep.shape, cv2.GC_PR_BGD, np.uint8)
m[dep > t - 12] = cv2.GC_PR_FGD
m[dep > t + 25] = cv2.GC_FGD
m[dep < t - 45] = cv2.GC_BGD
if len(sys.argv) > 5:   # indices manuels (ellipses en pixels) : cheveux sombres sur fond sombre, etc.
    import json
    ind = json.load(open(sys.argv[5]))
    for cx, cy, rx, ry in ind.get("fg", []): cv2.ellipse(m, (cx, cy), (rx, ry), 0, 0, 360, int(cv2.GC_FGD), -1)
    for cx, cy, rx, ry in ind.get("bg", []): cv2.ellipse(m, (cx, cy), (rx, ry), 0, 0, 360, int(cv2.GC_BGD), -1)
bg, fg = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(img8, m, None, bg, fg, 6, cv2.GC_INIT_WITH_MASK)
a = np.where((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD), 1.0, 0.0).astype(np.float32)
# garder la plus grande composante (le sujet), boucher les trous
n, lab, st, _ = cv2.connectedComponentsWithStats((a > 0.5).astype(np.uint8))
if n > 1:
    k = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); a = (lab == k).astype(np.float32)
a = cv2.morphologyEx(a, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
def guide(I, p, r, eps):
    bf = lambda x: cv2.boxFilter(x, -1, (r, r))
    mI, mp_ = bf(I), bf(p); cov = bf(I * p) - mI * mp_; var = bf(I * I) - mI * mI
    A = cov / (var + eps); B = mp_ - A * mI
    return bf(A) * I + bf(B)
gray = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
alpha = np.clip(guide(gray, a, 9, 2e-3), 0, 1)
alpha = np.clip((alpha - 0.08) / 0.84, 0, 1)          # pied et tête : pas de voile ni de trou
cv2.imwrite(sys.argv[3], (alpha * 65535).astype(np.uint16))
print("seuil", round(t), "couverture %.1f%%" % (100 * alpha.mean()))
