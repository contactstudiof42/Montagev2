# Labo 88 — l'écart d'un écho de poses (session 20, 2026-10-10) [TESTÉ EN LABO, image fixe]

But : éprouver la règle hypothétique de `culture/` (fiche Marey / Muybridge) : < 0,3 largeur de tête = traînée ; 0,5-1,5 = trajectoire ; > 2 = écho ; > ~4 = plusieurs personnes.

`python3 echo.py planche-ecarts.png [--uniforme]` : un marcheur filiforme blanc sur noir, 6 poses, écarts 0,2 / 0,5 / 1 / 2 / 4 têtes. Mesures (`.json`) : IoU de deux poses voisines, nombre de composantes connexes du composite.

| Écart (têtes) | IoU voisins | Composantes | Lecture (dégradé : anciennes poses plus pâles) | Lecture (uniforme) |
|---|---|---|---|---|
| 0,2 | 0,24 | 1 | traînée : un corps flou, on lit la vitesse | idem |
| 0,5 | 0,12 | 1 | éventail emmêlé : ni vitesse ni positions (la pire zone) | idem |
| 1 | 0,05 | 1 | **chronophotographie** : un corps décomposé, trajectoire lisible | un corps démultiplié (Duchamp) |
| 2 | 0 | 3 | écho : **un seul marcheur** qui laisse sa mémoire | **une file de six personnes** |
| 4 | 0 | 6 | une procession ; le dégradé relie à peine | six personnes |

## Ce que ça établit
1. La règle tient pour 0,2, 1 et 4. **0,5 est une zone morte** : trop recouvert pour lire les positions, trop séparé pour faire un flou. Choisir 0,2 ou 1, jamais entre les deux.
2. **Le dégradé de mémoire fait l'identité, plus que l'écart** : à 2 têtes, des poses égales se lisent comme plusieurs personnes ; des poses qui pâlissent avec l'âge se lisent comme un seul corps. Le seuil « plusieurs personnes » passe de ~2 à ~4 têtes avec le dégradé.
3. Le nombre de composantes connexes du composite est un indicateur simple : 1 = un corps (traînée ou chronophotographie) ; N = N silhouettes séparables. Il ne dit pas si on les relie (c'est le dégradé qui le dit).

## Régler l'écart en images (pièce 20, rush à strobe)
écart en images = (écart visé en têtes × largeur de tête en px) ÷ (vitesse du sujet en px/image). Exemple : tête 40 px, sujet à 20 px/image, écho à 2 têtes → une pose toutes les 4 images. Mesurer la vitesse sur deux images du rush, pas à l'œil.

## Limites
Image fixe, marcheur filiforme, fond noir. En mouvement, l'écho se renouvelle et la lecture peut changer ; un vrai corps (volume, vêtements) recouvre plus qu'un filiforme à écart égal. À refaire sur le rush à strobe (BACKLOG 84) et dans AE (Echo, Time Displacement : PLAN-TESTS 61).
