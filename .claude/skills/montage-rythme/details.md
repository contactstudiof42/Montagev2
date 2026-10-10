# Rythme : détails, mesures et maquettes

Annexe de `SKILL.md` (montage-rythme). Légende des marqueurs : voir SKILL.md. Les pièces numérotées (`atelier/NN-*/CRITIQUE.md`) sont des maquettes Blender / Pillow / ffmpeg : principes à confirmer sur de vraies images en phase 2.

## Référence de l'utilisateur : Interstellar (`GOUTS.md` — son goût prime)
Fiche : `culture/interstellar-rythme.md`. Ficelles à réutiliser en priorité :
1. **Poser la règle du temps, puis la faire entendre** : une règle simple (« 1 h ici = 7 ans là-bas »), puis un son régulier qui devient un compteur. En pub : un tic, un battement ou un bruit répétitif qui matérialise l'enjeu temporel. (Le chiffre « 1,25 s » souvent cité pour le tic de la planète de Miller n'est pas confirmé.)
2. **Le son qui arrache** : le son de la scène suivante démarre sous la fin d'une scène émotionnelle (décompte, moteur), puis on coupe net sur le temps fort. Ici, pas de plan de transition : l'adieu à la ferme enchaîne directement sur le décollage.
3. **Compresser d'un côté, dilater de l'autre** : le temps raconté défile vite (écrans, messages), pendant que le visage de celui qui regarde reste longtemps à l'écran, sans coupe.
4. **Raccourcir les segments du montage parallèle à l'approche du climax** (par exemple 8 s / 4 s / 2 s / 1 s) : l'accélération vient de la structure, pas d'un changement de style des plans.
5. **Un motif musical qui monte par couches** autorise un montage de plus en plus serré. Pendant la tension, on retire les plans de respiration (extérieurs rassurants).
6. **Mis à l'épreuve : pièce 29 « Deux horloges »** (session 24, `atelier/29-deux-horloges/`, v1-v5) [ÉPROUVÉ EN MAQUETTE] (maquette 2D ; son jugé sur enveloppe, pas écouté) :
   - l'ellipse est **dans la coupe** : dans chaque plan, le temps des deux lignes presque arrêté (un accéléré dans le plan se lit comme un effet, et un jour/nuit accéléré clignote) ;
   - chaque ligne a son **compteur visible** (goutte en macro ici, bâtons au mur et plante là-bas) ; v1-v3 ratées en partie parce que la goutte faisait 5 px ;
   - pulsation **indépendante** des coupes = pression diffuse ; pulsation **sur** les retours = causalité (« à chaque tic, on voit ce qui est perdu »). v5 (retours sur le tic) = référence ;
   - final par l'absence : enseigner la règle (tic = perte) cinq fois, puis la rompre (dernier retour sans tic, tenu 2,6 s ; les bâtons n'ont plus bougé : personne ne compte) ;
   - écran partagé (v8, 9:16 empilé) : l'écart se **comprend** (on compare) mais ne se **sent** plus (on ne s'absente jamais d'une ligne) : partagé pour expliquer, alternance pour émouvoir ;
   - les grandes références (`culture/montage-alterne-grandes-references.md` : Griffith, *Le Parrain*, *Le Silence des agneaux*, *Dunkirk*) accélèrent jusqu'au bout et finissent par **une jonction** des lignes ; une fin sans jonction est un parti pris à défendre, et le son d'une ligne posé sur l'autre donne l'ironie (le baptême sur les meurtres) ;
   - piège : couper sur une pulsation qui ne tombe pas sur des images entières (1,25 s = 31,25 images à 25 i/s, mais 30 pile à 24 i/s) ; choisir le tempo selon la cadence du projet.
Limite : le mixage où le dialogue passe sous les effets est à proscrire pour les réseaux et la pub (vision sans son, intelligibilité).

## Référence de l'utilisateur : Ziak, « Même pas un grincement » — le rythme macro (mesuré sur le clip réel)
Analyse complète : `culture/ziak-meme-pas-un-grincement.md`, chronologie `culture/ziak-chronologie-mesures.png`.
- 88 plans, médiane 1,67 s, à 143,6 BPM : **les coupes ne sont pas calées sur le beat** (niveau du hasard), mais il y a **26 coupes/min quand la basse est là, 13,4 quand elle disparaît**, et un plan long et immobile dans chaque creux de basse de plus de 5 s.
- **Principe** : sur une musique déjà très rythmée (drill, trap, électro), le montage peut suivre **l'arrangement** (densité de coupes selon l'énergie) plutôt que **les temps**. L'image garde sa propre gravité ; la musique respire dans l'image sans calage mécanique.
- **Seconde horloge** : une pulsation visuelle (éclairs toutes les 15 images) en désaccord avec le tempo crée une tension qui ne se résout pas.
- Choisir consciemment : **micro** (couper sur les temps : plaisir, énergie, kinetic) ou **macro** (suivre l'arrangement : menace contenue, gravité). Les deux sont dans les goûts de l'utilisateur, **pour des usages différents** (confirmé) : micro pour les réseaux, macro pour le clip et le film de marque.

## Pièce 03 « Rythme macro » (`atelier/03-rythme-macro/`) [ÉPROUVÉ EN MAQUETTE]
Même musique drill synthétique (140 BPM, intro / couplet / coupure / reprise), même banque de plans, trois montages : A micro (coupe tous les 2 temps), B macro (densité par section), C hybride.
- **Le calage sur les temps est une texture ; la densité par section est la forme.** A, parfaitement calé, se lit sur la planche comme un motif périodique : l'intro clairsemée et le couplet chargé y sont identiques, l'image n'entend que le métronome. B et C laissent lire la structure du morceau.
- **Hybride (C) = défaut pour la pub et les réseaux** : intro tenue, micro-calage seulement là où la musique pousse, accélération au temps sur les 2 mesures avant la coupure (effet roulement), image d'exception sur la coupure. **Macro pur (B) = clip grave**, menace contenue.
- **Un accent ne vaut que par sa rareté** : le plan chaud utilisé 1 fois sur la coupure fait l'événement du montage ; 4 fois à intervalle régulier (A), il devient du papier peint.
- Une matière sans sujet (abstraite) ne tient pas un plan long de 7 s : la durée tenable dépend de ce qu'il y a à lire dans le plan.

## Tempo et cadence (labo `labo/outils/tempos.py`, session 24) [TESTÉ EN LABO]
- À 25 i/s, seuls 60, 75, 100, 125, 150 BPM ont une noire en images entières ; à 24 i/s : 60, 72, 80, 90, 96, 120, 144, 160, 180 ; à 23,976 / 29,97 : aucun.
- **Ne jamais couper « toutes les N images » sur une musique** : 120 BPM à 25 i/s = 12,5 images ; couper toutes les 12 dérive de 0,64 s en 8 mesures. Couper sur la grille arrondie de chaque temps (marqueurs de temps, `labo/marqueurs/beats_xml.py`).

## Mesurer le rythme (labo)
- **Montage scripté calé sur un tempo** [TESTÉ EN LABO, atelier 03] : calculer chaque coupe en **numéro d'image absolu** (`round(t*fps)`), jamais en additionnant des durées arrondies plan par plan. Mesuré : à 25 i/s et 140 BPM (10,71 images par temps), l'addition de durées arrondies fait dériver de **−460 ms sur 24 s** (plus d'un temps) ; en images absolues, écart max **17 ms** (≤ ½ image, incompressible, imperceptible). Vérifier au `scdet=threshold=8`. Dans un logiciel de montage, même logique : poser les marqueurs de temps sur la timeline et couper sur l'image la plus proche, ne pas taper des durées.
- **Outil complet** [TESTÉ EN LABO, 2026-10-09] : `python3 -I labo/analyse-clip/analyse_clip.py <video> <sortie>` donne les coupes et les flashs, les durées, le tempo, le calage des coupes sur le beat (avec la référence du hasard), les coupes selon la présence de la basse, et la lumière. Pensé pour les images sombres, où `scdet` sous-détecte : il trouvait 38 coupes au lieu de 87 sur Ziak. **Distinguer les flashs des coupes** : sur Ziak, 18 « coupes » étaient des éclairs.
- Détection de coupes [TESTÉ EN LABO, session 1 — `labo/rythme/RESULTATS.md`] :
  `ffmpeg -i film.mp4 -vf "scdet=threshold=10,metadata=print:key=lavfi.scd.time:file=-" -f null - 2>/dev/null | grep -o "lavfi.scd.time=[0-9.]*" | cut -d= -f2`
  → temps des coupes → durées de plans → histogramme. Fiable sur coupes franches (8/8 au centième) ; **rate les fondus enchaînés** ; entre plans très proches, descendre le seuil à 3 (risque de faux positifs, à tester sur matériau réel).

- **Fondus** [TESTÉ EN LABO, session 4, `labo/fondus/variance.py`] : scdet n'en voit aucun ; la méthode « écart au milieu » (l'image du milieu ≈ moyenne de ses voisines à ±L/2) + détection du noir en trouve 3/4 sans faux positif, puis **4/4 sans faux positif sur une 2e vérité terrain indépendante** (mêmes seuils) ; elle rate les fondus entre deux plans pauvres et proches en luminance et peut confondre un mouvement lent et régulier. Toujours contrôler visuellement.
- **Grille de temps importable** [détection TESTÉE EN LABO, session 4] : `labo/marqueurs/beats_xml.py` → marqueurs XML FCP7 ; vérifier la **phase** (1er marqueur), pas seulement le BPM.

## Le rythme que le sujet impose (atelier 04, session 4) [ÉPROUVÉ EN MAQUETTE]
Avant de choisir un tempo, regarder si le sujet a déjà une dramaturgie physique : la marée découvre lentement ce qui est haut, puis le sol d'un coup ; une bougie fond lentement puis s'éteint d'un coup ; une foule se remplit goutte à goutte puis déborde. **Lent puis brusque** est la forme naturelle de la révélation : la cadrer, la laisser se poser (tenue finale ≥ 1 s), ne pas la remplacer par une accélération de montage.

## Où couper dans une chaîne causale (atelier 07, session 6) [ÉPROUVÉ EN MAQUETTE]
Démonstration produit, réaction en chaîne, gag mécanique, plan « Cog » : trois montages du même événement simulé (`atelier/07-causalite/CRITIQUE.md`).
1. **La mécanique décide où l'on peut couper.** Lister les contacts à l'image près (en tournage : visionner image par image ; en 3D : les lire dans la simulation). Une cascade (un contact toutes les 2-3 images) ne se coupe pas : la tenir dans un seul plan.
2. **Couper dans les respirations** : pendant que l'objet voyage entre deux contacts (roulement, vol, chute), à 4 images ou plus de tout contact, et dans le sens du mouvement (sortie par la droite, entrée par la gauche).
3. **Couper sur le contact escamote la preuve** : le plan suivant commence quand l'effet a déjà démarré, la cause est hors cadre. C'est le langage du kinetic (coupe sur l'impact pour l'énergie), légitime quand la preuve n'est pas l'argument ; c'est une faute dans une démonstration.
4. **Ouvrir le plan avant la cause** : montrer l'effet en puissance (les dominos debout, la tasse au bord) quelques images avant que la cause n'entre. Le spectateur anticipe, et l'anticipation est le plaisir de ce genre de séquence.
5. **Cadrer la conséquence** : l'impact final et l'objet au repos doivent être dans le cadre. Un plan large pensé pour la chaîne perd souvent sa fin au bord de l'image.

## Le plan de retour (atelier 12, session 9) [ÉPROUVÉ EN MAQUETTE] (perception à confirmer)
- Quand un plan revient (même cadre, après un plan de coupe) et que **quelque chose a changé**, le faire durer **plus longtemps que le plan de départ** (4 s puis 6 s) : la première seconde sert à reconnaître le lieu, le reste à comparer. Trop court (3 s), on reconnaît sans relire ; trop long au départ (8 s), le plan devient décor avant l'anomalie. Voir `montage-grammaire` (cécité au changement).
- Le plan de coupe entre les deux (la fenêtre) doit être assez long pour qu'on « oublie » le premier (3 s), et **ne rien montrer de la zone qui va changer** (sinon tricherie de raccord).

## Le tempo propre du sujet (atelier 14 « Balancier », session 9) [ÉPROUVÉ EN MAQUETTE]
- Quand un objet ou un corps produit un rythme (pendule, respiration, danse), **couper sur ses points morts** (vitesse nulle aux extrémités) : la coupe ne prend rien au geste et passe inaperçue (A : 2 coupes à 0 image d'un point mort). Couper au milieu d'un passage casse le mouvement et se voit.
- Si ce tempo **change** (amorti, accéléré), tenir le cadre assez longtemps pour qu'on compare le mouvement à lui-même : 3 plans sur 15 s ont montré l'épuisement, 19 plans l'ont masqué. Voir `montage-kinetic-editing` 3e.

## Dilater par la durée plutôt que par la vitesse (examen n°6 et atelier 15, session 10) [ÉPROUVÉ EN MAQUETTE] (planches et mesures ; perception en mouvement à confirmer)
- Pour étirer l'instant décisif, **tenir le plan au-delà de l'attente** (laisser sonner deux fois de trop avant de décrocher) avant de penser ralenti. La durée dilate le temps intérieur sans changer la texture de l'image ; le ralenti dit « ceci est spécial » et surligne souvent ce que le son porte déjà.
- Le ralenti d'image se réserve aux rushes tournés en haute cadence, ou aux mouvements que l'interpolation sait inventer (grands mouvements simples, fond lisse) ; jamais sur mains, fils, objets fins, occlusions à partir de 25 i/s.
- **L'attente doit être habitée** (atelier 15) : deux sonneries de trop sur un téléphone seul = temps vide. Il faut un signe de quelqu'un qui pourrait agir et n'agit pas (la main posée sur le combiné pendant deux sonneries), puis le geste à vitesse réelle : il garde son poids parce qu'il libère l'attente.
- Ralenti interpolé ×3 depuis 25 i/s (atelier 15) : 43 dB de moyenne mais le combiné et la main en blocs sur 2 images sur 3, cordon dédoublé → pulsation nette/cassé/cassé à 8 Hz sur le sujet. **Juger la pire image dans la zone du sujet, jamais la moyenne.**


## Une descente qui endort (atelier 25 « Au lit », session 20) [ÉPROUVÉ EN MAQUETTE] (courbes mesurées ; « endort » non vérifié)
- Endormir n'est pas aplatir : la version plate (tout constant) devient une **boucle reconnaissable** (même séquence, même YAVG au dixième) ; ce qui berce, c'est une **direction lente commune à tous les canaux** (débit, silences, durée des plans, volume, lumière).
- Un seul canal qui ne suit pas (image et son forts sous une voix qui ralentit) contredit la descente là où l'on devrait lâcher.
- Durées de plan croissantes (5 → 20 s) et **retour d'un même cadre changé** (la fenêtre, moins de lumières) : le retour mesure le temps qui passe mieux qu'un ralentissement.
- Détail : `atelier/25-au-lit/CRITIQUE.md`.

## Une densité qui décroît (atelier 26, session 22) [ÉPROUVÉ EN MAQUETTE] (maquette 2D mesurée)
- Une relance dans une forme qui ralentit est **un coup**, pas une rafale ; le jour où il n'y a plus d'outil à retirer, c'est un **changement de régime** (autre caméra, autre texture, autre son) qui relance.
- Retirer les ponctuations sans **allonger les plans** ne calme rien : les coupes qui restent deviennent les plus gros chocs du film.
- Le temps long a besoin d'un mouvement interne, mais dosé à quelques % : une lumière qui palpite sur tout le cadre compte comme un événement. Détails et mesures : `atelier/26-densite-decroissante/CRITIQUE.md`.

## Le gag de contradiction à l'image près (atelier 27, session 23) [ÉPROUVÉ EN MAQUETTE] (maquette 2D + voix de synthèse)
- **Le plan d'arrivée d'abord** : une coupe juste ne sauve pas un plan qui ne se lit pas en < 0,5 s (même costume, objet reconnaissable à sa silhouette, action sans ambiguïté). Le second rire est un **changement de forme** (yeux fermés de plaisir → grands ouverts sur la caméra), pas un déplacement de quelques pixels.
- **Écart après le mot-clé** : 0 image rogne la voyelle finale ; **2 images = le point sec** ; 8 images = un temps mort que le spectateur lit comme « attendez la suite » (la chute devient prévisible) ; un écart **négatif** (couper dans le mot) change de gag : le montage coupe la parole, ton narrateur moqueur.
- **Règle de trois** (v3-v4) : la 3e occurrence garde la forme des deux premières (cadre, écart de coupe, place du son) et change une seule chose lisible ; elle ne doit pas commencer comme les autres finissent. Une réaction muette ne se règle pas en secondes : 1 s n'a pas laissé exister le silence, 4 s fixes = temps mort ; il faut un **bouton** (un dernier petit geste), puis couper ~0,6 s après.
- **Pas de pré-lap** sur une contradiction : le son du plan B masque le mot-clé ou annonce la chute ; son et image changent à la même image. Détails : `atelier/27-jamais/CRITIQUE.md`.

## Le rire comme piste de montage (fiche `culture/timing-comique-sitcom.md`, session 23) [THÉORIQUE, sources de monteurs]
- Le rire du public dure plus longtemps que l'écran ne le supporte : on le raccourcit, et la réplique suivante tombe **sur la fin du rire**, jamais dans le pic.
- Monter un peu long, resserrer la mise en place sans toucher à l'ordre des mots, puis une passe finale « 5 images ici, 12 là » ; laisser respirer la chute.
- Sur la chute, couper sur **celui qui écoute** (sa réaction autorise le rire), mais garder les yeux de celui qui parle au moment du mot.
- Faux documentaire : chaque coupe doit pouvoir venir d'une caméra présente ; le talking head est une chute ou un démenti que la scène suivante contredit sans respiration.

## Peu de coupes : chacune pèse (pièce 25 v4, session 23) [ÉPROUVÉ EN MAQUETTE] (maquette mesurée)
- Deux plans au lieu de six : la descente tient dans le plan (lumières qui s'éteignent une à une), mais l'unique coupe devient l'événement le plus fort du film (−40 % de luminance d'un coup). Dans une forme lente faite pour apaiser, la remplacer par un **fondu long** (12 s) : la courbe reste monotone, et la superposition peut porter du sens si les deux cadres sont composés pour se rencontrer (la lune qui apparaît dans le ciel de la fenêtre). Détails : `atelier/25-au-lit/CRITIQUE.md` v4.

## La réaction tenue dans le drame (examen n°13 et `culture/reaction-tenue-drame.md`, session 24) [THÉORIQUE, sources écrites]
- Aucune norme de durée sourcée au milieu d'un dialogue ; une réaction tenue tient si l'enjeu est posé juste avant et si le plan **change encore** (micro-geste, son qui vit). Couper après le dernier geste, pas à une durée fixe (même logique que le « bouton » de la pièce 27).

## Le silence vu de loin (pièce 34 « De dehors », session 25) [ÉPROUVÉ EN MAQUETTE] (maquette Blender + voix de synthèse ; décrochage réel non mesuré)
- De près, un silence est une **réaction tenue** (il a un visage). De loin, le même silence est un **trou** : 15 s puis 21 s sans rien à lire sur une voiture fixe (v1). Les répliques tiennent seules, les silences non.
- Donner au silence un support visible **qui soit un acte des personnages** : la liseuse qu'il éteint juste après « je pars » (il ne veut pas être vu), la buée de leur souffle qui monte, le chauffage demandé qui la dégage. Test : retirer l'événement, le sens change-t-il ? Si non (les phares d'une voiture qui passe), c'est du remplissage : couper.
- Un compteur lent (buée) n'existe qu'à la taille de lecture : sur une voiture à 15 % de la largeur, invisible ; une **poussée lente de 100 s** (zoom ×2,4, accélération douce en t^1,6) l'amène à la lecture sans se faire remarquer. `mesure.py` (trous sans événement) dit « réglé » dès v3 alors que l'œil ne voit rien : mesurer l'événement **et** sa taille.
