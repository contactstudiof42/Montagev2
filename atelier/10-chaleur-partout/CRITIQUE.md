# Pièce 10 « Chaleur partout » — critique (session 7, images fixes)

Planches : `planche-ABC.png` (v1), `planche-B2C2C3.png` (v2) ; mesures `mesures-*.json` (`mesure.py` : luminance moyenne, part de pixels chauds R > B + 0,08, froids B > R + 0,08). Rendus : `atelier/rendus/10/` (un rendu Cycles 24 échantillons par version, ~10 s).

## v1
- **A (censé être mon système)** : raté comme démonstration : la tasse en faïence blanche n'est pas chaude (3,6 % de pixels chauds, tous dans le bois). Mon « une seule chaleur » n'existe que si l'objet chaud est **dans le décor** (leçon de l'atelier 05 retrouvée : la couleur se décide au tournage).
- **B (renversé)** : **réussi** : lampe de bureau, nuit dehors, 62 % de pixels chauds ; on lit « le soir, chez quelqu'un », pas « sépia ». Ce qui l'évite : un **dégradé réel** de lumière (une source, des coins sombres, une ombre portée), là où le filtre de l'atelier 08 v1 teintait tout uniformément. Critère 1 tenu. Défaut : la sphère émissive de la lampe flotte dans le cadre comme une lune (aucun pied) → v2 : source hors champ.
- **C (l'événement froid)** : **raté, et c'est la leçon** : l'écran du téléphone, en émission forte, sort **blanc** (0 % de pixels froids mesurés) : AgX désature les émissions intenses vers le blanc.

## v2
- B2 : lampe hors champ : meilleur, la chaleur est motivée sans objet parasite.
- C2 / C3 (écran plus faible, lumière de débordement plus forte) : toujours **0 % de froid**. Deux causes, vues sur l'agrandissement : (1) le téléphone est à plat et la caméra à hauteur de table : on ne voit presque pas sa face ; (2) **une lumière froide qui tombe sur un bois brun déjà éclairé en orange donne du blanc, pas du bleu** : la couleur perçue est lumière × surface × ambiance. Le froid ne se lit que sur une surface neutre ou vu en direct.
- Donc le critère 2 (le bleu attire l'œil à < 1 % du cadre) n'est pas testable tant que le bleu n'existe pas à l'image. Pièce à poursuivre.

## Leçons (versées dans `montage-couleur-et-intention`)
1. **La chaleur partout se lit « intime » si elle a une source et un dégradé** ; uniforme, elle se lit « filtre ancien ».
2. **Un événement froid dans un monde chaud est plus difficile à fabriquer que l'inverse** : sous AgX, l'émission intense blanchit, et la lumière froide sur une matière chaude se neutralise. Il faut une **surface neutre** (papier, mur blanc, visage) pour recevoir le bleu, ou voir la source de face, et baisser la chaleur ambiante autour de l'événement.
3. Mon système (« une seule chaleur ») a besoin d'un objet chaud **dans le décor** ; le renverser demande un objet froid **qui reçoive la lumière**. Dans les deux cas, la décision est au décor (tournage), pas à l'étalonnage.

## v3 proposée
Caméra plus haute (plongée sur la table), téléphone légèrement relevé sur la tasse ou posé sur une feuille blanche, écran en émission modérée (≈ 2) ; lampe baissée de 30 % autour ; puis un montage de 8 s : B tenu, le téléphone s'allume, rien d'autre ne bouge.

## v3 (`planche-B4C4C5.png`) — plongée, feuille blanche sous le téléphone
- Caméra en plongée (la table devient le décor, on voit le téléphone de face), feuille A4 neutre sous le téléphone, écran en émission modérée (2), débordement 10 W ; C5 avec la lampe baissée d'un tiers.
- **Saillance : réussie.** La feuille éclairée devient le point le plus lumineux du cadre : l'œil y va en premier (critère 2 tenu sur la planche), dans un monde resté chaud (50 % de pixels chauds en C4).
- **Couleur : toujours ratée.** La feuille sort **blanche** (0 % de pixels froids ; zone de la feuille mesurée R 0,93 / G 0,90 / B 0,87 : encore **légèrement chaude**, la lampe l emporte) : le débordement est trop fort, et AgX compresse les hautes lumières vers le blanc. L'événement se lit « une lumière s'allume », pas « le froid entre ».
- Pour v4 : débordement à 2-3 W au lieu de 10 (rester sous la compression des hautes lumières), ou standard « Filmic / Standard » pour ce plan, ou étalonnage secondaire qui pousse le bleu **dans** la zone (une clé sur la feuille). Leçon générale : **la saillance vient de la luminance, la couleur ne se lit que sous le blanc** ; un événement coloré doit être exposé plus bas qu'on ne le croit.

## v4 (session 8) — `planche-v4.png` (6 essais choisis), `planche-v4-toutes.png` (les 12), `mesures-v4.json`
Méthode de mesure nouvelle (`mesure_zone.py`) : la **zone de l'événement** = pixels dont la luminance monte de plus de 0,03 entre la version éteinte et la version allumée (même scène, même graine) ; on mesure la couleur moyenne de cette zone (B − R > 0 = froid) et sa saillance (luminance de la zone / luminance moyenne du cadre).

| essai | réglage | zone B − R | saillance | lecture |
|---|---|---|---|---|
| C6 | débordement 2,5 W (au lieu de 10) | −0,09 | 2,6 | encore un halo blanc chaud |
| C8 | idem, vue **Standard** au lieu d'AgX | **−0,18** | 2,3 | **plus chaud** que sous AgX |
| C7 / C10 / C11 | lampe 40 / 20 / 8 W | −0,02 / −0,08 / −0,06 | 2,9-3,1 | baisser la lampe ne refroidit pas la feuille |
| C12 / C14 | émission 0,5 / 0,3, débordement 0,15 / 0,05 W | −0,01 / −0,03 | 2,3-2,6 | l'écran devient gris, l'événement **disparaît** |
| **C15** | couleur saturée (0,15 / 0,4 / 1 : « gélatine CTB ») | **+0,02** | 2,6 | **premier bleu lisible** : l'écran lui-même, vu de face |
| C6 + clé | clé secondaire simulée dans la zone (R −18 %, B +15 %) | **+0,10** | — | bleu net, sans toucher au reste |

**Ce que v4 réfute** : mon explication de v3 (« AgX compresse les hautes lumières vers le blanc ») n'était pas la bonne. En Standard, la feuille est *plus* chaude (C8). La vraie cause : **la source froide est à 3 cm de la feuille** : sa lumière sature localement quelle que soit sa puissance (entre « blanc » et « invisible », il n'y a presque pas de fenêtre : C6 contre C14), et la couleur pâle (0,55 / 0,75 / 1) d'un vrai écran est trop proche du blanc pour survivre à côté d'une lampe très orangée.

**Ce qui marche** : (1) **pousser la couleur de la source au-delà du vrai** (C15), comme on gélatine un écran ou une fenêtre au tournage ; l'écran vu de face porte le froid à lui seul ; (2) **une clé secondaire** sur la zone en post (C6 + clé) : le bleu le plus net, à moindre coût, et réglable après coup.

**Critique DA de C15** : l'intention (« le froid entre dans un monde chaud ») est servie à petite échelle : un rectangle bleu dans un cadre à 51 % chaud, l'œil y va (saillance 2,6). Mais c'est un **signe**, pas une **lumière** : rien autour ne bleuit, donc on lit « un téléphone s'allume », pas « le froid gagne la pièce ». Pour l'événement *ressenti*, il faudrait que le bleu touche un visage ou une main (une surface que le spectateur habite) : c'est la pièce qui manque ici, pas un réglage.

**Leçons (versées dans `montage-couleur-et-intention`)** :
1. **Un écran ou une fenêtre « froids » au tournage se gélatinent plus bleus que nature** : la couleur réaliste d'une source froide est trop pâle pour se lire à côté d'une source chaude saturée. C'est le rapport des *saturations* qui compte, pas seulement des températures.
2. **Une source très proche d'une surface n'a pas de bon réglage** : elle sature ou disparaît. Éloigner la source (10-30 cm) ou recevoir sa lumière sur un visage, pas sur la surface où elle est posée.
3. **Vérifier une explication avant de l'écrire dans un skill** : ma cause « AgX » de v3 était fausse ; un seul essai contrôlé (C8) l'a montré. Les règles de couleur doivent venir d'essais à une variable.

v5 proposée (si on y revient) : une main ou un visage simple au-dessus du téléphone (à 25 cm), écran en C15 ; mesurer le bleu sur la main ; puis 8 s de montage (B tenu 5 s, allumage en 3 images).
