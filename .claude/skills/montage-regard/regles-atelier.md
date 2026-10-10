Annexe de `SKILL.md` : preuves par pièce des règles de jugement (versions, mesures, sessions) et précisions de la grille ; les principes eux-mêmes ne sont pas répétés ici (le SKILL.md fait foi).

# montage-regard — preuves et précisions

Toutes [ÉPROUVÉ EN MAQUETTE] (maquette Blender / Pillow / ffmpeg, à confirmer sur vraies images en phase 2) sauf mention. Journal daté des premières leçons : `journal.md`.

## Sources des principes
- Principe 2 (ordre des priorités de Murch) : `culture/walter-murch-blink-of-an-eye.md`.
- Principe 4 (Bass) : source et tensions dans `montage-references` § C ; application au motion dans `montage-motion-design-principes` § Principes.
- Principe 5 : atelier 01 v1, pulse symétrique ±10 % (détail dans `journal.md`).

## Précisions de la grille et de la méthode
- Pièges supplémentaires : Lisibilité → aussi le **kerning** ; Rythme → la **symétrie mécanique** ; Composition → l'espace négatif a-t-il un sens ? ; Couleur → les couleurs par défaut **du logiciel** ; Mouvement → l'amplitude excessive ; Originalité → clichés type carton centré, zoom lent, particules.
- Le critère **Liaison** a été ajouté en session 2, après l'atelier 02 v4 (une suite d'objets bien rythmée mais sans lien n'est pas une montée).
- La commande de planche du SKILL.md est [TESTÉ EN LABO] depuis la session 1 (intervalle type : 1 image sur 20).
- Planche « 1re image de chaque plan » : 02 v1 (7 plans sur 19 illisibles à leur 1re image), 04 v2 (caméra sous l'eau pendant 97 images, invisible sur l'image du milieu), 07.
- Relire comme un inconnu : 16 v3, un signe rendu lisible devient un autre signe (la Terre au bout d'un fil = un ballon).
- Un détecteur ne juge pas le raccord (pièce 30, session 24) : une coupe cachée peut tromper le détecteur (score nul) et se voir quand même, parce que ce qui vit hors du cache a changé.

## Preuves par règle (numéros des « Règles de jugement » du SKILL.md)
1. **Mesurer** : 01 v6 (bruit de rendu imaginaire, en fait l'encodage H.264 du dégradé), 05 (« neutre » vérifié au biais R-B : mon premier constat était bleu à −19), contrôle de flashs de la session 7 (outil « plein écran » trop indulgent contre la fenêtre locale du WCAG). Détail : `journal.md`.
2. **Isoler la variable** : 10 v4, un seul rendu en vue Standard (feuille *plus* chaude) a réfuté « AgX blanchit le froid ». Vraie cause : une source à 3 cm de la surface (sature ou disparaît) et une couleur d'écran réaliste trop pâle à côté d'une lampe orangée saturée. Seul fait mesuré sur AgX : il plafonne le blanc vers 222/255 (règle 3). Détail couleur : `montage-couleur-et-intention/details.md`.
3. **Étage du défaut** (22 v3-v4 et 23, session 19) : blanc gris = transformée de vue (pixel max 222 partout, ciel compris), pas la lumière ; une chaise noyée parmi d'autres se sépare par l'**espace** (écart de 4 m), pas par la profondeur de champ (invisible à 1,25 m) ; l'image « surveillance » vient de l'illuminateur dans l'axe et du grade vert, pas du noir et blanc. Et **chaque écart d'espace a un sens** : isoler la chaise l'a rendue lisible mais a dit « à part » au lieu de « au bout d'une lignée » ; relire la correction contre le texte.
4. **Échelle de la mesure** (28, session 23) : la variance du laplacien déclarait « aussi flou » un cheval effacé par l'optique et un cheval lisible sous un gaussien de 2 px ; mesurer par corrélation sur l'image réduite et calibrer les seuils à l'œil sur une bande.
5. **Saillance** (12 v4) : j'étais satisfait, la mesure a placé l'attention à 34 % de la diagonale de l'anomalie (confirmé par un modèle publié, `labo/saillance/`) ; une fenêtre dans le champ vole l'attention à tout le reste. Détail éteint par l'éclairage : tasse blanche sur table au soleil.
6. **Énergie lumineuse** (18, session 12) : retirer trois points lumineux au fond ne se voit pas (−4 % de luminance) ; retirer la lumière portée autour du sujet se voit à chaque fois (−29 % à −58 %). Outro qui rallume : saillance du personnage 5,8 → 1,5 si l'on rallume la source proche, 3,7 si l'on rallume une lointaine.
7. **Taille de lecture** (29 v1-v6, session 24) : une goutte de 5 px, un bâton inachevé de 7 px ne disent rien. Signe **singulier** (pièce 34, session 25) : trouvé même à 180 px de large ; la taille ne compte que pour un signe de forme ou de texture. Sources chaudes (16 v4) : une chaleur de 2 px n'existe pas ; mon tic « une seule chaleur méritée » revient même quand la pièce veut l'éviter, d'où le compte sur chaque planche. Corollaire de la règle « détail dimensionné à l'écran » (session 5).
8. **Plan d'arrivée** (27, session 23) : vérifier qui, quoi, pourquoi en moins d'une demi-seconde ; un réglage fin ne sauve pas un plan illisible.
9. **Liaison** : 02 v4 ; liens possibles : cause, regard, mouvement, son, idée (Honda « Cog »).
10. **Rythme du sujet** : 04 v1 (la marée découvre lentement le haut, puis tout le sol d'un coup).
11. **Déplacer le mouvement** : 01 v2 (réduire l'amplitude du même paramètre = mouvement invisible).
12. **Effet et registre** : 05 (halation sans source ponctuelle = ciel teinté ; « souvenir » exige un regard, contrechamp, voix ou son).
13. **Conséquence dans le cadre** : 07 (impact final au bord ou hors champ dans deux montages sur trois ; domino à 3 % de la largeur).
14. **Retour** : 08 (la reprise du plan large du début, identique au pixel, pèse plus que le plan vide ; chercher la trace avant le flash-back).
15. **Correction locale** : 07 v2 (la tasse arrêtée au sol ne basculait plus).
16. **Casser une règle** : 11, 180° franchi pour tous les plans à la fois, placé sur la bascule du rapport de force.
17. **Depuis la caméra** : 12 v2 (deux objets alignés dans l'axe = un seul) ; 16 v4 (ligne qui traverse = fissure, qui touche au bord = lien) : juger les raccords de lignes dans le plan de l'image.
18. **Lecture parasite d'échelle** (16 v4) : ballon, jouet, maquette ; changer l'échelle par rapport au cadre plutôt que la forme ; coupé par le bord, l'objet n'est ni tenu ni manipulable.
19. **Source dans le champ** (17 v1 → v3) : décentrée et basse, elle laisse le visage dans l'ombre. Précision : la cause d'un apaisement doit **précéder** l'apaisement, au son comme à l'image (17, son).
20. **Courbe de la lumière** (18 v4-v6, sessions 14-15) : une extinction sèche **n'a pas d'auteur** tant que le montage ne lui en donne pas un (geste, contacteur entendu juste avant). Cause **après** = au mieux « on comprend après », et ambiguë (« il a éteint » ou « il va rallumer ») sans changement d'état visible. Clé de l'insert : **avant**, à la luminance du plan qu'il précède (insert 2,4× plus clair = la coupe fait la chute à la place de l'extinction) ; **après**, éclairé par ce qui reste (la lanterne), jamais à la clé du jour (il rallume le film) ni à celle du noir (illisible).
21. **Texte et image** (19, session 13) : un vers illustré se lit deux fois et rien ne se relie ; v2, la porte avant la rue = un trajet qui recule, l'œil le sent avant le sens ; le regard caméra le plus fort tombe là où le texte parle d'être regardé ; 19 v4, bras de profil dans le torse = rien : placer l'artiste pour que ses mains décollent du corps, en contre-jour.
22. **Valeur opposée** (20, session 15) : un nom blanc dans un flash blanc est invisible (v2) ; noir dans le coup puis inversé en blanc dans le noir, il se lit sur toute sa durée et l'inversion imite la rémanence de l'œil (v4). Sur 2,4 s de saccade automatique, aucun coup de lumière retenu (v1) : tout se monte image par image.
23. **Leviers** (31 v4b, sessions 24-25) : focale longue = enfermé ou écrasé, courte et proche = l'espace s'ouvre ; un seul levier inversé dit autre chose (le soir, la menace).
24. **Axe de posture** (31 v4, session 25) : dans l'axe, le geste se raccourcit à rien. Si un personnage change de posture entre deux plans, l'axe change avec (diptyque : aller de profil, retour de face). Au repérage : le décor permet-il cet axe (mur volant, escalier ouvert) ?
25. **Pudeur** (34, session 25) : aussi la vitre sale ; la caméra désire, l'écran protège, la tension est dans l'écart des deux ; mieux qu'une coupe ou un hors-champ.
26. **Règle sonore rompue** (30, session 24) : un tic posé sur les retours, puis retiré.
27. **Temps** : constat de la session 23.
28. **Direction écartée** : examens n°1 et n°13, pièce 34 (la piste refusée sur le papier a donné la meilleure image du projet, la voiture-lanterne) ; méthode (10 à 20 min de maquette) dans `montage-direction-artistique`.
