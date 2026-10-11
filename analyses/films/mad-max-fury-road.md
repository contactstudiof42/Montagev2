# Mad Max: Fury Road (George Miller, 2015) — montage Margaret Sixel

_Fiche ouverte le 2026-10-11 (phase 2, sessions 2-3, film vague 1 n°5). **État : terminée** (passe globale, 7 séquences, recomptage des pics, test du centrage). Source : 1080p SDR, VO anglaise (piste audio 1), sous-titres anglais texte (`videos/_travail/madmax/sous-titres.srt`). Planches commitées : `madmax-courbes.png`, `madmax-couleur.png`, puis une image par plan avec le volume momentané en dessous : `madmax-ouverture.png` (0:02:30-0:05:40), `madmax-tempete.png` (0:27:00-0:29:50), `madmax-combat.png` (0:36:00-0:39:10), `madmax-canyon.png` (0:53:00-0:55:30), `madmax-genoux.png` (1:19:20-1:22:00), `madmax-final.png` (1:38:00-1:40:30), `madmax-nux.png` (1:45:00-1:47:00)._

**Lu avant l'analyse** : `montage-rythme` (respiration, climax), `montage-kinetic-editing` (« respiration obligatoire », le « mur » de densité constante), `montage-grammaire` (lisibilité d'un alterné), grille de `montage-regard` (lisibilité). **Aucune fiche de phase 1** sur ce film, sur Miller ni sur Sixel dans `culture/`. Ce que je savais en arrivant, sans source ici : un film d'action « lisible malgré la vitesse », souvent attribué au cadrage centré et aux images accélérées [NON VÉRIFIÉ].

## Intention
Une seule poursuite aller-retour, presque sans dialogue : faire sentir la fuite comme une respiration (on court, on souffle, on revient) et garder le spectateur orienté à tout moment malgré la vitesse. [DÉDUIT]

## Forme [mesures automatiques, corrigées à l'œil]
- **2 h 00 (dont le générique de fin à partir de 1:53), au moins 2 371 plans, ASL 3,0 s, médiane 2,0 s**. Histogramme : < 1 s : 416 · 1-2 s : 791 · 2-4 s : 690 · 4-8 s : 359 · 8-15 s : 87 · ≥ 15 s : 28. C'est le film le plus découpé de la vague (ASL : Whiplash 4,2 s, Interstellar 4,4, Dîner de cons 4,6, Joker 6,6).
- **Le nombre de plans est faux dans les deux sens** :
  - **trop haut dans la tempête** (0:27-0:30) : les éclairs sont comptés comme des coupes. Recompté avec `verif_plan.py` : **77 coupes en 170 s au lieu de 146**, soit environ 27 coupes/min, pas 52. Vu à 4 images/s (0:27:26-0:27:34) : un plan de Furiosa dans la cabine (5 s) compté comme 4 plans, un plan de War Boy sur sa perche compté comme 6. [VU SUR IMAGES]
  - **trop bas dans l'action sombre et accélérée** : à 0:04:52, un « plan » de 15,7 s contient au moins 8 plans (combat, War Boys dans l'eau bleue, tunnel, la fillette) ; ni PySceneDetect ni `verif_plan.py` (1 coupe trouvée) ne les voient. À 0:02:25, un « plan » de 31,9 s en contient au moins deux, avec un raccord probable dans le nuage de poussière. [VU SUR IMAGES]
  - Calibration hors de ces cas : canyon 79 coupes (détecteur) contre 75 (`verif_plan`), final 88 contre 82. Les deux comptages s'accordent à 5-7 % près en plein jour.
- **La densité monte et retombe en vagues**, beaucoup plus que dans les quatre autres films de la vague. Minutes à 30 coupes/min ou plus : 0:22-0:24, 0:26-0:29 (tempête, gonflée), 0:33-0:36 (combat), 0:51-0:58 (canyon, motos), et **1:32-1:38, sept minutes d'affilée (le final)**. Creux : 0:30-0:32 (6 à 11 coupes/min, l'après-tempête), **1:16-1:27 (4 à 16 coupes/min, la plupart sous 10 : les Vuvalini, la nuit, la décision de revenir)**. **Écart d'un facteur 10 entre creux et crêtes** ; Interstellar ne varie que de 12 à 18.
- **Le sommet n'est pas la minute la plus rapide, c'est le plateau le plus long.** Une fois la tempête corrigée, les crêtes se valent à peu près (canyon environ 31/min, final environ 34/min mesuré par `verif_plan`) ; ce qui distingue le final, c'est la durée (7 min au-dessus de 30). [mesuré]
- **Son** : -16 LUFS intégrés (le film le plus fort de la vague). Pendant les poursuites, le volume momentané forme un plateau presque plat (vers -11 LUFS) ; il ne redescend que dans les creux.
- **Couleur** : jour orange saturé, **nuit bleue** (1:04-1:14 le marais et les corbeaux, 1:22-1:25 la nuit des graines), un pic de rouge saturé dans la tempête, et un générique désaturé. Les minutes de nuit coupent un peu moins (15,6 coupes/min contre 21,8 de jour), mais le creux le plus profond (1:16-1:27) commence en plein jour : la couleur et le rythme ne se calquent pas strictement. [mesuré]

## Séquences analysées

### La fuite dans la Citadelle (0:02:30-0:05:40) [VU SUR IMAGES, `madmax-ouverture.png`]
- 62 plans (minimum). Les **hallucinations de Max** (la fillette, les morts) arrivent en flashs d'une demi-seconde à une seconde, **en bleu-vert froid**, au milieu des tunnels orange : la couleur dit « dans sa tête » sans un mot. Un visage en rouge saturé (0:05:14) pour « You promised to help us! ».
- Le sable qui engloutit la caméra cache probablement une coupe (0:02:55) : la poussière sert de volet.

### La tempête (0:27:00-0:29:50) [VU SUR IMAGES, `madmax-tempete.png`]
- Environ 77 vraies coupes en 170 s. **Deux couleurs alternent** : l'extérieur rouge-orange (feu, sable) et l'intérieur des voitures en gris-blanc froid (Nux, ses lunettes, les éclairs). Comme dans Interstellar, chaque ligne a sa matière, ce qui rend lisibles des plans d'une demi-seconde.
- Le visage de Nux revient toutes les 5 à 10 coupes, **au centre du cadre** (« Oh, what a day! What a lovely day! » 0:28:45-0:28:47) : c'est le point d'ancrage dans le chaos.
- Puis le creux de 0:30-0:32 (6 à 11 coupes/min) : l'après est tenu, comme dans Joker et Whiplash.

### Le combat Max / Furiosa (0:36:00-0:39:10) [VU SUR IMAGES, `madmax-combat.png`]
- 87 plans. Le combat (0:36:00-0:37:30) coupe toutes les 0,5 à 3 s, mais **un plan large qui montre tout le monde revient régulièrement** (0:36:35, 0:36:48, 0:36:58, 0:37:00, 0:37:11, 0:37:14) : six fois en 40 s on revoit la géographie (Max, Furiosa, les épouses, le camion).
- Dès que la bagarre s'arrête (l'arrivée de Nux, la négociation), les plans passent à 4-7 s, puis 12,2 s sur le face-à-face (0:38:35). Le volume tombe en même temps.

### Le canyon et les motos (0:53:00-0:55:30) [VU SUR IMAGES, `madmax-canyon.png`]
- 80 plans, 1,9 s en moyenne. Alternance stricte : plan large du canyon (où sont les véhicules) / intérieur de la cabine (qui fait quoi). Les explosions et les motos qui sautent sont au centre du cadre.

### Furiosa apprend que la Terre verte n'existe plus (1:19:20-1:22:00) [VU SUR IMAGES, `madmax-genoux.png`]
- 22 plans, 7,3 s en moyenne, au fond du plus grand creux du film. La nouvelle arrive **dans un plan en mouvement de 35,5 s** (1:20:42, vérifié continu : `verif_plan` et tuile toutes les 2 s) qui tourne autour du groupe puis se resserre sur le visage de Furiosa. Avant, 26,7 s (vérifié), après, un plan de groupe de 16,7 s.
- La réaction n'est pas un gros plan : Furiosa s'éloigne seule dans les dunes (14,4 s) puis tombe à genoux **en plan très large** (8,6 s). Le moment le plus intime du film est filmé de loin. La musique monte sur ces deux plans (volume momentané en hausse continue).

### Le final (1:38:00-1:40:30) [VU SUR IMAGES, `madmax-final.png`]
- 89 plans (environ 82 réels), 1,7 s en moyenne, sur un plateau de volume presque plat. Mêmes outils que le canyon : plans larges de géographie, cabines, visages au centre. Quelques plans tenus dans la masse (8,3 s à 1:38:58, 4,8 s à 1:39:23).

### Le sacrifice de Nux (1:45:00-1:47:00) [VU SUR IMAGES, `madmax-nux.png`]
- 37 plans. Au milieu de la poursuite, **« Witness me » est tenu 7,1 s** (1:46:05) sur Nux, puis l'éboulement du canyon en plan large de 9,1 s, puis 13 s sur l'épave.
- **Puis environ 9 s de noir complet** (vers 1:46:58-1:47:07), pendant que le son retombe de -11 à -36 LUFS en 8 s (un decrescendo, pas une coupe sèche). On rouvre sur un soleil bas et le camion de Joe qui passe. [mesuré, vu à 1 image/s]

## Le sujet au centre du cadre [VU SUR IMAGES, échantillon]
- Hypothèse souvent citée : Miller cadre au centre pour que l'œil n'ait pas à chercher d'un plan court à l'autre [NON VÉRIFIÉ pour la source].
- **Mesure automatique ratée** : la saillance « spectral residual » (`labo/outils/centrage.py`) ne trouve le sujet qu'environ une fois sur trois, et donne le même résultat pour les cinq films. Chiffres inutilisables.
- **Comptage à l'œil** (`labo/outils/echantillon_tiers.py`, 24 images de milieu de plan tirées au hasard, plans > 1,5 s, graine 1) : sujet principal dans le tiers central pour **environ 20 images sur 24 dans Mad Max**, environ 12 sur 24 dans Interstellar, environ 8 sur 24 dans Joker (Arthur souvent au bord du cadre, avec du vide à côté). Jugé par moi, sur un petit échantillon : l'écart est net, le chiffre exact non.

## Confirme, contredit, complète
- **Contredit en partie** la leçon n° 1 de la vague (« le climax ne coupe pas plus vite que le reste ») : dans un film de poursuite, le final est bien la passe la plus dense, mais à peine (34 contre 31 coupes/min au canyon). **Ce qui le distingue, c'est sa durée** : sept minutes de crête d'affilée. À ajouter à `montage-rythme` : le climax d'un film d'action se marque par la longueur du plateau, pas par la vitesse.
- **Confirme à l'échelle d'un long métrage** la règle de `montage-kinetic-editing` (« respiration obligatoire », pas de « mur » de densité) : les vagues de Mad Max vont de 4 à 40 coupes/min. Le film le plus rapide de la vague est aussi celui qui respire le plus.
- **Confirme** `montage-grammaire` (montage alterné, Interstellar) : chaque ligne a sa matière (intérieur froid, extérieur rouge dans la tempête ; visions bleu-vert, Citadelle orange), ce qui rend lisible un plan d'une demi-seconde.
- **Complète** `montage-regard` (lisibilité) : avec des plans de 1 à 2 s, la lisibilité tient à trois choses vues ici : le sujet au centre, un plan de géographie qui revient toutes les 5 à 10 coupes, une couleur par lieu.
- **Confirme** « l'après est tenu » et « le silence après le plus fort » (Joker, Interstellar) : le creux de 0:30 après la tempête, les plans qui s'allongent après le combat, et 9 s de noir avec decrescendo après le sacrifice de Nux.
- **Confirme** « on ne coupe pas dans la preuve » sous une autre forme : la nouvelle la plus dure du film (la Terre verte n'existe plus) est un plan de 35,5 s.
- **Nouveau** : **le moment le plus intime filmé le plus loin** (Furiosa à genoux, plan très large). Le gros plan aurait été attendu ; la distance laisse le spectateur seul avec elle.
- Méthode : **les éclairs inventent des coupes, l'action accélérée dans le sombre en cache** ; les deux erreurs peuvent coexister dans le même film (inscrit dans `PROMPT-PHASE-2.md`).

## Principes transférables
1. **Respirer en vagues** : un montage très rapide tient sur la durée s'il retombe franchement (facteur 5 à 10 entre creux et crêtes), pas s'il ralentit un peu.
2. **Le climax d'une action se marque par la durée de la crête**, pas par une vitesse de coupe supérieure.
3. **Plans très courts = sujet au centre** : l'œil n'a pas à chercher. Un cadrage décentré (Joker) va avec des plans tenus.
4. **Rendre la géographie toutes les 5 à 10 coupes** : un plan large où l'on voit tout le monde, même au milieu d'une bagarre.
5. **Une couleur par monde** (cabine froide / extérieur rouge ; visions bleu-vert) pour qu'une demi-seconde suffise.
6. **Le plus intime de loin** ; **le plus dur en un seul plan** ; **après le plus fort, le noir et un son qui retombe**.

Pour Studio F42 (pubs et réseaux « souvent énergiques », GOUTS.md) : les principes 1, 3 et 4 s'appliquent directement à un montage kinetic de 30 à 60 s (une respiration franche, sujet centré dans le 9:16, un plan d'orientation). [DÉDUIT, à éprouver en maquette]

## Ce que Diego en a dit
Rien pour l'instant (`GOUTS.md`, `NOTES-DIEGO.md`, `RETOURS-DIEGO.md`).

## Pas fait
- Les images accélérées (undercranking) et les plans ralentis n'ont pas été mesurés (il faudrait comparer le mouvement image par image à une vitesse normale).
- Le son n'est pas écouté ; la musique (le guitariste sur son camion) n'a pas été séparée.
- Le nombre réel de plans du film (au moins 2 371 détectés ; un chiffre d'environ 2 700 circule [NON VÉRIFIÉ]).

## Doutes
- Le comptage du centrage est fait à l'œil par moi sur 24 images par film : l'ordre (Mad Max > Interstellar > Joker) est net, les chiffres sont approximatifs.
- La date du noir après Nux (vers 1:46:58) est lue sur une tuile à 1 image/s : à une seconde près.
