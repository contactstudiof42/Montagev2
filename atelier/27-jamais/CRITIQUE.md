# Pièce 27 « Jamais » — critique (session 23)

Commandes : `python3 atelier/27-jamais/piece.py atelier/rendus/27 ECART TENUE [PRELAP] [--v2] [--nom NOM]` (0,6 s par version ; `voix.wav` = `espeak-ng -v fr -s 150 -p 45 -w voix.wav "Moi, manger du chou-fleur ? Jamais."`), puis `bande.py RENDUS SORTIE.png NOM…` (bande-film image par image autour de la coupe, enveloppe du son ; rouge = fin du mot-clé, blanc = coupe, jaune = regard caméra).

## v1 — 6 versions (écart −4, 0, 4, 8, 12 images ; pré-lap 6 images)
Planches : `v1-ecarts.png`, `v1-planche.png`.
- **Le plan d'arrivée ne se lisait pas, donc le timing ne servait à rien.** Planche v1 : le personnage du plan B n'a plus son pull bleu (on ne sait pas que c'est lui), le chou-fleur est une rangée de ronds blancs (pop-corn ? nuage ?), la fourchette est à côté de la bouche, et le « regard caméra » (les pupilles qui montent de 14 px) est invisible. Avec une coupe à 0-4 images, le spectateur a ~0,5 s pour identifier qui, quoi, et que ça contredit la phrase : il faut que le plan d'arrivée soit une **icône** (même costume, objet reconnaissable à la silhouette, action sans ambiguïté). C'est la leçon principale : **la précision de la coupe ne vaut que si le plan d'arrivée se lit en moins d'une demi-seconde.**
- **Le pré-lap tue le mot-clé.** Avec une coupe à 0 et le craquement 6 images avant l'image, la bande montre le craquement **par-dessus la fin de « jamais »** : le son du plan B masque le mot qui fait le gag. Un pré-lap n'est possible que si l'écart après le mot-clé est au moins égal au pré-lap, et alors il **annonce** la chute (le whoosh d'annonce que la fiche condamne). Pour une contradiction : son et image changent **à la même image**. Le « smash » est là : ambiance de pièce → premier craquement sur la première image du plan B.
- **Le plan A cadre au mur volait l'œil** (plus grande surface claire, à droite) : retiré en v2.

## v2 — plan d'arrivée refait, 5 écarts (−4, 0, 2, 4, 8), tenue 2 s
Planches : `v2-planche.png`, `v2-ecarts.png`.
- Plan B : même pull bleu (identité immédiate), chou-fleur entier entamé avec ses feuilles vertes (silhouette lisible), fourchette **dans** la bouche, et surtout un **double contraste** : les yeux plissés de plaisir (^ ^) — il n'en mange pas seulement, il adore — puis grands ouverts sur la caméra à 0,6 s : pris en flagrant délit. Le second rire est un changement de forme (arcs → disques blancs), pas un déplacement de pupille : lisible à 28 px sur la bande.
- **Écarts lus sur la bande** :
  - **0 image** : la coupe tombe sur la queue de la voyelle de « -mais » (la dernière barre forte est encore là) : la fin du mot est rognée. Pas fatal (le mot est reconnu), mais la phrase n'est pas « posée ».
  - **2 images (80 ms)** : deux images de bouche fermée, visage figé dans sa certitude, puis la coupe. Le mot est entier, la conviction est posée, et rien n'a le temps de se passer. **Ma référence.**
  - **4 images** : encore sec, mais la pose commence à se voir comme une pause.
  - **8 images (0,32 s)** : un temps mort lisible sur la bande (8 images identiques, silence). C'est un « attendez la suite » : le spectateur devine la coupe avant qu'elle arrive, la contradiction devient prévisible. À réserver au cas où l'on **veut** que le public l'anticipe (gag récurrent connu, complicité), pas à la première occurrence.
  - **−4 images** : on coupe **dans** « jamais » (« jamè- ») : ce n'est plus le même gag. C'est le montage qui lui coupe la parole, un narrateur qui se moque (ton *Arrested Development*). Plus méchant, plus complice ; le risque est que le mot-clé ne soit pas reconnu. À essayer seulement si le mot-clé est identifiable sur ses premières syllabes.
- **Accord avec la fiche** (« 0 à 4 images après la dernière syllabe ») : oui, avec une précision : **0 rogne la voyelle finale d'une voix réelle, 2 est le point sec**. Et la fiche ne disait pas que l'écart négatif change la nature du gag.

## Grille
- Intention servie : v2 oui sur planche ; v1 non (plan d'arrivée illisible).
- Lisibilité : v2 bonne (identité, objet, action) ; le chou-fleur reste stylisé (pourrait passer pour un bouquet).
- Rythme : écart 2 images, regard à 0,6 s, tenue 2 s (1,4 s après le regard) : non testée en variantes (Y28).
- Composition : A et B centrés sur le même axe : la coupe se lit comme un « avant / après », ce qui sert la contradiction.
- Originalité : forme classique (Gilligan cut) ; le seul apport est le double contraste (plaisir + flagrant délit).
- Justesse : pas de SFX d'annonce, pas de musique, la mastication s'arrête au regard : le silence fait la réaction.

## Limites
Ni écouté ni vu en temps réel ; jugement sur bandes à l'image près. Voix de synthèse : une vraie voix a une queue de voyelle plus longue et une respiration ; refaire la mesure de l'écart sur une vraie prise (phase 2 ou fichier fourni).

## Suite (Y28)
Tenue du plan d'arrivée 1 / 2 / 3 / 4 s (bande-film complète à 5 i/s) ; silence-gag (un son appris 3 fois puis retiré) ; règle de trois avec la même phrase « Jamais » sur trois aliments, la 3e trahie.

## v3 — « Trois fois jamais » (Y28 : règle de trois + silence-gag + tenue), `trois.py`
Commande : voix `l1.wav` / `l2.wav` / `l3.wav` (espeak-ng, « Le brocoli ? Jamais. », « Les épinards ? Jamais. », « Le chou-fleur ? Jamais. »), puis `python3 atelier/27-jamais/trois.py atelier/rendus/27 TENUE [--ting3] [--v4]` (~1 s par version). Planches : `v3-planche.png` (A, 1re image de B, B à 0,9 s, pour chaque occurrence), `v3-timeline.png` (film entier à 5 i/s, enveloppe, coupes en blanc ; tenues 1, 2, 4 s et contre-épreuve où le ting reste).
- **Forme constante, vérifiée sur l'enveloppe** : les occurrences 1 et 2 ont la même forme sonore après la coupe (pic du « ting » de fourchette, puis la mastication, puis le silence au regard caméra). Le motif est appris en deux fois, comme le dit la fiche.
- **Le silence-gag se voit sur la bande** : après la 3e coupe, l'enveloppe reste plate (ambiance seule) là où la contre-épreuve `ting3` montre encore le pic. L'absence est un événement parce qu'il y a une place exacte où on l'attend : la première image du plan B.
- **Faute de v3 : l'assiette vide est ambiguë.** Assiette vide + fourchette posée + chou-fleur sur la table : ça peut se lire « il a déjà tout mangé » (la chute est encore la même) au lieu de « il a tenu parole ». Et ses yeux grands ouverts dès la 1re image reprennent l'état final des plans 1 et 2 : la 3e occurrence commence comme les deux autres finissent.
- **Tenue** : à 1 s, la coupe tombe ~0,5 s après la fin du ting qu'on attendait (il dure ~0,4 s) : le silence a à peine existé. À 4 s, le plan est fixe et muet : un temps mort. Entre les deux, il faut un **bouton** (un dernier petit geste qui relance) plutôt qu'une durée.

## v4 — la trahison rimée avec le plan A (`--v4`, tenue 2,2 s)
Planche : `v4-planche.png` (plan A, puis B3 à 0,04 / 1,0 / 1,4 / 1,6 / 2,1 s).
- B3 reprend **les sourcils froncés et les bras croisés du plan A** : la coupe montre un homme inchangé, « toujours non ». Le chou-fleur est servi **intact dans l'assiette** : lisible comme « on le lui a servi, il n'y a pas touché ».
- **Bouton** : à 1,3 s, il repousse l'assiette d'un doigt (raclement, 0,3 s), puis on tient jusqu'à 2,2 s. Le seul son de la réaction est celui de son refus. C'est le second rire, et c'est lui qui dit quand couper (≈ 0,6 s après le bouton).
- Défaut restant : le bras qui sort du croisé est presque invisible (l'assiette est collée au corps) ; on voit un doigt au bord du pull. À refaire avec l'assiette plus loin, ou avec un vrai acteur.
- **Leçon** : dans une règle de trois, la 3e occurrence garde **la forme** des deux premières (même cadre, même écart de coupe, même place pour le son) et change **une seule chose lisible** ; et la réaction finale ne se règle pas en secondes mais par un bouton, après lequel on coupe vite.
