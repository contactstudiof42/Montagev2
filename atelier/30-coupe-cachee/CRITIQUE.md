# Pièce 30 « Coupe cachée » — critique (session 24, 2026-10-10)

Rendus (ignorés) : `atelier/rendus/30/{A..E}.mp4` (`python3 piece.py X atelier/rendus/30`, 1 s chacun).
Mesures : `python3 mesure.py atelier/rendus/30 planche.png A B C D` (score scdet image par image, écart hors objet entre
l'image 44, avant le passage, et l'image 80, après ; témoin = deux images de la même prise).
Planches : `v1-planche.png` (A-D), `v2-planche-DE.png` (D, E). Coupe à l'image 62 (blanc).

| Version | scdet à la coupe | écart hors objet avant / après (témoin 1,2) | lecture |
|---|---|---|---|
| A torchon plein cadre, prises non raccordées | **0,0** | 9,5 (21 000 px) | coupe invisible… mais après le passage, le mur a pâli de 6 % et la trotteuse a sauté de 37 s |
| B coupe sèche, sans cache | 4,1 | 9,5 | comparaison avant / après, pas de magie (attendu) |
| C torchon étroit, non raccordées | 2,5 | 9,5 | la lumière saute **à la coupe** (hors du cache) ; et la plante dépasse au-dessus du torchon dès l'image 62 |
| D torchon étroit, raccordées | 0,3 (bruit) | 1,6 | raccord propre, mais la plante dépasse toujours du cache |
| **E** torchon couvrant l'union tasse + plante, raccordées | **0,1** | **1,5** | **référence** : rien ne trahit la coupe, la plante se découvre avec le torchon |

## Jugement
- L'intention (« c'est magique », lisible sans le son, chute en 1 image) n'est servie que par E. B est un autre film (la comparaison, principe LaBelle) : honnête, mais pas magique.
- **Un cache ne cache que ce qu'il couvre, et seulement à l'image de coupe.** A trompe le détecteur (score 0) mais pas l'œil : tout ce qui vit hors du cache (lumière, horloge, figurant, caméra) a continué entre les deux prises et saute visiblement **après** le passage. Le score scdet mesure la coupe, pas le raccord : il faut les deux mesures.
- **Le cache doit couvrir l'union des deux silhouettes**, pas l'objet de départ : la plante est plus haute que la tasse ; C et D se trahissent par le haut. Erreur de conception, pas de montage : elle se règle au plateau.
- Le passage plein cadre (A) est la solution de facilité quand on ne peut pas raccorder (pub tournée vite) : mais il ne marche que si la lumière est verrouillée.
- Limite : 2D, lumière simulée par un facteur global, pas de flou de bougé du torchon (un vrai torchon rapide flou aiderait la coupe). Pas de spectateur.

## Ce que j'en retiens (versé dans `montage-preparation-tournage-vfx` et `montage-grammaire`)
1. Coupe cachée = **trois conditions** : cache sur l'union des silhouettes à l'image de coupe ; tout ce qui vit hors du cache figé ou retiré (horloge, écran, figurant, nuages : lumière de studio ou plan court) ; caméra verrouillée (pied, pas de reprise entre les prises).
2. Vérifier en montage avec deux mesures : score de coupe ≈ bruit (scdet ≤ 1) **et** écart hors objet avant / après ≈ témoin de la même prise.
3. Le choix « cacher ou montrer » se décide sur l'effet voulu (continuité = magie, comparaison = humour) avant le tournage, pas au montage.

## v3 — ce que la post rattrape (G, H ; `v3-planche-GH.png`, même session)
| Version | écart hors objet avant / après (témoin 1,2) |
|---|---|
| A torchon plein cadre, rien rattrapé | 9,5 |
| G = A + gain d'étalonnage sur la prise 2 (÷ 1,06) | 5,4 |
| H = G + recadrage de 2 px (stabilisation) | 3,6 |
| E raccordé au tournage | 1,5 |
- La post rattrape **la lumière globale** (un gain) et **le déplacement de caméra** (un recadrage) : l'écart tombe de 62 %. Elle ne rattrape pas ce qui **vit** dans le décor : le résidu de H se concentre dans le quart haut-gauche (l'horloge : trotteuse décalée de 37 s ; le reste du résidu, plus étendu qu'une aiguille, n'est pas entièrement expliqué : probablement le cadran écrêté par le gain et la compression). Il faudrait une plaque propre et une roto de l'horloge, ou l'avoir retirée au tournage.
- Règle de devis : sur une coupe cachée, **une lumière qui bouge coûte un gain, une caméra qui bouge coûte une stabilisation, un élément vivant dans le champ coûte une roto** ; le retirer au tournage ne coûte rien.
