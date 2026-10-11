"""Contrôle de photosensibilité simplifié (WCAG 2.1 SC 2.3.1, logique proche d'ITU-R BT.1702).
python3 -I flash_check.py video.mp4 [--fps 25] [--detail]
Par image (réduite à 64×36) : luminance relative linéaire (sRGB → linéaire, Rec.709), part de l'écran
qui varie, et « rouge saturé » (R/(R+G+B) ≥ 0,8, variation de (R-G-B)×320 > 20, définition WCAG).
Transition = variation ≥ 10 % de luminance relative avec l'état sombre < 0,80, sur ≥ 25 % de la PIRE
fenêtre de 1/3 × 1/3 de l'écran (le champ de 10° du WCAG : 341×256 px sur 1024×768). Option --plein-ecran :
ancien critère (25 % de tout l'écran), trop permissif (session 7 : il laissait passer un carré de 6 % de l'écran).
Flash = paire de transitions opposées. Échec si > 3 flashs dans une fenêtre glissante d'une seconde.
Ce n'est PAS un Harding FPA : un outil de montage pour repérer les séquences à risque avant le test officiel.
"""
import subprocess, sys
import numpy as np

src = sys.argv[1]
fps = float(sys.argv[sys.argv.index("--fps") + 1]) if "--fps" in sys.argv else 25.0
w, h = 64, 36
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-vf", f"scale={w}:{h}:flags=area",
                      "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
v = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float64) / 255
lin = np.where(v <= 0.04045, v / 12.92, ((v + 0.055) / 1.055) ** 2.4)
L = lin @ np.array([0.2126, 0.7152, 0.0722])                   # luminance relative par pixel
s = v.sum(-1) + 1e-9
red = np.where(v[..., 0] / s >= 0.8, np.clip((v[..., 0] - v[..., 1] - v[..., 2]) * 320, 0, None), 0)


LOCAL = "--plein-ecran" not in sys.argv
WY, WX = h // 3, w // 3   # fenêtre « 10° » du WCAG : 341×256 sur un écran 1024×768, soit 1/3 × 1/3


def part(mask):
    """part maximale du masque : sur tout l'écran (ancien critère) ou dans la pire fenêtre 1/3 × 1/3 (WCAG)."""
    if not LOCAL:
        return mask.mean()
    I = np.pad(mask.astype(np.float64).cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    S = I[WY:, WX:] - I[:-WY, WX:] - I[WY:, :-WX] + I[:-WY, :-WX]
    return S.max() / (WY * WX)


def transitions(prev, cur):
    """+1 / -1 / 0 pour la transition prev → cur (montée / descente / rien), critère luminance + surface."""
    d = cur - prev; dark = np.minimum(prev, cur)
    up = part((d >= 0.1) & (dark < 0.8)); dn = part((d <= -0.1) & (dark < 0.8))
    return 1 if up >= 0.25 else -1 if dn >= 0.25 else 0


def trans_rouge(prev, cur):
    d = cur - prev
    return 1 if part(d > 20) >= 0.25 else -1 if part(d < -20) >= 0.25 else 0


def flashes(T):
    """indices d'images où se termine un flash (paire de transitions opposées consécutives)."""
    out, last = [], 0
    for i, t in enumerate(T):
        if t != 0:
            if last != 0 and t == -last:
                out.append(i); last = 0
            else:
                last = t
    return out


res = {}
for nom, X, f in (("general", L, transitions), ("rouge", red, trans_rouge)):
    T = [0] + [f(X[i - 1], X[i]) for i in range(1, len(X))]
    F = flashes(T); win = int(round(fps))
    pire = max((sum(1 for k in F if i <= k < i + win) for i in range(max(1, len(X) - win + 1))), default=0)
    res[nom] = (len(F), pire)
    if "--detail" in sys.argv and F:   # images où se termine chaque flash (pour savoir quoi corriger)
        print(nom, "flashs aux images", F)
ok = all(p <= 3 for _, p in res.values())
print(f"{src}: {len(L)} images ; flashs généraux {res['general'][0]} (pire seconde {res['general'][1]}) ; "
      f"flashs rouges {res['rouge'][0]} (pire seconde {res['rouge'][1]}) -> {'OK' if ok else 'ÉCHEC'} [{'fenêtre 1/3' if LOCAL else 'plein écran'}]")
