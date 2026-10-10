# Pièce 06 « Versions » — critiques

Grille : intention servie ? lisibilité, rythme, composition, cohérence, couleur, mouvement, originalité ou cliché, justesse.

## v1 (`v1-coupes.png`, `v1-comparaison.png`, `v1-mesures.json`)
Montage : insert (20 images) + plan large f14-65, trois fois ; arpège en boucle de 72 images (= exactement une version) ; musique coupée net à la dernière chute ; 1 s de noir. 241 images, -22,1 LUFS.
- **Critère 1, même scène : tenu.** Planche de comparaison (lignes = versions, colonnes = mêmes images) : cadre identique, la tasse occupe les mêmes pixels aux images 56 et 64 dans les trois lignes. La boucle musicale qui redémarre à chaque version dit « on recommence » sans carton.
- **Critère 2, détail lisible : raté pour la secousse.** 6 mm d'amplitude sur une table qui fait ~130 px de large pour 1,2 m : **0,6 px**. Personne ne la verra ; la version 2 est donc, pour le spectateur, une simple répétition de la 1. Erreur d'échelle : j'ai choisi l'amplitude « réaliste » en mètres sans la convertir en pixels à l'écran. Leçon : **un détail se dimensionne à l'écran, pas dans la scène.**
- **L'ombre (version 3)** est lisible (bande sombre qui traverse le mur à f38, tache au sol à f30), mais elle se lit comme **une porte qui se ferme ou un objet**, pas comme quelqu'un : un pavé n'a pas d'épaules. Et la tache rectangulaire au sol, en bas à gauche, attire l'œil pour rien.
- **Composition** : la tasse fait ~15 px de large dans le plan large ; l'élément le plus fort du cadre est la bande de lumière de la fenêtre sur le mur, qui n'a aucun rôle. Le sujet est trop petit pour qu'on cherche une différence sur lui.
- **Insert** : la tasse au bord, immobile, flou de profondeur : la question est posée. Mais il est identique trois fois, ce qui est voulu (Morris), et il n'a aucune durée propre : 0,8 s, c'est court pour une question.
- **Bug** : après l'impact (non montré) la tasse finit à moitié dans le sol ; corrigé par `repos_sol` pour la v2.
- Bilan : la structure fonctionne, mais l'exercice échoue sur son point central (on ne peut pas douter d'un détail qu'on ne voit pas).

## v2 (paramètres `v2-params.json`, montage `v2-edl.json`)
Corrections : focale 38 → 55 mm (la tasse ~45 px, la fenêtre sort du cadre), secousse 6 → 25 mm sur 11 images **et un choc sourd** au son (version 2 seulement : le détail changé passe aussi par l'oreille), silhouette avec épaules et tête, pose de repos corrigée.
Résultat (`v2-coupes.png`, `v2-comparaison.png`, `v2-mesures.json`, 241 images, -21,9 LUFS) :
- **Secousse : maintenant mesurable.** Écart maximal entre « seule » et « tremble » aux images 36-46 : 193-201 niveaux sur 255 (les arêtes de la table et de la tasse se déplacent de plusieurs pixels), qui décroît à 110 avec l'amortissement. Sur une planche d'images fixes, elle reste peu visible : c'est un détail **de mouvement**, et le choc sourd au son la rend perceptible même à qui regarde ailleurs. Critère 2 tenu pour la version 2, à confirmer à l'œil en phase 2 (je ne vois pas la vidéo).
- **Ombre : toujours ambiguë, et peut-être tant mieux.** La silhouette à épaules et tête projette une bande sombre dont la tête sort du cadre : on lit « quelque chose est passé devant la fenêtre », pas encore « quelqu'un ». Pour l'intention (le doute), c'est presque juste : une ombre trop humaine trancherait (cf. examen n°4, même problème). Je la garde, mais je note le risque inverse : qu'on n'y voie qu'une variation de lumière.
- **Composition** : en 55 mm, la tasse fait ~45 px et la fenêtre sort du cadre ; l'image devient plus plate (un mur blanc uniforme). La chute sort du cadre par le bas à l'image 64 : on ne voit jamais l'impact, ce qui sert l'intention (le verdict n'est pas montré) ; c'est un accident à garder.
- **Ce qui manque encore** : la version 3 doit changer le sens des deux premières (critère 3). Rien ne le garantit aujourd'hui : l'ombre arrive 20 images avant la chute, on peut la croire sans rapport. Piste v3 : faire passer l'ombre **juste avant** la bascule (f44-49) et, dans la version 1, glisser une variation de lumière minuscule au même moment (la relecture devient possible : « était-ce déjà là ? »).
- Note d'étape : structure et lisibilité acquises ; le doute n'est pas encore fabriqué.

## v3 (`v3-comparaison.png` aux images 38-52, `v3-coupes.png`, paramètres `v3-params-*.json`)
Corrections : l'ombre passe aux images 38-50 et quitte le cadre **au moment où la tasse commence à basculer** (image 50) ; dans la version 1, la fenêtre baisse de 15 % pendant 3 images (45-47), soit une luminance moyenne de 189 → 183 (-3 %), puis revient. La version 2 est reprise de la v2.
- **Causalité suggérée sans être montrée** : sur la planche, l'ombre (lignes 3, images 46-48) précède immédiatement la bascule ; on lit « quelqu'un passe, la tasse tombe ». C'est le montage de la coïncidence qui accuse, exactement le mécanisme de Morris, et le spectateur le fabrique lui-même.
- **L'indice de la version 1** est à la limite du visible (-3 % sur 3 images) : sur la planche, la vignette de l'image 46 est à peine plus sombre. Bon dosage pour une relecture (« était-ce déjà là ? »), mais je ne peux pas savoir si un spectateur le remarque au deuxième visionnage : c'est le premier test à faire avec un humain. S'il passe inaperçu, monter à -6 % plutôt que l'allonger (une durée plus longue en ferait un événement).
- **Critère 3** (la 3e version change le sens des deux premières) : plausible sur le papier, pas vérifiable sans spectateur. Critères 1, 2 et 4 tenus.
- Reste : la tasse et la pièce sont nues (rendu « maquette ») ; une version avec un vrai décor (traces de vie, une deuxième tasse ?) dirait qui vit là. Et l'insert pourrait varier d'une version à l'autre de façon imperceptible, comme chez Morris où l'objet revient chargé d'un sens nouveau.
- **Version de référence : v3.**
