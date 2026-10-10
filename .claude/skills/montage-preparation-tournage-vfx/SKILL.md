---
name: montage-preparation-tournage-vfx
description: Préparer un tournage qui aura des effets en post-production (supervision VFX légère) — repérer les plans à effets, choisir effet plateau / numérique / IA, réglages caméra utiles à la post (shutter, codec, log, 10 bits, marge de recadrage, open gate pour le vertical), fond vert ou bleu (éclairage, distance, débordement), marqueurs de tracking, plaques propres, HDRI et références de lumière, son seul, checklist plateau. Mots d'un réalisateur : « on verra en post », « tu peux l'effacer ? », « on tourne sur fond vert ? », « il faudra une version verticale », « on remplace le ciel », « on rajoute un écran », « ça va se tracker ? ».
---

# Préparer un tournage pour les effets (version légère)

Toutes les recettes sont **[THÉORIQUE]** (pratique de plateau courante, non testée ici) sauf mention. Le but n'est pas de tout prévoir, mais d'éviter les deux phrases qui coûtent le plus cher : « on verra en post » et « on n'a pas de plaque ».

## 1. Quand et pourquoi
- **Tout plan où quelque chose sera ajouté, retiré, remplacé ou recadré.** Un effet raté vient presque toujours d'une information manquante au tournage, pas d'un manque de talent en post.
- **Choisir la méthode par l'intention**, pas par la mode :
  - *Plateau* (pratique) quand l'acteur doit réagir à la chose, quand la lumière de l'effet doit toucher le décor (feu, écran, flash), ou quand c'est moins cher qu'on croit (une lampe orange vaut mieux qu'un feu compositeé : atelier 02, la lumière du feu sur le décor fait plus que la flamme) ;
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
- **Distance sujet-fond : 2 à 3 m au moins** pour réduire le débordement (spill) et pouvoir flouter le fond ; éclairer le sujet avec la lumière de la *future* scène (direction, couleur, dureté).
- Pas de reflets (lunettes, montres, chrome), pas de fumée devant un fond vert, cheveux : prévoir un contre-jour.
- Matières qui posent problème : voilages, cheveux fins, verre, mouvement rapide (→ shutter plus fermé).

## 5. Tracking et plaques
- **Marqueurs de tracking** : croix ou points contrastés (scotch de couleur proche du fond pour un fond vert, mais d'une teinte différente), répartis en profondeur, toujours au moins 4 à 8 visibles ; pas sur le visage ou les zones qui seront visibles à l'image finale si on peut l'éviter.
- **Plaque propre** (clean plate) : le même plan, même cadre et même mouvement, **sans** le sujet ou l'objet à effacer. Si la caméra bouge, refaire le même mouvement (tête motorisée si possible) ; sinon une plaque fixe large dont on reconstituera le mouvement.
- **Références lumière** : une boule grise et une boule chromée (ou une HDRI 360°) à la place du futur objet 3D ; une charte couleur (Macbeth) en début de plan.
- **Son seul** (« wild ») des objets filmés : ce seront les SFX à cause visible (atelier 02 ; examen n°2).

## 6. Checklist plateau (à remplir pour chaque plan à effets)
- [ ] Focale, diaph, distance, hauteur, inclinaison, cadence, shutter notés.
- [ ] Charte couleur + boule grise/chromée ou HDRI filmées.
- [ ] Marqueurs en place et visibles ; photo du décor avec un mètre pour l'échelle.
- [ ] Plaque propre tournée (même mouvement).
- [ ] Prise de référence « effet pratique » si possible (lampe, flash, fumée), même imparfaite.
- [ ] Son seul enregistré.
- [ ] Marge de recadrage vérifiée sur le moniteur avec la grille 9:16 si un vertical est prévu.
- [ ] Autorisations pour les effets pratiques (fumigènes, flammes, drone) : capitainerie, mairie, pompiers.

## 7. À vérifier en phase 2
- Keying sur un vrai plan fond vert CC0 (ffmpeg `chromakey`, AE Keylight, Resolve 3D Keyer) : effet de la distance au fond et du shutter sur le bord.
- Camera tracking d'un plan à marqueurs (Blender, AE 3D Camera Tracker) ; erreur de reprojection obtenue.
