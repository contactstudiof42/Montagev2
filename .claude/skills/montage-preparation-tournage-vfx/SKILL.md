---
name: montage-preparation-tournage-vfx
description: Préparer un tournage qui aura des effets en post-production (supervision VFX légère) — repérer les plans à effets, choisir effet plateau / numérique / IA, réglages caméra utiles à la post (shutter, codec, log, 10 bits, marge de recadrage, open gate pour le vertical), fond vert ou bleu (éclairage, distance, débordement), marqueurs de tracking, plaques propres, HDRI et références de lumière, son seul, checklist plateau. Mots d'un réalisateur : « on verra en post », « tu peux l'effacer ? », « on tourne sur fond vert ? », « il faudra une version verticale », « on remplace le ciel », « on rajoute un écran », « ça va se tracker ? ».
---

# Préparer un tournage pour les effets (version légère)

Toutes les recettes sont **[THÉORIQUE]** (pratique de plateau courante, non testée ici) sauf mention. Le but n'est pas de tout prévoir, mais d'éviter les deux phrases qui coûtent le plus cher : « on verra en post » et « on n'a pas de plaque ».

## 1. Quand et pourquoi
- **Tout plan où quelque chose sera ajouté, retiré, remplacé ou recadré.** Un effet raté vient presque toujours d'une information manquante au tournage, pas d'un manque de talent en post.
- **Choisir la méthode par l'intention**, pas par la mode :
  - *Plateau* (pratique) quand l'acteur doit réagir à la chose, quand la lumière de l'effet doit toucher le décor (feu, écran, flash), ou quand c'est moins cher qu'on croit (une lampe orange vaut mieux qu'un feu compositée : atelier 02, la lumière du feu sur le décor fait plus que la flamme) ;
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
- **Son seul** (« wild ») des objets filmés : ce seront les SFX à cause visible (atelier 02 ; examen n°2).

- **Effacer une source de lumière, c'est effacer sa lumière portée** *(examen n°7, session 12)* [THÉORIQUE] : un lampadaire retiré laisse son halo sur le sol, les murs, les visages ; sur un plan où quelqu'un passe dessous, c'est une relumière complète. Préférer une source **lointaine** (au fond du cadre, halo petit) ou une **source contrôlée** qu'on éteint réellement (faux lampadaire : un tube sur un mât, une lampe de chantier) ; décider la courbe d'après la technologie *(corrigé session 12, sources ci-dessous)* : à **l'extinction**, LED comme lampe à décharge s'éteignent presque instantanément (pour la décharge : déduit, l'arc cesse avec le courant) ; la différence est à **l'allumage** : un sodium haute pression met **2 à 10 min** à atteindre son flux en changeant de couleur à mesure que le sodium se vaporise, et une lampe chaude coupée ne peut pas se rallumer avant **plusieurs minutes** (le gaz doit refroidir) — au tournage, ne pas éteindre un sodium pour une prise sans prévoir ce délai ; en post, un rallumage « sodium » crédible est lent et change de teinte (PSU EGEE 102 : https://courses.ems.psu.edu/egee102/node/2366 ; Maréchal, HPS et coupure de courant : https://marechal.com/en/p-hps-lamps-and-power-failure.html ; DIALux, réamorçage : https://dialux4.support-en.dial.de/support/solutions/articles/9000078324-restriking). Plan fixe sur pied + plaque propre longue. **Atelier 18** [TESTÉ EN ATELIER, Blender] : les sources qui se voient partir sont justement les proches (lumière portée) ; les lointaines, faciles en post, partent sans qu'on le voie (−4 % de luminance). Partager : proches = sources contrôlées éteintes réellement, lointaines = effacement en post. **Mesurer la part de chaque source depuis la caméra** (les allumer une par une devant le moniteur, ou `atelier/18-soustraction/part.py` en 3D) : en cadrage serré, le lampadaire « proche » ne pesait que 2 %, son voisin 41 %.

## 5 bis. Écrans dans le champ (téléphone, ordinateur, TV) — session 11 [THÉORIQUE, sources ci-dessous]
**Quand et pourquoi** : d'abord se demander ce que l'écran doit faire. S'il **éclaire un visage** (la nuit, une confidence : atelier 17, fiche Willis), c'est la lumière qui compte : garder un **vrai écran allumé** (contenu de remplacement neutre, luminosité réglée) plutôt qu'un vert, car la lueur sur la peau est l'effet. Si le **contenu doit être lu** (texto, interface), il sera remplacé en post : alors préparer le remplacement.
- **Exposer pour la pièce, régler l'écran** à part (luminosité baissée jusqu'à ce qu'il ne brûle pas) ; tester l'écran avant le plateau (PremiumBeat).
- **Remplacement** : écran gris moyen (~20 %) ou vert sombre peu lumineux, avec **4-5 petits marqueurs** dans les coins ; petits, car chaque marqueur est à effacer (praticien sur forum Logik : gris 20 % + 5 marqueurs). **Vert franc** seulement si le doigt ou la main couvre longtemps l'écran (ZeroVFX) : le vert lumineux déborde sur les doigts et le visage, il faut alors le baisser.
- **Garder la lumière** quand l'écran est remplacé : ajouter une petite source (LED, panneau) **de la couleur et de la taille de l'écran** hors champ ou derrière l'appareil, sinon le visage n'est plus éclairé par ce qu'il regarde.
- **Scintillement** : écrans à rafraîchissement ou gradation PWM (OLED en faible luminosité) peuvent battre avec la cadence et l'obturation ; tester à l'œil sur le moniteur de retour, monter la luminosité de l'écran et baisser l'ouverture, ou régler l'obturation (règle générale du scintillement des sources, à vérifier en phase 2 sur de vrais appareils).
- **Gros plans de doigts** : appareil calé (un support contre la main de l'acteur), mise au point qui tient à 2-3 cm près ; retirer les reflets au tournage (drapeau noir) plutôt qu'en post.
- Sources (consultées le 2026-10-10, par résumés de recherche) : https://www.premiumbeat.com/blog/5-tips-for-shooting-digital-screens ; https://www.zerovfx.com/tips/how-to-shoot-monitor-composites ; https://forum.logik.tv/t/screen-replacement-advice-for-producers/1773

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
- Keying des cheveux fins : `chromakey` ffmpeg les perd (≈ 42 % d'erreur sur les bords, labo) ; comparer Keylight / Resolve 3D Keyer / Delta Keyer avec le même protocole à vérité terrain.
- Keying sur un vrai plan fond vert CC0 (ffmpeg `chromakey`, AE Keylight, Resolve 3D Keyer) : effet de la distance au fond et du shutter sur le bord.
- Camera tracking d'un plan à marqueurs (Blender, AE 3D Camera Tracker) ; erreur de reprojection obtenue.
