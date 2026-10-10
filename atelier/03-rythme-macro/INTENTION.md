# Atelier 03 — « Rythme macro » (micro contre macro sur la même musique)

**Session 3, 2026-10-10.** BACKLOG 0c.

## Intention (écrite avant de créer)
Vérifier dans mes propres images ce que l'analyse du clip de Ziak a mesuré : sur une musique drill déjà très rythmée, **couper sur les temps** (micro) donne de l'énergie mais rend l'image servile ; **couper sur l'arrangement** (macro : densité de coupes qui suit les sections, pas les temps) laisse l'image garder sa gravité et produit une menace contenue.

Même musique (synthétisée, 140 BPM, 14 mesures ≈ 24 s : intro clairsemée 4 mesures, couplet avec 808 et caisse claire 8 mesures, coupure 1 mesure, reprise 1 mesure), même banque de plans (6 plans abstraits générés par ffmpeg, palette acier froide, un seul plan porte un accent chaud), deux montages :
- **A — micro** : une coupe tous les 2 temps (0,857 s), du début à la fin.
- **B — macro** : intro = un seul plan tenu ; couplet = une coupe par mesure puis par demi-mesure sur les 4 dernières (montée de densité) ; coupure = le seul plan chaud, tenu, ralenti ; reprise = retour au plan d'ouverture. Plus une « seconde horloge » : un léger battement de lumière toutes les 15 images (0,6 s), qui ne tombe pas sur le tempo (0,4286 s par temps).

## Critères de réussite
1. Sur la planche « timeline », on doit lire la structure de la musique dans B et pas dans A.
2. Au moins 80 % des coupes de B tombent sur un début de mesure ou de demi-mesure (calé sur l'arrangement, pas au hasard).
3. Le plan chaud n'apparaît qu'une fois, au moment de la coupure : il doit être l'événement du montage B.
4. Critique honnête : est-ce que B est « mieux » ou seulement « différent » ? Dans quel usage A gagne-t-il ?

## Médias
Tout est généré (sources lavfi de ffmpeg : mandelbrot, life, cellauto, gradients ; son synthétisé en numpy). Aucune licence tierce.
