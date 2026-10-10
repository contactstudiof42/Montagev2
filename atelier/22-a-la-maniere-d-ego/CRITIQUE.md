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
