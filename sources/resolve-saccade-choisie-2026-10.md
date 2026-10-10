# Saccade choisie (step-printing) dans DaVinci Resolve 19 à 21

> BACKLOG 90 [TECH]. Recherche faite le 2026-10-10. Complète `sources/premiere-ae-saccade-choisie-2026-10.md` (définitions, usage artistique, version Premiere / After Effects).
> **Tout ce document est [THÉORIQUE]** : rien n'a été testé dans Resolve (pas installable dans la VM).
> Méthode : les trois manuels de référence officiels ont été téléchargés en PDF depuis documents.blackmagicdesign.com, convertis en texte (`pdftotext`) et lus aux pages citées. Les numéros de page imprimés en pied de page sont identiques aux numéros de page du PDF dans les trois manuels.
> Libellés : interface **anglaise**, cités tels qu'ils apparaissent dans le manuel. Un nom absent du manuel est signalé comme tel.

## Sources (consultées le 2026-10-10)
- **RM21** : *DaVinci Resolve 21 Reference Manual*, juillet 2026, 4444 p. https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_21_Reference_Manual.pdf
- **RM20** : *DaVinci Resolve 20 Reference Manual*, juillet 2025, 4234 p. https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_20_Reference_Manual.pdf
- **RM19** : *DaVinci Resolve 19.1 Reference Manual*, février 2025, 4032 p. https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_19_Reference_Manual.pdf
- **Liens en 403** : aucun. Les PDF se téléchargent directement. Un extrait relayé par mans.io (manuel « Speed Editor ») est apparu dans la recherche ; il n'a pas été utilisé puisque le manuel officiel était lisible.

Correspondance des sections entre versions (même texte sauf mention) :

| Section | RM21 | RM20 | RM19 |
|---|---|---|---|
| Chapitre « Speed Effects » (Freeze Frame, Retime Controls, Retime Curves, Speed Effect Processing) | ch. 58, p. 1253-1266 | p. 1070-1082 | p. 994-1005 |
| Project Settings > Master Settings > Frame Interpolation | ch. 6, p. 148-149 | p. 146 | p. 142 |
| Tableau d'import XML / AAF / EDL (« Importing Effects when Conforming Edits ») | ch. 22, p. 482-485 | p. 1134-1137 | p. 1052-1055 |
| Tableau des allers-retours (« Delivery Effects Processing ») | ch. 185, p. 4172-4173 | p. 4020-4021 | p. 3840-3841 |
| Fusion Trails | ch. 97, p. 2350-2352 | p. 2238 | p. 2125 |
| Fusion Time Speed / Time Stretcher | ch. 111, p. 2657-2662 | p. 2534 et suiv. | p. 2404 et suiv. |
| Resolve FX Temporal (Motion Trails, Smear…) | ch. 166, p. 3750-3753 | p. 3600-3601 | p. 3444-3445 |

## 1. Les contrôles de vitesse et où ils se règlent

### 1.1 Freeze Frame [THÉORIQUE]
- **Clip > Freeze Frame**, raccourci **Shift-R** : le clip *entier* devient une image figée, celle qui est sous la tête de lecture. Pour l'annuler, il faut retirer l'effet de vitesse avec le dialogue **Remove Attributes**, ou décocher **Freeze Frame** dans le dialogue Change Clip Speed. [RM21 p. 1254]
- **Clip > Change Clip Speed** (ou clic droit > Change Clip Speed) : cases **Ripple Sequence**, **Reverse Speed**, **Freeze Frame**, **Pitch Correction**, et boutons Maintain Timing / Stretch to fit. [RM21 p. 1255-1256]
- **Inspector > Video > Speed Change** (disponible dans les pages Cut et Edit) : **Direction** (avant, arrière ou freeze frame), **Speed %** et **Frames Per Second** (les deux acceptent des clés), **Duration**, **Ripple Sequence**, **Pitch Correction**. [RM21 p. 1256]

### 1.2 Retime Controls [THÉORIQUE]
- **Clip > Retime Controls** (Cmd-R), ou clic droit > **Retime Clip**. Une piste de contrôle apparaît au-dessus du clip, avec des flèches de vitesse et un menu **Clip Speed** en bas au centre. [RM21 p. 1257]
- **Geler un instant au milieu du clip** : avec les Retime Controls ouverts, placer la tête de lecture sur l'image voulue, puis choisir **Freeze Frame** dans le menu Clip Speed. Deux *speed points* encadrent la tenue (barres rouges verticales). Il suffit ensuite de tirer le second pour régler la durée ; la lecture reprend à l'image suivante. [RM21 p. 1258-1259]
- Autres entrées du menu : **Add Speed Point**, **Change Speed**, **Reverse Segment**, **Clear Speed Point**, **Rewind**, **Speed Ramp**. [RM21 p. 1259-1260]
- **Piège pour la saccade** : « The change in speed from each speed segment to the next is automatically eased » [RM21 p. 1259]. Entre deux tenues faites par speed points, le passage est *adouci*, ce qui risque de transformer une saccade en ralenti. À vérifier en test.
- Fermer les contrôles (X, Échap, ou Cmd-R) ne change pas le timing. Un badge Retime reste alors sur le clip. [RM21 p. 1261]

### 1.3 Retime Curves : Retime Frame et Retime Speed [THÉORIQUE]
- **Retime Frame** : c'est un graphe temps source / temps timeline (axe vertical = image source, axe horizontal = image de timeline). Une diagonale correspond à 100 %, un segment plat à une tenue, un segment descendant à une lecture inversée. **Retime Speed** : une ligne plate à 100 %, sur laquelle on tire les *segments* (pas les points). Elle ne permet pas la marche arrière. Les points de ces courbes correspondent un à un aux speed points des Retime Controls. [RM21 p. 1261-1264]
- **Accès, différent selon les versions** :
  - **19 / 20** : clic droit sur le clip > **Retime Curve**. Le menu **Curve**, en haut à gauche du Curve Editor, choisit Retime Speed et/ou Retime Frame, et le bouton Curve de la barre de titre du clip ouvre ou ferme la courbe. [RM20 p. 1081 ; RM19 p. 1004]
  - **21** : sélectionner le clip, onglet **Keyframes** en haut de l'interface, icône **Keyframe Curves**, puis choisir Retime Speed et Retime Frame dans la liste des paramètres. [RM21 p. 1264]
- **Clés en palier (Step)** :
  - **RM21** documente dans le Curve Editor de la page Edit les boutons **Step In** (« using the value of the previous keyframe ») et **Step Out** (« using the value of the next keyframe »). On sélectionne plusieurs clés, puis on clique sur l'icône Step In ou Step Out en haut du Keyframe Editor. [RM21 ch. 60, p. 1303 et 1306-1307]
  - **RM21** ajoute une section « Retime Keyframing Controls » : les paramètres de retime y utilisent « the same bezier easing tools as the other parameters » (exemple donné : « easing into a freeze frame »). [RM21 p. 1305]
  - **Non trouvé** par recherche texte dans RM19 et RM20 : ni « Step In/Out » dans le chapitre de keyframing de la page Edit, ni « Retime Keyframing Controls ». Cela semble nouveau en 21.
  - **Déduction, non écrite dans le manuel** : en 21, des clés **Step** sur la courbe **Retime Frame** donneraient un vrai step-printing (chaque clé = une image source tenue jusqu'à la clé suivante). Le manuel ne dit nulle part explicitement que Step s'applique à Retime Frame. **À tester en priorité.**

### 1.4 Retime Process et Motion Estimation [THÉORIQUE]
- **Deux niveaux de réglage** [RM21 p. 1265 ; RM20 p. 1081-1082] :
  1. **Projet** : Project Settings > **Master Settings** > groupe **Frame Interpolation** > **Retime Process**. [RM21 p. 148]
  2. **Clip** : Inspector (Video) > groupe **Retime and Scaling** > **Retime Process**, plus **Motion Estimation** si Optical Flow est choisi. Le groupe contient aussi Scaling et Resize Filter. [RM21 p. 1249]
- **Priorité** : chaque clip est réglé par défaut sur **« Project Settings »**. Changer le réglage du projet modifie donc tous les clips « except for those with custom settings selected » [RM21 p. 148]. **Le réglage du clip l'emporte sur celui du projet.** Il n'existe pas de troisième niveau propre à la timeline : aucun réglage Retime Process n'a été trouvé dans Timeline Settings.
- **Ce réglage s'applique aussi aux clips de cadence différente de la timeline** (« clips in mixed frame rate timelines »), pas seulement aux effets de vitesse. [RM21 p. 148, 481]
- Les trois options [RM21 p. 148-149, 1265] :
  - **Nearest** : « frames are either dropped for fast motion, or duplicated for slow motion ». **C'est le seul mode sans mélange : c'est celui de la saccade.**
  - **Frame Blend** : « adjacent duplicated frames are dissolved together ». Il fond les tenues entre elles.
  - **Optical Flow** : fabrique de nouvelles images par estimation de mouvement. Il interpole et annule la saccade (artefacts possibles quand deux mouvements se croisent).
- **Motion Estimation** (ne sert qu'avec Optical Flow) : Project Settings, ou Standard Faster / Standard Better / Enhanced Faster / Enhanced Better / Speed Warp Faster / Speed Warp Better, plus **AI Speed Warp Metal** (macOS) dans 21. [RM21 p. 149, 1265-1266]
  - Le même réglage de projet sert à Image Stabilization et à Temporal Noise Reduction (page Color). Ce n'est donc pas un réglage propre au retime. [RM21 p. 149]
  - Speed Warp utilise le DaVinci Neural Engine. La restriction à la version Studio est affirmée par des tiers mais **n'a pas été trouvée** dans les passages lus.
- **Au rendu** : en mode Single clip, les effets de vitesse sont « baked » avec le Retime Process du projet ou celui de chaque clip. [RM21 p. 4173]

## 2. Tenir une image choisie N images, sans mélange [THÉORIQUE, méthodes déduites des fonctions documentées]

1. **Verrou anti-mélange d'abord** : passer **Retime Process = Nearest** sur chaque clip saccadé (Inspector), ou dans Master Settings si tout le projet est concerné. Si le rush est à cadence haute (50 ou 60p) sur une timeline à 24 ou 25, c'est aussi ce réglage qui décide si les images sont *sautées* (Nearest) ou *fondues* (Frame Blend). [RM21 p. 148, 481]
2. **Montage manuel image par image (méthode la plus sûre, l'équivalent du Frame Hold de Premiere)** : couper le clip à chaque frontière de tenue (lame), placer la tête de lecture sur l'image source voulue dans chaque segment, faire **Shift-R** (le segment entier fige cette image), puis trimer le segment à N images. Chaque segment = une image choisie, et la timeline devient la partition. Limite : Freeze Frame fige « the frame you parked the playhead over », donc l'image doit appartenir au segment. On la choisit avant de trimer, ou par slip. [RM21 p. 1254]
3. **Retime Controls > Freeze Frame en série** sur un seul clip : c'est possible pour quelques tenues longues, mais les transitions entre segments sont automatiquement adoucies [RM21 p. 1259]. Cette méthode est donc à réserver aux tenues de « pensée » (une seconde et plus), pas aux saccades de 2 à 4 images.
4. **Retime Frame en paliers (21)** : clés aux images choisies, passées en **Step In / Step Out**. C'est l'équivalent des clés Hold de Time Remap dans After Effects. Elle n'est pas confirmée pour la courbe Retime Frame (voir 1.3).
5. **Fusion, la voie la plus explicite** : MediaIn → **Time Stretcher**, avec **Interpolate Mode = Nearest** [RM21 p. 2661]. Sur la spline **Source Time** (« from which frame in the original sequence to begin sampling »), on pose une clé par image choisie, avec pour valeur le numéro de l'image source [RM21 p. 2661-2662]. Les clés sont ensuite passées en **Step In** ou **Step Out** dans le Spline Editor : boutons de la barre d'outils, menu contextuel, ou raccourcis **I** et **O** [RM21 ch. 71, p. 1605 ; ch. 63, p. 1360, qui compare Step à « a hold keyframe in After Effects »]. La combinaison Time Stretcher + Step est une déduction ; chaque élément est documenté séparément.
   - **Time Speed** : il ne sert pas à la saccade choisie, car sa **Speed** « cannot be animated ». Il est utile seulement pour un décalage (**Delay**) ou une vitesse fixe. Son bouton **Freeze Frame** règle Speed et Delay pour figer l'image courante. [RM21 p. 2658-2659]
   - En mode **Blend**, le curseur **Sample Spread** mélange les images voisines. Il faut l'éviter en restant en **Nearest**. [RM21 p. 2658, 2661]
6. **Saccade régulière (texture, pas choix)** : Resolve FX Temporal > **Stop Motion** [RM21 p. 3753], avec **Set Reference Frame**, **Reference Frame**, **Sampling Variation** (cadence plus irrégulière) et **Frame Repeat** (1 à 10). Il n'est pas marqué « Studio Version Only » et il **n'a pas été trouvé** dans RM19 / RM20 (sans doute nouveau en 21). C'est l'équivalent de Posterize Time.

## 3. Écho et traînée [THÉORIQUE]
- **Fusion > Trails [TRLS]** (Effect) [RM21 p. 2350-2352] : « ghost-like after-trail » de l'image, *uniquement le mouvement précédent*.
  - Contrôles : **Restart**, **Preroll**, **Reset/Preroll on Render**, **This Time Only**, **Preroll Frames**, **Lock RGBA**, **Gain** (plus haut = traînée plus longue et plus dense), **Rotate**, **Offset X/Y**, **Scale**, **Blur Size**. Il a une entrée Effect Mask pour limiter la traînée à une zone.
  - Pièges : l'effet repose sur un tampon d'images, donc il faut un pré-roll. Il faut appuyer sur Reset entre deux prévisualisations, sinon la traînée s'accumule. Trails « cannot render properly over the network » [RM21 p. 1421].
- **Resolve FX Temporal > Motion Trails (Studio Version Only)** [RM21 p. 3751-3752] : copies de l'image « to simulate clips shot with long shutter speeds ».
  - Réglages : **Trail Length**, **Dropoff** (cumulatif : 0,5 donne 50 %, puis 25 %, puis 12,5 %), **Composite Gamma** (Timeline / Rec. 709 / Linear / Custom), **Input Alpha**.
  - Groupe **Move Trail** : Pan, Pan Angle, Zoom, Rotate, **Reuse Current Frame**, Border Type. Point important pour la saccade : avec **Reuse Current Frame** désactivé (par défaut), les copies sont les images −1, −2, etc. **Pendant une tenue, ces images précédentes sont identiques à l'image tenue**, d'où une traînée qui s'éteint pendant la tenue et réapparaît au saut. C'est une déduction à vérifier, mais c'est possiblement le comportement voulu pour le look Wong Kar-wai.
- **Smear (Studio Version Only)** : fond **Frames Either Side** images de part et d'autre, avec **Luma Threshold** et **Chroma Threshold**. C'est un flou de *mélange*, qui annule la saccade s'il est posé après elle. [RM21 p. 3752]
- **Motion Blur (Studio Version Only)** : flou par flux optique (Motion Est. Type, Motion Range, Motion Blur 0-100, **Blur Direction** : Both Directions / From Previous Frame / Towards Next Frame, Granularity). C'est le même outil que la palette Motion Effects de la page Color [RM21 p. 3751, 3590]. **From Previous Frame** imite l'obturateur lent sans regarder l'image suivante.
- **Ordre de traitement** : dans Fusion, il est explicite (MediaIn → Time Stretcher en Nearest → Trails → MediaOut). Dans la page Edit, l'ordre entre le retime et un Resolve FX appliqué au clip **n'est pas documenté dans les passages lus**. Pour être sûr que la traînée vient *après* la saccade, on peut faire un compound clip de la saccade puis poser Motion Trails dessus. C'est une prudence, pas une règle du manuel. Rappel de `resolve-fusion-fairlight-2026-10.md` : les FX de la page Edit ne sont pas vus dans Fusion.
- **OpenFX tiers** : rien de propre à la traînée n'est documenté par Blackmagic. Le manuel ne cite que Genarts Smoke and Rain, à propos du rendu réseau [RM21 p. 1421].

## 4. Échange XML / AAF avec Premiere [THÉORIQUE, sourcé]
- **Premiere vers Resolve (import)**, tableau RM21 p. 482 (identique en RM20 p. 1134 et RM19 p. 1052) :
  - Linear Speed Effects : EDL Oui, FCP 7 XML Oui, FCPX XML Oui, AAF Oui.
  - Variable Speed Effects : EDL Non, XML Oui, AAF Oui.
  - **Freeze Frames : EDL Non, FCP 7 XML Non, FCPX XML Non, AAF Oui** (et l'AAF visé est celui de Media Composer / Symphony avec Timewarp).
  - Le XML de Premiere est un XML FCP 7. **Un Frame Hold de Premiere ne passe donc pas.**
- Les effets variables importés sont convertis en « one speed keyframe per frame ». Le mode d'interpolation (Frame Blend / Optical Flow) ne voyage que dans le XML FCPX (depuis la version 11.1). Il faut sinon le régler à la main dans Resolve pour retrouver la référence. [RM21 p. 485]
- Les effets non pris en charge ne sont ni importés ni affichés, mais ils sont « preserved internally » et réinjectés dans le XML ou l'AAF réexporté. [RM21 p. 482]
- **Resolve vers Premiere (aller-retour, rendu en Individual source clips)**, tableau RM21 p. 4172 :
  - Linear et Variable Speed Effects : « Sent Back » pour Premiere Pro.
  - **Freeze Frames : « N/A » pour Premiere** (« Rendered » seulement pour Media Composer).
  - Resolve ajoute 3 images de poignée aux clips à vitesse modifiée. [RM21 p. 4173]
- **Conséquence pratique** : une saccade choisie ne survit pas proprement à un échange. Il faut soit la construire dans l'application qui finalise, soit la **rendre en média** (rendu Single clip, qui « bake » les vitesses avec le Retime Process choisi [RM21 p. 4172-4173]) et échanger ce média. Le comportement d'une saccade faite de clips coupés + Freeze Frame à travers un XML n'est pas documenté.

## 5. Tableau de correspondance

| Besoin | Premiere / After Effects | Resolve |
|---|---|---|
| Tenir une image | Frame Hold Options (Hold On : In Point) / clé Hold de Time Remap | Freeze Frame (Shift-R) sur un segment coupé ; Retime Controls > Freeze Frame |
| Partition image par image | Coupes + Frame Hold / clés Hold sur Time Remap | Coupes + Shift-R ; Fusion Time Stretcher (Source Time en Step) ; Retime Frame en Step (21, à vérifier) |
| Pas de mélange | Time Interpolation = Frame Sampling / Frame Blending Off | Retime Process = **Nearest** (clip ; sinon projet) ; Fusion Interpolate Mode = Nearest |
| Saccade régulière | Posterize Time | Resolve FX **Stop Motion** (21) |
| Traînée | Echo, CC Wide Time | Fusion **Trails** ; Resolve FX **Motion Trails** (Studio) ; Motion Blur « From Previous Frame » (Studio) |

## 6. Tests phase 2
1. Rush 50p sur une timeline à 25 : Retime Process Project = Frame Blend, puis clip = Nearest. Exporter et vérifier qu'aucune image n'est fondue (priorité du clip sur le projet).
2. Retime Controls : trois Freeze Frame de 3 images. Compter à l'export s'il y a des images de transition adoucies entre les tenues (piège de l'« automatically eased »).
3. Resolve 21 : courbe Retime Frame avec clés Step In ou Step Out. Le palier est-il exact à l'image près ?
4. Fusion : Time Stretcher (Nearest, Source Time en Step), puis Trails. Comparer avec Motion Trails posé sur un compound clip de la version Edit.
5. Échange : XML FCP 7 d'une saccade faite de segments Shift-R vers Premiere. Qu'est-ce qui arrive (clip à 0 %, plan non figé, absent) ?
