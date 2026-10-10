# Pièce 20 « La lumière écrit » (session 15, issue de l'examen n°8, BACKLOG 80)

**Intention** : éprouver en mouvement la direction A de l'examen n°8 avant de la proposer à qui que ce soit. 10 s, 9:16, 25 i/s, 128 BPM : une foule dans le noir, révélée par des coups de strobe retimés par saccade ; chaque coup révèle un nom de la programmation (noms inventés). Question unique : **la saccade se lit-elle comme un choix ou comme un bug ?**

**Hypothèse à tester** : si *tout* est figé entre deux coups, on croit à une panne de lecture ; si **quelque chose continue de bouger** (les lasers, qui ne flashent pas), l'image tenue se lit comme un arrêt voulu (la lumière fige, le monde continue).

Versions prévues :
- v1 : saccade automatique (une image sur 12 tenue, tout figé), noms qui apparaissent au hasard des coups ;
- v2 : coups choisis sur les noires (2,13 /s), tout figé entre deux coups, nom qui persiste en fondu ;
- v3 : comme v2, mais les lasers continuent de tourner en continu pendant les images tenues.

Mesures : `flash_check.py` sur chaque version ; planche contact ; critique. Média : tout est synthétique (numpy), aucun média tiers. Noms d'artistes inventés.
