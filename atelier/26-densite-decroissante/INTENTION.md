# Pièce 26 — « Densité décroissante » (maquette, BACKLOG Y20, session 22)

**D'où elle vient** : examen n°11 (divertissement YouTube de groupe « chaque heure, on retire un objet de la maison », direction B : le montage perd ses outils avec la maison) et labo `labo/youtube/densite.py`, qui a révélé la faute « chaque relance coïncide avec la disparition d'un outil, donc avec un creux ».

**Intention** : vérifier sur une maquette qui bouge et qui sonne (pas seulement sur un tableau) que :
1. la **relance = pic** (l'outil sert une dernière fois, en rafale, puis disparaît) se voit et s'entend comme une relance, alors que la version de l'examen (l'outil disparaît à la relance) se lit comme un essoufflement ;
2. le **temps long final** (le plan de 40 s à la bougie) a besoin d'un **mouvement interne** (flamme, souffles, lumière qui dérive) pour ne pas être une image arrêtée — principe de la fiche slow TV.

**Forme** : pas une compression ×6,7 (3 événements par seconde : une bouillie qui ne dit rien de la vraie perception), mais un **échantillonnage** à densité réelle : six extraits de 25 s autour de chaque relance + l'extrait final de 40 s, séparés par un carton de 0,6 s qui donne l'heure du film (≈ 3:15 au total). Formes 2D (Pillow) : une pièce vue de face, 48 objets-rectangles, cinq personnages-ronds, un compteur fixe. Sons synthétiques (numpy) : musique (pulsation 120 bpm), bruitages « cartoon », whoosh des punch-ins, clic des captions, ambiance de pièce, porte-refrain.

**Versions prévues**
- **v1** : découpage de l'examen tel quel (l'outil part à la relance, la densité baisse tout de suite).
- **v2** : correction « relance = pic » (rafale de 3 s avec l'outil qui part, puis retrait).
- **v3** : v2 + mouvement interne dans les deux derniers extraits (flamme, souffle, dérive de lumière).

**Mesures** : événements par fenêtre de 5 s (depuis le découpage), activité visuelle (différence moyenne entre images, `signalstats` YDIF), loudness court terme par extrait (ebur128), planche contact (1 image / 5 s).

**Ce qui dira que c'est réussi** : autour de chaque relance, la v2 montre un pic net d'événements **et** d'activité visuelle, puis un palier plus bas ; la v1 un simple palier qui descend. Le plan final de la v3 a une activité visuelle non nulle et lente (≥ 10 fois plus faible que le début, mais pas zéro).

**Médias** : tout est généré (formes, sons) : aucune licence tierce.
