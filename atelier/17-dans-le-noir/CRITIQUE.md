# Pièce 17 « 3 h 12, dans le noir » — critique (session 11)
Planches : une image par seconde (0 → 9 s), `planche.py` (luminance moyenne par seconde imprimée).

## v1 — `v1-planche.png` : écran bleu froid, tenu devant la poitrine, caméra de face (l'anti-référence attendue)
- Luminance : 0,007 → 0,188 à l'allumage (×27) puis stable.
- **Lecture d'un inconnu** : une figure frontale, symétrique, une tête blanche qui luit au-dessus d'un rectangle lumineux : **une apparition, un autel**, pas « un parent et un bébé ». Le bébé est invisible. Critères 1 et 4 échouent.
- Je m'attendais à l'horreur « lampe torche sous le menton » ; le défaut réel est autre : **la symétrie frontale + une source au centre = une icône**. Et l'écran éclaire toute la pièce (murs bleus jusqu'aux bords) : aucun téléphone ne fait ça, le noir n'existe plus. **L'énergie de la source décide si le noir reste un noir.**

## v2 — `v2-planche.png` : écran chaud (mode nuit), posé sur l'accoudoir, caméra de trois quarts
- Luminance : 0,004 → 0,105, stable.
- Le registre change complètement : chaud, enveloppant, on est dans une chambre. **Mais** les zones les plus claires sont **le dossier du fauteuil et le mur** : la lumière part vers le mobilier, et le regard avec elle (règle 12 de `montage-regard`, la saillance, encore). La couverture n'est qu'une tache blanche ; le parent et le bébé ne se lisent pas.
- **Bug de mouvement trouvé en préparant la v3** : le bercement est écrit `sin(2πt/P(t))` avec une période qui s'allonge ; la fréquence réelle tombe à 0,02 Hz vers 4-6 s : le bercement **se fige puis repart**, au lieu de s'apaiser (mesuré : `labo/ae-expressions/bercement/test.js`). v1 et v2 ont ce défaut ; v3 intègre la phase.

## v3 — tenu bas devant les genoux, écran incliné vers la couverture, bras qui portent, énergie /4 (`v3-essai-image80.png` ; planche : voir plus bas)
- Image d'essai (6,6 s) : la lumière tombe sur **les bras et la couverture** ; le visage du parent reste **dans l'ombre au-dessus** (les yeux cachés, à la Willis : ce n'est plus son visage qui compte, c'est ce qu'il tient) ; le mobilier retombe dans le noir. On lit « quelqu'un qui tient quelque chose de précieux dans une lueur ». Le bébé lui-même reste peu lisible (formes primitives).
