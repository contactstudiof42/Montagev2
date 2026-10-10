# Pièce 28 « Flou → net » — critique (session 23)

Commandes : `blender -b -P atelier/28-flou-net/scene.py -- atelier/rendus/28 1 --sharp` (plaque nette) puis `… -- atelier/rendus/28 0.4,1.5,5,15,45` (5 mises au point, ~6 s par image en Cycles 24 échantillons, 640×360). Planche : `v1-planche.png` (net ; optique à 0,4 / 1,5 / 5 / 15 / 45 m ; post gaussien r = 2, 6, 14 px). Mesures : `v1-mesures.json` (variance du laplacien par zone).

## Ce que montre la planche
1. **Le flou optique rend les hautes lumières plus grandes, pas plus ternes.** À une mise au point de 1,5 m, chaque reflet devient un **disque** net et clair (bokeh) ; le monde flou est **lumineux et doux**. Le gaussien de post étale la même énergie en tache grise : à r = 14 px, les reflets ont disparu, le monde flou est **terne**. Pour la pub (« émouvant mais pas triste »), c'est décisif : le flou optique dit « rêverie », le gaussien dit « malade ». L'affirmation de l'examen est confirmée, et j'ai maintenant la raison exacte.
2. **Le flou optique dépend de la distance ; le gaussien non.** Le montant de fenêtre devient un voile sombre quand on fait le point au loin, et reste net quand on fait le point sur lui : la profondeur se lit par **ce qui échange sa netteté**. Le gaussien floute la fenêtre et les chevaux ensemble : on perd la vitre, donc le train, donc le point de vue.
3. **Mise au point de départ** : à 0,4 m (sur la vitre), les chevaux **disparaissent complètement** (dissous dans l'herbe) : on ne peut rien deviner, le garde-fou de l'examen (« on le devine dès 3 s ») est faux à ce réglage. À **1,5 m**, ce sont des silhouettes brunes reconnaissables comme « des animaux » sans être des chevaux : c'est le bon point de départ. À 5 m, ils sont déjà presque lisibles. **La bascule utile se joue entre 1,5 et 15 m**, pas entre 0,4 et 45 m : sur un moteur de mise au point, c'est là que la courbe doit ralentir.
4. **Faute de mesure (utile)** : j'ai voulu égaler les deux flous par la variance du laplacien sur le cheval. Le gaussien r = 2 « égale » la MAP 0,4 m (4,1 contre 3,7) alors qu'à l'œil le cheval y est parfaitement lisible et que l'optique l'efface. Cette mesure ne voit que le détail le plus fin ; elle sature dès 2 px de flou et ne dit **rien de la lisibilité d'une forme**. Pour juger « deviner / voir », il faut une mesure à l'échelle de l'objet (contraste local à la taille du cheval) ou l'œil sur planche.

## Grille
- Intention servie : oui pour la question technique ; la pièce ne fait pas encore la courbe temporelle (3 vitesses de bascule) : à faire (Y31 suite).
- Limites : chevaux en boîtes, pas de respiration de focale (le grossissement qui change avec la mise au point sur un vrai objectif), pas de vibrations du train, Cycles 24 échantillons (léger bruit).

## Ce qui change dans l'examen n°12
- Départ de la mise au point vers 1,5 m (pas sur la vitre), et la vitre reste dans le cadre en voile : elle dit « train » sans un plan de plus.
- Le flou ne se fait pas en post : si l'optique ne suffit pas au montage, partir de la prise nette et **défocaliser avec un flou de lentille à profondeur** (carte de profondeur, bokeh en disque), jamais un gaussien.

## v2 — la bascule dans le temps (40 mises au point de 1,5 à 45 m, espacées en log ; Cycles 12 échantillons, 97 s pour les 40)
Fichiers : `v2-bascule.png` (10 des 40 images recadrées sur les chevaux, avec la distance et r), `v2-lisibilite.json`, `v2-courbes.json`.
- **Mesure à l'échelle de l'objet** (corrige la faute de v1) : corrélation entre l'image et la plaque nette, sur la zone des chevaux réduite au quart (on compare des formes, plus des pixels). Seuils **calibrés à l'œil sur la bande** : r ≈ 0,85 = « des animaux » (silhouette devinée), r ≈ 0,95 = « des chevaux » (lisible), r ≥ 0,99 = plus aucun changement visible.
- **Constat** : tout le changement perceptible se joue entre **1,5 et ~5-8 m** (35 % de la course en log distance). Au-delà, la mise au point bouge encore mais l'image ne change plus.
- **Trois courbes classiques sur 15 s** (moment où l'on devine / où c'est lisible / temps mort final où rien ne change) :
  - linéaire : 1,6 s / 4,4 s / **8,2 s de temps mort** ;
  - rapide puis pose (le geste naturel d'un pointeur, ease-out) : 0,7 s / 2,0 s / **11,8 s de temps mort** : la révélation est finie avant que le spectateur ait compris qu'il regardait quelque chose ;
  - lente puis rapide (ease-in) : 6,1 s / 9,2 s / 4 s.
  - **sur mesure** (1,5 → 5 m en 12 s, puis 5 → 45 m en 3 s) : **3,6 s / 10,0 s / 2,5 s** : on devine tôt, on voit tard, et les 2,5 s restantes servent à compter.
- **Leçon** : une bascule de point se dessine sur la **plage perceptive** (là où l'objet passe de silhouette à lisible), pas sur la distance. Sur un moteur de mise au point, programmer la courbe en conséquence (la majeure partie de la durée sur 1,5-5 m), et vérifier sur une bande de netteté avant le tournage. Le geste « naturel » d'un pointeur (rapide puis pose) est exactement l'inverse de ce que veut une révélation lente.
- **Correction de l'examen n°12** : le comptage commence quand les chevaux sont lisibles, soit vers 10 s, pas à 6 s ; la seule coupe (17 s) peut rester.
