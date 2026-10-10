# Pièce 13 « Le fond raccorde » — critique (v1, v2, v3)

Planche : `planche-v1-v2-v3.png` (ligne 1 = v1 « le fond seul », ligne 2 = v2 « la lumière », ligne 3 = v3 « deux mondes » ; 8 plans alternés A/B). Mesures : `mesures.json` (`mesure.py` : Lab de la peau sur un masque rendu, Lab du mur, ΔE76 de la peau par rapport au premier plan du personnage, et teinte perçue **estimée** par un modèle d'induction chromatique simple, k = 0,2 — hypothèse, pas perception mesurée). Tout est généré dans Blender ; aucun média tiers.

Essai préalable (`test`) : visages surexposés (peau presque blanche), tête flottante, cadres centrés. Corrigé : clé 120 → 45 W, cou, visage décalé pour laisser l'espace devant le regard.

## Mesures clés (plan 3 de B, la dernière marche)
| version | ΔE peau B (mesuré) | mur B (a*, b*) | peau B perçue estimée (a*, b*) | lecture |
|---|---|---|---|---|
| départ | 0 | (0, 0) | (5,0 ; 7,2) | — |
| v1 fond seul | **1,7** (rebond du mur) | (−0,8 ; −21,6) | (5,0 ; **10,0**) : *plus chaude* | B isolé dans un monde froid |
| v2 lumière | **6,5** | (−0,7 ; −2,6) | (3,2 ; **2,7**) : grise, lilas | B change physiquement (malade, éteint) |
| v3 deux mondes | 1,7 (B) / 1,6 (A) | B (−0,8 ; −21,6), A (6,8 ; 20,1) | A perçue (4,3 ; **5,0**) : *plus pâle* | la relation se coupe |

## Ce que je vois et ce que j'en pense
1. **v1 : le fond froid ne refroidit pas le personnage, il l'isole.** Contre le bleu, la peau ressort *plus chaude* (contraste simultané, cohérent avec la planche : le visage de B au plan 3 paraît plus rose que dans v2). Le spectateur attribue le froid **au monde autour de B**, pas à B. C'est juste pour « il se retrouve seul », faux pour « il devient froid ». La progression en 4 marches se lit (marche 1 timide, 2 et 3 nettes) sans jamais faire effet.
2. **v2 : la lumière froide change le corps.** La peau devient grise et lilas (ΔE 6,5) : on lit « il pâlit, il s'éteint » — plus fort, plus physique. Mais A et B sont dans la même pièce, face à face : la lumière de B change et pas celle de A, **sans source visible** : c'est un faux raccord lumière, sauf à le motiver (un écran, une fenêtre, un nuage) ou à l'assumer comme sortie du réalisme.
3. **v3 : deux mondes, c'est le plus graphique et le plus démonstratif.** Paradoxe utile : le mur orange de A **pâlit** son visage (b* perçu 7,6 → 5,0). Réchauffer le fond refroidit la peau, et inversement. C'est la logique du *teal and orange* : un fond froid fait ressortir une peau chaude. À réserver aux récits où la séparation est le sujet (rupture, deux camps) ; sinon c'est un schéma de manuel.
4. Recommandation pour « B se ferme » : **v1 jusqu'à la marche 2, puis une seule marche de lumière (v2) au moment de la bascule** — le monde se ferme d'abord, puis le corps.

## v4 « le monde, puis le corps » — `planche-v4.png` (paires 2B → 3B de v1, v2, v4)
- Dernier plan de B : mur inchangé (marche 2), clé refroidie d'une marche. Peau ΔE 4,7 ; teinte perçue estimée b* 8,7 → 6,2 : **le visage pâlit alors que le monde ne bouge plus**. C'est la marche la plus discrète des trois paires et la plus juste : le changement se lit comme venant de B, pas du décor, et il arrive une seule fois, à la bascule.
- Le faux raccord lumière de v2 existe toujours, mais réduit à une marche, sur un seul plan : il passe pour un état, pas pour une erreur. À motiver en tournage (B s'écarte d'une lampe, un nuage) si le film est réaliste.
- **v4 = référence.**

## Limites
- Modèle d'induction très simplifié (k fixe, pas de dépendance à la surface ni à la luminance) : les sens des décalages sont conformes à la littérature sur le contraste simultané, les amplitudes non. Test avec des spectateurs en phase 2.
- Têtes abstraites, pas de vraie peau (diffusion sous-surfacique absente) ; plans fixes, pas de montage vidéo rendu (la planche suffit pour la question).

## Versé dans les skills
`montage-couleur-et-intention` : le fond est attribué au monde, la lumière au corps ; un fond froid réchauffe la peau perçue.
