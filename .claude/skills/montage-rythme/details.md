Annexe de `SKILL.md` : mesures, détail des pièces et des références de montage-rythme ; les principes ne sont pas répétés ici (le SKILL.md fait foi).

# Rythme : détails, mesures et maquettes

Légende des marqueurs : voir SKILL.md. Les pièces numérotées (`atelier/NN-*/CRITIQUE.md`) sont des maquettes Blender / Pillow / ffmpeg : principes à confirmer sur de vraies images en phase 2.

## Interstellar (fiche `culture/interstellar-rythme.md`) : précisions
- Règle du temps : une phrase simple (« 1 h ici = 7 ans là-bas »), puis un son régulier qui la matérialise ; en pub, un tic, un battement ou un bruit répétitif. Le chiffre « 1,25 s » souvent cité pour le tic de la planète de Miller n'est pas confirmé.
- Son qui arrache : le décompte ou le moteur démarre sous la fin de la scène, puis coupe nette sur le temps fort, sans plan de transition (l'adieu à la ferme enchaîne sur le décollage).
- Compresser / dilater : le temps raconté défile par écrans et messages pendant que le visage reste.
- Segments raccourcis du montage parallèle : l'accélération vient de la structure, pas d'un changement de style des plans. Un motif musical qui monte par couches autorise ce montage de plus en plus serré ; on retire alors les extérieurs rassurants.

### Pièce 29 « Deux horloges » (`atelier/29-deux-horloges/`, v1-v8) [ÉPROUVÉ EN MAQUETTE] (maquette 2D ; son jugé sur enveloppe, pas écouté)
- Ellipse dans la coupe : dans chaque plan, le temps est presque arrêté ; un accéléré dans le plan se lit comme un effet, un jour / nuit accéléré clignote.
- Chaque ligne a son **compteur visible** (goutte en macro ici, bâtons au mur et plante là-bas) ; v1-v3 ratées en partie parce que la goutte faisait 5 px.
- Pulsation **indépendante** des coupes = pression diffuse (la variante « sur les retours », v5, est la référence).
- Final par l'absence : la règle (tic = perte) enseignée cinq fois, puis rompue (dernier retour sans tic, tenu 2,6 s ; les bâtons n'ont plus bougé : personne ne compte).
- Écran partagé (v8, 9:16 empilé) : l'écart se comprend mais ne se sent plus (on ne s'absente jamais d'une ligne).
- Les grandes références (`culture/montage-alterne-grandes-references.md` : Griffith, *Le Parrain*, *Le Silence des agneaux*, *Dunkirk*) accélèrent jusqu'au bout et finissent par **une jonction** des lignes ; une fin sans jonction est un parti pris à défendre ; le son d'une ligne posé sur l'autre donne l'ironie (le baptême sur les meurtres).
- Exemple du piège de cadence : une pulsation de 1,25 s = 31,25 images à 25 i/s, mais 30 pile à 24 i/s.

## Ziak, « Même pas un grincement » (mesuré sur le clip réel)
Analyse : `culture/ziak-meme-pas-un-grincement.md`, chronologie `culture/ziak-chronologie-mesures.png`.
- 88 plans, médiane 1,67 s, à 143,6 BPM ; calage des coupes sur le beat au niveau du hasard ; un plan long et immobile dans chaque creux de basse de plus de 5 s.
- Le rythme macro convient surtout à une musique déjà très rythmée (drill, trap, électro) : la musique respire dans l'image sans calage mécanique.
- **Seconde horloge** : une pulsation visuelle (éclairs toutes les 15 images) en désaccord avec le tempo crée une tension qui ne se résout pas.
- Partage micro / macro selon l'usage : confirmé par l'utilisateur.

## Pièce 03 « Rythme macro » (`atelier/03-rythme-macro/`) [ÉPROUVÉ EN MAQUETTE]
- Dispositif : même musique drill synthétique (140 BPM, intro / couplet / coupure / reprise), même banque de plans, trois montages : A micro (coupe tous les 2 temps), B macro (densité par section), C hybride.
- A, parfaitement calé, se lit sur la planche comme un motif périodique : intro clairsemée et couplet chargé y sont identiques. B et C laissent lire la structure du morceau.
- Hybride C : l'accélération avant la coupure est un calage au temps sur les 2 dernières mesures (effet roulement). Macro pur B = clip grave, menace contenue.
- Une matière sans sujet (abstraite) ne tient pas un plan long de 7 s : la durée tenable dépend de ce qu'il y a à lire dans le plan.

## Tempo et cadence (`labo/outils/tempos.py`) [TESTÉ EN LABO]
- À 23,976 et 29,97 i/s, aucun tempo courant n'a une noire en images entières.
- Exemple de dérive : 120 BPM à 25 i/s = 12,5 images par temps ; couper toutes les 12 images dérive de 0,64 s en 8 mesures.

## Mesurer le rythme (labo)
- **Montage scripté en images absolues** [TESTÉ EN LABO, atelier 03] : à 25 i/s et 140 BPM (10,71 images par temps), écart max **17 ms** en images absolues (≤ ½ image, imperceptible), contre −460 ms en additionnant des durées arrondies. Vérifier au `scdet=threshold=8`.
- **Outil complet** [TESTÉ EN LABO, 2026-10-09] : `python3 -I labo/analyse-clip/analyse_clip.py <video> <sortie>` (coupes et flashs, durées, tempo, calage sur le beat avec la référence du hasard, coupes selon la présence de la basse, lumière). Sur Ziak, `scdet` trouvait 38 coupes au lieu de 87, et 18 « coupes » étaient des éclairs : distinguer les flashs des coupes.
- **Détection de coupes franches** [TESTÉ EN LABO, session 1, `labo/rythme/RESULTATS.md`] :
  `ffmpeg -i film.mp4 -vf "scdet=threshold=10,metadata=print:key=lavfi.scd.time:file=-" -f null - 2>/dev/null | grep -o "lavfi.scd.time=[0-9.]*" | cut -d= -f2`
  → temps des coupes → durées → histogramme. 8/8 au centième sur coupes franches ; entre plans très proches, seuil 3 (risque de faux positifs, à tester sur matériau réel).
- **Fondus** [TESTÉ EN LABO, session 4, `labo/fondus/variance.py`] : « écart au milieu » (l'image du milieu ≈ moyenne de ses voisines à ±L/2) + détection du noir : 3/4 sans faux positif, puis 4/4 sans faux positif sur une 2e vérité terrain indépendante (mêmes seuils). Rate les fondus entre deux plans pauvres et proches en luminance, peut confondre un mouvement lent et régulier : contrôler à l'œil.
- **Grille de temps** : `labo/marqueurs/beats_xml.py` produit des marqueurs XML FCP7 [détection TESTÉE EN LABO, session 4].

## Pièce 04 : le rythme que le sujet impose [ÉPROUVÉ EN MAQUETTE]
Exemples de dramaturgie physique « lent puis brusque » : la marée découvre lentement ce qui est haut, puis le sol d'un coup ; une bougie fond puis s'éteint ; une foule se remplit goutte à goutte puis déborde. Regarder si le sujet l'a avant de choisir un tempo.

## Pièce 07 : chaîne causale (`atelier/07-causalite/CRITIQUE.md`) [ÉPROUVÉ EN MAQUETTE]
- Lister les contacts à l'image près (au tournage : visionner image par image ; en 3D : les lire dans la simulation). Une cascade (un contact toutes les 2-3 images) ne se coupe pas : un seul plan.
- Couper dans le sens du mouvement (sortie par la droite, entrée par la gauche).
- Couper sur le contact : le plan suivant commence quand l'effet a démarré, la cause est hors cadre ; c'est le langage du kinetic, légitime quand la preuve n'est pas l'argument.
- Ouvrir quelques images avant la cause (dominos debout, tasse au bord) : l'anticipation est le plaisir du genre. Un plan large pensé pour la chaîne perd souvent sa fin au bord du cadre.

## Pièce 12 : le plan de retour [ÉPROUVÉ EN MAQUETTE] (perception à confirmer)
- La première seconde sert à reconnaître le lieu, le reste à comparer. Trop court (3 s) : on reconnaît sans relire ; trop long au départ (8 s) : le plan devient décor avant l'anomalie. Voir `montage-grammaire` (cécité au changement).
- Le plan de coupe intermédiaire (la fenêtre) dure assez pour qu'on « oublie » le premier (3 s) et ne montre rien de la zone qui va changer.

## Pièce 14 « Balancier » : le tempo propre du sujet [ÉPROUVÉ EN MAQUETTE]
- Point mort = vitesse nulle aux extrémités : la coupe n'y prend rien au geste (A : 2 coupes à 0 image d'un point mort) ; au milieu d'un passage, elle casse le mouvement et se voit.
- Tempo qui change (amorti) : 3 plans sur 15 s ont montré l'épuisement, 19 plans l'ont masqué. Voir `montage-kinetic-editing` 3e.

## Pièce 15 et examen n°6 : dilater par la durée [ÉPROUVÉ EN MAQUETTE] (planches et mesures ; perception en mouvement à confirmer)
- Exemple : laisser sonner deux fois de trop avant de décrocher. La durée dilate le temps intérieur sans changer la texture de l'image ; le ralenti dit « ceci est spécial » et surligne souvent ce que le son porte déjà.
- L'interpolation ne sait inventer que les grands mouvements simples sur fond lisse.
- Attente habitée : deux sonneries sur un téléphone seul = temps vide ; la main posée sur le combiné pendant deux sonneries, puis le geste à vitesse réelle, qui garde son poids parce qu'il libère l'attente.
- Ralenti interpolé ×3 depuis 25 i/s : 43 dB de moyenne, mais combiné et main en blocs sur 2 images sur 3, cordon dédoublé → pulsation nette / cassé / cassé à 8 Hz sur le sujet.

## Pièce 25 « Au lit » : une descente (`atelier/25-au-lit/CRITIQUE.md`) [ÉPROUVÉ EN MAQUETTE] (courbes mesurées ; « endort » non vérifié)
- La version plate (tout constant) devient une **boucle reconnaissable** (même séquence, même YAVG au dixième).
- Un seul canal qui ne suit pas (image et son forts sous une voix qui ralentit) contredit la descente là où l'on devrait lâcher.
- Durées de plan croissantes (5 → 20 s) ; le **retour d'un même cadre changé** (la fenêtre, moins de lumières) mesure le temps mieux qu'un ralentissement.
- v4, deux plans au lieu de six : l'unique coupe devient l'événement le plus fort du film (−40 % de luminance d'un coup) ; un **fondu long** (12 s) garde la courbe monotone, et la superposition porte du sens si les deux cadres se rencontrent (la lune qui apparaît dans le ciel de la fenêtre).

## Pièce 26 : une densité qui décroît (`atelier/26-densite-decroissante/CRITIQUE.md`) [ÉPROUVÉ EN MAQUETTE] (maquette 2D mesurée)
- Quand il n'y a plus d'outil à retirer, le coup qui relance est un **changement de régime** (autre caméra, autre texture, autre son).
- Ponctuations retirées sans allonger les plans : les coupes qui restent deviennent les plus gros chocs du film.
- Le temps long a besoin d'un mouvement interne dosé à quelques % : une lumière qui palpite sur tout le cadre compte déjà comme un événement.

## Pièce 27 : le gag de contradiction (`atelier/27-jamais/CRITIQUE.md`) [ÉPROUVÉ EN MAQUETTE] (maquette 2D + voix de synthèse)
- Plan d'arrivée lisible : même costume, objet reconnaissable à sa silhouette, action sans ambiguïté ; le second rire est un **changement de forme** (yeux fermés de plaisir → grands ouverts sur la caméra), pas un déplacement de quelques pixels.
- Écart de 8 images : lu comme « attendez la suite », la chute devient prévisible. Écart **négatif** (couper dans le mot) : autre gag, le montage coupe la parole (narrateur moqueur).
- Règle de trois (v3-v4) : la 3e occurrence garde la forme des deux premières (cadre, écart de coupe, place du son) et change une seule chose lisible ; elle ne commence pas comme les autres finissent.
- Réaction muette : 1 s ne laisse pas exister le silence, 4 s fixes = temps mort.
- Pré-lap : le son du plan B masque le mot-clé ou annonce la chute ; son et image changent à la même image.

## Le rire comme piste de montage (fiche `culture/timing-comique-sitcom.md`) [SOURCÉ] (sources de monteurs)
- Le rire du public dure plus que l'écran ne le supporte : on le raccourcit, la réplique suivante ne tombe jamais dans le pic.
- Monter un peu long, resserrer la mise en place sans toucher à l'ordre des mots, puis une passe finale « 5 images ici, 12 là ».
- Couper sur celui qui écoute, mais garder les yeux de celui qui parle au moment du mot.
- Faux documentaire : chaque coupe doit pouvoir venir d'une caméra présente ; le talking head est une chute ou un démenti que la scène suivante contredit sans respiration.

## Réaction tenue (examen n°13, `culture/reaction-tenue-drame.md`) [SOURCÉ]
Le plan « change encore » = un micro-geste, un son qui vit ; même logique que le « bouton » de la pièce 27.

## Pièce 34 « De dehors » : le silence vu de loin [ÉPROUVÉ EN MAQUETTE] (maquette Blender + voix de synthèse ; décrochage réel non mesuré)
- v1 : 15 s puis 21 s sans rien à lire sur une voiture fixe ; les répliques tiennent seules, les silences non.
- Supports qui sont des actes : la liseuse qu'il éteint juste après « je pars » (il ne veut pas être vu), la buée de leur souffle qui monte, le chauffage demandé qui la dégage. Test : retirer l'événement, le sens change-t-il ? Si non (les phares d'une voiture qui passe), c'est du remplissage : couper.
- Taille de lecture : sur une voiture à 15 % de la largeur, la buée est invisible ; une **poussée lente de 100 s** (zoom ×2,4, accélération douce en t^1,6) l'amène à la lecture sans se faire remarquer. `mesure.py` (trous sans événement) dit « réglé » dès v3 alors que l'œil ne voit rien : mesurer l'événement **et** sa taille.
