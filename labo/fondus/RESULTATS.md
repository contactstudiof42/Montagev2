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

## Session 4 (2026-10-10) : méthode « écart au milieu » — `variance.py`
**Mesure** : R(t,h) = |F_t − (F_{t−h}+F_{t+h})/2| / |F_{t−h} − F_{t+h}| sur la luma 80×45, h ∈ {3, 6, 12}. Au milieu d'un fondu, l'image est la moyenne de ses voisines lointaines (R petit) ; dans un plan qui défile, la moyenne de deux images décalées est un flou qui ne ressemble pas à l'image du milieu (R grand). Le fondu au noir est détecté à part (luma moyenne < 3), car son milieu n'est pas un mélange (R ≈ 0,7).

| Réglage | Fondus (4) | Faux positifs |
|---|---|---|
| R < 0,3 et creux de variance (var_t < 0,85·min) | 0/4 | 0 |
| R < 0,3, écart des extrémités > 8 | 3/4 | 1 (plan mandelbrot, 0,24-2,72 s : zoom lent quasi linéaire) |
| **R < 0,3, écart > 20, + détecteur noir** | **3/4** | **0** |

**Ce que j'apprends** [TESTÉ EN LABO] :
1. **L'hypothèse du creux de variance est fausse en général** : la variance du mélange vaut 0,25·vA + 0,25·vB + 0,5·cov ; si l'un des deux plans est pauvre (dégradé, ciel), le milieu du fondu est *plus* texturé que lui. Le creux n'existe qu'entre deux plans de même richesse et non corrélés.
2. **L'écart au milieu tolère le mouvement rapide** (mire qui défile : R = 0,64 à 2,3, jamais détectée), là où la différence image à image et scdet échouaient.
3. **Il confond un fondu avec un mouvement lent et régulier** (zoom mandelbrot : le milieu est vraiment la moyenne de ses voisines) : d'où le seuil sur l'écart des extrémités. Un vrai travelling lent ou un changement de lumière progressif sera un faux positif possible.
4. **Raté** : le fondu de 25 images entre deux plans pauvres et proches en luma (cellauto → dégradé : écart des extrémités 9-12 seulement en luma 80×45). Piste : travailler en couleur (chroma) et à plus haute résolution.
5. **Limite de rigueur** : les seuils sont réglés sur la même vérité terrain que celle qui les évalue (surapprentissage probable). Prochain test obligatoire : une autre chaîne (autres sources, autres durées), puis un extrait CC0 réel monté en fondus.

Conséquence pour mes mesures de rythme : scdet pour les coupes + `variance.py` pour les fondus (3/4 ici), et toujours un contrôle visuel de la planche aux endroits détectés.
