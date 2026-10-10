# Labo whip-flot : continuité de direction à une coupe en filé (BACKLOG 66, 2026-10-10)

Suite de `labo/kinetic/whip/` : la corrélation de phase n'y donnait pas le sens du mouvement de part et d'autre de la coupe. Ici, on le mesure avec un flot optique.

## Cas de vérité terrain (`gen.py`)
Pas de Blender ici, donc les images sont **synthétiques** (numpy + OpenCV). Une fenêtre de 320×180 balaie une grande texture (bruit multi-échelle coloré et 500 rectangles nets). A et B utilisent deux textures différentes, comme deux lieux distincts. Le plan A accélère de 0 à vmax px/image (profil quadratique sur 12 images) ; le plan B part de vmax et décélère. Le flou de bougé moyenne 16 sous-images sur un obturateur de 180°, avec un bruit gaussien σ = 2. Le mouvement continue au-delà des bords des plans (règle 1 du labo whip), sauf dans `bord_net` où il est figé hors des clés.
15 cas :
- même sens à 30, 60 et 100 px/image, plus un cas vers la gauche ;
- inverse à 30, 60 et 100 ;
- horizontal contre vertical (×2) ;
- écarts d'angle de 30° et de 60° ;
- contrôle fixe ;
- bord net ;
- deux pièges à texture périodique (barres de 24 px), en même sens et en sens inverse.

Commande : `python3 gen.py labo/rendus/whip-flot` (≈ 27 s). Les images restent hors git.

## Mesure (`mesure_flot.py`)
On mesure le flot sur les 3 paires d'images avant la coupe (A 9→12) et les 3 après (B 1→4). Le vecteur dominant est la médiane des vecteurs. La confiance est la **cohérence** |Σv| / Σ|v|, de 0 (vecteurs dans tous les sens) à 1 (tous parallèles). On calcule aussi la part de pixels à moins de 30° du vecteur dominant (dans le JSON).
Quatre méthodes :
- **fb** : Farneback en pleine résolution, pyramide de 6 niveaux ;
- **fb4** : Farneback sur des images réduites au quart ;
- **dis** : flot DIS d'OpenCV, preset MEDIUM ;
- **mv** : vecteurs de mouvement du codec. A et B sont encodés bout à bout en H.264 (`-bf 0`, `me=esa:merange=128`), et le décodage se fait avec `flags2=+export_mvs` lu par PyAV (`side_data MOTION_VECTORS`). Côté B, on prend les images 2 à 4, car l'image 1 après la coupe est surtout codée en intra.

On calcule le cosinus entre les directions et un score « pondéré » vA·vB / max(|vA|,|vB|)². Ce score vaut 1 si direction et vitesse sont identiques ; il baisse quand la vitesse saute.

**Règle de décision** (appliquée dans cet ordre) :
1. max(|v|) < 1 px/image → **statique** ;
2. cohérence < seuil → **incertain** ;
3. un seul côté immobile → **arrêt** ;
4. cos ≥ 0,7 (écart ≤ 45°) → **raccord** ;
5. cos ≤ −0,5 → **inverse** ;
6. sinon → **cassure** d'axe.

**Règle retenue** : on prend DIS si sa cohérence est ≥ 0,85 des deux côtés. Sinon on prend les vecteurs du codec avec le même seuil. Sinon le résultat est « incertain ».

RAFT n'a **pas été testé** : torch n'est pas installé, et l'installer sur CPU (≈ 200 Mo plus les poids) dépassait le temps prévu.

## Chiffres [TESTÉ EN LABO, synthétique]
Chaque cellule donne vA → vB (px/image), puis la cohérence minimale, le cosinus et la décision. ✗ = décision fausse. Vitesse vraie : ≈ 23, 46 et 76 px/image pour vmax = 30, 60 et 100.

| cas | vérité | fb | fb4 | dis | mv (H.264) |
|---|---|---|---|---|---|
| meme_sens_30 | raccord | (2,0)→(2,0) · 0.79 · raccord | (23,0)→(20,0) · 0.89 · raccord | (23,0)→(23,0) · 1.00 · raccord | (23,0)→(23,0) · 0.97 · raccord |
| meme_sens_60 | raccord | (0,0)→(0,0) · statique ✗ | (25,2)→(27,0) · 0.72 · raccord | (46,0)→(46,0) · 1.00 · raccord | (46,0)→(46,0) · 0.95 · raccord |
| meme_sens_100 | raccord | statique ✗ | (−3,8)→(−3,−3) · 0.32 · incertain ✗ | (−3,9)→(76,0) · 0.51 · cassure ✗ | (76,0)→(76,0) · 0.97 · raccord |
| meme_sens_gauche | raccord | statique ✗ | (−18,1)→(−6,0) · raccord | (−46,0)→(−21,4) · 0.89 · raccord | (−46,0)→(−46,0) · raccord |
| diag_30deg | raccord | statique ✗ | cos 0.95 · raccord | (46,0)→(40,23) · cos 0.87 · raccord | cos 0.87 · raccord |
| inverse_30 | inverse | (2,0)→(−1,0) · inverse | inverse | (23,0)→(−23,0) · 1.00 · inverse | inverse |
| inverse_60 | inverse | statique ✗ | inverse | (46,0)→(−46,0) · 1.00 · inverse | inverse |
| inverse_100 | inverse | statique ✗ | 0.34 · incertain ✗ | (−40,−5)→(7,−5) · 0.80 · inverse (par chance) | (−77,0)→(76,0) · 0.97 · inverse |
| vert_horiz_60 | cassure | statique ✗ | cos −0.01 · cassure | (46,0)→(0,46) · cos 0.00 · cassure | cassure |
| horiz_vert_60 | cassure | statique ✗ | cassure | (0,−46)→(−46,0) · cassure | cassure |
| diag_60deg | cassure | statique ✗ | cos 0.46 · cassure | cos 0.50 · cassure | cos 0.50 · cassure |
| controle_fixe | statique | statique | statique | statique | statique |
| bord_net_60 | raccord | statique ✗ | raccord | (45,0)→(45,0) · 1.00 · raccord | (60,0)→(44,0) · raccord |
| rayures_60 | raccord | statique ✗ | (2,3)→(2,−6) · inverse ✗ | (10,12)→(2,0) · 0.70 · raccord (faux vecteurs) | (0,0)→(10,−21) · 0.00 · incertain ✗ |
| rayures_inv_60 | inverse | statique ✗ | inverse (petits vecteurs) | 0.61 · cassure ✗ | (0,−38)→(12,−30) · 0.53 · raccord ✗ |
| **total juste** | | **3/15** | **12/15** | **13/15** | **13/15** |
| **temps / coupe** (6 paires, 320×180, CPU) | | 0.19 s | 0.01 s | 0.05 s | 1.5 s (encodage compris) |

**Règle retenue (DIS puis MV, cohérence ≥ 0,85) : 13/15 justes, 2 « incertain » (les deux pièges à rayures), 0 erreur.** On reproduit le tableau complet avec `python3 mesure_flot.py <dossier> --mvs`. Pour une seule coupe : `python3 mesure_flot.py --paire dossierA dossierB --mvs`.

## Ce qui marche, ce qui échoue, et pourquoi
- **Farneback en pleine résolution échoue** sur le filé : il voit 0 à 2 px au lieu de 23 à 76 px/image. Son modèle polynomial local ne suit que de petits déplacements. Sur une image floue, les niveaux grossiers de la pyramide n'ont plus de texture, et ajouter des niveaux aggrave le résultat (6 niveaux donnent 0,3 px, 3 niveaux donnent 9,5 px à 23 px réels). Il ne réussit que les cas lents ou fixes.
- **Farneback au quart de la résolution** retrouve le **sens** jusqu'à environ 50 px/image, mais il sous-estime la vitesse d'un facteur 2 à 4.
- **DIS est exact** (±1 px, cohérence ≈ 1,0) tant que le déplacement reste sous environ 15 % de la largeur de l'image par image. À 76 px/image (24 % de la largeur), il décroche : la cohérence tombe à 0,5–0,8, et il faut alors s'abstenir.
- **Les vecteurs du codec** (recherche exhaustive, rayon 128) sont exacts à **toutes** les vitesses testées, y compris 76 px/image, et contournent la limite de DIS. Ils sont 30 fois plus lents, à cause de l'encodage. Ils restent imprécis sur la première image après la coupe, codée en intra.
- **Une texture périodique piège toutes les méthodes** : avec des barres de 24 px et un déplacement de 46 px, le déplacement est ambigu à une période près. La cohérence le révèle (≤ 0,7), d'où le seuil à 0,85 : avec lui, l'outil s'abstient au lieu de se tromper. C'est le cas de vrais plans de stores, de grilles ou de façades répétitives.
- **Ce que le flot ne voit pas : la coupe à bord net.** Dans `bord_net`, l'image 12 de A n'a que la moitié de son flou, mais le déplacement entre images reste continu, donc le flot dit « raccord ». L'accroche décrite dans le labo whip est un défaut de **flou**, pas de direction. Il faut combiner cet outil avec l'indice de flou de `../whip/mesure.py`. Les vecteurs du codec montrent tout de même un saut (60 → 44 px), visible dans le score pondéré.
- La cohérence du contrôle fixe est basse (0,04–0,3) : c'est normal, car il n'y a que du bruit. C'est pour cela que le test « statique » sur la magnitude passe avant le test de confiance.
- Pas de passage sur une pièce kinetic existante : aucune vidéo ni aucun rendu n'est présent dans le dépôt (`atelier/02-etincelle/` ne contient que des scripts et des EDL), et Blender est absent de cette machine. L'outil est prêt à l'usage : `--paire dossierA dossierB`, avec des images `f_*.png`.

## Leçon artistique pour le monteur kinetic [TESTÉ EN LABO pour la mesure ; la perception reste à valider à l'œil]
1. **Un filé raccorde quand la direction se prolonge** : même sens, ou un écart de 30° au plus (cos ≥ 0,87). L'œil suit le filé à travers la coupe, et la coupe disparaît dans le mouvement. Un écart de 45° est la limite de la règle (cos 0,7).
2. **Le sens inverse (cos ≈ −1) ne fait pas un raccord, il fait un choc** : le mouvement « rebondit ». C'est utilisable seulement comme effet voulu (impact, retournement, ping-pong rythmique sur le temps fort). Sinon, c'est la coupe la plus visible du lot.
3. **Une coupe perpendiculaire (horizontal → vertical, cos ≈ 0) casse l'axe** : on lit un changement d'espace, pas une continuité. C'est acceptable pour changer de chapitre, mais pas à l'intérieur d'une phrase de mouvement.
4. **La direction ne suffit pas** : il faut aussi la continuité du **flou** et de la **vitesse**. Une dernière ou une première image nette fait accrocher la coupe même dans le bon sens (labo whip). Il faut viser une vitesse comparable de part et d'autre (score pondéré proche de 1).
5. **Se méfier des motifs répétitifs** (rayures, grilles) dans un filé : la machine comme l'œil peuvent y lire le mauvais sens (effet de roue de charrette). On choisit des surfaces à texture irrégulière pour les sorties et les entrées en filé.
6. **Un filé très rapide**, au-delà d'environ un quart de cadre par image, n'a plus de direction lisible pour DIS. C'est probablement aussi vrai pour l'œil, qui ne voit alors qu'un « flash » de couleur. La direction compte surtout dans les 2 ou 3 images de ralentissement de B.

## Fichiers
- `gen.py` : génère les cas de vérité terrain.
- `mesure_flot.py` : mesures Farneback, Farneback au quart, DIS et vecteurs du codec, avec le score et la règle de décision.
- Images et `resultats.json` : dans le dossier de sortie, hors git.

## Validation sur de vrais rendus Blender (session 13, après le sous-agent) [TESTÉ EN LABO, Blender 4.2.3 Cycles]
`../whip/scene.py` (colonnes autour d'une caméra qui pivote, flou de bougé 0,5, 192×108, objectif 24 mm ≈ 74° de champ). A = lieu 0 en sortie, Bm = lieu 1 en entrée même sens, Bi = sens inverse. Rendus dans `labo/rendus/whipreel/` (non versionnés), 2 s par plan.

| VMAX (°/image ≈ % de largeur) | cas | DIS : vA → vB · cohérence · décision | Vecteurs codec | fb4 (quart) |
|---|---|---|---|---|
| 8° ≈ 11 % | Bm (raccord) | 17 → 15 · 0,99/1,00 · **raccord** | raccord | **inverse ✗** |
| 8° ≈ 11 % | Bi (inverse) | 17 → −15 · 0,99/1,00 · **inverse** | inverse | **raccord ✗** |
| 30° ≈ 40 % | Bm | −10 → −24 · 0,57/0,88 · raccord (cohérence A trop basse) | 42 → 47 · 0,37 · incertain | raccord |
| 30° ≈ 40 % | Bi | −10 → −11 · 0,57/0,83 · **raccord ✗** (cohérence basse) | 42 → −48 · 0,37 · incertain (signe juste) | inverse |

- **À 11 % de largeur par image, DIS et codec sont justes et sûrs (cohérence ≈ 1)** ; **Farneback au quart se trompe de sens avec assurance dans les deux cas** : à ne jamais utiliser seul.
- **À 40 % (le vrai filé du labo whip), aucune méthode n'est fiable** : DIS se trompe (mais sa cohérence 0,57 < 0,85 le fait écarter) ; le codec trouve le bon signe mais avec une cohérence de 0,37. **La règle combinée s'abstient : 0 erreur.** Les vecteurs bruts du codec gardent pourtant le bon signe dans les deux cas : piste pour une règle sur le signe seul quand |v| > 30 % de la largeur.
- Lecture artistique (hypothèse à vérifier à l'œil en phase 2) : au-delà d'environ un quart de cadre par image, le filé n'a plus de direction lisible **image par image** ; la direction se lit alors dans **l'accélération de A et le ralentissement de B** (les images lentes autour du filé). C'est là qu'il faut soigner le sens, pas au cœur du flou.
