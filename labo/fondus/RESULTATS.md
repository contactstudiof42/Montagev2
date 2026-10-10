# Labo — détecter les fondus (session 3, 2026-10-10)

**Question** : `scdet` (mon outil de mesure des coupes, `labo/analyse-clip`) voit-il les fondus enchaînés et les fondus au noir ? Sinon, peut-on les détecter simplement ?

## Protocole
`test_fondus.py <dossier>` : 7 plans générés (mandelbrot, testsrc2, cellauto, gradients, **mire qui défile vite** = piège à faux positifs, life, barres), 3 s chacun, composés **image par image en numpy** pour que la vérité terrain soit exacte : coupes à 3,00 et 10,52 s ; fondus enchaînés de 12 images (5,52-6,00), 25 images (7,52-8,52), 6 images (15,32-15,56) ; fondu au noir et retour en 24 images (12,56-13,52). Résultats bruts : `resultats.json`.

## Résultats
| Méthode | Coupes (2) | Fondus (4) | Faux positifs |
|---|---|---|---|
| `scdet` seuil 4, 8, 12 | 2/2 | **0/4** | 1 (10,56 : 2e image du plan qui défile) |
| `scdet` seuil 20 | 1/2 (rate 3,00) | 0/4 | 0 |
| Différence moyenne image à image + règles (pic isolé = coupe, plateau ≥ 4 images = fondu) | 1/2 | 1/4 approximatif | 3 (le plan rapide et le plan cellauto passent pour des fondus) |
| Linéarité (`linearite.py` : chaque image intérieure = (1-α)·A + α·B, α progressif) | — | 1/4 (le fondu de 6 images vers un plan fixe) | 1 à 9 selon le seuil |

## Conclusions
1. **`scdet` ne voit aucun fondu**, même de 6 images, quel que soit le seuil. Toutes mes mesures de rythme faites au scdet (Ziak, ateliers) **sous-comptent les transitions douces** : à garder en tête quand je mesure un film qui fond (documentaire, pub luxe). [TESTÉ EN LABO]
2. **La différence image à image ne distingue pas un fondu d'un mouvement** : un plan qui bouge vite a la même signature qu'un fondu enchaîné. [TESTÉ EN LABO]
3. **La linéarité stricte échoue dès que les plans bougent** pendant le fondu (le mélange n'est plus celui des images extrêmes) : elle ne marche que sur des plans quasi fixes. Échec utile : il faut une méthode tolérante au mouvement.
4. Piège ffmpeg rencontré (noté pour `montage-loudness-livraison` / labo) : `xfade` refuse deux entrées de bases de temps différentes (sortie de `concat` 1/1000000 contre 1/12800 du fichier) ; `fps=25,settb=AVTB` sur chaque entrée règle l'erreur, mais les décalages `offset` après `concat` ne tombaient pas où je les calculais (17,32 s au lieu de 15,56 s) : pour une vérité terrain, composer en numpy.

## Prochaine étape
Méthode de la courbe de variance (pendant un fondu, la variance de luminance de l'image décrit une parabole entre celles des deux plans) combinée à une différence calculée sur des images **décalées de L/2** de part et d'autre (tolérance au mouvement). Re-tester sur la même vérité terrain, puis sur un extrait CC0 réel.
