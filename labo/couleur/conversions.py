"""Labo couleur (a) : conversions entre espaces et vérification des allers-retours.

Point de départ : valeurs scene-linear Rec.709 (primaires sRGB/709, D65).
Chaque conversion est faite avec colour-science, puis refaite en sens inverse.
Contrôle croisé avec OpenColorIO (config intégrée studio-config ACES 2.0).
Usage : python3 conversions.py
"""
import json, warnings
warnings.filterwarnings("ignore")
import numpy as np
import colour

CS = colour.RGB_COLOURSPACES
CAT = "Bradford"  # D65 -> D60 (ACES). Les configs OCIO ACES utilisent aussi Bradford pour 709->AP1? voir RESULTATS.

# Couleurs de référence, scene-linear Rec.709
REF = {
    "gris 18 %": [0.18, 0.18, 0.18],
    "blanc diffus 1.0": [1.0, 1.0, 1.0],
    "noir 0.0": [0.0, 0.0, 0.0],
    "rouge 709 pur": [1.0, 0.0, 0.0],
    "vert 709 pur": [0.0, 1.0, 0.0],
    "bleu 709 pur": [0.0, 0.0, 1.0],
    "peau (ColorChecker light skin, lin)": list(colour.cctf_decoding(np.array([194, 150, 130]) / 255, "sRGB")),
    "spéculaire 4.0 (au-dessus du blanc)": [4.0, 4.0, 4.0],
}

def lin709_to(x, cible):
    if cible == "sRGB (encodé IEC 61966-2-1)":
        return colour.cctf_encoding(np.clip(x, 0, 1), "sRGB")
    if cible == "Rec.709 OETF (caméra)":
        return colour.oetf(np.clip(x, 0, 1), "ITU-R BT.709")
    if cible == "Rec.709 affichage BT.1886 (gamma 2.4 inverse)":
        return colour.eotf_inverse(np.clip(x, 0, 1), "ITU-R BT.1886")
    if cible == "Rec.2020 linéaire":
        return colour.RGB_to_RGB(x, CS["ITU-R BT.709"], CS["ITU-R BT.2020"], apply_cctf_encoding=False)
    if cible == "ACEScg (AP1 linéaire)":
        return colour.RGB_to_RGB(x, CS["ITU-R BT.709"], CS["ACEScg"], chromatic_adaptation_transform=CAT)
    if cible == "ACEScct":
        return colour.log_encoding(lin709_to(x, "ACEScg (AP1 linéaire)"), "ACEScct")
    if cible == "ARRI LogC3 EI800 / AWG3":
        awg = colour.RGB_to_RGB(x, CS["ITU-R BT.709"], CS["ARRI Wide Gamut 3"], chromatic_adaptation_transform=CAT)
        return colour.log_encoding(awg, "ARRI LogC3")
    if cible == "Sony S-Log3 / S-Gamut3.Cine":
        sg = colour.RGB_to_RGB(x, CS["ITU-R BT.709"], CS["S-Gamut3.Cine"], chromatic_adaptation_transform=CAT)
        return colour.log_encoding(sg, "S-Log3")
    raise KeyError(cible)

def to_lin709(y, source):
    if source == "sRGB (encodé IEC 61966-2-1)":
        return colour.cctf_decoding(y, "sRGB")
    if source == "Rec.709 OETF (caméra)":
        return colour.oetf_inverse(y, "ITU-R BT.709")
    if source == "Rec.709 affichage BT.1886 (gamma 2.4 inverse)":
        return colour.eotf(y, "ITU-R BT.1886")
    if source == "Rec.2020 linéaire":
        return colour.RGB_to_RGB(y, CS["ITU-R BT.2020"], CS["ITU-R BT.709"])
    if source == "ACEScg (AP1 linéaire)":
        return colour.RGB_to_RGB(y, CS["ACEScg"], CS["ITU-R BT.709"], chromatic_adaptation_transform=CAT)
    if source == "ACEScct":
        return to_lin709(colour.log_decoding(y, "ACEScct"), "ACEScg (AP1 linéaire)")
    if source == "ARRI LogC3 EI800 / AWG3":
        return colour.RGB_to_RGB(colour.log_decoding(y, "ARRI LogC3"), CS["ARRI Wide Gamut 3"], CS["ITU-R BT.709"], chromatic_adaptation_transform=CAT)
    if source == "Sony S-Log3 / S-Gamut3.Cine":
        return colour.RGB_to_RGB(colour.log_decoding(y, "S-Log3"), CS["S-Gamut3.Cine"], CS["ITU-R BT.709"], chromatic_adaptation_transform=CAT)
    raise KeyError(source)

CIBLES = ["sRGB (encodé IEC 61966-2-1)", "Rec.709 OETF (caméra)", "Rec.709 affichage BT.1886 (gamma 2.4 inverse)",
          "Rec.2020 linéaire", "ACEScg (AP1 linéaire)", "ACEScct", "ARRI LogC3 EI800 / AWG3", "Sony S-Log3 / S-Gamut3.Cine"]

def main():
    noms = list(REF)
    X = np.array([REF[n] for n in noms], dtype=np.float64)
    out = {"valeurs": {}, "aller_retour_erreur_max": {}}
    lignes = []
    for c in CIBLES:
        Y = lin709_to(X, c)
        back = to_lin709(Y, c)
        # les encodages display (sRGB, 709, 1886) clippent 0-1 : on compare à l'entrée clippée
        ref = np.clip(X, 0, 1) if ("sRGB" in c or "709" in c and "lin" not in c) else X
        err = float(np.max(np.abs(back - ref)))
        out["aller_retour_erreur_max"][c] = err
        out["valeurs"][c] = {n: [round(float(v), 6) for v in Y[i]] for i, n in enumerate(noms)}
        lignes.append(f"{c:50s} erreur max aller-retour = {err:.2e}")
    for l in lignes:
        print(l)
    print("\nValeurs clés (gris 18 %) :")
    for c in CIBLES:
        print(f"  {c:50s} {out['valeurs'][c]['gris 18 %']}")
    print("\nRouge 709 pur dans d'autres primaires (montre que le rouge 709 n'est pas 'pur' en 2020/AP1) :")
    for c in ["Rec.2020 linéaire", "ACEScg (AP1 linéaire)"]:
        print(f"  {c:30s} {out['valeurs'][c]['rouge 709 pur']}")

    # Contrôle croisé OCIO
    try:
        import PyOpenColorIO as OCIO
        cfgname = "studio-config-v4.0.0_aces-v2.0_ocio-v2.5"
        cfg = OCIO.Config.CreateFromBuiltinConfig(cfgname)
        names = [cs.getName() for cs in cfg.getColorSpaces()]
        def find(*mots):
            for n in names:
                if all(m.lower() in n.lower() for m in mots):
                    return n
            return None
        src = find("Linear Rec.709")
        pairs = {"ACEScg (AP1 linéaire)": find("ACEScg"), "ACEScct": find("ACEScct"),
                 "ARRI LogC3 EI800 / AWG3": find("LogC3", "EI800"), "Sony S-Log3 / S-Gamut3.Cine": find("S-Log3", "S-Gamut3.Cine"),
                 "Rec.2020 linéaire": find("Linear Rec.2020")}
        out["ocio"] = {"config": cfgname, "source": src, "ecarts_max_vs_colour": {}}
        print(f"\nContrôle croisé OCIO {OCIO.__version__} ({cfgname}), source = {src!r}")
        for c, dst in pairs.items():
            if not dst:
                print(f"  {c}: espace introuvable dans la config"); continue
            proc = cfg.getProcessor(src, dst).getDefaultCPUProcessor()
            Xo = X.astype(np.float32).copy()
            res = np.array([proc.applyRGB(list(map(float, px))) for px in Xo])
            d = float(np.max(np.abs(res - lin709_to(X, c))))
            out["ocio"]["ecarts_max_vs_colour"][c] = {"espace_ocio": dst, "ecart_max": d}
            print(f"  {c:32s} -> {dst!r:45s} écart max colour vs OCIO = {d:.2e}")
    except Exception as e:  # noqa
        out["ocio"] = {"erreur": repr(e)}
        print("OCIO indisponible :", e)

    with open(__file__.replace("conversions.py", "conversions.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
