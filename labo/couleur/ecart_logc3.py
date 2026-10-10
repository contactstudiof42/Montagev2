"""D'où vient l'écart de ~2e-3 entre colour et OCIO sur LogC3 / S-Log3 ? (BACKLOG 41, session 7)
python3 -I labo/couleur/ecart_logc3.py
On sépare les deux étages : (1) la matrice 709 -> gamut caméra (linéaire), (2) la courbe log seule.
"""
import numpy as np, colour, PyOpenColorIO as OCIO
cfg = OCIO.Config.CreateFromBuiltinConfig("studio-config-v4.0.0_aces-v2.0_ocio-v2.5")
names = [c.getName() for c in cfg.getColorSpaces()]
rng = np.random.default_rng(0)
X = np.concatenate([rng.uniform(0, 1, (2000, 3)), np.array([[.18, .18, .18], [1, 0, 0], [0, 1, 0], [0, 0, 1]])]).astype(np.float32)


def ocio(src, dst, x):
    p = cfg.getProcessor(src, dst).getDefaultCPUProcessor(); y = np.ascontiguousarray(x, np.float32).copy(); p.applyRGB(y); return y


SRC = "Linear Rec.709 (sRGB)"
cas = [("ARRI LogC3 (EI800)", "ARRI Wide Gamut 3", colour.models.log_encoding_ARRILogC3),
       ("S-Log3 S-Gamut3.Cine", "S-Gamut3.Cine", colour.models.log_encoding_SLog3)]
lin_names = [n for n in names if n.startswith("Linear")]
print("Espaces linéaires disponibles :", [n for n in lin_names if "ARRI" in n or "S-Gamut" in n])
for log_name, gamut, enc in cas:
    lin_ocio = [n for n in lin_names if gamut.split()[0] in n and gamut.split()[-1].split(".")[0] in n]
    lin_ocio = lin_ocio[0] if lin_ocio else None
    # colour : matrice directe 709 -> gamut (blancs D65 identiques : pas de CAT)
    M = colour.matrix_RGB_to_RGB(colour.RGB_COLOURSPACES["ITU-R BT.709"], colour.RGB_COLOURSPACES[gamut], chromatic_adaptation_transform=None)
    lin_colour = X @ M.T
    full_ocio = ocio(SRC, log_name, X)
    full_colour = enc(lin_colour)
    print(f"\n== {log_name}  (linéaire OCIO : {lin_ocio})")
    print(f"  chaîne complète : écart max {np.abs(full_ocio - full_colour).max():.2e}")
    if lin_ocio:
        lo = ocio(SRC, lin_ocio, X)
        print(f"  étage matrice (linéaire) : écart max {np.abs(lo - lin_colour).max():.2e}")
        curve_ocio = ocio(lin_ocio, log_name, lin_colour)
        print(f"  étage courbe seule (même entrée) : écart max {np.abs(curve_ocio - enc(lin_colour)).max():.2e}")
        # chaîne colour avec la matrice OCIO : isole la courbe
        print(f"  matrice OCIO + courbe colour : écart max {np.abs(full_ocio - enc(lo)).max():.2e}")
        # Bradford aller-retour D65->D60->D65 : la matrice passe-t-elle par ACES ?
        Mb = colour.matrix_RGB_to_RGB(colour.RGB_COLOURSPACES["ITU-R BT.709"], colour.RGB_COLOURSPACES["ACES2065-1"], "Bradford")
        Mg = colour.matrix_RGB_to_RGB(colour.RGB_COLOURSPACES["ACES2065-1"], colour.RGB_COLOURSPACES[gamut], "CAT02")
        print(f"  hypothèse 709 -Bradford-> AP0 -CAT02-> gamut : écart à OCIO {np.abs(X @ (Mg @ Mb).T - lo).max():.2e}")
        Mg2 = colour.matrix_RGB_to_RGB(colour.RGB_COLOURSPACES["ACES2065-1"], colour.RGB_COLOURSPACES[gamut], "Bradford")
        print(f"  hypothèse 709 -Bradford-> AP0 -Bradford-> gamut : écart à OCIO {np.abs(X @ (Mg2 @ Mb).T - lo).max():.2e}")
    g = np.array([[.18, .18, .18]], np.float32)
    print(f"  gris 18 % : OCIO {ocio(SRC, log_name, g)[0][0]:.5f}  colour {enc(g @ M.T)[0][0]:.5f}")
