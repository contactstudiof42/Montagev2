---
name: montage-preparation-tournage-vfx
description: Préparer un tournage qui aura des effets (supervision VFX légère) — repérer les plans à effets, choisir plateau / numérique / IA, réglages caméra pour la post (shutter, log, 10 bits, marge, open gate pour le vertical), fond vert, marqueurs de tracking, plaques propres, HDRI, écrans dans le champ, lumière à éteindre, son seul, checklist plateau. Mots d'un réalisateur : « on verra en post », « tu peux l'effacer ? », « on tourne sur fond vert ? », « on remplace l'écran du téléphone », « on éteint le lampadaire en post ? », « ça va se tracker ? ».
---

# Préparer un tournage pour les effets (version légère)

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] pratique de plateau courante, non vérifiée ici (défaut de ce skill) · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer sur un vrai plateau (phase 2).

**Fait foi sur** : ce qu'il faut capter au tournage pour la post (réglages, fond vert, plaques, références lumière, écrans, sources à éteindre). **Ailleurs** : le sens d'une couleur ou d'une lumière, espaces et log → `montage-couleur` ; plans générés → `montage-ia-generative` ; vertical → `montage-formats`.

**Statut honnête** (audit 2, 2026-10-13) : jamais pratiqué sur un plateau ; savoir sourcé et maquettes, aucune règle encore gagnée en projet. Version d'avant : `archives/audit-2/skills/montage-preparation-tournage-vfx/`.

Le but n'est pas de tout prévoir, mais d'éviter les deux phrases qui coûtent le plus cher : « on verra en post » et « on n'a pas de plaque ». Détails des maquettes : [`details.md`](details.md) ; nuit infrarouge : [`infrarouge.md`](infrarouge.md).

## 1. Quand et pourquoi
- **Tout plan où quelque chose sera ajouté, retiré, remplacé ou recadré.** Un effet raté vient presque toujours d'une information manquante au tournage, pas d'un manque de talent en post.
- **Choisir la méthode par l'intention**, pas par la mode :
  - *Plateau* (pratique) quand l'acteur doit réagir à la chose, quand la lumière de l'effet doit toucher le décor (feu, écran, flash), ou quand c'est moins cher qu'on croit (une lampe orange vaut mieux qu'un feu composité : la lumière du feu sur le décor fait plus que la flamme [ÉPROUVÉ EN MAQUETTE] (pièce 02)) ;
  - *Numérique* quand c'est dangereux, impossible ou répétitif (multiplication de foule, effacement, ciel) ;
  - *IA générative* (voir `montage-ia-generative`, daté) pour un plan d'ambiance sans personnage identifiable ou pour rallonger un plan de 1 à 2 s, jamais pour un visage ou un produit qui doit être exact.
- **Dire non** à l'effet qui ne raconte rien (`montage-direction-artistique`, étape 5) avant de le préparer.

## 2. Repérage des plans à effets (avant le plateau)
Pour chaque plan concerné, une ligne : n° de plan · ce qui change en post · méthode · ce qu'il faut capter · qui vérifie sur le plateau.

## 3. Réglages caméra utiles à la post
- **Log et 10 bits minimum** (ProRes 422 HQ, ou RAW) : les noirs et les dégradés supportent l'étalonnage et l'incrustation. Mesuré au labo : en 8 bits, un dégradé sombre fait des bandes, et le 10 bits les supprime (`labo/encodage/RESULTATS.md`, [TESTÉ EN LABO]).
- **Shutter** : 180° par défaut ; plus fermé (90° ou 45°) pour un plan à détourer ou à tracker vite (moins de flou de bougé, des bords nets), ou pour une esthétique saccadée volontaire. Ne pas fermer sous une lumière qui scintille (LED bas de gamme, néons) sans test.
- **Marge de recadrage** : tourner plus large ou en résolution supérieure (4K pour un livrable HD), **open gate** si le capteur le permet quand un **9:16** est prévu. Composer les plans clés avec une zone verticale sûre au centre (examen n°2).
- **Cadence** : décider avant (24/25/30 ; 50/60 pour les ralentis) ; ne pas mélanger 25 et 30 sans raison.
- **Objectif** : noter la focale, la distance de mise au point, la hauteur et l'inclinaison de la caméra pour chaque plan à effets (indispensable au camera tracking et à la 3D). Une grille ou une mire de distorsion filmée en début de journée par objectif.

## 4. Fond vert / bleu
- **Vert** pour la plupart des cas (le capteur y est plus sensible, moins de bruit) ; **bleu** si le sujet porte du vert, pour les cheveux blonds, ou de nuit (moins de débordement chaud).
- **Fond éclairé à part et uniformément** (écart ≤ 1/3 de diaphragme sur toute la surface), sans le surexposer : viser le niveau du gris moyen ou légèrement en dessous.
- **Distance sujet-fond : 2 à 3 m au moins** pour réduire le débordement (spill) et pouvoir flouter le fond ; éclairer le sujet avec la lumière de la *future* scène (direction, couleur, dureté). [TESTÉ EN LABO, synthèse 3D : de 0,3 à 3 m, débordement ÷ 2,6 et trous dans le sujet ÷ 6 — `labo/keying/RESULTATS.md`]
- **Fond saturé, pas brillant** : un vert écrêté se délave et le keyer mange le sujet (labo : tolérance 0,20 → 86-92 % d'un sujet gris effacé). `despill` supprime ensuite le vert résiduel du sujet [TESTÉ EN LABO].
- Pas de reflets (lunettes, montres, chrome), pas de fumée devant un fond vert, cheveux : prévoir un contre-jour.
- Matières qui posent problème : voilages, cheveux fins, verre, mouvement rapide (→ shutter plus fermé).

## 5. Tracking et plaques
- **Marqueurs de tracking** : croix ou points contrastés (scotch de couleur proche du fond pour un fond vert, mais d'une teinte différente), répartis en profondeur, toujours au moins 4 à 8 visibles ; pas sur le visage ou les zones qui seront visibles à l'image finale si on peut l'éviter.
- **Plaque propre** (clean plate) : le même plan, même cadre et même mouvement, **sans** le sujet ou l'objet à effacer. Si la caméra bouge, refaire le même mouvement (tête motorisée si possible) ; sinon une plaque fixe large dont on reconstituera le mouvement.
- **Références lumière** : une boule grise et une boule chromée (ou une HDRI 360°) à la place du futur objet 3D ; une charte couleur (Macbeth) en début de plan.
- **Son seul** (« wild ») des objets filmés : ce seront les SFX à cause visible.

- **Effacer une source de lumière, c'est effacer sa lumière portée** [THÉORIQUE] : préférer une source lointaine ou une source contrôlée qu'on éteint réellement. À l'allumage, un sodium haute pression met 2 à 10 min et change de teinte, et ne se rallume pas à chaud avant plusieurs minutes [SOURCÉ] : ne pas l'éteindre pour une prise sans prévoir ce délai. Les sources proches se voient partir, les lointaines non : proches = éteintes réellement, lointaines = effacées en post ; mesurer la part de chaque source depuis la caméra (les allumer une par une). [ÉPROUVÉ EN MAQUETTE] (pièce 18) Texte complet et sources : `details.md`.

## 5 bis. Écrans dans le champ (téléphone, ordinateur, TV) [SOURCÉ] (sources ci-dessous)
**Quand et pourquoi** : d'abord se demander ce que l'écran doit faire. S'il **éclaire un visage** (la nuit, une confidence : fiche Willis, pièce 17), c'est la lumière qui compte : garder un **vrai écran allumé** (contenu de remplacement neutre, luminosité réglée) plutôt qu'un vert, car la lueur sur la peau est l'effet. Si le **contenu doit être lu** (texto, interface), il sera remplacé en post : alors préparer le remplacement.
- **Exposer pour la pièce, régler l'écran** à part (luminosité baissée jusqu'à ce qu'il ne brûle pas) ; tester l'écran avant le plateau (PremiumBeat).
- **Remplacement** : écran gris moyen (~20 %) ou vert sombre peu lumineux, avec **4-5 petits marqueurs** dans les coins ; petits, car chaque marqueur est à effacer (praticien sur forum Logik : gris 20 % + 5 marqueurs). **Vert franc** seulement si le doigt ou la main couvre longtemps l'écran (ZeroVFX) : le vert lumineux déborde sur les doigts et le visage, il faut alors le baisser.
- **Garder la lumière** quand l'écran est remplacé : ajouter une petite source (LED, panneau) **de la couleur et de la taille de l'écran** hors champ ou derrière l'appareil, sinon le visage n'est plus éclairé par ce qu'il regarde.
- **Scintillement** : écrans à rafraîchissement ou gradation PWM (OLED en faible luminosité) peuvent battre avec la cadence et l'obturation ; tester à l'œil sur le moniteur de retour, monter la luminosité de l'écran et baisser l'ouverture, ou régler l'obturation (règle générale du scintillement des sources, à vérifier sur de vrais appareils).
- **Gros plans de doigts** : appareil calé (un support contre la main de l'acteur), mise au point qui tient à 2-3 cm près ; retirer les reflets au tournage (drapeau noir) plutôt qu'en post.
- Sources (PremiumBeat, ZeroVFX, forum Logik, consultées le 2026-10-10) : liens dans `details.md`.

## 5 ter. Une lumière qui s'éteint ou se rallume à l'écran [ÉPROUVÉ EN MAQUETTE] (pièce 18, rendu 3D ; au tournage : THÉORIQUE)
- **Deux plaques verrouillées, source allumée et éteinte**, même exposition : après linéarisation, leur différence est la contribution de la source, et n'importe quelle courbe d'extinction ou de rallumage se compose au montage. Rien ne doit bouger entre les plaques, la source ne doit pas brûler.
- Décider **qui éteint** (geste, contacteur) et le tourner ou l'enregistrer : une extinction sans cause se lit « coupure ».
- Gestes à lire (mains, signes) : dans le plan de l'image, écartés du torse, fond plus sombre que le corps ; en plan moyen, il faut un geste très ample. (pièce 19)

## 5 quater. Coupe cachée par un cache (« à la Zach King », pub, Short) [ÉPROUVÉ EN MAQUETTE] (pièce 30, maquette 2D)
Seulement si l'effet voulu est la **continuité** (sinon une coupe sèche dans le même cadre). Le cache couvre l'**union des deux silhouettes** (+ marge de flou de bougé) ; tout ce qui vit hors du cache est figé ou retiré (une lumière qui varie de 6 % trahit la coupe) ; caméra verrouillée ; contrôle au montage par mesure et à l'œil. Un élément vivant laissé dans le champ coûte une roto et une plaque propre. Procédure et chiffres : `details.md`.

## 6. Checklist plateau (à remplir pour chaque plan à effets)
- [ ] Focale, diaph, distance, hauteur, inclinaison, cadence, shutter notés.
- [ ] Charte couleur + boule grise/chromée ou HDRI filmées.
- [ ] Marqueurs en place et visibles ; photo du décor avec un mètre pour l'échelle.
- [ ] Plaque propre tournée (même mouvement).
- [ ] Prise de référence « effet pratique » si possible (lampe, flash, fumée), même imparfaite.
- [ ] Son seul enregistré.
- [ ] Marge de recadrage vérifiée sur le moniteur avec la grille 9:16 si un vertical est prévu.
- [ ] Autorisations pour les effets pratiques (fumigènes, flammes, drone) : capitainerie, mairie, pompiers.

## 7. À vérifier dans les logiciels ou sur un plateau
- Keying des cheveux fins : `chromakey` ffmpeg les perd (≈ 42 % d'erreur sur les bords, labo) ; comparer Keylight / Resolve 3D Keyer / Delta Keyer avec le même protocole à vérité terrain.
- Keying sur un vrai plan fond vert CC0 (ffmpeg `chromakey`, AE Keylight, Resolve 3D Keyer) : effet de la distance au fond et du shutter sur le bord.
- Camera tracking d'un plan à marqueurs (Blender, AE 3D Camera Tracker) ; erreur de reprojection obtenue.

## Filmer la nuit à l'infrarouge [ÉPROUVÉ EN MAQUETTE] (pièce 23 ; à valider sur une vraie caméra IR)
Jamais l'illuminateur intégré (signature « surveillance ») ; un projecteur IR 850 nm décalé, motivé, étroit et faible ; filtre coupe-IR retiré, balance fixe, trépied. Grade : `montage-couleur`. Recettes et sources : [`infrarouge.md`](infrarouge.md).

## Optique, buée, décor : préparer l'image elle-même (détail : `details.md`)
- **Flou optique plutôt que flou de post** : l'optique agrandit les hautes lumières en disques (monde flou lumineux), le gaussien les éteint (monde terne) ; en post, flou de lentille à carte de profondeur, jamais un gaussien. Une bascule de point se programme sur la plage perceptive (silhouette → lisible), pas sur la distance. Un flou se dimensionne à l'écran de diffusion (moitié moins de pixels sur mobile). [ÉPROUVÉ EN MAQUETTE] (pièce 28)
- **Reflet dans une vitre** : affaire de rapport de lumière (extérieur à ~−3 diaph du visage), pas de mise au point. [ÉPROUVÉ EN MAQUETTE] (pièce 28)
- **Ombres qui défilent** (forêt vue d'un train) = stroboscope plein cadre, échec photosensibilité possible : repérer un talus ou un pont, contrôler chaque prise. [ÉPROUVÉ EN MAQUETTE] (pièce 28, `flash_check.py`)
- **Buée** : décider plateau ou post ; en post, plaque sans buée + plaque embuée, fondu avec un cache par vitre ; noter l'état de buée à chaque prise. [THÉORIQUE]
- **Axe de lecture d'un corps** : un voûté se lit de profil, des bras ouverts de face ; prévoir au repérage la place de la caméra dans un lieu étroit. [ÉPROUVÉ EN MAQUETTE] (pièce 31)
