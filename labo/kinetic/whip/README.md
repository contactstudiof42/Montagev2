# Labo whip pan : le flou de bougé aux bords d'un plan (session 11, 2026-10-10) — [TESTÉ EN LABO, Blender 4.2.3 Cycles]

Question : un raccord « whip pan » (fin de A qui file, début de B qui file) peut-il se faire en 3D avec des plans rendus séparément ?
`scene.py` : colonnes colorées autour d'une caméra qui pivote ; `sortie` accélère jusqu'à 30°/image, `entree` part de 30°/image et décélère ; flou de bougé obturateur 0,5 ; 192×108, 16 échantillons (≈ 2 s par plan de 12 images). `mesure.py` : indice de flou horizontal (gradient vertical / gradient horizontal ; > 1 = flou horizontal) et décalage par corrélation de phase.

## Résultat
| Clés d'animation | Flou A 9 → 12 | B 1 → 3 | À la coupe |
|---|---|---|---|
| Seulement dans le plan (1 → 12) | 1,01 1,04 1,03 **0,85** | **0,87** 1,05 1,04 | **deux images nettes** encadrent la coupe : le mouvement « s'arrête » une image de chaque côté, le raccord saute (`coupe-flou-planche.png`, ligne du haut) |
| Prolongées d'une image avant et après (0 → 13) | 1,02 1,03 1,04 **1,07** | **1,06** 1,04 1,02 | flou continu, la coupe disparaît dans le filé (ligne du bas) |
Cause : le flou de bougé intègre le mouvement **autour** de l'instant de l'image ; si l'animation s'arrête sur la dernière clé, la dernière image n'a que la moitié du mouvement (et la première de même).

**Échec de mesure** : la corrélation de phase ne donne pas de décalages fiables sur ces images (flou fort, motifs répétitifs, bruit) : elle ne distingue même pas le sens (B dans le même sens ou en sens inverse). La continuité de **direction** n'est donc **pas mesurée** ici ; il faudrait un flot optique (RAFT, ou `minterpolate` en mode vecteurs) — BACKLOG.

## Règles
1. **Un plan qui doit couper en mouvement s'anime au-delà de ses bords** (au moins une image avant et après, mieux : quelques images de « poignée ») ; sinon la première et la dernière image sont nettes et le whip pan accroche. Même logique en tournage réel : on filme la sortie et l'entrée bien au-delà du point de coupe.
2. Dans After Effects (THÉORIQUE, phase 2) : même risque si les clés s'arrêtent au point de sortie du calque ; prolonger les clés au-delà du point de sortie ou découper après coup.
