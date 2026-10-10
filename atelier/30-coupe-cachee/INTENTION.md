# Pièce 30 « Coupe cachée » — intention (session 24, 2026-10-10)

Source : `culture/shorts-narratifs-verticaux.md` (principe 4 : **cacher la coupe quand l'effet est la continuité**, Zach King ;
la montrer quand l'effet est la comparaison). Format : Short vertical 9:16, 8 s, 270×480, 25 i/s, 2D (Pillow), sans son
(principe 1 : lisible sans le son).

**Effet visé** : « c'est magique ». Une tasse sur une table ; un torchon passe devant ; c'est une plante. Lisible en 1 s,
une seule idée, la chute est la dernière image.

**Question de métier** : qu'est-ce qui trahit une coupe cachée ? Le cache couvre l'objet, mais la vie hors du cache
(une trotteuse d'horloge, la lumière d'une fenêtre, un pied de caméra effleuré entre les deux prises) continue.
Je simule deux prises réelles : la prise 2 est tournée 37 s plus tard (trotteuse décalée), la lumière a bougé de 6 %, la caméra de 2 px.

**Versions**
- A : torchon qui couvre **tout le cadre** à l'image de coupe ; prises non raccordées.
- B : pas de torchon, coupe sèche au même instant (la comparaison, pas la magie).
- C : torchon étroit qui ne couvre que l'objet ; prises non raccordées.
- D : torchon étroit, prises **raccordées** (horloge retirée du décor, lumière et caméra verrouillées) : la préparation de plateau.

**Mesures** : score scdet à l'image de coupe (la coupe est-elle « vue » par un détecteur ?) ; écart hors objet entre
l'avant et l'après du passage (l'erreur de raccord qui reste visible une fois le torchon passé).
**Critère** : la version retenue n'est détectée ni par scdet ni par l'œil sur la planche, et sa chute se lit en 1 image.
