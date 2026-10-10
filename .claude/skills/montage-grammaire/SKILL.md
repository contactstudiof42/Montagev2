---
name: montage-grammaire
description: Grammaire du montage et fondamentaux — raccords (regard, mouvement, direction, axe, plan, son), règle des 180°, champ/contrechamp, jump cut, insert, plan de coupe, ellipse, J-cut et L-cut, montage parallèle, faux raccord, « ça saute », « on est perdu dans l'espace », « le dialogue ne coule pas », monter une interview ou une scène dialoguée.
---

# Grammaire du montage

Version 1 (session 1, 2026-10-09), complétée en session 7 (180° et J-cut testés). **[THÉORIQUE]** sauf mention : conventions classiques du métier, non encore mises à l'épreuve dans l'atelier. À relier à `montage-rythme` (où couper) et `montage-regard` (l'émotion gagne les arbitrages, Murch).

## Pourquoi une grammaire (et quand la casser)
La grammaire sert à une chose : que le spectateur **ne se pose pas de question involontaire** (où sont-ils ? qui regarde qui ? combien de temps a passé ?). Chaque règle protège l'attention pour qu'elle reste sur l'émotion. On la casse quand **la question est voulue** : désorientation (*Se7en*, montage paranoïaque de *Goodfellas*), urgence (jump cuts d'*À bout de souffle*), subjectivité. Casser une règle par ignorance se voit ; la casser par choix se sent, et elle doit alors être cassée **franchement et avec constance**.

## Les raccords
| Raccord | Ce qu'il fait | Piège |
|---|---|---|
| **Regard** | Plan d'un regard → ce qui est regardé : crée le point de vue (effet Koulechov : le spectateur projette l'émotion) | La direction du regard doit être cohérente avec la position de l'objet |
| **Mouvement** | Couper pendant un geste, le finir dans le plan suivant : la coupe disparaît | Couper au tout début ou à l'arrêt du geste : la coupe se voit |
| **Direction** | Un personnage qui sort à droite entre par la gauche : continuité du trajet | Inverser la direction = le personnage fait demi-tour (sauf intention) |
| **Dans l'axe** | Rapprochement dans le même axe : accent, choc | Variation de valeur trop faible (< ~30 % de taille) = saut disgracieux |
| **Forme / graphique** | Une forme en appelle une autre (os → vaisseau, *2001*) : transition-idée | Gratuit s'il n'y a pas de sens entre les deux |
| **Son** | Le son du plan suivant arrive avant (J-cut) ou celui du plan précédent continue (L-cut) | Sans J/L, un dialogue monté « au carré » sonne haché |

## Règle des 180°
**[TESTÉ EN LABO, session 7]** (`labo/grammaire/RESULTATS.md`, planche `axe180-planche.png`) : deux personnages Blender face à face, caméras des deux côtés de la ligne. Bon côté : A regarde à droite, B à gauche (ils se parlent). Axe franchi : A regarde **aussi à gauche**, comme s'ils parlaient à un tiers. En amorce, l'erreur se voit deux fois (l'épaule de l'autre saute de bord). **Contrôle automatisable** : projeter tête et direction du regard dans le cadre ; en champ / contrechamp, les signes doivent être opposés.

**Casser l'axe avec un sens** [TESTÉ EN ATELIER, session 8, `atelier/11-dialogue/`, v4 = référence] : franchir pour **tous les plans à la fois** ne crée qu'**un seul saut de regard**, à la jointure ; le plan suivant établit un nouvel axe cohérent. Placé sur l'image où le rapport de force bascule, le saut devient un choc spatial qui double le choc dramatique. Ce qui en fait un sens et pas une erreur : (1) il est complet (pas d'aller-retour) ; (2) **un plan large du nouveau côté arrive tout de suite** (2e plan après le saut), pas en conclusion ; (3) **le fond change** : chaque côté de l'axe montre un autre décor (mur éclairé / noir), donc choisir le côté = choisir à qui appartient le monde de la scène (à préparer au tournage). Coupe franche pour un renversement brutal ; travelling qui traverse l'axe pour une bascule lente (le mouvement explique, la coupe fait subir). Finir sur le personnage qui a perdu la scène. Contrôle automatique sur tout un montage : `labo/grammaire/sauts_regard.py` (franchissement complet = 1 saut, partiel = 2).
Dans une scène, une ligne imaginaire relie les deux personnages (ou un personnage et ce qu'il regarde, ou la direction d'un mouvement). Tant que la caméra reste d'un même côté, les regards se répondent (l'un regarde à gauche, l'autre à droite). Franchir la ligne inverse les directions : le spectateur croit qu'ils regardent dans la même direction.
**Pour la franchir proprement** : un plan dans l'axe (sur la ligne), un mouvement de caméra visible qui la traverse, un personnage qui se déplace, ou un plan large qui redéfinit l'espace.
**La casser volontairement** : signifier un basculement de rapport de force, un malaise (Kubrick, Ozu qui l'ignore systématiquement : la constance en fait un style).

## Dialogue et interview
- **Champ/contrechamp** : couper sur la **réaction** autant que sur la réplique. Le plus fort d'une scène est souvent le visage de celui qui écoute.
- **J-cut / L-cut** : décaler image et son de quelques images à quelques secondes ; le dialogue « coule ».
  - **J-cut de mémoire** [TESTÉ EN ATELIER, pièce 08] : le son du souvenir (souffle de bande, un oiseau) arrive 12 images (0,5 s) avant son image (mesuré : +5 dB à 0,5 s de la coupe) ; on entre dans le passé par l'oreille. Au retour, **pas de L-cut** : couper le son net avec l'image, le silence du présent est le coup.
  - **Raccord dans l'axe du temps** (pièce 08) : même cadre, deux époques (la tasse, puis le bord vide). Décider s'il est aligné au pixel (effet « magique ») ou décalé (la mémoire qui flotte) : à moitié aligné, il paraît raté.
- **Interview** : couper à la fin d'une pensée (respiration, regard qui se détourne). Masquer une coupe dans une phrase par un plan de coupe (insert, archive, mains) ou **assumer le jump cut** (avec un léger recadrage de 10-20 % si on a de la marge en 4K) ; ne jamais faire un fondu au milieu d'une phrase, cela crie « coupure ».
- **Plans de coupe** : les tourner en abondance (mains, détails, lieu) ; ce sont les jokers du montage.

## Temps
- **Ellipse** : enlever ce que le spectateur peut reconstruire ; il préfère compléter que subir.
- **Montage parallèle** : deux actions alternées créent une relation (course contre la montre, contraste). Accélérer l'alternance fait monter la tension.
- **Montage-séquence** (montage de temps compressé) : une durée longue en quelques plans, souvent sur musique ; cliché de la « préparation » si mal utilisé (voir le montage « hip-hop » de Wright, `culture/`).

## Montage son (bases)
- Trois couches : **voix** (l'ancre), **ambiances et bruitages**, **musique**. Monter les ambiances en continu sous les coupes image : une ambiance qui coupe avec l'image fait sauter le spectateur.
- Fondus audio de quelques images sur chaque coupe son, pour éviter les clics.
- Niveaux, loudness et livraison : `montage-loudness-livraison`.

## À faire
- Reste après l'atelier 11 : l'aire de regard, la règle des 30 %, un vrai visage (phase 2 ou personnage articulé).
- Vérifier les conventions chiffrées (30 % de variation de valeur, durées de J-cut) par des sources de monteurs et le mettre à jour.
