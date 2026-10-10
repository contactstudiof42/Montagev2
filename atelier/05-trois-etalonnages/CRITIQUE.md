# Pièce 05 « Trois étalonnages » — critiques

Grille : intention servie ? lisibilité, composition, cohérence, couleur, originalité ou cliché, justesse.
Mesures : `vN-mesures.json` (luminance médiane / p1 / p99 en 0-255, % de pixels chauds — teinte < 50°, saturation > 0,25, valeur > 0,08 — dans l'image et hors de la chaise, biais R-B du ciel et du sable en 1/255).
Source : 3 images du plan v6-surface de la pièce 04 (f70, f160, f230), 640×360, AgX Base Contrast. Matériau gris, plat, peu saturé (sat. moyenne 0,08) : l'équivalent d'un rush Rec.709 tourné par temps couvert.

## v1 (`v1-planche.png`) — trois erreurs de débutant, mesurées
- **A « Constat »** : biais -19 sur le ciel et le sable. Je voulais du neutre, j'ai fait du **bleu clinique** : le gain bleu à 1,06 sur une image déjà froide (-9 à la source) a doublé la dominante. Constat ≠ froid. Critère 4 raté.
- **B « Souvenir »** : laiteux réel (p1 = 65 à 105), mais saturation 0,02 : c'est **gris**, pas doux. Et la chaise perd ses noirs : on lit du brouillard, pas un souvenir.
- **C « Menace »** : raté sur toute la ligne. 0,1 % de pixels chauds (la rouille a disparu) et un **teal saturé** (sat. 0,40) qui recouvre tout : le cliché exact que le skill interdit. Deux causes : (1) **ordre des nodes** : la secondaire qui pousse la rouille était *avant* les primaires qui écrasent, donc écrasée à son tour ; (2) des **gammas différents par canal** (0,75 / 0,80 / 0,78) sur une image grise fabriquent une dominante forte : une petite différence de gamma vaut une grosse balance des blancs.

## v2 (`v2-planche.png`) — primaires corrigées
- A : gain légèrement chaud (1,04 / 1,03 / 1,00) qui *annule* le froid de la source : biais du ciel -3,7. Neutre, net, la rouille lisible comme matière. **Critère 4 tenu.**
- B : lift réduit (p1 = 50-95), hautes lumières chaudes plus visibles (biais +5,7 au ciel), saturation 0,75 : plus doux que gris.
- C : gammas égaux, médiane 66 (bas et dense), froid léger par split-toning, secondaire placée en dernier… **et toujours 0 % de chaud**. La rouille écrasée par les primaires n'a plus de couleur à qualifier : on ne peut pas sauver une teinte qui n'existe plus.

## v3 (`v3-planche.png`) — la clé prise sur la source
- C : la secondaire prend sa **clé et sa correction sur l'image source** (l'équivalent d'un node parallèle branché sur l'entrée dans Resolve). Chaud : 0,05 % → 0,45 % → 1,71 % entre f70, f160 et f230, **0 % hors de la chaise**. Belle surprise : la chaleur *grandit avec la découverte* ; l'étalonnage raconte la marée sans qu'on l'ait écrit.
- Mais **liseré rouge** sur les montants de la chaise : la rouille de la source est presque noire (v ≈ 0,12-0,17, sat 0,23-0,36) ; l'intérieur des pieds tombe sous le seuil, seuls les bords (mélange rouille-gris, plus clairs) sont qualifiés. Le défaut classique d'un qualifieur sur un objet fin et sombre. La chaîne vire au **rouge** plutôt qu'à la rouille (sat_in 2,0 : trop).

## v4 (`v4-planche.png`, source `atelier/rendus/05m/`) — la matière plutôt que l'étalonnage
Hypothèse : « une seule chaleur » se décide au tournage (principe 8 du skill). Re-rendu avec une rouille plus claire et plus saturée (`rust_col` [0,30 ; 0,10 ; 0,035] au lieu de [0,11 ; 0,05 ; 0,03]), même plan, même lumière.
- **C « Menace »** avec une secondaire douce (sat_in 1,3) : la chaîne se lit **rouille**, pas rouge ; 2,0 % de chaud à f230, toujours 0 % hors chaise. Le liseré persiste sur les pieds de la chaise, mais beaucoup moins visible. **Meilleure version de C.**
- **C « matière seule »** (même primaires, aucune secondaire qui pousse) : 0,44 % de chaud seulement. La matière seule ne survit pas à un étalonnage dense : il faut **les deux** — la chaleur se tourne, l'étalonnage la protège.
- **Effet de bord instructif** : avec la rouille claire, A et B héritent aussi de la chaleur (1,6-1,7 % à f230). Ce que le décor porte, toutes les directions en héritent : décider la matière au tournage, c'est fermer des portes à l'étalonnage. Ici c'est acceptable (A : la rouille comme fait ; B : la rouille comme trace), mais un projet qui veut un « constat » strictement neutre devrait garder une rouille sourde.

## Jugement d'ensemble (v4)
- Trois sentiments distincts ? **A et C oui, B à moitié.** A (neutre, net) se lit « pièce à conviction » ; C (bas, froid, une chaleur qui monte) se lit « quelque chose remonte ». B se lit **brume** plus que **souvenir** : l'étalonnage seul donne un registre (douceur, distance), pas un temps passé. Pour que B dise « il y a longtemps », il faudrait le contexte (montage, voix, son : Koulechov) ou un marqueur de support (grain, halo, cadre). Leçon : **l'étalonnage choisit le registre, le montage donne le sens.**
- Lisibilité : la chaise reste lisible dans les quatre (p1 ≤ 26 sauf B à f70 où elle est encore sous l'eau).
- Originalité : C reste proche de mon propre système (froid + une chaleur) : c'est votre goût (Joker, Ziak), mais je dois veiller à ne pas en faire un tic. A est la direction la plus « juste » pour ce plan pris isolément.
- Limites : étalonnage sur une image 8 bits déjà tonemappée (AgX), pas sur du log ; images fixes (le qualifieur peut scintiller en mouvement : non testé) ; mes opérateurs imitent Resolve sans en reproduire les formules exactes (test MCP 31).

## v5 (`v5-planche.png`, `v5-B-detail.png`) — « souvenir » par un marqueur de support ?
Test de l'hypothèse de v4 : un marqueur de support (grain, halation, vignette) suffit-il à faire lire « il y a longtemps » sans contexte ?
- **Raté, et instructif.** Grain σ 0,03 avec une taille de 2 px : des **taches** et non du grain, qui se lisent comme du bruit de capteur en basse lumière (vidéo de surveillance), soit l'inverse d'un souvenir. La halation sur un ciel couvert, sans source ponctuelle, n'a rien à entourer : elle se contente de **teinter tout le ciel** (biais passé de +5,7 à +14,2). C'est un effet sans objet. Un effet de support a besoin de ce qu'il imite : la halation suppose des spéculaires, le grain suppose une émulsion fine.

## v6 (`v6-planche.png`, `v6-B-detail.png`) — le support, en retenue
- B : vignette 0,25 et grain fin (σ 0,012 pondéré tons moyens, soit environ 3/255 ; même ordre que le σ≈2 qui protège des bandes dans `labo/encodage`), sans halation. Le grain fait réapparaître la ligne d'horizon et donne une **surface** à l'image, et la vignette resserre le regard sur la chaise. On lit « photo argentique », un peu plus « autrefois » qu'en v4, mais toujours pas « souvenir de quelqu'un ». Confirmation : **le support date l'image, il ne lui donne pas un sujet.** Pour « souvenir », il faut un regard (un contrechamp, une voix, un son hors champ).
- Planche finale de comparaison : `v6-planche.png` (lignes B, B+support v5, B+support v6, A, C).

## À faire ensuite
- v5 : B avec un marqueur de support (grain fin + halation douce) pour voir si « souvenir » se lit sans contexte.
- Rendre 3 s en mouvement de la version C et mesurer le scintillement de la clé image par image.
- Refaire l'exercice depuis un rendu EXR linéaire (scene-referred) pour comparer la latitude.
