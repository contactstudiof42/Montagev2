---
name: montage-couleur-pipeline
description: Gestion des couleurs et préparation de l'étalonnage — espaces (Rec.709, Rec.2020, sRGB, P3, ACES, ACEScg, ACEScct), log caméra (LogC3/C4, S-Log3, V-Log), LUT .cube techniques ou de look, OCIO, CST, IDT/ODT, RCM DaVinci, scene- ou display-referred, gamma 2.4 ou 2.2, tags couleur. Mots entendus : « l'image est délavée », « c'est grisâtre », « mes couleurs changent à l'export », « QuickTime n'affiche pas comme Premiere », « la LUT ne rend pas pareil », « on étalonne dans quel espace ? ». Quel look et pourquoi : montage-couleur-et-intention.
---

# Pipeline couleur : du rush log au master

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette, hypothèse à confirmer sur de vraies images (phase 2).

**Fait foi sur** : espaces, log, LUT (technique et créative : fabrication, application, garde-fous), ordre des transformations, tags. **Ailleurs** : quel look, quelle palette, faut-il un teal & orange → `montage-couleur-et-intention` ; tags et QC à l'export → `montage-loudness-livraison` ; RCM et nodes dans Resolve → `montage-resolve`.

Preuves : `labo/couleur/RESULTATS.md` (scripts `conversions.py`, `look_lut.py`). Sources : `sources/couleur-pipeline.md`.

## 1. Quand s'en servir

- **Avant** de toucher à l'étalonnage : décider de l'espace de travail, de la transformation d'entrée par caméra et de la sortie.
- Quand une image « change » entre logiciel, lecteur et plateforme : c'est presque toujours un problème de tag ou de transformation, rarement d'étalonnage.
- Quand on reçoit une LUT (d'un chef op, d'un pack en ligne) : savoir ce qu'elle attend en entrée avant de l'utiliser.

## 2. Pourquoi : ce qui compte

- [THÉORIQUE] **Une LUT créative n'est pas une conversion technique.** Une LUT technique change d'espace (LogC3 vers Rec.709) : elle est « juste » ou « fausse ». Une LUT créative (un look) est un choix artistique : elle attend une entrée précise et ne veut rien dire sur une autre. Mélanger les deux rôles dans une seule LUT « LogC vers look » enferme le projet : on ne peut plus changer la sortie (HDR, cinéma) sans refaire le look.
- [TESTÉ EN LABO] **Travailler en log ou en scene-referred garde la latitude.** Au labo, un spéculaire à 4.0 (2 diaphs au-dessus du blanc) survit à ACEScg, ACEScct, LogC3 et S-Log3, mais il est **écrêté** dès qu'on encode en sRGB ou Rec.709. Étalonner après l'écrêtage, c'est étalonner une image déjà amputée : hautes lumières plates, ciels cramés, pas de récupération possible.
- [TESTÉ EN LABO] **Normaliser d'abord, regarder ensuite.** Le même gris 18 % vaut 0.391 en LogC3, 0.411 en S-Log3, 0.414 en ACEScct et 0.489 en Rec.709/2.4. Un look posé sur l'image avant la normalisation travaille sur de mauvaises valeurs : le contraste tombe au mauvais endroit et les teintes dérivent différemment d'une caméra à l'autre. Ordre : **entrée (log caméra vers espace de travail) → corrections primaires → look → sortie**. Le look vient après la normalisation, pour être le même sur toutes les caméras.
- **Teal & orange : le dosage technique** (le choix de sens est dans `montage-couleur-et-intention`). S'il est choisi : modéré (±0,03 sur 1.0 suffit à se voir [ÉPROUVÉ EN MAQUETTE], sur mire), noirs et blancs gardés neutres, peau surveillée sur le vectorscope (ligne chair), appliqué **après** la normalisation.
- [THÉORIQUE] **Un écran, un espace de sortie, une référence.** Si on étalonne sur un écran sRGB de portable pour une diffusion TV Rec.709/2.4, on étalonne à l'aveugle. Dire sur quoi on regarde fait partie du pipeline.

## 3. Choisir son pipeline (décision rapide) [THÉORIQUE]

| Situation | Pipeline conseillé |
|---|---|
| Rushes 709 d'un téléphone ou d'un hybride sans log, livraison web | Display-referred Rec.709/2.4 suffit. Pas besoin d'ACES. |
| Une caméra log, livraison web/TV | Resolve RCM (DaVinci Wide Gamut / Intermediate) ou CST LogC/S-Log vers 709 en nœud d'entrée, puis look. |
| Plusieurs caméras log, VFX, ou livraison HDR et SDR | ACES (ACEScct pour étalonner, ACEScg pour le compositing) ou RCM, avec une config OCIO partagée avec l'AE/Nuke. |
| On reçoit une LUT de tournage (LUT de visée) | Elle sert de point de départ et de référence de l'intention du chef op, pas de rendu final. Vérifier son entrée (LogC3 EI800 ? S-Log3/SGamut3.Cine ?). |

## 4. Recettes

### 4.1 Convertir des valeurs entre espaces avec colour-science [TESTÉ EN LABO]

```python
import colour, numpy as np
CS = colour.RGB_COLOURSPACES
lin709 = np.array([0.18, 0.18, 0.18])
acescg = colour.RGB_to_RGB(lin709, CS["ITU-R BT.709"], CS["ACEScg"], chromatic_adaptation_transform="Bradford")
acescct = colour.log_encoding(acescg, "ACEScct")              # 0.4136
logc3 = colour.log_encoding(colour.RGB_to_RGB(lin709, CS["ITU-R BT.709"], CS["ARRI Wide Gamut 3"]), "ARRI LogC3")  # 0.3910
```
Allers-retours exacts (1e-15 ; LogC3 5e-6). colour et OCIO (studio-config ACES 2.0) concordent à 4e-8 sur ACEScg avec Bradford. Sur LogC3 et S-Log3, ils diffèrent de 2e-3 (≈ 2 codes 10 bits), donc on prend **un seul moteur de référence par projet**.

### 4.2 Convertir avec OCIO (config intégrée, sans fichier) [TESTÉ EN LABO]

```python
import PyOpenColorIO as OCIO
cfg = OCIO.Config.CreateFromBuiltinConfig("studio-config-v4.0.0_aces-v2.0_ocio-v2.5")
p = cfg.getProcessor("ARRI LogC3 (EI800)", "ACEScct").getDefaultCPUProcessor()
p.applyRGB([0.391, 0.391, 0.391])
```
OCIO 2.6 embarque les configs `cg-config` et `studio-config` (ACES 1.3, 2.0 et 2.1). Les noms exacts des espaces se lisent avec `[c.getName() for c in cfg.getColorSpaces()]`.

### 4.3 Fabriquer une LUT créative .cube [TESTÉ EN LABO]

1. Définir le look comme une fonction sur des valeurs **Rec.709/2.4 normalisées 0 à 1** (et l'écrire dans le TITLE et les commentaires du .cube).
2. `lut = colour.LUT3D(colour.LUT3D.linear_table(33)); lut.table = look(lut.table); colour.write_LUT(lut, "look.cube")`.
3. Garde-fous : courbe qui fixe 0 et 1, teintes pondérées à 0 au noir et au blanc purs (sinon noir bleuté, défaut constaté au labo), gris moyen quasi inchangé (écart < 0,003 au labo).
Script complet : `labo/couleur/look_lut.py`. Une 33³ pèse environ 1 Mo.

### 4.4 Appliquer une LUT avec ffmpeg [TESTÉ EN LABO]

```bash
ffmpeg -i entree_709.mov -vf "lut3d=file=look.cube:interp=tetrahedral" -c:v prores_ks -profile:v 3 sortie.mov
```
ffmpeg et colour-science (tétraédrique) donnent le même résultat : écart moyen **0,0017 code 8 bits**. Une LUT 33 points s'écarte de la fonction exacte de 1,4 code 8 bits au maximum, dans les couleurs très saturées : en 65 points ou avec une transformation analytique pour une conversion log exigeante.

### 4.5 Log caméra vers Rec.709 dans ffmpeg avec une LUT technique [THÉORIQUE]

Même commande avec la LUT constructeur (ARRI LogC3 vers Rec.709, Sony S-Log3 vers 709) **avant** le look : `-vf "lut3d=arri_logc3_709.cube,lut3d=look.cube"`. À valider sur un vrai rush log (aucun disponible au labo).

### 4.6 Taguer la sortie [TESTÉ EN LABO] (dans `labo/livraison`)

`-color_primaries bt709 -color_trc bt709 -colorspace bt709` (et `-color_range tv`). Voir `montage-loudness-livraison`.

## 5. Pièges [THÉORIQUE] (chiffres mesurés au labo)

- **Gamma 2.4 vs 2.2 vs sRGB.** Rec.709 diffusion = écran BT.1886 (≈ gamma 2.4, salle sombre). sRGB = fonction par morceaux proche de 2.2 (bureau éclairé). Le gris 18 % vaut 0.489 en 2.4 et 0.461 en sRGB. Étalonné en 2.4 et vu en 2.2, l'image paraît **délavée** dans les ombres. Étalonné en 2.2 et vu en 2.4, elle paraît **bouchée**. Le célèbre décalage « QuickTime vs Premiere/Resolve » vient de là (et du tag 1-1-1). Choisir sa cible (TV : 2.4 ; web : beaucoup choisissent 2.4 tagué 709, d'autres 2.2) et l'écrire dans le cahier des charges.
- **Tags couleur à l'export.** Un fichier sans `color_primaries/transfer/matrix` est interprété au hasard par chaque lecteur (BT.601 vs 709 en particulier, d'où des verts et des rouges qui bougent). Toujours taguer et vérifier avec `ffprobe -show_streams`.
- **LUT sur une mauvaise entrée.** Une LUT LogC3 sur du S-Log3, ou une LUT 709 sur du log : contraste et saturation faux, que l'on « corrige » ensuite à la main en détruisant l'image. Vérifier l'entrée attendue (TITLE, nom, doc du fournisseur). Vérifier aussi l'EI pour LogC3 (la courbe change avec l'EI).
- **LUT = boîte fermée de 0 à 1.** Tout ce qui dépasse 1.0 est écrêté par une LUT 3D classique. Ne jamais mettre une LUT créative sur du linéaire scene-referred.
- **Plage vidéo vs plage pleine.** 16-235 lu comme 0-255 : image délavée. 0-255 lu comme 16-235 : noirs bouchés. Vérifier `color_range`.
- **Double transformation.** Resolve en RCM convertit déjà l'entrée : ajouter en plus une LUT LogC vers 709 donne une image surcontrastée. Une seule transformation d'entrée.
- **Look qui contamine la peau.** Une peau qui sort de la ligne chair au vectorscope (vers le rouge ou le jaune) trahit un look trop poussé.

## 6. À vérifier en phase 2 (Resolve, After Effects)

**DaVinci Resolve**
- [ ] RCM : DaVinci YRGB Color Managed, espace de travail DaVinci Wide Gamut / Intermediate, sortie Rec.709 Gamma 2.4 ; vérifier que la transformation d'entrée est bien lue depuis les métadonnées caméra (et la forcer sinon).
- [ ] ACES : ACEScct, IDT par clip, ODT Rec.709 ; noter la version ACES (1.3 ou 2.0) proposée par la version de Resolve installée.
- [ ] Charger `look_teal_orange_modere_33.cube` sur un nœud après la normalisation et comparer à l'application ffmpeg (écart attendu ≈ 0).
- [ ] Export : vérifier les tags (`ffprobe`) avec « Rec.709 Gamma 2.4 » vs « Rec.709-A » (option Mac/QuickTime) et comparer dans QuickTime, VLC et un navigateur.
- [ ] Comparer un CST LogC3 vers 709 de Resolve avec la conversion colour/OCIO sur une mire (écart en codes 10 bits).

**After Effects**
- [ ] Gestion des couleurs de projet : mode OCIO avec la config ACES intégrée ou chargée (`studio-config`), espace de travail ACEScg, linéarisation, vue de sortie.
- [ ] Effet OCIO (ou plug-in) sur un calque de réglage : conversion LogC3 (EI800) vers ACEScct, comparée à `conversions.py`.
- [ ] Rendu : vérifier que l'export applique la transformation de sortie une seule fois et que les tags sont corrects.
- [ ] Aller-retour Resolve vers AE vers Resolve en EXR ACEScg : l'image doit revenir identique.

## Écart entre logiciels sur les logs caméra [TESTÉ EN LABO]
OCIO (config studio ACES 2.0) et colour-science diffèrent de ~2e-3 sur LogC3 / S-Log3 depuis Rec.709 : **les courbes sont identiques (1e-6)**, l'écart vient de la matrice : OCIO passe par ACES2065-1 (Bradford à l'aller, CAT02 dans les matrices IDT des constructeurs au retour). Gris identiques, couleurs saturées décalées d'~2 codes 10 bits. Pour diagnostiquer un écart entre deux outils : **comparer d'abord des gris** (courbe), **puis des primaires** (matrice / CAT). Détail : `labo/couleur/RESULTATS.md` §4, `labo/couleur/ecart_logc3.py`.
