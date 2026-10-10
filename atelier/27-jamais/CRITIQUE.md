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
