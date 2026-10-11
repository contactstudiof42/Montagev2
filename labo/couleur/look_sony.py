"""Look « tirage film » pour des rushes Sony S-Log3 / S-Gamut3.Cine, cuit en une seule LUT .cube (un seul nœud dans Resolve).

Chaîne (celle d'un étalonneur, mais calculée) :
  1. S-Log3 -> linéaire scène (formule Sony), S-Gamut3.Cine -> primaires Rec.709 (colour-science, CAT Bradford),
     compression douce des valeurs hors gamut (pas de négatifs durs).
  2. Exposition (EXPO, en diaphs) et balance (gains R, G, B) : réglages de la scène, avant le film.
  3. Encodage Cineon log (685 / 300, noir 95), puis l'émulation de tirage Kodak 2383 D65 Rec.709 de Resolve
     (`LUT/Film Looks/Rec709 Kodak 2383 D65.cube`, interpolation trilinéaire) : contraste, noirs denses, couleur du tirage.
  4. Dosage : mélange avec une sortie « neutre » (même exposition, courbe de Rec.709 simple) selon FORCE, puis
     saturation des tons moyens (SAT) en protégeant les ombres.
Entrée : valeurs RVB 0-1 telles que Resolve et ffmpeg les lisent d'un HEVC Sony (niveaux vidéo ramenés à 0-1).
  5. Pied de courbe (PIED : noirs écrasés comme les références, 5 à 11 sur 255) et ombres neutralisées puis froides (OMBRES).
Usage : look_sony.py SORTIE.cube [EXPO=0.0] [FORCE=0.8] [SAT=1.0] [PIED=0] [OMBRES=0]
"""
import sys, numpy as np, colour

FILM = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/Film Looks/Rec709 Kodak 2383 D65.cube"
M = colour.matrix_RGB_to_RGB(colour.RGB_COLOURSPACES["S-Gamut3.Cine"], colour.RGB_COLOURSPACES["ITU-R BT.709"], "Bradford")
W709 = np.array([0.2126, 0.7152, 0.0722])

def slog3_vers_lin(x):
    x = np.asarray(x, np.float64)
    return np.where(x >= 171.2102946929 / 1023, 10 ** ((x * 1023 - 420) / 261.5) * 0.19 - 0.01, (x * 1023 - 95) * 0.01125 / (171.2102946929 - 95))

def compresse_gamut(rgb, seuil=0.8):
    # rapproche du gris les canaux trop éloignés (distance à l'achromatique), au-delà de `seuil` : pas de négatifs durs
    ach = rgb.max(-1, keepdims=True)
    d = np.where(ach > 1e-6, (ach - rgb) / np.maximum(np.abs(ach), 1e-6), 0)
    lim = 1.15
    dc = np.where(d > seuil, seuil + (d - seuil) / (1 + ((d - seuil) / (lim - seuil)) ** 1.2) ** (1 / 1.2), d)
    return ach - dc * np.abs(ach)

def lin_vers_cineon(lin):
    b = 10 ** ((95 - 685) / 300)
    return (685 + 300 * np.log10(np.maximum(lin * (1 - b) + b, 1e-6))) / 1023

def lit_cube(f):
    n = None; v = []
    for l in open(f):
        l = l.strip()
        if l.startswith("LUT_3D_SIZE"): n = int(l.split()[1])
        elif l and (l[0].isdigit() or l[0] in "-."): v.append([float(t) for t in l.split()[:3]])
    return np.array(v).reshape(n, n, n, 3), n   # indices [b][g][r] (R le plus rapide)

def applique_cube(rgb, cube, n):
    p = np.clip(rgb, 0, 1) * (n - 1); i0 = np.floor(p).astype(int); i0 = np.minimum(i0, n - 2); f = p - i0
    r0, g0, b0 = i0[..., 0], i0[..., 1], i0[..., 2]; fr, fg, fb = f[..., 0:1], f[..., 1:2], f[..., 2:3]
    c = lambda db, dg, dr: cube[b0 + db, g0 + dg, r0 + dr]
    c00 = c(0, 0, 0) * (1 - fr) + c(0, 0, 1) * fr; c01 = c(0, 1, 0) * (1 - fr) + c(0, 1, 1) * fr
    c10 = c(1, 0, 0) * (1 - fr) + c(1, 0, 1) * fr; c11 = c(1, 1, 0) * (1 - fr) + c(1, 1, 1) * fr
    c0 = c00 * (1 - fg) + c01 * fg; c1 = c10 * (1 - fg) + c11 * fg
    return c0 * (1 - fb) + c1 * fb

FILMC = lit_cube(FILM)

def look(x, expo=0.0, force=0.8, sat=1.0, gains=(1, 1, 1), pied=0.0, ombres=0.0):
    lin = slog3_vers_lin(x) @ M.T
    lin = compresse_gamut(lin) * (2 ** expo) * np.array(gains)
    film = applique_cube(lin_vers_cineon(lin), *FILMC)
    neutre = colour.models.eotf_inverse_BT1886(np.clip(lin, 0, 1))      # Rec.709 simple, sans épaule
    out = force * film + (1 - force) * neutre
    if sat != 1.0:
        y = (out @ W709)[..., None]
        w = np.clip((y - 0.05) / 0.25, 0, 1)            # pas de saturation ajoutée dans les ombres (film : ombres denses, pas colorées)
        out = y + (out - y) * (1 + (sat - 1) * w)
    if pied > 0:      # pied de courbe : écrase les noirs (x²/(x+t)), mi-tons presque gardés ; appliqué à la luminance, teinte gardée
        y = np.maximum((out @ W709)[..., None], 1e-6)
        y2 = y * y / (y + pied) * (1 + pied)
        out = out * (y2 / y)
    if ombres > 0:    # ombres neutralisées puis légèrement froides : la peau chaude se détache d'un noir propre
        y = (out @ W709)[..., None]
        w = np.clip(1 - y / 0.35, 0, 1) ** 2
        out = out + w * ombres * ((y - out) * 0.6 + y * np.array([-0.10, 0.02, 0.12]))
    return np.clip(out, 0, 1)

def ecrit_cube(f, n=33, **kw):
    g = np.linspace(0, 1, n)
    b, gg, r = np.meshgrid(g, g, g, indexing="ij")
    rgb = np.stack([r, gg, b], -1).reshape(-1, 3)
    out = look(rgb, **kw)
    with open(f, "w") as h:
        h.write(f'TITLE "P3 Sony look film 2383 {kw}"\nLUT_3D_SIZE {n}\n')
        for v in out: h.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")

if __name__ == "__main__":
    a = sys.argv[1:]
    kw = dict(expo=float(a[1]) if len(a) > 1 else 0.0, force=float(a[2]) if len(a) > 2 else 0.8, sat=float(a[3]) if len(a) > 3 else 1.0)
    if len(a) > 4: kw["pied"] = float(a[4])
    if len(a) > 5: kw["ombres"] = float(a[5])
    ecrit_cube(a[0], **kw); print("écrit", a[0], kw)
