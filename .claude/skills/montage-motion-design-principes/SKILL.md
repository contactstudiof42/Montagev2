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

## 5. Ce que les projets du cabinet ont appris (2026-10) [TESTÉ EN CONDITIONS RÉELLES]
Leçons validées par Diego (`/Users/diego/Post-prod clients/LECONS-A-REMONTER.md`), intégrées le 2026-10-29. Construction dans After Effects : `montage-after-effects` § 6.

### Carton titre [genre : motion design, carton titre ; contre-indication : le titre de marque, qui suit la DA du client (§ 3)]
- **Le titre centré sur deux lignes fait « PowerPoint » ; des éléments vivants dessinés en formes (oiseaux vectoriels) font « cheap à la mort ».** Validé : une typo très hiérarchisée (un mot énorme, de petites lignes très espacées) trouvée dans des références, et du vrai footage composité pour tout ce qui vit (oiseaux, brume). Pas d'étalonnage dans After Effects : il se fait ensuite dans Resolve. (Gagnée : 2026-10-21.)
- **Caméra animée (dolly, Vertigo)** : un texte posé en 3D près de la caméra grossit et déborde en fin de plan. Un titre qui doit rester lisible passe en 2D, hors caméra ; la parallaxe reste sur les couches d'image. Lisible sur un ciel ou un paysage clair : ombre portée très douce (opacité 30 %, distance 6, douceur 70 en UHD) et un calque d'effet qui baisse l'exposition de 0,4 IL pendant que le texte est à l'écran. (2026-10-28)
- **Parallaxe 2,5D à partir d'une photo** [genre : motion design, parallaxe photo] : des couches découpées grossièrement font glisser et dédoubler le premier plan dès que la parallaxe est marquée. Refaire les couches dans Photoshop : sélectionner le sujet pour les bâtiments ; fond propre par remplissage d'après le contenu en sélectionnant tout l'objet à effacer ; éléments fins (pylônes) détourés par différence entre la photo et le fond propre. (2026-10-28 ; limites de Photoshop par script : `montage-pilotage-mcp` § 4.)

### Frise chronologique, défilement d'années [genre : motion design, frise, compte à rebours]
- **Le rythme qui plaît** : « le temps qui s'arrête un peu, c'est mou » : quasi-arrêt avec dérive très lente sur chaque date importante, passages amortis entre elles, un milieu très rapide. Une date qui porte un titre a besoin d'un vrai arrêt pour qu'on lise le titre ; les dates de transition (juste avant l'atterrissage) peuvent être courtes.
- **Quand ça accélère jusqu'à 1 ou 2 images par année**, en travelling les dates deviennent illisibles (une image nette, une traînée) : dès qu'une année dure moins de 0,16 s, passer en compteur fixe (une seule date immobile au centre, son texte calé sur le jalon le plus proche, les images défilent derrière, obturateur 90°). Relais en coupe franche, sur l'image où la date mobile est exactement à la place du compteur (pas de fondu : double exposition). Ralentir à nouveau sur les 3 ou 4 derniers jalons pour atterrir.
- **Pointe de vitesse en flou de mouvement (filés)** [genre : motion design, frise, transitions rapides] : des images floues font une bouillie grise qui écrase l'effet. Assombrir les images (environ −0,8 diaph) pendant la pointe et garder les éléments dorés ou lumineux à pleine lumière : ce sont eux qui dessinent les filés. Entrer dans la vitesse en 3 ou 4 jalons encore à demi lisibles, pas en 6 images. Obturateur autour de 120° (à 180°, les passages lents deviennent flous aussi).
- **Archives sans date** [genre : motion design, frise, archives] : vérifier chaque image contre son année ; masques chirurgicaux, téléphones, logos ou panneaux datés trahissent l'époque (un masque de 2020 en 1998, un panneau « 1997 » sous 1998). Réserver les images marquées à leur période ; le plus ancien d'aspect pour les premières années.
- Après tout changement de rythme d'une frise en time remap décalé, revérifier chaque jalon (`montage-after-effects` § 6).

### Des personnes filmées dans un motion design [genre : motion design, frise, habillage]
Un détourage tracé à la main par masques polygonaux, surtout sur des VHS molles, est jugé « catastrophique ». Sans vraie roto propre, partir sur du géométrique assumé, façon cubisme : un même rush coupé en 2 facettes décalées (15 à 35 px, 108 %, légère rotation, petite avance temporelle) ; coupes sur 2 ou 3 angles seulement ; aucun côté vertical ni toit symétrique (sinon on lit des maisons) ; un sujet reconnaissable par jalon (une machine, un produit) ; filets fins seulement dans le prolongement d'arêtes réelles, jamais à moins de 30 px d'un texte. Chaque image fixe passe devant le directeur artistique avant d'être montrée. (2026-10-29)

### Finir sur un visuel de charte [universel]
Si le logo animé n'a pas la même mise en page que le visuel final, le fondu montre deux cadres décalés. Reconstruire l'apparition à partir du visuel net lui-même (chaque élément repris du visuel, fond reconstitué sous les textes) : un seul exemplaire de chaque élément, et la dernière image est exactement le visuel. (2026-10-29)
