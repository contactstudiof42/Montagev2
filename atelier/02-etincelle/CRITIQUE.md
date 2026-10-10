# Pièce 02 « Étincelle » — critiques successives

Grille : intention servie ? lisibilité, rythme, composition, cohérence, couleur, mouvement, originalité/cliché, justesse.

## v1 (`v1-planche.png`, `v1-mesures.json`) — 257 images, 8,6 s, -14,3 LUFS / -2,2 dBTP mesurés sur le MP4
**Ce qui marche**
- **La règle couleur tient** : 160 images de froid cyan-vert, puis la seule chaleur arrive avec l'allumette ; dans le plan large final, la flaque orange au sol au milieu du froid est la meilleure image de la pièce. Le principe Ziak/Joker (une chaleur comptée) se voit sur la planche sans explication.
- La structure sonore est juste sur le papier : tic toutes les 15 images indépendant des coupes, riser coupé une image avant 9 images de silence, puis craquement + impact + feu.

**Ce qui est raté**
1. **Le hook est illisible** : l'image 1 est un cube presque noir, coupé par le cadre, sous une caption. Un spectateur de fil ne voit rien : l'impact sonore tombe sur du vide. C'est la faute la plus grave pour ce format.
2. **Les plans de sphères ne montrent pas de sphères** (3 plans sur 19) : un sol gris en contre-plongée. Les whoosh soulignent un mouvement qu'on ne voit pas : du SFX gratuit, exactement ce que le skill reproche à l'amateur.
3. **Quatre plans sont noirs** (pendule pris aux extrêmes de son balancement, cube encore hors champ). J'ai choisi les fenêtres de source au compteur, pas à l'image. Leçon : **en montage rapide, chaque plan de 4 à 8 images doit contenir son sujet dès sa première image** ; au-delà de 0,2 s on ne laisse pas le temps à l'objet d'entrer.
4. **L'allumette ressemble à une sucette** (tête sphérique et brillante, bâton clair) et la flamme macro est un cône blanc surexposé : l'objet-promesse n'est pas crédible, donc la délivrance non plus.
5. La caption « L'ÉTINCELLE » déborde du cadre (corps trop gros pour 9:16).
6. Le plan large était trop loin : l'allumette fait 2 % de la hauteur.

**Justesse** : le parti pris (froid, accélération, silence, une flamme) est bon ; l'exécution plan par plan ne le sert pas. Pas trop d'effets : le problème est la lisibilité, pas l'excès.

## v2 — corrections
- Hook : cube posé sur le sol dès l'image 1 (source 9, lumière lisible), caption plus petite et plus basse (zone sûre).
- Fenêtres de source recalées sur les passages du pendule au point bas (images 15, 30, 45, 60, 75) : le sujet est présent à chaque première image.
- Caméra des sphères reculée (35 mm) : on voit la sphère traverser.
- Allumette : tête oblongue et mate, bâton sombre ; flamme et émission divisées par 3.
- Plan large rapproché (l'allumette ≈ 25 % de la hauteur) et tenu 90 images (3 s).
- Grain monochrome σ ≈ 2/255 avant l'encodage (leçon du labo d'encodage : les dégradés sombres font des bandes après ré-encodage).

## v2 (`v2-planche.png`) — 267 images, 8,9 s, -14,2 LUFS / -2,0 dBTP
- Mieux : allumette crédible (tête oblongue mate), flamme moins brûlée, plan large rapproché où la flaque chaude occupe le bas du cadre, caption dans la zone sûre, grain posé.
- Encore raté : **les plans du pendule restent noirs** (5 sur 19) : j'avais recalé les fenêtres « autour » du passage au point bas, mais le pendule balaie ±1,3 m devant un 45 mm : dès 4 images du passage, il est hors champ. Le calcul était juste, l'hypothèse sur le cadre était fausse. Les sphères : toujours invisibles (minuscules sur l'horizon).

## v3 (`v3-planche.png`)
- Fenêtres du pendule commençant **une image avant** chaque passage (14, 29, 44, 59, 74) : les 5 plans montrent la boule et sa tige. Le hook devient le pendule (sujet lisible, reflet blanc) avec le tic à -8 dB sur l'image 1 et la caption « ATTENDS » : son et image racontent la même chose dès la 1re image (le temps qui passe).
- Reste : sphères minuscules (diagnostic sur une planche de toutes les images de la caméra : elles traversent à l'horizon, 6 px de haut).

## v4 (`v4-planche.png`, `v4-mesures.json`, `v4-couleur.json`) — version de référence
- Caméra des sphères au ras du sol en 50 mm, sphères ralenties (4,4 m en 24 images au lieu de 10 m en 20) : les trois plans de sphères montrent des billes chromées qui traversent, les whoosh ont enfin une cause.
- **Mesure de la règle couleur** sur le MP4 : pixels « chauds » ≤ 0,25 % de l'image avant l'allumage (traces brunâtres de la tête), **6,3 % en moyenne après** ; luminance moyenne 14 → 22/255. La chaleur est bien un événement compté (Ziak : 0,16 % sur tout le clip). La règle tient à la mesure, pas seulement à l'œil.
- Calage SFX vérifié dans `v4-mesures.json` : impacts aux images où le cube touche le sol (16, 88, 141), whoosh à crête sur les coupes vers les sphères (30, 97, 129), riser jusqu'à 152 puis 9 images de silence, allumage à 162.

**Critique de DA sur la v4 (grille)**
- *Intention* : servie dans la structure (froid → silence → une flamme). L'attente fonctionne mieux sur le papier qu'à l'image : les objets (pendule, cube, billes) n'ont pas de lien narratif avec l'allumette. C'est un défilé d'objets, pas une réaction en chaîne. **Le vrai défaut de conception est là** : une bille qui roule devrait *causer* le frottement de l'allumette (principe de Honda « Cog », fiche du jour). Ce serait la v5 : la dernière bille frappe l'allumette, qui s'enflamme ; la coupe sur l'impact devient une cause, plus seulement un rythme.
- *Lisibilité* : bonne dans 19 plans sur 19 à la 1re image (contre 12 sur 19 en v1).
- *Rythme* : l'accélération 15 → 4 images est mesurable ; on ne sait pas encore si 9 images de silence suffisent (0,3 s) : à juger à l'écoute en phase 2.
- *Couleur* : juste et mesurée. La flamme macro reste trop graphique (cône) : une simulation de flamme ou un vrai plan tourné ferait mieux.
- *Originalité / cliché* : « allumette qui s'allume dans le noir » est un cliché de bande-annonce. Il est rendu acceptable par la règle du temps et la retenue de la couleur, pas par l'idée elle-même. À dépasser en v5 (la causalité).
- *Justesse* : pas d'excès d'effets ; un seul flash, un seul shake, à l'allumage.
