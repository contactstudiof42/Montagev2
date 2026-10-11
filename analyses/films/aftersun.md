# Aftersun (Charlotte Wells, 2022 ; montage Blair McClendon)

_Fiche ouverte le 2026-10-11 (phase 2, session 9, film vague 3 n°3). **État : passe globale + 6 séquences (ouverture, magasin de tapis, karaoké, rave de la minute 75, « Under Pressure », dernier plan) + 14 plans longs vérifiés** ; restent le plongeon et la surface de l'eau, le miroir nuit / jour, le balcon (voir « À faire »). Source : 1080p (SDR), VO anglaise, sous-titres anglais complets. Travail dans `videos/_travail/aftersun/`. Planches commitées : `aftersun-courbes.png`, `aftersun-ouverture.png` (0:00-5:30), `aftersun-karaoke.png` (1:01:50-1:04:10), `aftersun-rave-75.png` (1:13:40-1:16:30), `aftersun-under-pressure.png` (1:27:50-1:32:45), `aftersun-dernier-plan.png` (tuile, 1 image / 3 s sur 1:32:40-1:35:20), `aftersun-tapis-fausses-coupes.png` (tuile à 6 images/s, leçon de méthode). Fiche de phase 1 confrontée : `culture/aftersun-wells-mcclendon.md` (écrite sans voir le film)._

Skills relus : `montage-rythme` (respiration, plan long), `montage-grammaire` (ellipse, raccord par le son), `montage-son-et-emotion` (musique avec ou contre l'image, silence), `montage-couleur-et-intention` (une texture par régime), grille de `montage-regard` ; fiches `culture/aftersun-wells-mcclendon.md` et `culture/reaction-tenue-drame.md`.

## Intention
Faire vivre au spectateur ce que vit Sophie adulte : rassembler des fragments d'un été avec son père, et comprendre trop tard ce qu'elle ne voyait pas à 11 ans. Le deuil n'est jamais dit.

## Forme [mesuré]
- **1 h 41 dont environ 87 s de logos au début et 6 min 20 de générique (dès 1:35:21)**. PySceneDetect donne 553 plans, ASL 11,0 s, médiane 4,3 s : **chiffres faux**, gonflés par trois sources de fausses coupes (voir « Leçons de méthode »).
- **Film seul (1:27-1:35:21), fausses coupes du magasin de tapis retirées : au moins 458 plans, ASL 12,3 s, médiane 5,5 s.** Hors des quatre passages de rave aux stroboscopes (environ 140 s en tout, où le compte est indécidable) : **361 plans, médiane 7,5 s, et les 99 plans de 15 s ou plus couvrent 72 % de la durée.** C'est le film le plus lent mesuré en phase 2 (Spotlight : médiane 4,1 s ; Joker : 4,5 s). Les scènes de nuit peuvent cacher des coupes : comptes minimaux.
- **Densité presque plate (3 à 8 coupes/min) avec trois crêtes, et ce sont les trois raves** (minutes 2-3, 75, 90-91). Les autres crêtes de la courbe brute (minutes 44-47, 100-101) sont fausses.
- **-26,4 LUFS intégrés, le film le plus calme mesuré** (Dîner de cons -24,8, Spotlight -20,3). Les deux minutes les plus fortes sont **les deux chansons** : le karaoké (minutes 62-63, -21 LUFS) et « Under Pressure » (minutes 90-91, -21,6 / -22,0). La minute la plus faible du film est la 74, juste avant la rave de la minute 75.

## Séquences

### L'ouverture : la cassette rembobinée (1:27-5:30) [VU SUR IMAGES, `aftersun-ouverture.png` ; tuile éclaircie à 1 image/s]
- Premier plan du film : **une image MiniDV tenue 61,4 s** (vrai plan, `verif_plan.py` : 0 coupe), Sophie filme son père à la fenêtre de l'hôtel, on entend leur échange.
- Puis 2:29-3:31 : des éclats de noir de la rave (0,5 à 2 s), et **la cassette qui se rembobine** : on reconnaît en accéléré, avec des artefacts de compression (macroblocs), **l'aéroport et Sophie qui fait au revoir** (c'est la dernière image d'archive du film, voir le dernier plan), puis des images de vacances (parapente, Sophie aux lunettes rouges). Un gros plan de Calum dans le noir (3:29), puis le car de l'aller (Sophie, 2,5 s ; l'animatrice, 11,0 s ; Sophie endormie, **46,7 s**).
- **Le film s'ouvre sur sa fin, déjà montrée et illisible.** L'archive est un objet qu'on manipule (rembobiner, accélérer), pas un flash-back. Le volume monte de -49 à -18 LUFS momentané entre 2:20 et 2:47 : la rave est entendue avant d'être vue.

### Le magasin de tapis (43:17-47:36) [VU SUR IMAGES ; `verif_plan.py` + tuile à 6 images/s, `aftersun-tapis-fausses-coupes.png`]
- Calum achète un tapis trop cher pour lui. **Plans tenus et fixes : 22,3 s, 50,1 s, 9,7 s puis environ 9,7 et 9,3 s** sur Sophie assise au milieu des tapis, puis la vente (12,9 s, puis environ 49 s jusqu'à 47:18 avec deux coupes).
- Ce passage avait été pris pour les stroboscopes de la rave en session 8 : **faux**. Ce sont des plans fixes, sombres, très saturés en rouge, où PySceneDetect déclenche une « coupe » toutes les 0,5 s exactement (environ 60 fausses coupes) ; `verif_plan.py` y trouve 3 coupes en 23 s et 2 en 56 s, la tuile n'en montre aucune autre.

### Le karaoké, « Losing My Religion » (1:02:17-1:04:20) [VU SUR IMAGES, `aftersun-karaoke.png`]
- Calum refuse de chanter avec elle ; Sophie chante seule, faux. **Toute la chanson (environ 1 min 50) en cinq plans** : Sophie en gros plan 35,9 s, **Calum dans le public 11,7 s** (le seul contrechamp), Sophie au large 12,8 s, l'écran des paroles 7,3 s, Sophie au large **43,7 s**. Puis Calum de dos (12,9 s, « Big applause for Sophie »).
- **La gêne est tenue sur elle, pas montée** : un seul contrechamp sur lui, et la durée fait le reste. C'est la minute la plus forte du film (-21 LUFS) : le volume du morceau sert l'embarras, pas la fête.

### La rave de la minute 75 (1:14:17-1:15:20) [VU SUR IMAGES, `aftersun-rave-75.png`]
- Après Sophie qui rentre seule la nuit (couloir 27,2 s, chambre 44,6 s, la minute la plus calme du film, -50 LUFS), **18 s de rave** : Calum en chemise rayée, la tête renversée, entre rire et cri, en éclats de 0,6 à 1,7 s séparés de noir. Volume de -52 à -30 LUFS momentané en une seconde. Puis on revient au matin en **un plan de 64,8 s** (vrai plan).
- La rave n'est pas un lieu des vacances : c'est **l'espace de Sophie adulte**, et ici c'est Calum qu'on y voit seul. Elle coupe la nuit la plus inquiète du séjour.

### « Under Pressure » : la dernière danse et la rave alternées (1:29:46-1:32:30) [VU SUR IMAGES, `aftersun-under-pressure.png` ; LUFS mesuré, pas écouté]
- Le dernier soir, Calum invite Sophie à danser ; elle refuse (« I never, ever dance »), il danse seul (18,6 s), puis la scène bascule.
- **1:30:09-1:32:26 : 2 min 17 d'alternance** entre la rave (noir, éclats stroboscopiques de 0,5 à 2 s, Sophie adulte qui cherche son père, l'attrape, le perd) et la piste de danse en Turquie, en plans plus longs (10,0 s, 20,0 s, 10,3 s : Sophie en veste adidas qui serre son père ; 5,7 s, 3,6 s, 12,6 s sur Calum en chemise blanche sous les guirlandes). Les deux étreintes se répondent : celle de l'enfant (le souvenir, en plans tenus) et celle de l'adulte (l'espace mental, en éclats).
- **Le son** : médiane -21 LUFS momentané sur la séquence, contre -42 pendant le dîner qui précède (+21 LU), le passage le plus long au plus fort du film. À 1:32:27, la dernière étreinte est coupée par **12 s de noir**, dont **8 s de silence quasi total** (-66 à -68 LUFS momentané de 1:32:31 à 1:32:38). Puis la voix de la cassette (« Bye-bye. I love you ») sur un filé MiniDV de l'aéroport.
- Je n'ai pas pu vérifier à l'oreille si la chanson est désossée (voix isolées), comme l'écrit la fiche de phase 1 : `[NON VÉRIFIÉ]`, reste à écouter.

### Le dernier plan, 160 s sans coupe (1:32:40-1:35:20) [VU SUR IMAGES, `aftersun-dernier-plan.png` ; `verif_plan.py` : 0 coupe ; tuile à 1,5 image/s sur la transition]
- **Un seul plan** : l'archive MiniDV de l'aéroport (Sophie fait au revoir, « I love you »), puis la caméra **panoramique vers la droite et l'image de la cassette glisse hors du cadre** : elle était projetée (ou à l'écran) dans l'appartement sombre de Sophie adulte. Le panoramique traverse l'appartement (bibliothèque, vélo), la lumière du jour monte (même procédé que le miroir nuit / jour relevé par Reverse Shot), trouve Sophie adulte, puis un mur pâle, puis **le couloir blanc de l'aéroport où Calum tient le caméscope** : c'est lui qui filmait. Il le baisse, se retourne, s'éloigne vers les portes du fond.
- **L'après tenu : environ 16 s de couloir vide** (1:35:05-1:35:21) une fois les portes refermées, puis le générique. Le volume y pulse régulièrement (de -50 à -23 LUFS toutes les 4 s environ) : peut-être la rave derrière les portes, `[mesuré, pas écouté]`.
- **Trois temps (archive, présent, souvenir-espace mental) dans un seul mouvement de caméra**, sans coupe. La coupe aurait séparé les époques ; le panoramique les met dans la même pièce.

## Couleur [mesuré sur échantillons à 1 image/s, 160×90 ; le look fin n'est pas jugeable sur le proxy]
- Le MiniDV est neutre à chaud (rouge - bleu +1 à l'ouverture, +12 à l'aéroport), noirs relevés et hautes lumières écrasées (98e centile 154-180 / 255).
- **Le présent de Sophie adulte est le plus froid** : appartement -17, couloir de la fin -25 ; les vacances en 35 mm vont de -14 (nuits) à +10 (dîner aux guirlandes), le jour autour de -3.
- La fiche de phase 1 parlait de « trois régimes d'image » : il y en a quatre à l'écran (35 mm des vacances, MiniDV, rave noire aux stroboscopes, présent froid de l'appartement), et le présent est surtout visible au dernier plan.

## Confrontation avec la fiche de phase 1 (`culture/aftersun-wells-mcclendon.md`)
- **Tient** : trois régimes d'image (complété : un quatrième, le présent froid) ; la rave aux stroboscopes « faite surtout d'images noires » (VU : sur 32 images à 4 i/s, 2 seulement sont lisibles) ; « Under Pressure » alterné avec la danse du dernier soir ; la fin à l'aéroport où l'on comprend que Calum filmait, puis le couloir et les portes ; les plans de respiration longs (médiane hors rave 7,5 s, au-dessus des 5-7 s chronométrés par McClendon et Wells).
- **Complété** : « panoramique circulaire » (Slate) = un seul plan de 160 s qui passe par l'image projetée de la cassette ; l'ouverture montre déjà la fin, en rembobinage ; la rave apparaît quatre fois (ouverture, minute 75, Under Pressure, derrière les portes), pas seulement au final.
- **Non vérifié** : la version désossée de « Under Pressure » (à écouter), le téléphone qui déborde sur la scène des lacets, le plan sur la surface de l'eau (à regarder, minute 30 environ, « A proper dive, Soph » à 30:02).
- Aucune affirmation de la fiche n'est contredite par les images vues. C'est la première fiche de phase 1 sans erreur relevée, peut-être parce qu'elle ne donnait aucun chiffre.

## Ce qui confirme, contredit ou complète mes skills
- **Confirme `montage-rythme`, « plans longs réservés à ce qui compte »** (sixième film) **mais le renverse en partie** : ici le plan long est la norme (72 % de la durée) et **ce qui est réservé, ce sont les plans courts** : les seules rafales du film sont les raves. Même logique que *The Social Network* (la norme rompue à la fin), dans l'autre sens. [VU SUR IMAGES]
- **Confirme « le plus fort est suivi du plus grand vide »** (vague 1) : la crête sonore d'« Under Pressure » finit sur 12 s de noir dont 8 s de silence ; le dernier plan finit sur 16 s de couloir vide. [mesuré, VU SUR IMAGES]
- **Confirme `montage-couleur-et-intention`, « une matière par monde »**, version mémoire : la texture dit l'époque sans carton (MiniDV, 35 mm, noir stroboscopique, présent froid). [VU SUR IMAGES, mesuré]
- **Complète `montage-son-et-emotion`** : **les deux moments les plus forts du film sont deux chansons, et chacune est un refus** (Calum refuse de chanter, Sophie refuse de danser). Le volume ne marque pas la fête mais l'écart entre eux. [mesuré, pas écouté]
- **Nouveau pour `montage-grammaire`** : **unir des époques par un mouvement de caméra au lieu d'une coupe** (archive → présent → souvenir dans un même panoramique). Et **ouvrir sur la fin, rendue illisible** (la cassette rembobinée) : le spectateur reconnaîtra l'image au dernier plan. [VU SUR IMAGES]

## Principes transférables
1. **Dans un film tenu, la rafale est l'exception qui signale un autre monde** : si 70 % du film est en plans de plus de 15 s, une rafale de dix plans d'une demi-seconde suffit à changer d'espace mental. Pour F42 : un film de marque lent peut garder sa rafale pour un seul moment (le rêve, le souvenir, le produit en action).
2. **Mettre deux époques dans un même mouvement** (panoramique, travelling, image projetée dans le décor) plutôt que de couper : le lien devient physique.
3. **L'archive comme objet** (rembobiner, accélérer, artefacts) dit « c'est un souvenir » sans carton ni voix off.
4. **La scène la plus forte peut être une gêne tenue** : un seul contrechamp, la durée fait le reste.
5. **Finir sur le vide** : quand le personnage sort, garder le décor 10 à 20 s avant le générique.

## Ce que Diego en a dit
Rien pour l'instant (aucune note dans `NOTES-DIEGO.md`). GOUTS.md : « ma préférence perso, c'est le grain et le look film » ; *Aftersun* est l'exemple le plus net du corpus d'un grain qui a un sens (deux supports, deux temps). Rapprochement de ma part, pas de Diego.

## Leçons de méthode (reportées dans `PROMPT-PHASE-2.md`)
- **Série de « plans » de durée exactement égale (0,5 s) sur une image fixe = détecteur saturé**, pas des coupes (magasin de tapis : plans sombres très saturés en rouge ; générique déroulant à la fin). Je l'avais prise pour les stroboscopes de la rave. Avant de nommer la cause d'une rafale, regarder la planche du passage.
- **Retirer logos et générique avant toute statistique de film** : ici 87 s de logos et 6 min 20 de générique (dont une rafale de fausses coupes) déplaçaient la médiane.

## À faire
- Regarder le plongeon et la surface de l'eau (vers 30:00), le miroir nuit / jour, la scène des lacets et du téléphone.
- Vérifier le plan de nuit de Calum de dos derrière les rideaux (7:56-10:33, environ 157 s sans coupe pour `verif_plan.py` ; scène sombre : à recompter à 2-4 images/s).
- Écouter « Under Pressure » et la fin du couloir (pulsation de 4 s).
