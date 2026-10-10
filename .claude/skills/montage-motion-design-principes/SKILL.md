---
name: montage-motion-design-principes
description: Principes artistiques du motion design et de la typographie animée — donner du sens à un mouvement, carton-titre, générique, logo animé, typo cinétique, habillage, lower third, animation d'interface, « l'animation fait cheap », « ça bouge pour rien », choisir quoi animer et comment.
---

# Motion design : faire bouger avec une raison

Version 1 (session 1, 2026-10-09). Sources : fiches `culture/saul-bass-generiques.md`, `culture/kyle-cooper-se7en.md`, pièce d'atelier `atelier/01-respiration/`. Technique After Effects : `montage-after-effects`.

## Principes
1. **Un concept, un signe** (Saul Bass). Avant d'animer, réduire le message à une forme dessinable en quelques secondes ; toute l'animation sert à révéler ou transformer ce signe. Si on anime « des éléments », on n'a pas encore d'idée. (Principe source : `montage-references` §C6 ; ici, seulement son application au mouvement.)
2. **Animer le paramètre qui porte le sens.** Échelle, position, opacité sont des réflexes ; le bon paramètre est celui qui *raconte*. Atelier 01 : pour une apnée, ce n'est pas l'échelle du mot (un pulse de logo, v1) mais son **interlettrage** qui se resserre (un corps qui se retient, v3). Corriger un excès en réduisant l'amplitude du même paramètre donne un mouvement invisible (v2) : il faut **déplacer** le mouvement, pas l'atténuer.
3. **Le mouvement a une cause et une matière.** Choisir l'overshoot, c'est choisir un matériau (élastique, métal) ; pas d'overshoot : verre, pierre, luxe. L'easing par défaut (ease in/out symétrique) n'a pas de matière. Réglages concrets (graphe de vitesse, influence, durées types à 25 i/s) : `montage-after-effects`.
4. **Asymétrie.** Entrée et sortie d'un mouvement ne se ressemblent pas : on entre vite et on se pose, ou on s'élance et on s'arrête net. La symétrie parfaite se lit comme une machine (atelier 01 v1 : 4 s / 4 s).
5. **Montrer le processus plutôt que le résultat** (Kyle Cooper, Se7en) : le geste qui fabrique dit plus que l'objet fini.
6. **Lisibilité d'abord.** Un texte doit être lisible au moins le double de son temps de lecture à voix haute, immobile ou presque pendant ce temps. Le mouvement se fait avant et après la lecture, pas pendant.
7. **Le silence visuel.** Un temps immobile, trop long, crée de la tension (rétention de l'atelier 01 v3) ; un temps immobile court se lit comme un arrêt. La durée fait la différence.

## Clichés à refuser (sauf parti pris assumé)
- Le zoom lent continu sur un carton centré.
- Les particules et le glow « pour faire riche ».
- Le texte qui tape lettre à lettre avec un son de machine à écrire (sauf si l'écriture *est* le sujet).
- Les transitions « whoosh » entre chaque plan (sauf en kinetic editing social, où la densité de SFX est le langage : voir `montage-kinetic-editing`).
- Le kinetic typography qui fait danser chaque mot : on ne lit plus rien.

## Questions à se poser avant d'animer
1. Quelle est la phrase d'intention ? 2. Quel est le signe unique ? 3. Quel paramètre porte le sens ? 4. Quelle matière (poids, élasticité) ? 5. Où sont les temps immobiles ? 6. Qu'est-ce que j'enlève ?

## Journal des leçons
- 2026-10-09, atelier 01 v1→v4 : déplacer le mouvement vers le paramètre signifiant (interlettrage) ; fond en dégradé plutôt qu'aplat ; rétention plus longue que confortable pour créer l'inquiétude (vérifié sur la planche v3) ; l'amplitude d'interlettrage dépend de la police (0,90 écrase EB Garamond italique, 0,93 en v5).
- **Rupture de forme = échelle + position + teinte ; la police n'ajoute qu'en grand** (atelier 09, session 7, principe Noé / Tom Kan) [TESTÉ EN ATELIER] : dix polices à 12 % de la hauteur, nom centré, se lisent comme un diaporama, presque comme une seule police ; en sautant de 10 à 60 % de la hauteur, avec ancrage changeant et débord du cadre, chaque coupe devient un choc, et là seulement la police compte. **Le sommet d'une courbe change de règle** (stabilité, fond commun, grande taille), il n'ajoute pas du chaos au chaos. `atelier/09-generique-equipe/CRITIQUE.md`.
