# Labo saillance — session 9, 2026-10-10 — [TESTÉ EN LABO, modèles seulement ; aucun oculomètre]

BACKLOG 52. Question : mon indicateur maison de l'atelier 12 (`atelier/12-inquietude-calme/mesure.py` : fenêtre la plus lumineuse × contrastée) est-il confirmé par un modèle publié ?

- `residu_spectral.py plan1.png plan3.png` : saillance par **résidu spectral** (Hou et Zhang, CVPR 2007) : image réduite à 64 px, log-amplitude moins sa moyenne locale, reconstruction avec la phase, flou. **Piège rencontré** : sans précaution, le pic tombe dans un coin (la FFT traite l'image comme périodique, les bords opposés se raccordent mal) ; marge de 6 % exclue.
- Sorties : pic de saillance du plan 1, distance du pic à l'anomalie, saillance moyenne de la zone de l'anomalie rapportée à la moyenne de l'image, centile de la zone.

## Pièce 12 (`resultats-piece12.txt`)
| version | maison : distance zone saillante → anomalie (% diag.) | résidu spectral : centile de la zone | zone / moyenne |
|---|---|---|---|
| v1 (pièce noire) | 23,0 | 85,2 | 2,04 |
| v2 (clinique) | 16,6 | 78,7 | 1,40 |
| v3 (soleil au sol, table sombre) | 14,6 | **88,6** | **2,24** |
| v4 (soleil sur la table, fenêtre dans le cadre) | **34,4** (pire) | **62,8** (pire) | 0,89 |
| v7 (45 mm) | **9,0** (meilleur) | 74,7 | 1,26 |

## Lecture
1. **Accord sur l'essentiel** : les deux modèles jugent la v4 la pire, celle dont j'étais content à l'œil. La règle « mesurer avant de croire qu'on guide le regard » tient.
2. **Désaccord v3 / v7** : le résidu spectral (sensible aux petits objets isolés) préfère la v3, où la tasse blanche se détache sur une table **sombre** ; mon indicateur (sensible aux grandes plages claires) préfère la v7, où la table est au soleil. Les deux ont raison sur un point différent : **éclairer la zone y attire l'œil, mais peut éteindre le contraste du détail lui-même** (blanc sur clair).
3. Conséquence pour l'atelier 12 (v8, BACKLOG 50) : garder la zone désignée (cadre, centre, flaque de lumière **à côté** de la tasse) tout en laissant la tasse se détacher sur un fond plus sombre : flaque de lumière sur la chaise vide, tasse à la lisière.

## Limites
Deux modèles bas niveau, aucun spectateur. Les modèles appris (DeepGaze, etc.) et un vrai test humain (PLAN-TESTS 44) restent à faire.
