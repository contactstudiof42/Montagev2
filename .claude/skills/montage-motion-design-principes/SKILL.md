---
name: montage-motion-design-principes
description: Principes artistiques du motion design et de la typographie animée — quoi animer et pourquoi : carton-titre, générique, line-up, logo animé, typo cinétique, habillage, lower third, explicatif animé, animation d'interface, traces et échos de mouvement. Mots entendus : « l'animation fait cheap », « ça bouge pour rien », « on n'a pas le temps de lire », « le logo doit claquer mais rester premium », « trop de choses bougent », « ça fait template ». Réglages techniques After Effects (courbes, expressions) : montage-after-effects.
---

# Motion design : faire bouger avec une raison

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer sur de vraies images (phase 2).

**Fait foi sur** : le sens d'un mouvement, la lisibilité du texte animé, cartons et génériques. **Ailleurs** : graphe de vitesse, easing, expressions → `montage-after-effects` ; principe « un concept, un signe » en général → `montage-references` § C, n° 9 ; durée des plans et calage musical → `montage-rythme`.

Sources : `culture/saul-bass-generiques.md`, `culture/kyle-cooper-se7en.md`, `culture/mclaren-pas-de-deux-et-chronophotographie.md`, `culture/chronophotographie-marey-muybridge.md`.

## Principes
1. **Un concept, un signe** (Saul Bass) : réduire le message à une forme dessinable, toute l'animation la révèle ou la transforme. Si on anime « des éléments », on n'a pas encore d'idée. [SOURCÉ]
2. **Animer le paramètre qui porte le sens.** Pour une apnée, pas l'échelle du mot (pulse de logo) mais son **interlettrage** qui se resserre. Corriger un excès en réduisant l'amplitude donne un mouvement invisible : **déplacer** le mouvement, pas l'atténuer. L'amplitude dépend de la police (0,90 écrase un Garamond italique, 0,93 tient) ; fond en dégradé plutôt qu'aplat. [ÉPROUVÉ EN MAQUETTE] (pièce 01)
3. **Le mouvement a une cause et une matière** : overshoot = élastique, métal ; sans overshoot = verre, pierre, luxe ; l'ease symétrique par défaut n'a pas de matière. [THÉORIQUE]
4. **Asymétrie** : on entre vite et on se pose, ou on s'élance et on s'arrête net ; la symétrie (4 s / 4 s) se lit comme une machine. [ÉPROUVÉ EN MAQUETTE] (pièce 01)
5. **Montrer le processus plutôt que le résultat** (Kyle Cooper, *Se7en*). [SOURCÉ]
6. **Lisibilité d'abord** : un texte reste lisible au moins le double de son temps de lecture à voix haute, immobile ou presque ; le mouvement se fait avant et après la lecture. [THÉORIQUE]
7. **Carton-liste (line-up, générique) : on balaie, on ne lit pas.** ~100 ms par élément pour trouver un mot connu, ~250-300 ms quand il faut fixer chaque mot. Pour 20-24 noms : ≥ 4 s de tenue immobile, 6-7 s pour conclure « il n'y est pas ». Accélérer : ordre connu, groupes de 4-6, têtes d'affiche hors liste. Extrapolé de listes ≤ 16 éléments : à valider par un test chronométré. [SOURCÉ] (Hornof & Kieras 1997, Boettcher & Wolfe 2015)
8. **Hiérarchiser une liste, c'est économiser des événements** : 19 noms « un nom = un coup » = un compteur (l'œil décroche au 6e) ; en trois rangs (seul et grand / paquets de 3 / énorme) : 11 coups, et la tête d'affiche redevient attendue. Caler chaque section sur un nombre entier de mesures (un reste de 0,7 s fait un trou involontaire). [ÉPROUVÉ EN MAQUETTE] (pièce 20)
9. **Le silence visuel** : un temps immobile trop long crée de la tension ; court, il se lit comme un arrêt. [ÉPROUVÉ EN MAQUETTE] (pièce 01)
10. **Rupture de forme = échelle + position + teinte ; la police n'ajoute qu'en grand** : dix polices à 12 % de hauteur = un diaporama ; en sautant de 10 à 60 % avec débord du cadre, chaque coupe devient un choc. Le sommet d'une courbe change de règle (stabilité, grande taille), il n'ajoute pas du chaos au chaos. [ÉPROUVÉ EN MAQUETTE] (pièce 09, principe Noé / Tom Kan)
11. **Explicatif : un objet qui change de rôle montre des rapports, des pictogrammes montrent des noms.** L'argument (proportion, cause) est dans la transformation ; garder la trace du départ (le trou). Caler chaque transformation sur le **début** de la phrase qui la nomme (mesuré sur la voix définitive). Mouvement de repos sous le seuil de l'événement. [ÉPROUVÉ EN MAQUETTE] (pièce 21) Vu sur EGO « Bibliothèque-Univers » (13:17-14:16) [VU SUR IMAGES] : le chiffre de Vigenère expliqué en une minute presque sans coupe par une seule chaîne de lettres lumineuses qui devient nombres, soustraction, puis le mot MAMA (`analyses/youtube/ego-bibliotheque-univers.md`).
12. **Un changement d'échelle a besoin d'un témoin** : un repère de taille connue reste dans le cadre, sinon l'infini devient une texture. [ÉPROUVÉ EN MAQUETTE] (pièce 22)
13. **Caméra qui monte : la visée monte avec** : un travelling avant montant sur cible fixe décapite la figure ; animer la cible avec la caméra (même easing). Vaut pour AE (point d'intérêt) et pour une grue réelle. [ÉPROUVÉ EN MAQUETTE] (pièce 31)
14. **L'habillage tiré du sujet, pas plaqué** (vu dans trois clips) : ouvrir en **construisant la première image** (cadre qui grandit dans le noir, Booba « 6G » ; mosaïque de carreaux qui se remplit en 15 s, Yvnnis « Gare du Nord ») ; reprendre le motif à la fin (les carreaux, puis le plan de métro dessiné sur l'artiste et la voie suivie en vue satellite jusqu'à la gare) ; ou faire de l'interface le dispositif du film (HOUDI « Belle chanson » : écran « Select player », « Stage clear », générique en police d'arcade révèlent que le clip était un niveau de jeu). Dans les trois, aucun carton décoratif : le graphisme dit comment lire le film. [VU SUR IMAGES] (`analyses/clips/booba-6g.md`, `yvnnis-gare-du-nord.md`, `houdi-belle-chanson.md`)
15. **Le texte qui s'écrit au rythme de la voix tient un plan long** (vu dans trois documentaires YouTube) : citation qui apparaît ligne à ligne sur du papier, source en bas (« Les Jeux Tiger », 23 à 29 s) ; appel reconstitué en relevé d'écoute, texte à la machine et forme d'onde (« CIA », 27 s) ; **une police et une couleur par témoin anonyme**, mot en cours coloré, avec un mannequin éclairé pour avatar (« Créer YggTorrent », plans de 24 à 45 s, fin de 3 min en voix seules sur noir). La typographie y fait le portrait de la voix : le mot à mot n'est pas un effet de rétention mais une identité. [VU SUR IMAGES] (`analyses/youtube/`)

## La trace d'un mouvement (écho, chronophotographie)
- **L'écart de temps entre les traces décide de la lecture** : continu = vitesse (flou) ; quelques images = écho (durée, mémoire, corps multiplié) ; régulier et net = analyse. Exige un fond qui disparaît et un sujet en contre-jour. [SOURCÉ] (McLaren, *Pas de deux*)
- **Superposée** dans un cadre = une trajectoire (fond noir) ; **juxtaposée** (grille) = des phases (repère fixe). [SOURCÉ] (Marey / Muybridge)
- Écart entre poses, en largeurs du membre qui bouge : < 0,3 traînée ; 1 trajectoire ; ≥ 2 écho ; > 4 plusieurs personnes ; **0,5 est une zone morte** ; et **le dégradé de mémoire fait l'identité plus que l'écart** (poses qui pâlissent = un seul corps ; égales = une file de personnes). Écart en images = têtes visées × largeur de tête (px) ÷ vitesse (px/image). [ÉPROUVÉ EN MAQUETTE] (`labo/echo/`, image fixe, et pièce 20)

## Clichés à refuser (sauf parti pris assumé)
- Le zoom lent continu sur un carton centré ; particules et glow « pour faire riche ».
- Le texte qui tape lettre à lettre avec une machine à écrire (sauf si l'écriture est le sujet).
- Le whoosh entre chaque plan (sauf kinetic social : `montage-kinetic-editing`).
- La typo cinétique qui fait danser chaque mot : on ne lit plus rien.

## Questions avant d'animer
1. Quelle est la phrase d'intention ? 2. Quel est le signe unique ? 3. Quel paramètre porte le sens ? 4. Quelle matière (poids, élasticité) ? 5. Où sont les temps immobiles ? 6. Qu'est-ce que j'enlève ?

Détails des pièces : `atelier/01-respiration/`, `atelier/09-generique-equipe/CRITIQUE.md`, `atelier/20-la-lumiere-ecrit/`, `atelier/21-objet-qui-change-de-role/`, `atelier/22-a-la-maniere-d-ego/`, `atelier/31-meme-escalier/`.
