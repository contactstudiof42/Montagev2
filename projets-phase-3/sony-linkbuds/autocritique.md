# Autocritique — Sony LinkBuds Clip, V5

_2026-10-11. Rendu `videos/phase-3/sony-linkbuds/rendus/sony_linkbuds_V5.mp4`. Relu en entier d'un œil neuf (planche du film, une image sur six), carnet de goût relu entrée par entrée. Autocritique V4 : `archives/phase-3/sony-linkbuds/V4/autocritique.md`. Par ordre de gravité._

## Ce qui ne va pas encore
1. **Le son n'a jamais été écouté.** Le pic (33,2-37,9 s) porte maintenant huit sons nouveaux par-dessus un riser de 4,7 s : la loudness et la crête tiennent (−13,9 LUFS, −1,1 dBTP), mais l'encombrement ne se mesure pas. Si c'est trop chargé, le riser (−16 dB) est le premier à baisser ou retirer.
2. **Le bloc 4 (9,4-18,7 s) est le plus long et peut paraître répétitif** : six plans de fentes « mains sur les hanches » à la suite (C6576, C6583, C6594, collage A1, C6580, C6581). C'est l'exercice filmé chez plusieurs participantes, une raison de montage existe, mais je n'ai pas tranché sans toi.
3. **Synchronisation Gyroflow de C6725 non prouvée** : le mouvement est trop faible pour mesurer le décalage gyroscope / image (corrélation faible) ; décalage imposé à 0. Le résultat, lui, est mesuré : 0,66 px de tremblement après le rail.
4. **Mes deux mesures du tremblement se contredisent sur les packshots** (points suivis sur la texture contre centre des zones claires) : la seconde dépend de l'exposition, la première est réputée fragile sur le tapis en carbone. J'ai tranché avec la première et vérifié à l'image, mais aucun chiffre n'est sûr à 0,5 px près.
5. **Le lavande du premier packshot tire un peu vers le rose** (LUT « jour ») ; l'exposition est juste (le boîtier garde sa matière), la teinte exacte du produit n'a pas été comparée à une photo Sony du coloris.
6. **Le pic est calculé hors de Resolve** (ProRes 4444 posé tel quel) : impossible à retoucher dans Resolve sans relancer `labo/outils/phase3/v5/pic_v5.py`.
7. Packshots : 5 s en tout, calés sur le dernier coup de la musique (1072). Si la fin te paraît encore longue, on peut retirer un coup (47 images) au dernier packshot, mais il faut alors couper la musique ailleurs.

## Ce qui a bougé hors de tes retours (règle « rien n'est figé »)
- **Packshots** : la V5 en cours les avait passés en Gyroflow seul (pour la preuve) ; ils tremblaient 3 à 6 fois plus que dans la V4. Correction « rail » rétablie après Gyroflow : 0,66 / 0,68 / 0,84 px.
- **C6627 (7,96 s)** : yeux fermés et menton rentré sur 4 images sur 6 ; remplacé par un autre moment du même rush (12,3 s), yeux ouverts, la sangle KORE qui monte.
- **Rafale rouge** : le troisième négatif (802) retiré, sinon 4 flashs dans une seconde avec le bras clair de C6676 juste après.
- **Boîtiers (117)** : essai d'un rendu Gyroflow synchronisé : il tremblait 7 fois plus que le rush brut, déjà stable. Le brut reste.
- **Grain** : 35 → 20 %.

## Contrôlé et juste
0 doublon (99 plans, sources du pic comprises) ; photosensibilité ≤ 3 flashs par seconde sur tout le film ; noirs à 0 sur les plans de salle, ombres propres amplifiées ×4 ; aucun blanc brûlé dans les boîtiers hors flash ; ouverture : béton égal sur les quatre lettres et le large (0,36-0,37), large KORE sans blanc brûlé ; visages de tous les plans vus image par image ; chaque transition a son son, calé à l'image (`sfx.md`) ; le pic suit les attaques de la musique et la référence (états de l'image, respiration au milieu) dans notre palette.

## Carnet de goût, entrée par entrée
1 look ✔ · 2 titre (inchangé) ✔ · 3 aucune transition intégrée ✔ · 4 séries du cadreur ✔ · 5 mouvement vu et mesuré ✔ (packshots corrigés) · 6 blanc du produit ✔ · 7 exposition sur tout le mouvement ✔ (zoom E → KORE, crash zoom du pic) · 8 plan par plan ✔ · 9 noirs ✔ · 10 visages ✔ · 11 une raison par plan et par effet ✔ (`plan.md`) · 12 graphisme de la DA, détourages contrôlés ✔ · 13 pas de photo à bord blanc ✔ · 14 inversions ✔ · 15 aucun remplissage ✔ · 16 flous : C6612b (24 s) flou de mouvement qui se résout, gardé · 17 film relu en entier ✔ (point 2 ci-dessus) · 18 pic comparé à la référence ✔.
