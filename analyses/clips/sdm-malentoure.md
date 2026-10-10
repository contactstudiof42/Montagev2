# SDM — « #Malentouré » (clip officiel)

_Analysé le 2026-10-11 (session 0 de la phase 2, test complet de la méthode). Réalisation : Maxime Ellies (générique de fin). Label : Capitol / 92i. Planche : `sdm-malentoure-planche.png`._

## Fiche technique [VU SUR IMAGES]
- 2 min 54 s (174,06 s), H.264 1920×1012 (environ 1,90:1, letterbox intégré), 25 i/s constant, BT.709 étiqueté. AAC 44,1 kHz stéréo.
- Son : **-13,3 LUFS intégrés**, true peak -0,9 dBFS, LRA 11,2 LU. C'est un master de streaming musical non normalisé. YouTube le baissera d'environ 0 à 1 dB selon sa cible (`montage-loudness-livraison`).
- Tempo détecté : 117,5 BPM (librosa). [NON VÉRIFIÉ] : sur de la drill, le vrai tempo ressenti est souvent le double ou le demi. À contrôler à l'oreille.

## Intention
Démonstration de force collective : un rappeur au centre d'une bande nombreuse, la nuit, dans une cité (claustras, escaliers, coursives). Le titre joue sur le mot : « mal entouré », alors que l'image montre un homme **très** entouré. L'ironie est portée par l'image, pas par le montage. [DÉDUIT]

## Forme
- **27 plans** détectés, et un raccord caché trouvé à l'œil (voir plus bas), soit **28 plans réels**. Plan moyen 6,4 s, médiane 3,9 s. Histogramme des durées (0-1, 1-2, 2-3, 3-5, 5-8, 8 s et plus) : 2 / 4 / 6 / 7 / 5 / 3. [VU SUR IMAGES]
- PySceneDetect (detect-adaptive) trouve 26 coupes, comme `analyse_clip.py`. Les deux outils ratent le même raccord caché.
- **Structure en trois blocs**, lisible sur la courbe du bas de la planche :
  1. 0:00-0:11 : intro calme (-22 LUFS), deux plans, puis le **titre** posé sur un couloir de claustras (0:06).
  2. **0:11-0:52 : un premier plan-séquence au Steadicam**. Contre-plongée sur la façade, puis panoramique descendant vers SDM qui rappe dans le passage, puis avancée dans la foule jusqu'à un visage barbu. Le refrain entre vers 0:13, quand la musique monte (-22 → -12 LUFS).
  3. 0:52-1:36 : un bloc **découpé**, de 15 plans de 1 à 8 s (environ 20 coupes par minute contre 1,5 dans les plans-séquences). Plongées zénithales, fumigènes rouges, la bande sur les escaliers.
  4. **1:36-2:13 : un deuxième plan-séquence** (36,8 s) avec le second rappeur (doudoune verte) : les deux en pied sur les escaliers, la caméra tourne autour d'eux, puis un **filé vers le bas** à 2:07,5 mène au gros plan du rappeur en vert.
  5. 2:13-2:48 : un deuxième bloc découpé, de 7 plans, avec la bande qui serre le rappeur au sol. Un dernier plan tenu de 12 s, en plongée sur le rappeur couché parmi les mains.
  6. 2:48 : noir, générique, noir. La musique redescend à -25 LUFS.
- **Le montage alterne la durée, pas la vitesse** : un long plan-séquence par couplet, du découpé entre les deux. La densité de coupes ne suit pas le volume, qui reste à peu près plat (-11 à -14 LUFS) de 0:15 à 2:40.

## Choix par domaine
- **Rythme** [VU SUR IMAGES] : les coupes ne tombent pas sur les temps. La concentration de phase vaut 0,13, alors que le hasard attendu est de 0,20 : les coupes ne sont pas plus alignées sur la grille que si elles tombaient au hasard. Le nombre de coupes par minute est le même avec ou sans basse (8,6 contre 9,6). Le montage est calé sur la **structure** du morceau (couplet = plan-séquence), pas sur le beat. C'est le même principe que chez Ziak, avec une autre forme (`culture/ziak-meme-pas-un-grincement.md`).
- **Cadre** : de la contre-plongée et de la plongée zénithale pour la masse (plans 4, 5, 22, 24), du plan rapproché frontal au grand-angle pour le rappeur (plans 18, 20, 21). Le grand-angle très près du visage déforme légèrement et donne de la présence.
- **Couleur** [VU SUR IMAGES] : nuit au sodium. La luminance moyenne est de 37 sur 255, et 48,5 % des pixels sont sous 30. Dominante jaune-vert sourde sur le béton, noirs denses mais pas bouchés : les visages restent lisibles grâce à une lumière d'appoint sur le rappeur. C'est exactement la réponse 8 de GOUTS.md (« visages sombres, mais un minimum de lumière sur l'info à voir »). **Une seule couleur saturée** : le rouge des fumigènes (plans 6 et 9, de 0:47 à 1:16), puis le vert de la doudoune du second rappeur, qui le détache de la bande en noir. C'est l'équivalent vestimentaire d'une « couleur méritée » (`montage-couleur-et-intention`).
- **Transitions** [VU SUR IMAGES, image par image] :
  - **0:47,6** : le Steadicam passe derrière une épaule sombre (occlusion d'environ 5 images), et quand l'image revient, on est ailleurs : sol rouge, fumigène, plan retourné. **C'est une coupe cachée par un « wipe » de corps.** Aucun des deux détecteurs ne la voit, parce que le passage au noir est progressif.
  - **2:07,5** : un filé vers le sol (environ 10 images floues) amène au gros plan. [NON VÉRIFIÉ] : est-ce un vrai mouvement continu ou une coupe cachée dans le flou ? L'image ne permet pas de trancher. Les deux sont vraisemblables au Steadicam.
  - Fin : une coupe au noir franche, puis le générique.
- **Typographie** : le titre « MAL ENTOURÉ » est en capitales grasses à chasse étroite, avec un grand « O » cerclé qui sépare MAL / ENT et OURÉ / SDM. Le mot est découpé par un cercle : il est littéralement **entouré**. Il est posé petit, au centre, dans un couloir. Le générique de fin réemploie le même bloc-titre et un bandeau blanc « Réalisé par ».
- **Son** : le mixage du morceau est plat et fort. Pas de sound design ajouté visible sur la courbe, à part l'intro calme et la queue. Le clip ne coupe pas la musique pour un effet. [VU SUR LA COURBE ; écoute non faite]
- **Effets** : aucun effet visible. Tout vient de la machinerie (Steadicam, et un poste « Motion control » crédité au générique) et des fumigènes, réels.
- **Paroles** (transcription Whisper, à 0:52,9 : « Je suis très mal entouré ») : à cet instant précis, l'image passe d'un gros plan de la bande compacte au plan zénithal sur la foule en contre-plongée (plan 4, 0:52). **L'image contredit la parole** : c'est le procédé décrit dans `culture/clips-illustrer-ou-contredire-paroles.md`. [VU SUR IMAGES ; transcription approximative, à vérifier à l'oreille]

## Ce que ça confirme, contredit ou complète
- **Confirme** `montage-formats` (« une idée de forme forte, plan-séquence par exemple, vaut mieux qu'un récit ») : ici, la forme, c'est **un plan-séquence par couplet**. [VU SUR IMAGES]
- **Confirme** que, dans le rap français, couper sur la structure plutôt que sur le beat n'est pas propre à Ziak. C'est un deuxième cas mesuré.
- **Complète** `montage-grammaire` : la coupe cachée par occlusion d'un corps au premier plan est le cache-coupe naturel du plan-séquence au Steadicam. Elle se prépare au tournage : finir le plan A et commencer le plan B sur un corps sombre qui traverse.
- **Contredit ma méthode, pas un skill** : un détecteur de coupes image à image (le mien et PySceneDetect) **rate les coupes cachées par occlusion ou par filé**. Pour toute vidéo à plans longs, il faut regarder 1 image toutes les 2 à 3 s dans les plans de plus de 15 s.

## Principes transférables
1. **Alterner la durée plutôt que la vitesse** : de longs plans-séquences pour les couplets, du découpé serré entre eux. L'énergie vient du contraste entre les deux régimes, pas d'une densité de coupes uniforme.
2. **Une couleur saturée et une seule par personnage ou par moment**, sur une nuit désaturée : le rouge des fumigènes pour la bande, le vert pour l'invité.
3. **Le titre comme dessin du mot** (« entouré » dans un cercle) : une idée typographique qui suffit, sans animation.
4. **Laisser l'image contredire le refrain** : il dit qu'il est mal entouré, on voit cent personnes.
5. Au tournage d'un plan-séquence : **prévoir les passages d'occlusion** où l'on pourra couper.

## Ce que Diego en a dit
Rien pour l'instant : ni NOTES-DIEGO.md ni RETOURS-DIEGO.md ne parlent de ce clip.

## Doutes
- Le vrai tempo du morceau et le calage des coupes sur les mesures (et pas seulement sur les temps) ne sont pas mesurés. À faire avec les temps forts de librosa par mesure de 4 temps.
- Le second rappeur (doudoune verte) n'est pas identifié. [NON VÉRIFIÉ]
