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
