---
name: montage-regard
description: Juger un plan, une coupe, un montage, une animation ou un étalonnage déjà faits — « est-ce que ça marche ? », « pourquoi ça ne fonctionne pas ? », « qu'est-ce qui cloche dans cette version ? », « on garde la V2 ou la V3 ? », « quelle prise est la meilleure ? », « c'est livrable ? », « on en fait trop ? », « qu'est-ce qu'on peut enlever ? », retour de DA, relecture avant livraison, autocritique d'une planche contact, vérifier qu'on regarde au bon endroit du cadre. Pour proposer une direction avant de faire : `montage-direction-artistique`.
---

# Le regard : principes de jugement et grille d'autocritique

Marqueurs : [VU SUR IMAGES] vérifié sur de vraies vidéos (phase 2, fiches dans `analyses/`) · [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer sur vraies images en phase 2 · [THÉORIQUE] déduit, non vérifié.

**Fait foi sur** : la grille d'autocritique, la méthode de visionnage (planches, mesures) et les règles de jugement. Pour la méthode des directions (dont « maquetter la direction qu'on écarte » et le test « mon propre système ») : `montage-direction-artistique`. Sources des principes d'auteurs : `montage-references`. Preuves détaillées par pièce : `regles-atelier.md` ; journal daté : `journal.md`.

## Principes que je défends
1. **L'intention d'abord, l'effet ensuite.** Reformuler en une phrase ce que le plan doit faire ressentir ou comprendre ; un choix est bon s'il sert cette phrase. [THÉORIQUE]
2. **L'émotion gagne les arbitrages** (Murch) : émotion > histoire > rythme > trace du regard > plan 2D > espace 3D. Un faux raccord qui sert l'émotion vaut mieux qu'un raccord parfait qui l'éteint. [SOURCÉ]
3. **Le rythme suit l'état intérieur, pas l'action** (Schoonmaker) : dilater l'instant décisif, compresser le reste. [SOURCÉ]
4. **Réduire** : un concept, un signe (Bass). Pas d'idée en une phrase = pas d'idée. [SOURCÉ]
5. **Le mouvement doit avoir une cause** : sans raison narrative ou physique, c'est une « animation », pas un geste (un pulse symétrique se lit comme un logo, pas comme une respiration). [ÉPROUVÉ EN MAQUETTE] (pièce 01)
6. **Le corps du spectateur est l'instrument** : la bonne coupe tombe là où il aurait cligné ou respiré ; si je ne ressens rien, aucune théorie ne sauve la pièce. [SOURCÉ] (Murch)
7. **Faire moins quand c'est plus juste** : l'excès courant est la redondance (l'effet qui dit la même chose que l'image, la musique qui surligne). [THÉORIQUE]

## Ce que j'évite
- L'effet de mode sans fonction (glitch, light leak, zoom de transition) : il date la pièce.
- Le centrage et la symétrie par défaut (à garder comme choix : frontalité, solennité).
- L'amplitude excessive : au-delà de quelques % d'échelle, un « respir » devient un zoom.
- Le fondu au noir d'un élément sur fond coloré : il passe par une ombre sale ; fondre vers la transparence ou depuis la couleur du fond. [ÉPROUVÉ EN MAQUETTE] (pièce 01)

## Grille d'autocritique (chaque planche contact)
Noter chaque critère de 0 à 3 avec **une phrase de preuve visuelle** (ce que je vois sur telle image), jamais une impression.

| Critère | Question | Piège |
|---|---|---|
| Intention | La phrase d'intention se perçoit-elle sans explication ? | « Joli » mais neutre |
| Lisibilité | L'information clé est-elle lue au premier regard, dans le temps imparti ? | Contraste, durée (≥ 2× le temps de lecture), signe trop petit |
| Liaison | Qu'est-ce qui relie chaque plan au suivant, autre que le tempo ? | Cause, regard, mouvement, son ou idée absents |
| Rythme | Les durées varient-elles avec une logique ? Le sommet est-il marqué par autre chose que la vitesse ? | Durées uniformes ; accélérer au climax par réflexe (13 films sur 13 ne coupent pas plus vite à leur sommet ; ils le marquent par le volume, le format, la durée de la crête ou un plan tenu) [VU SUR IMAGES] |
| Composition | Le cadre guide-t-il l'œil ? | Centrage par défaut ; la zone la plus claire vole le regard. Exception : en plans de 1 à 2 s, le centre est juste (l'œil n'a pas le temps de chercher : *Mad Max*) ; le décentrage va avec les plans tenus (*Joker*) [VU SUR IMAGES] |
| Cohérence | Typo, couleur, mouvement parlent-ils la même langue ? Aucun levier ne tire seul (l'« ensemble » de *Joker*, goût de l'utilisateur) ? | Un élément « d'un autre film » ; un levier poussé au détriment des autres |
| Couleur | La palette porte-t-elle l'émotion ? | Couleurs par défaut |
| Mouvement | Cause, courbe juste, fin ? | Easing par défaut |
| Originalité | Qu'est-ce qui la distingue de mille autres ? | Cliché du genre |
| Justesse | Que peut-on enlever ? | Redondance image / son / effet |

Verdict : **livrable** seulement si intention, lisibilité et justesse sont à 3 ; les autres peuvent être à 2 ; **et si le fichier passe `labo/outils/qc_livraison.sh`** (pistes, true peak ≤ -1 dBTP, noir de début et de fin) : six fichiers livrés du studio sur sept dépassaient -1 dBTP, un saturait (phase 2, projets F42). [VU SUR IMAGES, mesuré]

## Juger sa propre version (phase 3, projet Sony, notes de Diego du 2026-10-11) [TESTÉ EN CONDITIONS RÉELLES]
Ma V2 Sony passait tous mes contrôles chiffrés (loudness, crêtes, photosensibilité, plans sombres) et Diego l'a jugée « très moyenne » : look plat, transitions « PowerPoint », titre « d'enfant de 6 ans », packshots qui tremblent, trop sage pour le brief. Je savais juger tout ça chez les autres, pas chez moi. Règles :
1. **Se comparer, pas se calquer.** Avant le montage (look) et avant chaque livraison : 6 images de ma version (ouverture, produit, sommet, texte, transition, fin) **en pleine résolution, côte à côte** avec 6 images des références (`analyses/reseaux/`, films, pubs). Une question : « un monteur pro livrerait-il ça ? ». Les références donnent le niveau, le brief donne le style. Jamais de jugement de couleur sur une vignette ou une planche en palette. Les statistiques de luma ne voient pas un look plat (ma V2 avait des noirs et un contraste chiffrés proches de Claude nu, et paraissait pourtant laiteuse à côté de lui).
2. **Le brief prime sur le goût moyen des références.** Quand il demande « très rapide, beaucoup d'effets », j'ose autant qu'un monteur kinetic, puis je rends propre. La retenue apprise sur les références de Diego n'est pas une règle : un Claude sans formation a obéi au brief et a été jugé plus impressionnant.
3. **Voir le mouvement** : une image fixe ne montre pas un plan qui tremble. Mesure sur chaque plan retenu et chaque rendu avec `labo/outils/tremblement.py` (points suivis + RANSAC, reste après lissage de 0,4 s, en px ramenés à 1080 de large). Seuils calibrés le 2026-10-11 : plan fixe < 1,5 px de moyenne et < 3 px de pic ; packshots tremblants de la V2 Sony 4,3-4,7 px, pics 11-13 px. **Au-delà de 2 px de moyenne ou 5 px de pic : stabiliser (Gyroflow), remplacer ou justifier.** Pour un plan douteux : bande de 10 à 25 images consécutives recadrée sur un détail, ou superposition de 5 images (contours dédoublés).
   - **Stabiliser = rendre le mouvement fluide, pas figer le plan** (Diego, 2026-10-11). On garde le mouvement voulu du cadreur (travelling, glissement, approche), on retire seulement secousses et saccades : lissage modéré, pas d'annulation du mouvement, le moins de recadrage possible. On ne compare pas le déplacement total des pixels : on mesure le **tremblement résiduel** (mouvement moins sa version lissée) et on vérifie que **la trajectoire voulue est conservée** (`tremblement.py STAB --avant ORIGINAL` : `vitesse_conservee` 0,8-1,3 et `correlation_trajectoire` élevée ; proche de 0 = mouvement tué). Puis on **juge à l'œil** sur une bande d'images consécutives (`--bande`) : régulier et naturel, pas figé.
   - **D'abord lire l'intention du cadreur, plan par plan** (Diego, 2026-10-11) : (a) **fixe voulu, sans trépied** (les lettres K-O-R-E, un packshot posé sur un écouteur) → on épingle le sujet (Gyroflow puis compensation de toute la dérive) ; (b) **mouvement voulu, comme sur un rail** (travelling avant / arrière, approche, glissement) → on garde le trajet, la direction et l'allure (accélérations lissées), on retire les à-coups de la main en position, en échelle et en rotation ; jamais fixe. Gyroflow ne corrige que la rotation : le va-et-vient de la main (translation, échelle) se compense ensuite sur la trajectoire mesurée, lissée sur une fenêtre longue.
7. **Jamais deux fois le même moment d'un rush** dans un événementiel, un after movie ou un run and gun (sauf ressort de récit écrit) : `labo/outils/doublons_timeline.py` avant chaque rendu (`montage-grammaire`).
4. **La courbe de mes propres effets** : vitesse d'un zoom ou d'une transition image par image ; une vitesse constante, sans accélération ni freinage, signe l'amateur.
5. **Lire l'intention du cadreur au dérush** : chercher les **séries pensées pour être montées ensemble** (plans consécutifs au même cadre ou à la même valeur ; éléments d'un même objet filmés un par un, comme les lettres d'un logo ; mouvements qui se répondent d'un plan à l'autre ; même geste sous plusieurs angles). Pour chacune, écrire dans `derush.md` l'intention probable et le montage qu'elle appelle. Raté sur Sony : la série K, O, R, E puis le mot KORE, faite pour épeler la marque en raccords ; « un monteur humain aurait direct compris ».
6. **L'ordre des plans a une raison, bloc par bloc** : ni l'heure de tournage (trop chronologique, défaut de Claude nu), ni un mélange sans logique (défaut de ma V2). Une progression qu'on comprend (où on est, ce qui se passe), et pour chaque bloc une phrase « pourquoi ces plans, dans cet ordre » dans `plan.md`. Aucun plan posé au hasard.
7. **Quand un geste est bloqué, chercher le résultat, pas l'outil** : « pas de Magic Mask par script » ne voulait pas dire « pas de détourage » (Claude nu a seuillé la carte de profondeur de Resolve). Lister les autres chemins avant de déclarer une impossibilité.

## Le goût de chaque plan (notes de Diego sur la V4 Sony, 2026-10-11) [universel] [TESTÉ EN CONDITIONS RÉELLES]
V4 à 80 % livrable : la technique tient, ce qui reste est le goût. Toutes ces règles valent pour tout montage ; les cas Sony sont dans `CARNET-DE-GOUT.md` (images).
1. **Aucun plan de remplissage**, même dans une rafale de 3 images (« qu'est-ce que ça fout là ? » : un tapis avec un bout de pied flou). **Avant chaque rendu, contrôler le passage exact utilisé** (pas la vignette du dérush) : première, milieu et dernière image en pleine résolution ; netteté du sujet, exposition, visages.
2. **Un flou : volontaire ou raté ?** Volontaire : pose lente, bascule de point qui va quelque part, flou de mouvement qui sert l'énergie, flou qui se résout dans le plan. Raté : mise au point qui cherche ; sujet (surtout le produit) hors du plan de netteté sans intention ; bougé de main qui n'est pas un geste. Écrire la famille de chaque plan flou retenu.
3. **Les visages, image par image** sur toute la durée utilisée : yeux mi-clos, bouche tordue, grimace. On garde le moment flatteur, sauf si le film veut l'effort.
4. **Étalonner plan par plan**, pas par lot : chaque plan en pleine résolution (exposition, ombres, hautes lumières), puis à côté de ses voisins. Une LUT par lumière ne raccorde pas des plans exposés différemment.
5. **Noirs denses, pas de bruit** : agrandir et amplifier les zones d'ombre ; des ombres relevées révèlent le bruit du capteur, et le grain ajouté s'y additionne.
6. **Dans un mouvement continu (zoom, transition), l'exposition se règle sur tout le mouvement**, pas sur son début : première, milieu et dernière image.
7. **Un blanc de produit garde sa matière** : le comparer à la photo produit de la marque, pas seulement compter les pixels à 250.
8. **Chaque plan et chaque effet ont une raison** (servir ce qui vient après, le sens ou le rythme) ; une phrase « il est là parce que… » dans `plan.md`, sinon il sort.
9. **Tout élément graphique (fond, texture, couleur, papier, cadre) vient de la direction artistique** (`montage-direction-artistique`, `da.md` écrit avant le premier effet). Un élément joli sans lien avec le film est une faute de goût.
10. **Un détourage se juge au bord, à 200 %** : masque seul, sujet sur fond noir, blanc et couleur vive, bords difficiles agrandis (cheveux, épaules, mains) ; sinon autre outil, autre plan, ou pas de détourage.
11. **Des variantes sur les moments clés** (ouverture, collages, transitions majeures, sommet, titre, fin) : 2 ou 3 idées réellement différentes, comparées en pleine résolution ; je juge mieux entre options que je ne réussis du premier coup.
12. **Relire `CARNET-DE-GOUT.md`** (entrées [universel] et du genre) avant chaque livraison, et vérifier la version contre chacune.

13. **Rien n'est figé ; le silence du client n'est pas une validation** (Diego, 2026-10-11). À chaque version, après avoir appliqué les retours, relire le film entier comme si on le découvrait : rythme d'ensemble, calage musical, enchaînements, équilibre entre les blocs. Un ajout qui allonge, un plan retiré qui casse une transition : déplacer, raccourcir, remplacer ou supprimer ailleurs, même dans un bloc « réussi ». Seul ce qui est validé explicitement est fixé, et même ça peut bouger si le film l'exige (l'écrire dans la note de livraison).

## Méthode de visionnage
1. Planche à intervalle régulier avec numéro d'image : lire l'**arc**. [TESTÉ EN LABO]
   `ffmpeg -i v.mp4 -vf "select='not(mod(n\,20))',scale=320:-1,drawtext=text='%{n}':x=4:y=4:fontsize=12:fontcolor=yellow,tile=5x2" -frames:v 1 planche.png`
2. Montage rapide : planche « 1re image de chaque plan » ; plan animé : 1re, dernière et image de l'événement, pas le milieu.
3. Planche avant / après chaque coupe : un détecteur de coupe ne juge pas le raccord.
4. Mesures quand c'est possible : luminance (`signalstats`), durées de plans (`scdet`, PySceneDetect), loudness (`ebur128`). Saillance : les outils de maquette (`atelier/12-inquietude-calme/mesure.py`, `labo/saillance/`) servent sur une image construite ; sur de vraies vidéos, la saillance automatique ne trouve le sujet qu'une fois sur trois (phase 2) : compter à l'œil (`labo/outils/echantillon_tiers.py`).
5. Relire chaque planche **comme un inconnu** (« qu'est-ce que c'est ? » avant « est-ce que ça se voit ? »), puis contre l'intention écrite.
6. Limite assumée : je juge sur planches, mesures, formes d'onde et spectrogrammes ; **je n'écoute jamais le son** et ne vois pas la fluidité en temps réel. Après 45 vidéos réelles, cette limite tient toujours : ce que j'écris du son est une lecture de courbe.

## Juger une vraie vidéo : règles de vérification (phase 2, passe de révision) [VU SUR IMAGES]
Sur 45 conclusions d'analyse revérifiées avec de meilleurs instruments, 28 confirmées, 14 corrigées, 3 nouvelles (`analyses/REVISION.md`). Ce que j'avais **regardé** a tenu ; ce que j'avais **recopié d'un outil** s'est trompé une fois sur trois, toujours dans le même sens pour un même outil.
1. **Regarder avant de nommer une cause.** Une rafale de « plans » de 0,5 s que j'avais annoncée comme les stroboscopes d'une rave était un magasin de tapis (*Aftersun*) ; une « rafale de panique » était un seul plan porté flou (« Fou-Rire ») ; une « rafale de réaction », un téléviseur dans le champ (*Forrest Gump*).
2. **Une vignette par plan ne juge ni un plan long ni une rafale** : elle montre une image par plan *détecté*. Plan long : différence image par image + tuile à 1 image / 2 s (*Joker*, Pogo's : un vrai plan-séquence de 74 s que j'avais cru faux). Rafale : 6 images consécutives autour de chaque coupe (`labo/outils/bandes_coupes.py`) et, si les plans semblent à 2-3 images, toutes les images (Yvnnis « Gare du Nord » : la « rafale de huit devantures » en contenait environ 65 de 2 images).
3. **Un détecteur se trompe dans les deux sens, de façon prévisible** : il fusionne le sombre, l'action accélérée, le texte sur noir et tout plan de moins de 0,6 s ; il invente des coupes sur les éclairs, les écrans dans le champ, les plans portés flous et l'animation par saccades. Un nombre de plans est un minimum ; une série de plans à la durée minimale est un soupçon.
4. **Un pourcentage de parole ne se cite qu'après un spectrogramme** (25 à 30 coupes) : mesurée par l'énergie, la part des « coupes pendant la parole » était trop haute sept fois sur sept (de 6 à 36 points). La durée des silences (« l'air ») est plus robuste.
5. **Un calage sur la musique ne se cite que contre le hasard, sur la musique séparée de la voix** (`calage.py`, demucs) : sur le mixage, la voix fabrique de faux calages (HOUDI : 45 % contre 27 % au hasard, puis rien sur la musique seule).
6. **Retirer logos, générique monté et cartons avant toute statistique** (*Aftersun* : médiane 4,3 s brute, 5,5 s sur le film seul ; *Avengers* : ASL 4,0 s générique compris, 3,7 s sans).
7. **Une fiche écrite sans voir est juste dans l'esprit, fausse dans les chiffres** : cinq affirmations de phase 1 corrigées sur les deux films préférés de l'utilisateur, quatre sur neuf sur deux clips. Une référence citée de mémoire se vérifie sur l'image avant d'entrer dans un argument.
8. **N'attribuer un goût à l'utilisateur que s'il l'a dit** (`GOUTS.md`, `RETOURS-DIEGO.md`, une note de sa main) ; un exemple de format n'est pas un goût (retour du 2026-10-11).

## Règles de jugement (preuves : `regles-atelier.md`)
Toutes [ÉPROUVÉ EN MAQUETTE] sauf mention ; numéro de pièce entre parenthèses.
1. **Mesurer avant de corriger**, et vérifier l'outil de mesure quand il me donne raison trop facilement (01, 05).
2. **Une explication n'entre dans un skill qu'après un essai qui isole la variable** (10 : l'hypothèse « AgX blanchit » réfutée par un rendu en Standard). [TESTÉ EN LABO]
3. **Corriger à l'étage où le défaut naît** : un blanc gris venait de la transformée de vue, pas de la lumière (22-23).
4. **Une mesure ne voit que l'échelle qu'elle mesure** : pour la lisibilité d'une forme, mesurer à l'échelle de l'objet et calibrer à l'œil (28). [TESTÉ EN LABO]
5. **Mon œil se trompe sur la saillance** : le plus clair et le plus contrasté gagne le regard ; mesurer avant de croire qu'on guide l'œil. Éclairer une zone attire l'œil mais peut éteindre le détail : garder le détail contrasté dedans (12).
6. **L'œil lit l'énergie lumineuse autour du sujet**, pas le nombre de sources : pour qu'un monde s'éteigne, éteindre autour du sujet d'abord ; rallumer loin et petit pour ne pas lui reprendre la saillance (18).
7. **Un signe qui n'a pas la taille de lecture n'existe pas** à l'écran de diffusion, sauf s'il est singulier (seule teinte chaude, seule valeur claire) ; sinon l'amener (macro, poussée, insert) (29, 34). Compter les sources chaudes **à la taille de lecture** (16).
8. **Le plan d'arrivée d'abord** : il doit se lire en moins d'une demi-seconde avant tout réglage fin de la coupe (27).
9. **Ce qui relie un plan au suivant doit être autre chose que le tempo** (02 ; Honda « Cog »).
10. **Chercher le rythme que le sujet impose** avant d'en plaquer un (04).
11. **Déplacer le mouvement vers le paramètre qui porte le sens** plutôt que réduire l'amplitude du mauvais (01).
12. **Un effet a besoin de ce qu'il imite** ; une image fixe donne un registre, le sens vient du montage (05).
13. **Le cadre contient la conséquence** ; la lisibilité dépend de la part du cadre, pas de la résolution (07).
14. **Le sens en retard a besoin d'un retour** (reprise d'une image déjà vue) (08).
15. **Une correction locale peut casser ailleurs** : relire toute la planche (07).
16. **Casser une règle complètement, une fois, au bon endroit** ; à moitié, c'est une erreur (11, 180°).
17. **Vérifier un raccord depuis la caméra** : deux objets alignés dans l'axe se lisent comme un seul ; une ligne qui traverse une surface se lit fissure, qui la touche au bord se lit lien (12, 16).
18. **Pour tuer une lecture parasite d'échelle, changer l'échelle par rapport au cadre** (objet coupé par le bord = plus grand que l'image) (16).
19. **Une source dans le champ** centrée et symétrique fait une icône ; trop forte, elle tue le noir ; décentrée et basse, elle éclaire ce qu'on tient (17).
20. **La courbe d'une lumière qui change dit qui agit** : sèche = la physique, fondu = un régisseur, clignement = la panne ; la cause montrée **avant** donne l'auteur ; l'insert de la cause garde la clé du plan qu'il précède (18).
21. **Texte et image : sens en contrepoint, espace en continuité** ; un geste ne se lit que s'il sort de la silhouette (19). Détail clip : `montage-direction-artistique`.
22. **Le texte prend la valeur opposée à l'image** au moment où il apparaît (noir dans un flash blanc, puis inversé) ; un dispositif automatique (saccade, aléa, preset) ne porte pas une direction (20).
23. **Chaque levier ne dit que ce qu'il dit** : lumière = heure et valeur, hauteur de caméra = rapport de force, focale = l'espace dont dispose le personnage ; pour « il a changé », les trois dans le même sens (31).
24. **Une posture a son axe de lecture** : flexion en profil, ouverture de face ou de dos ; vérifier l'angle avant de dire qu'un corps « ne joue pas » (31).
25. **L'image peut fabriquer la pudeur seule** : un écran naturel (buée, reflet, rideau) qui se ferme à mesure que la caméra approche ; forcer l'entrée ensuite se décide sur le jeu réel (34).
26. **Une règle sonore apprise se rompt pour faire entendre l'absence** : enseigner, puis retirer (30).
27. **Le temps aussi se mesure** : mon estimation de la durée d'un travail se trompe d'un facteur 3 à 8 ; lire l'horloge plutôt que l'estimer.
28. **Une direction écartée sans maquette n'a pas été jugée** : voir `montage-direction-artistique` (fait foi).

## Renvois
`montage-grammaire` (raccords), `montage-rythme`, `montage-couleur-et-intention`, `montage-motion-design-principes`, `montage-son-et-emotion`.
