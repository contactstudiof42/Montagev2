# Labo expressions After Effects : résultats

Date : 2026-10-09. Commande : `cd labo/ae-expressions && /opt/node22/bin/node tests.js` (Node 22, aucun processus en arrière-plan).

## Ce que ce labo prouve, et ce qu'il ne prouve PAS

- **Prouvé** : chaque `.js` est du JavaScript valide (`node --check`), et sa **logique mathématique** donne des valeurs plausibles quand on l'évalue dans `mock.js`, un faux environnement AE simplifié.
- **PAS prouvé** : le comportement réel dans After Effects. `mock.js` imite `wiggle()` (bruit maison, pas l'algorithme Adobe), `ease()`/`easeIn()`/`easeOut()` (courbes cosinus/sinus, pas la courbe exacte d'AE), `loopOut()` (réécrit d'après la doc), `posterizeTime()`, `velocityAtTime()` (dérivée numérique), les clés (linéaires/ease seulement, pas de Bézier ni d'influence). Tout est **à valider dans AE en phase 2**.
- Les tests 02 et 03 (`loopOut`) ne testent que **notre propre mock** : ils servent de vérification de syntaxe, pas de preuve.
- Les maths vectorielles sont écrites avec `add()`/`mul()` (fonctions AE documentées) et non `value + [x, y]`, car Node ne fait pas l'addition de tableaux. Dans AE, les deux écritures marchent.

## Résultats (32 passent, 0 échouent)

| Résultat | Test | Détail |
|---|---|---|
| PASSE | node --check 01-wiggle-sliders.js | syntaxe OK |
| PASSE | node --check 02-loopout-cycle.js | syntaxe OK |
| PASSE | node --check 03-loopout-pingpong.js | syntaxe OK |
| PASSE | node --check 04-boucle-manuelle.js | syntaxe OK |
| PASSE | node --check 05-overshoot-inertiel.js | syntaxe OK |
| PASSE | node --check 06-echo-decalage.js | syntaxe OK |
| PASSE | node --check 07-mapping-linear-ease.js | syntaxe OK |
| PASSE | node --check 08-time-remap-vitesse.js | syntaxe OK |
| PASSE | node --check 09-compteur-texte.js | syntaxe OK |
| PASSE | node --check 10-posterize-wiggle.js | syntaxe OK |
| PASSE | node --check 11-respiration.js | syntaxe OK |
| PASSE | 01 wiggle borné | écart max 28.46 px pour amp 30 |
| PASSE | 01 wiggle déterministe | t=3.2 -> [964.7, 525.18] (deux fois) |
| PASSE | 02 loopOut cycle (mock) | t=2.25 -> 25 (attendu 25) |
| PASSE | 03 loopOut pingpong (mock) | t=1.25 -> 75 (attendu 75, retour) |
| PASSE | 04 boucle manuelle après clés | t=3.75 -> 50 (attendu 50) |
| PASSE | 04 boucle manuelle pendant clés | t=1.0 -> 100 (attendu 100) |
| PASSE | 05 overshoot dépasse la cible | pic 107.187 à t=0.56 s (cible 100 ; dépassement théorique max ≈ v/w·e^(-decay·t)) |
| PASSE | 05 overshoot se pose | t=3 s -> 100 |
| PASSE | 05 inactif pendant les clés | t=0.25 -> 50 (attendu 50) |
| PASSE | 05 overshoot sur tableau 2D | t=0.6 -> [106.99, 53.49] (1er essai à t=0.7 tombait pile sur un passage à zéro : sin(0.2·2π·2.5)=0) |
| PASSE | 06 écho (5 images de retard) | t=0.6 s -> [40, 0] (leader à t=0.4 -> 40) |
| PASSE | 07 ease() mappe et borne | p=0,20,40,60,100 -> 0, 0, 50, 100, 100 |
| PASSE | 08 remap 50 % | t=3 s, in=1 s -> 1 s de source (attendu 1) |
| PASSE | 08 remap borné à la fin | t=20 s -> 3.96 s (dernière image source) |
| PASSE | 09 compteur début | t=0 -> "0" |
| PASSE | 09 compteur fin + séparateur | t=3 -> "12⍽500" (⍽ = espace fine insécable) |
| PASSE | 09 compteur mi-course > moitié (easeOut) | t=2 -> "8⍽839" |
| PASSE | 10 posterizeTime tient la valeur | t=0.13 -> -0.23, t=0.24 -> -0.23, t=0.26 -> 4.226 (palier de 1/8 s) |
| PASSE | 11 respiration plein à la rétention | 0s:100.00 0.6s:102.00 1.2s:104.00 1.5s:104.00 1.6s:104.00 2.5s:101.17 3.4s:100.00 3.8s:100.00 4.6s:102.00 |
| PASSE | 11 respiration vide en pause et cyclique | pause = 100 %, t=4.6 = t=0.6 |
| PASSE | 11 expiration asymétrique | mi-expiration -> 101.17 % (< 102 = relâche rapide puis se pose) |


### Incident noté

Premier passage : 31/32. Le test « 05 overshoot sur tableau 2D » échouait à t = 0,7 s : 0,2 s après la clé, avec freq = 2,5, on a sin(0,2 × 2π × 2,5) = sin(π) = 0. L'expression était juste, c'est **le choix de l'instant de test** qui tombait sur un passage à zéro de l'oscillation. Test déplacé à t = 0,6 s : [106,99 ; 53,49], les deux axes dépassent proportionnellement à leur vitesse d'arrivée. Leçon pour AE : un overshoot n'est visible que si on regarde **entre** les passages à zéro ; image par image, à 25 i/s, avec une fréquence qui divise mal 25, l'oscillation peut paraître « sautée ».

## Lecture motion design des chiffres

- **Overshoot 05** : arrivée à 200 px/s, freq 2,5, decay 6 → pic à 107 (7 % de dépassement) 0,06 s après la clé, posé à < 0,01 px en 3 s. Pour un logo, c'est un dépassement franc ; pour de l'UI, descendre la vitesse d'arrivée ou monter decay.
- **Compteur 09** : avec `easeOut`, à mi-durée on est déjà à 8 839 / 12 500 (71 %). C'est voulu : le chiffre « arrive » et ralentit avant de se figer, l'œil a le temps de lire le dernier nombre.
- **Respiration 11** : 30 i inspiration / 10 i rétention / 45 i expiration / 15 i pause = 4 s (100 images). À mi-expiration, l'échelle est déjà redescendue à 101,17 % sur 104 : relâche rapide puis dépose lente, comme un vrai souffle.
- **Posterize 10** : la valeur tient bien 1/8 s (≈ 3 images à 25 i/s) puis saute.

## Fichiers

- `01-wiggle-sliders.js` … `11-respiration.js` : une expression par fichier, prête à coller.
- `mock.js` : faux globals AE (time, value, thisComp.frameDuration, key(), numKeys, nearestKey, valueAtTime, velocityAtTime, linear, ease, easeIn, easeOut, clamp, add/sub/mul/div, effect()(), loopOut, posterizeTime, wiggle).
- `tests.js` : `node --check` + évaluations ; régénère `resultats-tests.md`.
