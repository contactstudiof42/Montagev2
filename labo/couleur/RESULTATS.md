# Labo couleur : résultats (2026-10-09)

Environnement : Python 3.13.16, colour-science 0.4.7, OpenColorIO 2.6.0, ffmpeg 6.1.1 (Ubuntu). SciPy et Matplotlib absents (avertissements sans effet sur ce labo).

## 1. Installation

`time pip install colour-science opencolorio` : **8,1 s**, réussie. Les deux paquets étaient en fait déjà présents (`Requirement already satisfied`). OpenColorIO s'importe (`import PyOpenColorIO`) et embarque 10 configs intégrées, dont `studio-config-v4.0.0_aces-v2.0_ocio-v2.5` et `cg-config-v5.0.0_aces-v2.1_ocio-v2.6`. **Aucun échec.**

## 2. Conversions et allers-retours (`conversions.py`, 0,6 s)

Commande : `python3 labo/couleur/conversions.py` (sortie complète dans `conversions.json`).
Entrée : 8 couleurs en Rec.709 scene-linear (gris 18 %, blanc 1.0, noir, primaires R/V/B, peau ColorChecker, spéculaire 4.0). Adaptation D65 vers D60 (ACES) en Bradford.

| Espace cible | Erreur max aller-retour | Gris 18 % encodé |
|---|---|---|
| sRGB (fonction IEC 61966-2-1) | 0 | 0.4614 |
| Rec.709 OETF (caméra) | 8e-17 | 0.4090 |
| Rec.709 écran BT.1886 (gamma 2.4) | 0 | 0.4894 |
| Rec.2020 linéaire | 1.3e-15 | 0.18 |
| ACEScg | 6.2e-15 | 0.18 |
| ACEScct | 5.3e-15 | 0.4136 |
| ARRI LogC3 EI800 / AWG3 | **5.0e-6** | 0.3910 |
| Sony S-Log3 / S-Gamut3.Cine | 9.2e-10 | 0.4106 |

Lecture :
- Tous les allers-retours sont exacts à la précision machine, sauf LogC3 (5e-6, soit 0,005 code 10 bits). C'est négligeable : le décodage LogC3 de colour n'est pas l'inverse algébrique strict (segment linéaire et coupure).
- Les encodages d'affichage (sRGB, 709, 1886) **écrêtent** au-dessus de 1.0 : le spéculaire 4.0 est perdu. ACEScg, ACEScct et les logs caméra le **gardent**. C'est toute la raison de travailler en scene-referred.
- **Le même gris 18 % vaut 0.39 à 0.49 selon l'encodage.** Une LUT qui attend du LogC3 (gris à 0.391) appliquée sur du Rec.709 (gris à 0.489) donne un résultat faux, et inversement.
- Le rouge 709 « pur » vaut `[0.627, 0.069, 0.016]` en Rec.2020 et `[0.613, 0.070, 0.021]` en ACEScg : les primaires ne sont pas les mêmes, les nombres RGB ne sont pas interchangeables.

### Contrôle croisé avec OCIO (studio-config ACES 2.0)

| Conversion depuis `Linear Rec.709 (sRGB)` | Écart max colour vs OCIO |
|---|---|
| ACEScg | 4.4e-8 (float32) |
| ACEScct | 8.0e-7 |
| Linear Rec.2020 | 1.9e-8 |
| ARRI LogC3 (EI800) | **1.75e-3** |
| S-Log3 S-Gamut3.Cine | **2.05e-3** |

Les espaces ACES concordent à la précision float32 (OCIO utilise donc aussi Bradford pour 709 vers AP1). Pour les logs caméra, l'écart d'environ 2e-3 (≈ 2 codes 10 bits) vient très probablement du chemin : OCIO passe par ACES2065-1 avec les matrices IDT des constructeurs, alors que colour va directement de 709 vers AWG3/S-Gamut3.Cine (même blanc D65). Ce n'est pas une erreur, mais c'est invisible à l'œil et ça montre qu'il faut **un seul moteur de référence par projet**. Cause exacte non vérifiée.

## 3. LUT créative et application ffmpeg (`look_lut.py`, 1,7 s au total)

Commande : `python3 labo/couleur/look_lut.py` (sortie dans `look_lut.json`).

- Look « teal & orange modéré », **display-referred** (entrée et sortie Rec.709 BT.1886, 0 à 1) :
  - contraste en S doux `f(x) = x - 0.25·sin(2πx)/2π` (pente 0,75 aux extrémités, 1,25 au milieu, noir et blanc fixes) ;
  - ombres froides `(-0.020, +0.004, +0.030)` × `(1-Y)²`, hautes lumières chaudes `(+0.025, +0.008, -0.020)` × `Y²`, Y = luma Rec.709 ;
  - poids ramenés à 0 au noir et au blanc purs. **Première version ratée** : sans ce garde-fou, le noir pur devenait `(0, 0.004, 0.030)`, donc un noir bleuté (défaut classique des LUT trouvées en ligne). Corrigé.
- LUT 33³ écrite avec `colour.write_LUT` : `labo/rendus/couleur/look_teal_orange_modere_33.cube` (1,08 Mo, donc rangée dans `rendus/` et régénérable). Relecture `colour.read_LUT` : écart max 5e-8.
- Mire générée en Python (960×540, PPM 16 bits) : rampe de gris, balayage de teintes saturées et désaturées, ColorChecker 24 encodé en 709/2.4.
- Application : `ffmpeg -i mire.ppm -vf lut3d=file=look.cube:interp=tetrahedral -pix_fmt rgb48be -f rawvideo mire_look.ppm` : 0,12 s.
- Avant/après : `labo/couleur/avant_apres.png` (960×270, **11 Ko**). Gauche = avant, droite = après.

Effet mesuré sur des repères (valeurs 709/2.4) :

| Repère | Avant | Après |
|---|---|---|
| Noir | 0, 0, 0 | 0, 0, 0 |
| Gris moyen | 0.489 ×3 | 0.487, 0.490, 0.490 |
| Ombre | 0.15 ×3 | 0.103, 0.121, 0.141 |
| Haute lumière | 0.85 ×3 | 0.901, 0.889, 0.867 |
| Peau ColorChecker #2 | 0.785, 0.586, 0.523 | 0.832, 0.611, 0.524 |
| Blanc | 1, 1, 1 | 1, 1, 1 |

Le gris moyen ne bouge presque pas (écart < 0,003). La peau se réchauffe et gagne du contraste sans virer à l'orange.

## 4. ffmpeg et Python donnent-ils le même résultat ?

Même entrée quantifiée 16 bits, interpolation tétraédrique des deux côtés :

| Comparaison | Écart moyen | Écart max |
|---|---|---|
| ffmpeg `lut3d` vs Python `LUT3D.apply` (tétraédrique) | **0,0017 code 8 bits** (0,007 code 10 bits) | 0,004 code 8 bits |
| LUT 33 pts (Python) vs fonction exacte | 0,022 code 8 bits | **1,40 code 8 bits** (5,6 codes 10 bits) |
| ffmpeg vs fonction exacte | 0,023 code 8 bits | 1,40 code 8 bits |

**Réussite** : ffmpeg et colour sont identiques (l'écart est l'arrondi 16 bits). L'écart avec la fonction exacte vient de la **discrétisation 33 points** : il est concentré dans les couleurs très saturées (balayage de teintes), là où la courbe varie vite. 1,4 code 8 bits reste invisible en usage normal, mais une LUT 33 n'est pas une transformation mathématiquement exacte : pour un look à forte courbure ou une conversion log, préférer 65 points ou une transformation analytique (OCIO, DCTL).

## 5. Échecs et limites

- Aucun échec d'installation.
- Défaut corrigé : noir bleuté de la première version de la LUT (voir 3).
- Limites : pas de test sur une vraie image caméra (pas de rush log disponible), pas de test de l'export avec tags (`-color_primaries/-color_trc/-colorspace`) dans ce labo (voir `labo/livraison`), écart OCIO/colour sur les logs non expliqué de façon certaine.

## Temps

Installation 8,1 s ; conversions 0,6 s ; LUT + ffmpeg + PNG 1,7 s. Rédaction et mise au point : environ 10 minutes.

## 4. L'écart OCIO / colour de ~2e-3 sur LogC3 et S-Log3, expliqué (session 7, `ecart_logc3.py`) [TESTÉ EN LABO]
`python3 -I labo/couleur/ecart_logc3.py` (colour-science 0.4.7, OCIO studio-config v4.0.0 ACES 2.0 / OCIO 2.5 ; 2 004 couleurs dont gris et primaires).

| Étage | LogC3 EI800 / AWG3 | S-Log3 / S-Gamut3.Cine |
|---|---|---|
| Chaîne complète 709 lin. → log | 1,75e-3 | 2,05e-3 |
| Matrice seule (linéaire) | **2,73e-3** | **2,72e-3** |
| Courbe seule (même entrée linéaire) | 1,4e-6 | 1,1e-6 |
| Hypothèse « 709 → AP0 en Bradford, puis AP0 → gamut caméra en **CAT02** » contre OCIO | **1,2e-6** | **8,7e-8** |
| Même hypothèse tout en Bradford | 2,73e-3 | 2,72e-3 |
| Gris 18 % (OCIO = colour) | 0,39101 | 0,41056 |

**Conclusion** : les courbes log sont identiques ; tout l'écart est dans la **matrice**. La config OCIO ne va pas directement de Rec.709 au gamut caméra (blancs D65 tous les deux, aucune adaptation nécessaire) : elle passe par ACES2065-1 (D60) avec **Bradford** à l'aller (convention ACES), puis revient au gamut caméra par les matrices **IDT des constructeurs**, construites en **CAT02**. Bradford puis CAT02 inverse ne s'annulent pas exactement : ~2,7e-3 en linéaire sur les couleurs saturées, **zéro sur le neutre**. Ce n'est pas une erreur, c'est une convention de chaîne.
Conséquence pratique : pour comparer deux logiciels au millième, comparer d'abord sur des **gris** (identiques), puis sur des primaires ; un écart de cet ordre limité aux couleurs saturées signale une différence d'adaptation chromatique (CAT), pas un bug de courbe. ~2 codes 10 bits : invisible, mais assez pour faire échouer un test d'égalité stricte dans un pipeline (phase 2 : Resolve RCM / ACES contre OCIO).
