# Pièce 08 « Souvenir » — critiques successives

Grille : intention servie ? lisibilité, rythme, composition, cohérence, couleur, mouvement, originalité ou cliché, justesse.
Matériau : plateau Blender de la pièce 06 (créé par moi, aucun média tiers). Rendus non conservés (`atelier/rendus/08/`, relancer `scene.py` avec `p-*.json` ; les plans du présent sont immobiles : une image suffit).

## v1 — trois montages du même matériau (`v1-retard-planche.png`, `v1-controle-planche.png`, `v1-explicatif-planche.png`)
- **Contrôle (passé propre, 16:9)** : la tasse et la lumière d'été distinguent les deux plans, mais on lit « un autre moment de la journée », pas « il y a longtemps ». Même conclusion que l'atelier 05 : la lumière donne un registre, pas une époque.
- **Retard (passé en caméscope)** : dès la première image du plan 2, on sait qu'on a changé de régime : le **cadre 4:3 entre deux barres** fait plus que le bruit ou la couleur ; c'est le signe le plus fort et le moins coûteux. Critère 1 tenu. Mais la texture v1 est trop jaune (multiplicateur bleu 0,86) et le mur blanc vire crème uniforme : ça glisse vers le « filtre ». Bruit de chrominance en taches de ~10 px : crédible à 480 px, à la limite du sale.
- **Ce que la planche m'apprend sur le sens en retard** : je pensais que le plan 3 (le bord vide en insert) porterait le manque. Faux : seul, ce plan est **abstrait** (une bande brune floue) ; il ne prend son sens qu'au plan 4, quand la tasse apparaît au même endroit. Et c'est le **retour au plan large du début (plan 5, image identique au pixel près au plan 1)** qui pèse le plus : la même image, relue. Koulechov par la mémoire : ce n'est pas un plan nouveau qui dit l'absence, c'est **la répétition du premier** après qu'on a vu ce qui manquait. Critère 2 à reformuler.
- **Explicatif (passé d'abord)** : on comprend tout au plan 3, le reste confirme. Plus clair, moins fort : l'absence est **expliquée** au lieu d'être **découverte**. Le retard gagne, mais seulement s'il y a un retour.
- **Présent figé** (une seule image rendue, répétée) : les plans du présent sont immobiles au pixel près, sans bruit ni souffle. Au lieu d'un défaut, ça marche : le présent est **arrêté**, le passé bouge (caméra portée). À garder comme choix, mais à 480 px une très légère respiration (grain fin) éviterait l'effet « photo ».

## v2 — le J-cut et le cliché de la date
- **J-cut de 12 images** (`edl-v2-jcut.json`, planche identique à v1, la différence est au son) : mesuré, le souffle et l'oiseau du passé montent de 5 dB 0,5 s **avant** la coupe (−44,7 → −39,7 dB RMS à 1,9 s ; −51,3 → −33,5 à 2,2 s). Sur le papier, c'est la mémoire déclenchée par un son (un oiseau dans la pièce vide), et le spectateur entre dans le souvenir par l'oreille avant l'œil. Gardé. Non écouté (pas d'écoute possible en VM) : à juger en phase 2.
- **Date incrustée « JUL 08 1998 »** (`v2-date-detail.png`) : à 480 px elle est minuscule, et pourtant elle change tout : elle **date** ce qui devait rester ouvert. On passe de « souvenir de quelqu'un » à « archive d'une année ». Elle répond à la question que le montage devait laisser au spectateur. **Rejetée**, comme prévu, mais je sais maintenant pourquoi : ce n'est pas qu'elle est kitsch, c'est qu'elle **explique**.

## v3 — référence (`v3-planche.png`, `v3-raccord.png`)
- Ordre : présent large (2,4 s) → passé large (2 s, J-cut) → **passé insert, la tasse (1,2 s)** → **présent insert, le même bord, vide (2 s)** → présent large tenu (3,2 s).
- Le raccord tasse → bord vide est un **raccord dans l'axe du temps** : même caméra, même bord, la tasse s'efface et le 4:3 s'élargit en 16:9 ; le souffle de bande se coupe net sur la coupe (pas de L-cut : le silence du présent est le coup). Le bord vide n'est plus abstrait : il arrive juste après la tasse.
- Texture adoucie (balance 1,04/1,02/0,93, chroma 0,014 en grain plus fin) : le passé reste chaud et identifiable, sans le jaune de filtre.
- Plan final allongé à 3,2 s : il porte le poids (leçon de v1).
- **Ce qui reste faible** : (1) la caméra portée du passé fait que le bord n'est pas exactement au même endroit que dans le présent : le raccord est approché, pas parfait (choisir : bord aligné au pixel = effet « magique », ou décalé = la mémoire qui flotte ; aujourd'hui c'est indécis, donc raté) ; (2) le passé n'a pas de **regard** : on voit une tasse, pas *la tasse de quelqu'un*. Une main qui la pose, une vapeur, une trace de rouge à lèvres, un deuxième objet… un indice d'usage. (3) Aucun test avec un spectateur.

## Leçons (versées dans `montage-couleur-et-intention`, `montage-grammaire`, `montage-regard`)
1. **Un changement de format (4:3 entre barres) dit « autre régime de temps » plus vite que n'importe quel étalonnage.** La texture (bruit chroma, définition, balance) le confirme, elle ne le fonde pas.
2. **Le sens en retard a besoin d'un retour** : c'est la reprise d'une image déjà vue, relue, qui fait sentir le manque ; un plan nouveau de l'absence reste abstrait s'il précède ce qui manque.
3. **Le marqueur de date tue le souvenir parce qu'il répond** : un indice d'époque doit rester un indice (support, objet), jamais une information.
4. **J-cut de mémoire** : faire entrer le souvenir par le son, une demi-seconde avant l'image ; le couper net au retour.

## v4 proposée
Bord aligné au pixel (caméra portée seulement sur le plan large du passé) ; un indice d'usage sur la tasse (vapeur, ou une cuillère) ; grain très fin sur le présent ; tester 9:16.

## v4 (`v4-planche.png`, `v4-raccord.png`) — l'absence a un sujet
- **Trouvaille** : dans le présent, une **trace sèche de fond de tasse** sur la table, exactement là où la tasse était (même coordonnées dans la scène). Le plan de l'absence n'est plus abstrait : il montre une trace, donc un usage, donc quelqu'un. C'est la réponse au défaut n° 2 de v3 (« le passé n'a pas de regard ») trouvée **dans le présent** : l'indice d'usage le plus fort n'est pas dans le souvenir, c'est ce que le souvenir a laissé.
- Bord aligné : l'insert du passé n'a plus de caméra portée (le large garde la sienne) et les deux inserts partagent la même caméra, visée par un point (`insert_cible`) au lieu d'angles réglés à l'aveugle (deux essais ratés avant : haut de la tasse coupé, puis tasse sortie du cadre). Le raccord tasse → trace tombe au même endroit. **Choix tranché : aligné.**
- Passé insert et présent insert immobiles → **une image rendue chacun** ; la texture caméscope varie quand même à chaque image (bruit tiré à chaque image), le passé « vit » ; le présent reçoit un grain fin (σ = 2/255) pour ne plus faire « photo ».
- **Ce qui reste faible** : la cuillère se lit **paille** (trop fine, sans cuilleron) ; la surface du café reste beige (le disque reflète la fenêtre) ; la trace est trop nette et grise, elle devrait être brune et irrégulière (un anneau plus foncé au bord, comme un vrai fond de café séché). Ce sont des défauts de fabrication, pas de direction.
- Bilan de la pièce : v4 = **référence**. Ordre : présent large figé → passé large (J-cut d'oiseau) → la tasse, la cuillère → la trace, au même endroit → le présent large, relu.
