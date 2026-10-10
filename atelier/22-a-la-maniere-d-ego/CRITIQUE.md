# Pièce 22 — critiques successives

_Planches : `v1-A-planche.png`, `v1-B-planche.png`, `v2-A-planche.png`, `v2-B2-planche.png` (12 images à intervalle régulier). Rendus (non versionnés) : `atelier/rendus/22/`. Je n'entends pas le son : le jugement sonore porte sur le placement (timecodes), pas sur l'écoute._

## v1 (A « explicatif » 17,5 s / B « EGO » 25 s, même recul de 96 images)
**L'intention est-elle servie ?** À moitié. Le vertige existe (le champ qui devient texture jusqu'à l'horizon), mais **le « vous » disparaît** : dès u ≈ 0,3, la chaise 1 sort du bas du cadre. Le recul devient un travelling sur un motif répété ; on voit « beaucoup de chaises », pas « moi, devant toutes les autres ».
- **Lisibilité** : la 1re image est illisible (plongée à 62°, on voit un dossier en aplat, pas une chaise). « Voici une chaise » tombe sur une forme abstraite.
- **Narration** : « celle de votre mère, puis celle de sa mère » ne se voit pas : le champ arrive en bloc, aucune colonne n'est désignée.
- **Couleur** : YAVG médiane 188-190 (plage limitée) : un **gris délavé**, pas le blanc clinique d'EGO (médiane mesurée 235-254 sur ses miniatures). Le blanc gris fait « rendu par défaut ».
- **Dernière image** : la silhouette est collée au bord droit, aucun espace devant elle ; la chaise sous elle se confond avec la rangée.
- **A contre B** : dans A, le chiffre écrit « 117 000 000 000 » occupe le centre au moment même où le champ devient infini ; l'image et le texte disent la même chose, deux fois. On LIT au lieu de RESSENTIR. Dans B, la seule information pendant 3,8 s est l'image : c'est elle qui dit l'échelle, la voix ne fait que nommer après coup. **B est le bon parti pris** ; A est un explicatif honnête mais sans vertige.

## v2 (corrections : 64 images, `--v2`)
1. **La chaise de référence reste dans le cadre pendant tout le recul** (visée qui glisse lentement, plongée de 38° à 26°) : à mi-recul, la chaise 1 est seule devant le front du champ. C'est l'image de la pièce : une rangée vide, puis vous. (Vue sur la planche de test `t2`.)
2. Départ moins plongeant : l'assise et le dossier se lisent, la chaise est une chaise.
3. Exposition AgX +1 : on vise le blanc clinique.
4. Silhouette recadrée au tiers gauche, **le vide devant elle** (elle regarde vers le blanc) : le malaise doux vient de ce vide, pas de la foule derrière.
5. B2 : silence allongé (13,6 → 18,4 s, 4,8 s) et recul plus long ; la voix revient sur l'image arrêtée.

## Leçons (reportées dans les skills)
- **Un recul d'échelle a besoin d'un témoin qui reste dans le cadre** (l'objet de départ, ou une silhouette). Sans lui, le spectateur perd sa mesure et le vertige devient un motif décoratif. → `montage-motion-design-principes`, `montage-references` § F 22.
- **Le chiffre se dit, il ne s'écrit pas, quand l'image le montre déjà** (une miniature, un signe). L'écrire est juste quand l'image NE PEUT PAS le montrer. → `montage-youtube` 18.
- **Rendre un seul mouvement, le placer plusieurs fois** : un recul rendu à u régulier puis retimé par une courbe temps → u permet de comparer des montages sans re-rendre (l'équivalent AE : remappage temporel). Coût : 96 images en ~5 min contre 2 rendus complets. → `montage-blender`.
- **Le blanc d'EGO se mesure** : YAVG médiane < 200 (plage limitée) = gris ; il faut pousser l'exposition (+1 en AgX ici) jusqu'au bord du clipping du sol.

## Reste à faire (v3)
- Écouter (phase 2) : la coupe franche de la nappe à 13,6 s est-elle un choc ou un trou ? Faut-il un souffle qui monte pendant le recul au lieu du silence ?
- Une vraie voix humaine posée (pas espeak) change tout le rythme : refaire le placement sur une voix enregistrée.
- Tester la variante `--noir` (noir + lumière froide, l'autre pôle d'EGO).

## Verdict v2 (planches `v2-B2-planche.png`, `v2-A-planche.png`)
- **Gagné** : de l'image 4 à l'image 7 de la planche, la chaise 1 reste seule au bas du cadre, devant le front du champ. Le « vous » existe jusqu'au moment où le champ devient texture : le vertige a maintenant une mesure. C'est la correction qui compte.
- **Pas encore** : YAVG médiane 197 (contre 188 en v1) : plus clair, mais toujours sous le blanc clinique visé (> 200, EGO 235-254). Il faut aussi éclaircir le sol (albédo 0,8 → 0,9) plutôt que de pousser encore l'exposition, qui brûlerait les chaises.
- **Dernière image** : la silhouette est enfin petite, avec du vide devant elle, mais l'horizon coupe le cadre en deux et laisse une moitié basse de sol vide sans fonction. Le v3 la placera au tiers inférieur (caméra plus haute), pour que le blanc au-dessus devienne le « devant » vers lequel elle regarde.
- Les images 8-9 (fin du recul) restent une texture grise uniforme : c'est voulu (l'échelle échappe), mais 2 images de planche sur 12, c'est long sans voix. Dans B2, ce passage tombe dans le silence de 4,8 s : il faudra l'écouter en phase 2 pour savoir s'il tient ou s'il traîne.

## v3 (session 19 : `--v3`, `--v3b`, montage `B3`, planches `v3-B3-planche.png`, `v3c-B3-planche.png`, `v3n-B3-planche.png`, `v3bn-B3-planche.png`)
Corrections tentées : sol 0,8 → 0,9 ; plan final recadré (5 candidats rendus en image fixe, 7 s chacun, avant de lancer le recul) ; nappe qui **monte** pendant le recul (×2,5 de 13,6 à 18,0 s) puis se coupe net sous la voix (« il y en aurait… » tombe dans le vide) ; variante `--noir`.

**Le plan final est gagné.** Caméra latérale à 14 m, horizon au tiers haut : le champ entre en diagonale par la gauche et **s'arrête net**, la silhouette est assise sur la pointe, et tout le quart droit est du blanc vide vers lequel elle est tournée. On lit enfin « tout au bout » sans le dire : c'est le bord du champ qui le dit. Les candidats rejetés : silhouette de face (le vide passe derrière la caméra, on ne le voit pas), silhouette collée au bord droit (pas d'air devant), silhouette au milieu des rangées (on la perd dans la foule).

**Le blanc : faux diagnostic deux fois, puis le vrai.** Sol plus clair : YAVG 197 → 199. Couleur de brume 0,93 → 1,0 : 199 → 199. Mesure du pixel le plus clair : **222-225 sur 255 dans TOUTES les images, ciel compris**. Le plafond ne vient pas de la scène, il vient de la **transformée de vue AgX**, qui compresse les hautes lumières et n'atteint le blanc qu'à des valeurs de scène très hautes. Correction au bon endroit, l'étalonnage : une courbe qui place le point blanc (0,87 → 0,985, ffmpeg `curves`) → **YAVG 226**, le blanc clinique d'EGO, et les ombres des chaises sont gardées (le milieu de courbe ne bouge presque pas). Leçon : **mesurer le maximum avant de toucher aux lumières** ; un plafond identique partout = un plafond de pipeline, pas d'éclairage.

**Son (non écouté, placement seulement)** : B3 remplace le trou de B2 par une montée. Hypothèse à vérifier en phase 2 : la montée transforme le vertige en suspense (on attend quelque chose) alors que le silence de B2 le laissait en contemplation. EGO utilise les deux ; pour cette phrase, je parie que la coupe net APRÈS la montée (la voix seule dans le vide) est plus forte que le silence sans préparation, parce que le vide se mesure à ce qui vient de s'arrêter.

**Variante noire** : 
- v3n : la silhouette noire sur fond noir **disparaît** dans le plan final. Faute évidente sur le papier, invisible tant qu'on n'a pas inversé le monde.
- v3bn : silhouette claire → elle n'est éclairée que par un liseré (la lumière froide vient de derrière), on voit un **contour fantôme**. C'est beau et juste pour « le dernier d'une lignée » (une présence fragile), mais trop petit : il faudra une lumière motivée sur elle seule (une douche) pour qu'elle devienne la seule chose éclairée du monde.
- Le noir a un défaut que le blanc cache : en fin de recul, le champ lointain fait un **moiré** (8 échantillons, motif régulier plus fin que le pixel). Dans le blanc, la brume l'efface ; dans le noir, la lumière rasante le révèle. Correction : plus d'échantillons ou brume noire plus tôt, ou un léger flou de profondeur.
- Laquelle choisir : le blanc dit « tous les humains » (une salle d'attente infinie, clinique, calme) ; le noir dit « les morts » (un cimetière de chaises). Le texte parle des mères : **le blanc**, parce que le ton est tendre, pas funèbre. Le noir serait juste pour une phrase sur la disparition.

**Encore raté** : les trois premières images de la planche montrent un panneau blanc (le dossier vu de dos) : « Voici une chaise » tombe encore sur une forme ambiguë. v4 : départ de trois quarts face, ou une chaise moins schématique (un dossier ajouré).

## Leçons v3 (reportées dans les skills)
- **AgX plafonne le blanc** (~222/255 en sortie 8 bits avec Base Contrast) : le blanc pur se fait à l'étalonnage (point blanc), pas en ajoutant de la lumière. → `montage-blender`, `montage-couleur-et-intention`.
- **Inverser le monde inverse le rôle du sujet** : dans le blanc, le sujet est la tache sombre ; dans le noir, il doit devenir la lumière. → `montage-couleur-et-intention`.
- **Chercher le cadrage en image fixe avant de lancer l'animation** (5 essais × 7 s contre 3 min par recul). → `montage-blender`.

## v4 (session 19 : `--v4 --x0 1.6`, montage B3 + courbe de point blanc, planche `v4-B3-planche.png`, YAVG 229)
Problème visé : « Voici une chaise » tombait sur un panneau blanc.
- Essai 1 : départ de trois quarts (décalage latéral 0,25 → 1,0 → 1,8 m, 3 images fixes) : à 1,8 la chaise se lit (dossier, assise, pieds), mais **elle n'est pas seule** : huit chaises voisines à la même échelle se disputent « voici UNE chaise ».
- Essai 2 : profondeur de champ (f/1,4 qui se ferme jusqu'à f/64 avec le recul) : **presque invisible**, l'écart de 1,25 m entre la chaise et la rangée suivante est trop faible pour qu'un flou les sépare. Encore un défaut qu'on voulait régler à l'étage optique et qui naît dans la **mise en scène**.
- Essai 3 (retenu) : **la chaise 1 à 4 m devant le champ**. Les 4 premières images de la planche : une chaise, seule, lisible, dans le blanc. Images 5 à 7 : la chaise isolée au bas du cadre, le champ entier devant elle au-delà d'un vide. C'est l'image la plus claire de la pièce.
- **Mais le sens a bougé** : l'écart dit « à part », « séparé des autres », plus « au bout d'une lignée ». « Derrière elle, il y a celle de votre mère » ne se voit plus : la mère est à 4 m. Lisibilité gagnée, filiation perdue. v5 : garder **une seule colonne continue** qui part de la chaise 1 et rejoint le champ (la lignée), avec le vide de part et d'autre (la solitude). Les deux sens tiennent alors dans le même plan.
- Leçon : **isoler un sujet se fait d'abord par l'espace, ensuite par l'optique** ; et chaque écart d'espace a un sens qu'il faut relire contre le texte. → `montage-regard`.
