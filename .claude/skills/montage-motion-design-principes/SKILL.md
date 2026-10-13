---
name: montage-motion-design-principes
description: Principes artistiques du motion design et de la typographie animée — quoi animer et pourquoi : carton-titre, titre de marque, générique, line-up, logo animé, typo cinétique, habillage, lower third, explicatif animé, animation d'interface, traces et échos de mouvement. Mots entendus : « l'animation fait cheap », « ça bouge pour rien », « on n'a pas le temps de lire », « le logo doit claquer mais rester premium », « trop de choses bougent », « ça fait template », « on dirait un PowerPoint ». Réglages techniques After Effects (courbes, expressions) : montage-after-effects.
---

# Motion design : faire bouger avec une raison

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Savoir (principes 7 à 18, traces d'un mouvement, titres de film de mariage, clichés) : [savoir.md](savoir.md). Version d'avant : `archives/audit-2/skills/montage-motion-design-principes/`._

**Fait foi sur** : le sens d'un mouvement, la lisibilité du texte animé, les titres. Courbes, expressions et pilotage d'After Effects : `montage-after-effects` ; « un concept, un signe » en général : `montage-references`.

## 1. Les principes que les exercices vont trancher
[ÉPROUVÉ EN MAQUETTE] jusqu'aux exercices E1 et E2 de `PLAN-TESTS.md`, qui les confirmeront ou les corrigeront.
1. **Un concept, un signe** (Saul Bass) : réduire le message à une forme dessinable ; toute l'animation la révèle ou la transforme. Si on anime « des éléments », on n'a pas encore d'idée. [SOURCÉ]
2. **Animer le paramètre qui porte le sens** : pour une apnée, pas l'échelle du mot (pulse de logo) mais son interlettrage qui se resserre. Corriger un excès en réduisant l'amplitude donne un mouvement invisible : **déplacer** le mouvement, pas l'atténuer. (Gagnée : pièce 01, un « respir » symétrique lu comme un logo.)
3. **Le mouvement a une cause et une matière** : overshoot = élastique, métal ; sans overshoot = verre, pierre, luxe ; l'ease symétrique par défaut n'a pas de matière. [THÉORIQUE]
4. **Asymétrie** : on entre vite et on se pose, ou on s'élance et on s'arrête net ; la symétrie (4 s / 4 s) se lit comme une machine. (Gagnée : pièce 01.)
5. **Montrer le processus plutôt que le résultat** (Kyle Cooper, *Se7en*). [SOURCÉ]
6. **Lisibilité d'abord** : un texte reste lisible au moins le double de son temps de lecture à voix haute, immobile ou presque ; le mouvement se fait avant et après la lecture. [THÉORIQUE]

## 2. Un titre se juge à côté des références [universel]
Une police correcte ne suffit pas : il faut une **mise en page** (taille franche ou discrète, interlettrage choisi, placement qui dialogue avec l'image, rapport à la marge) et une **révélation choisie et sobre** (une montée de quelques pixels avec un fondu freiné en arrivant, un masque qui découvre, un interlettrage qui se resserre, un flou de mouvement qui se résorbe), jamais un grossissement uniforme centré ni un effet de bibliothèque. **Sinon, pas de texte du tout** (le plan de fin de la marque suffit). Le titre se pose à côté de ceux des références, en pleine résolution, avant d'être gardé. (Gagnée : V2 du film de marque kinetic, un titre centré grossi de 0,9 à 1, « un enfant de 6 ans qui a fait un PowerPoint » ; Diego sur la V3 : « quelque chose d'assez simple et épuré, à la Apple ».)

## 3. Titre de marque : reprendre la DA du client, animer sobrement [genre : film de marque]
- **Ne pas inventer un titre quand le client a déjà un dessin** (marque, charte, logo) : reprendre sa DA (graisses, accolement, air autour) ; retrouver les graisses en superposant le titre rendu à la référence en pleine résolution.
- **Animation sobre par défaut, même dans une vidéo très dynamique** : fondu + montée de 15 à 20 px + léger flou qui se résorbe, 12-16 images, freinée à l'arrivée (ease-out cubique), le deuxième mot 2-3 images après ; pas de grossissement, pas de rebond, pas d'interlettrage animé. La folie est dans le montage ; la marque reste calme. Si la DA du client a son propre langage de mouvement, c'est elle qui décide.
- **Le placer là où l'image le permet** : une zone uniforme pendant tout le plan (vérifiée sur les images de début, milieu et fin du mouvement de caméra).
(Diego, V2 et V3 du film de marque kinetic ; carnet 2.)

## 4. Questions avant d'animer
1. Quelle est la phrase d'intention ? 2. Quel est le signe unique ? 3. Quel paramètre porte le sens ? 4. Quelle matière (poids, élasticité) ? 5. Où sont les temps immobiles ? 6. Qu'est-ce que j'enlève ?
