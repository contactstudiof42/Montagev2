# Pièce 14 « Balancier » — critique (A contre B)

Planches : `A-planche.png`, `B-planche.png` (2 images/s, 15 s). EDL : `edl-A.json`, `edl-B.json` ; mesures : `mesures.json`. Rendus : `atelier/rendus/14/` (ignorés). Tout est généré (Blender, son en numpy : grincement de crochet synthétique à chaque point mort, souffle de pièce ; whoosh en bruit filtré pour B). Aucun média tiers.

## Ratés avant le montage
- 1er rendu : le cône de l'abat-jour était **fermé à sa base** (option par défaut du cône Blender) : la lampe n'éclairait la table qu'en biais, jamais à la verticale. Vu sur une planche de 6 images à 40 images rendues ; rendu arrêté, `end_fill_type="NOTHING"`. Leçon : **planche de contrôle dès les premières images** d'un long rendu (règle 3 du regard, appliquée à temps cette fois).
- Rendu réduit à 256×144, 6 échantillons, pour tenir la session (~1,7 image/s).

## Mesures
- Période du balancier 2,006 s (pendule de 1 m), amortissement τ = 6 s : à 15 s l'amplitude n'est plus que 8 % de celle du départ.
- **A** : 3 plans (large 0-7 s, serré 7-12 s, large 12-15 s), coupes aux images 177 et 302, **à 0 image d'un point mort**.
- **B** : 19 plans, durée médiane 1,0 s ; une coupe par point mort, puis par demi-période après 10 s (accélération finale), whoosh sur chaque coupe.

## Ce que je vois
1. **A laisse le sujet faire le rythme.** Le large montre la cause (la lampe) et l'effet (la lumière qui balaie le mur) ; le serré montre l'ombre de la tasse qui va et vient sur la table ; le retour au large montre que **presque plus rien ne bouge**. L'épuisement se voit parce que le cadre ne change pas pendant qu'il se produit : le spectateur compare le balancement à lui-même.
2. **B contredit son sujet.** La coupe impose une pulsation de 1 s constante (et l'accélère à la fin) pendant que la lampe ralentit : le montage **fabrique l'énergie que le sujet perd**. On ne voit plus l'amortissement, on voit une alternance. Les whooshs ajoutent une urgence que rien ne motive. B serait juste pour un autre sujet (une lampe qu'on secoue, une scène de panique), pas pour « l'énergie de quelqu'un qui s'épuise dans un objet ».
3. Coupe sur les points morts (A) : la lampe est immobile une fraction de seconde à l'image de coupe ; le raccord est invisible, la coupe ne prend rien au geste. Couper au milieu d'un passage (comme B après 10 s) casse le mouvement en deux et se voit.
4. **Défaut de A** : le serré est nettement plus clair et plus chaud que le large (la lampe est proche de la table, focale 50 mm, mêmes réglages d'exposition) : saut de lumière au raccord. Il faudrait baisser l'exposition du serré d'environ 1 diaphragme, ou l'assumer comme rapprochement de la source. v2.
5. Jugement : **A = référence.** Le principe de Jonze tient : quand le sujet porte son propre tempo, et surtout quand ce tempo change (amorti, accéléré), le montage doit se retirer pour que le changement se voie.

## Versé dans les skills
`montage-rythme` (le tempo propre du sujet, couper sur les points morts) et `montage-kinetic-editing` (quand ne pas l'utiliser : le kinetic écrase un tempo qui évolue).

## v2 (`v2.py`, `A2-planche.png`, `B2-planche.png`)
- Correction de mon idée de départ : un pendule est **isochrone** (sa période ne dépend pas de l'amplitude), donc « des coupes qui ralentissent avec la lampe » n'a pas de sens physique. Ce qui décroît, c'est l'amplitude, donc l'énergie.
- **Serré à −1 diaphragme** (en linéaire, ×0,5) : luminance moyenne 136 → 99 (large : 60, mais le large est surtout mur et sol sombres ; le serré ne cadre que la table éclairée, il doit rester plus clair). Le saut au raccord est réduit et devient un rapprochement de la source plutôt qu'un changement d'exposition. À juger en mouvement (phase 2).
- **B2 « kinetic honnête »** : coupes sur les points morts, de plus en plus espacées (1 s ×5, puis 2 s, 2 s, 4 s ; le dernier plan de 2 s casse la progression, défaut à corriger), whooshs proportionnels à l'amplitude. Le montage **suit l'énergie** du sujet au lieu de l'écraser : énergique au départ (le choc du départ, l'accroche des 2 premières secondes), puis il se retire.
- Jugement : A reste la plus juste pour un film (le spectateur est captif, l'épuisement se voit en continu) ; **B2 est la bonne version pour un réseau social** (accroche immédiate, puis retrait). Les deux obéissent au même principe : le montage suit le tempo et l'énergie du sujet. B (pulsation constante) est la seule fausse.
