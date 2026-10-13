---
name: montage-regard
description: Juger un plan, une coupe, un montage, une animation ou un étalonnage déjà faits, et compenser ce que je ne perçois pas (mouvement, son, durée) — « est-ce que ça marche ? », « pourquoi ça ne fonctionne pas ? », « qu'est-ce qui cloche dans cette version ? », « on garde la V2 ou la V3 ? », « quelle prise est la meilleure ? », « c'est livrable ? », « on en fait trop ? », « qu'est-ce qu'on peut enlever ? », « ça tremble ? », retour de DA, contrôles avant rendu, relecture avant livraison, autocritique. Pour proposer une direction avant de faire : `montage-direction-artistique`.
---

# Le regard : juger, compenser, contrôler

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Marqueurs, carte des sens et hiérarchie du goût : `CLAUDE.md`. Méthode de visionnage et outils : [savoir.md](savoir.md) ; règles d'atelier (maquettes) et leurs preuves : [regles-atelier.md](regles-atelier.md). Version d'avant : `archives/audit-2/skills/montage-regard/`._

**Fait foi sur** : juger une version (la mienne comprise), les compensations de ce que je ne perçois pas, la liste des contrôles avant rendu, le verdict « livrable », l'autocritique. Analyser une référence : `montage-nouvelle-reference`.

## 1. Se comparer à la référence, pas à soi
Le look de base et tout effet tiré d'une référence se jugent sur une planche côte à côte : 6 images de ma version aux moments clés du genre, en pleine résolution, à côté de 6 images **comparables** de références du même genre (portrait contre portrait, extérieur contre extérieur, N&B contre N&B). Une question : « un monteur pro livrerait-il ça ? ». Les références donnent le niveau, le brief donne le style. Jamais de jugement de couleur sur une vignette ou une planche en palette ; les statistiques de luma ne voient pas un look plat. Chercher en permanence des références très esthétiques et s'y caler, sans copier (Diego). « Jamais cheap » veut dire pas d'effet bas de gamme, pas seulement pas de défaut : un détourage propre sur un fond plat reste cheap. Puis le directeur artistique, à froid (`PROMPT-PHASE-3.md`). (Gagnée : V2 du film de marque kinetic, qui passait tous mes contrôles chiffrés et paraissait laiteuse à côté des références ; V3b du film de mariage, où je comparais deux réglages de ma propre image.)

## 2. Voir le mouvement
Je ne vois pas le mouvement réel : je le mesure et je le regarde image par image.
- **Une mesure relative au projet** : `labo/outils/tremblement.py` (reste après lissage de 0,4 s, en px ramenés à 1080 de large). Le seuil se calibre sur un plan stable **du projet**, jamais repris d'un autre. Un plan s'accepte s'il est sous ce seuil **et** si sa bande d'images consécutives (10 à 25 images, recadrée sur un détail) ou une superposition de 5 images (contours dédoublés) a été regardée ; pas parce qu'il est « réduit d'un quart ». Si la mesure signale la plupart des plans, elle ne guide plus : bandes, directeur artistique, et les plans douteux listés pour l'œil de Diego. (Gagnée : V4 du film de mariage, livrée avec 68 plans sur 83 au-dessus d'un seuil hérité d'une autre caméra.)
- **D'abord l'intention du cadreur** : fixe voulu (on épingle le sujet) ou mouvement voulu « comme sur un rail » (on garde le trajet et l'allure, on retire la main). Stabiliser, c'est rendre fluide, pas figer (Diego : « il faut pas que ce soit fixe ») : vérifier que la trajectoire voulue est conservée (`tremblement.py STAB --avant ORIGINAL` : vitesse gardée entre 0,8 et 1,3).
- **Les leviers dans l'ordre** : Gyroflow (si le rush porte des données gyroscopiques), ralentir (un rush 50p lu à 50 %), couper là où le plan est calme, remplacer. Dix essais au plus, moins si c'est perdu d'avance, puis un autre plan qui joue le même rôle ; seule exception, le tremblement voulu par le brief. (Diego : « un plan qu'on ne peut pas stabiliser, on le remplace » ; « pourquoi il n'a pas essayé de les ralentir ? »)
- **Mesurer le résultat, pas la méthode** : un plan « stabilisé et prouvé » peut trembler plus que le brut ; on compare le plan rendu, à mesure égale, et on garde le brut s'il est meilleur. Pour chaque plan stabilisé, vérifier dans la timeline que le média posé est bien le fichier stabilisé, puis regarder le plan rendu en bande. (Gagnée : un rendu Gyroflow « prouvé » tremblait sept fois plus que le brut.)
- **Une animation** (zoom, titre, transition) : courbe de position et de vitesse mesurée sur le rendu ; une vitesse constante, sans accélération ni freinage, signe l'amateur (gagnée : le titre « grossi uniformément » de la V2 du film de marque). Recettes : `montage-after-effects`.

Recettes de stabilisation (Gyroflow en ligne de commande, rail par clés) : `montage-resolve`, [recettes.md](../montage-resolve/recettes.md).

## 3. Contrôles avant chaque rendu (liste maître ; le carnet donne les mots de Diego et les images)
Sur le passage exact de chaque plan (première, milieu et dernière image, pleine résolution) :
1. Il montre ce que `plan.md` dit qu'il montre (une personne attendue est à l'image). (carnet 20)
2. Aucun remplissage : sujet net et raison écrite ; un effet sert la suite, le sens ou le rythme (le meilleur collage prépare le plan suivant). (11, 15)
3. Un flou est volontaire, sinon il sort. (16)
4. Les visages sur toute la durée utilisée ; la valeur humaine repérée au dérush est gardée. (10, 19)
5. Mouvement : sous le seuil du projet et bande regardée ; un plan bon seulement à la fin est coupé là où il est bon ; dix essais, puis on remplace. (5, 21, 22)
6. Exposition et couleurs clés (peaux, blancs réels, couleur de la marque) constantes d'un plan à l'autre, sur tout le mouvement. (7, 8, 23)
7. Blancs et noirs jugés côte à côte avec la référence, jamais au seul compteur : la robe, le ciel, le produit gardent leur matière ; les ombres agrandies ne montrent pas le bruit. (6, 9)
8. Tout élément graphique a sa ligne dans `da.md`. (12)
9. Détourage et plan produit vus à 200 % ; propre au bord ne veut pas dire « pas cheap ». (12, 24, 27)
10. Aucune transition de bibliothèque (glissement, poussée, volet), sauf parodie demandée. (3)
11. Parole coupée au mot près ; la re-transcription du rendu se lit en phrases complètes. (26)
12. Photosensibilité : tout effet ajouté (flash, inversion, fonds rapides) ; les flashs réels des rushes seulement en salve de plus de 3 par seconde ; un flash isolé ne fait jamais retirer un beau moment. (Diego, 2026-10-12 ; carnet 35)
13. Les règles du genre (doublons de moment, un son par transition…) : skill du genre (`montage-formats` en donne l'index).

Puis, sur le fichier encodé : loudness et crête (`qc_livraison.sh`).

## 4. Le verdict « livrable »
Livrable seulement si : (1) le directeur artistique dit « au niveau », ou chaque désaccord est écrit dans la note de livraison ; (2) le fichier passe `labo/outils/qc_livraison.sh` (pistes, crête ≤ −1 dBTP, noirs de début et de fin) (gagnée : six fichiers livrés du studio sur sept au-dessus de −1 dBTP) ; (3) s'il y a un effet ajouté de flash, d'inversion ou de fonds rapides, ou une salve de flashs réels de plus de 3 par seconde, il passe `labo/photosensibilite/flash_check.py` ; (4) s'il y a de la parole, la re-transcription du rendu se lit en phrases complètes (`montage-grammaire`).

## 5. L'autocritique montre ou doute ; elle ne coche pas
Pour chaque point qui compte : l'image ou la mesure qui le prouve (chemin du fichier), sinon « à vérifier » et ce qu'il faudrait pour le savoir. En tête : ce que je n'ai pas pu percevoir (mouvement, son, durée), minuté, qui passe tel quel dans la note de livraison. Le jugement de niveau est celui du directeur artistique, pas le mien : on juge mal ce qu'on vient de faire. (Gagnée : V3b du film de mariage, vingt coches du carnet pour un film noté 10 %.)

## 6. Rien n'est figé
Après chaque série de corrections, relire le film entier comme si on le découvrait : rythme d'ensemble, calage, enchaînements, équilibre des blocs ; une correction locale peut casser ailleurs. Seul ce que Diego a validé explicitement est fixé, et même ça peut bouger si le film l'exige. Tout plan remplacé hors de ses retours s'écrit dans la note de livraison : quel plan, pourquoi, par quoi. (Diego : « mon silence n'est pas une validation » ; gagnée : V5 du film de marque, un plan d'ouverture remplacé sans le dire.)

## 7. Mesurer avant de corriger, et douter de l'outil qui me donne raison
Une mesure qui me donne raison trop facilement se vérifie contre la norme ou contre l'image. (Gagnée : un contrôle de flashs « plein écran » trop indulgent en phase 1 ; en phase 3, `flash_check.py` qui échoue même sans flash, « 0 % de pixels à 250 » sur une robe sans matière, un seuil de tremblement hérité.)

## 8. La technique pure
Avant de déclarer une limite technique, vérifier l'état de l'art et l'essayer ; si l'outil manque, le demander (`CLAUDE.md`, liste des moyens). Un résultat technique ne se déclare pas réussi : il se montre à Diego image par image (à 200 % pour un ralenti interpolé). (Diego, 2026-10-12.)
