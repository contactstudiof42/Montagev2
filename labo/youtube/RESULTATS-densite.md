# Labo densite.py — courbe d'événements par minute d'un long YouTube (session 21, 2026-10-10)

**Outil** : `densite.py decoupage.json sortie.png [--decroissante] [--max-plateau 240]` (Pillow seul, `pip install pillow` 4 s). Compte coupes, punch-ins, SFX, captions, inserts par minute ; contrôle promesse < 30 s, plateau sans relance ≤ 4 min, écran de fin 5-20 s ; en mode décroissant, densité par tranche de 3 min qui ne remonte pas de plus de 20 % et 1er temps long (< 8 év./min) après la 1re récompense.

**Vérité terrain** (`densite_tests.py`, découpages synthétiques, graine fixe) : 3/3 conformes [TESTÉ EN LABO]
- `B-examen11` (courbe visée de l'examen n°11 : 28 → 4 év./min) : OK. Planche : `densite-B-examen11.png`.
- `fautif` (promesse à 40 s, plateau de 10 min, densité qui remonte, écran de fin 30 s) : 8 échecs, tous attendus.
- `A-constant` (24 év./min, relance toutes les 3 min) : OK.

**Ce que la planche a appris (regard, pas technique)** : dans le découpage B de l'examen, chaque relance coïncide avec la **disparition d'un outil** : la densité **baisse** au moment même où il faudrait une relance. Une relance qui s'accompagne d'un creux se lit comme un essoufflement. Correction : **la relance garde l'outil une dernière fois (pic local), l'outil disparaît juste après** — l'objet part avec son dernier bruitage. Versé dans l'examen n°11 et `montage-youtube` (principe 20).

**Limites** : la dernière minute partielle (écran de fin) est ramenée à la minute (0 ici) ; la densité ne dit rien de la **force** d'un événement (un rire dans une pièce vide pèse plus qu'un bruitage) ; seuils 4 min / 20 % / 8 év. = hypothèses tirées du guide MrBeast et de mes examens, à confronter à de vraies courbes de rétention en phase 2.
