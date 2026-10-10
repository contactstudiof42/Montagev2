# Labo grammaire — la règle des 180°, mesurée (session 7, 2026-10-10) — [TESTÉ EN LABO]

`blender -b -P axe180.py -- ../rendus/axe180` (Blender 4.2.3, ~5 s pour 7 images 320×180) ; planche `axe180-planche.png`, mesures `axe180-mesures.json`.
Deux personnages se font face sur l'axe X (A orange à gauche, B bleu à droite) ; le « nez » donne la direction du regard. Pour chaque caméra, le script projette la tête et le nez dans le cadre (`world_to_camera_view`) et en déduit le sens du regard **à l'écran**.

| Caméra | Côté de la ligne | Personnage cadré | Regard à l'écran | Amorce de l'autre |
|---|---|---|---|---|
| E (ensemble) | -Y | A et B | A → droite, B → gauche | — |
| A1 | -Y (bon) | A | droite | — |
| B1 | -Y (bon) | B | gauche | — |
| A2 | +Y (franchi) | A | **gauche** | — |
| A1 amorce | -Y (bon) | A | droite | épaule de B à droite (x = 1,10) |
| B1 amorce | -Y (bon) | B | gauche | épaule de A à gauche (x = -0,10) |
| A2 amorce | +Y (franchi) | A | **gauche** | épaule de B **à gauche** (x = -0,10) |

Lecture :
- A1 → B1 : regards opposés (droite / gauche) : ils se parlent. A2 → B1 : **les deux regardent à gauche** : à l'écran ils regardent dans la même direction, comme s'ils parlaient à un tiers. C'est le faux raccord, et il est mesurable par un simple signe.
- En amorce, franchir l'axe se voit **deux fois** : le regard s'inverse et l'épaule de l'autre saute de bord. L'amorce aide à situer, mais elle rend l'erreur plus visible.
- Un contrôle automatique est possible dès qu'on connaît la position de la caméra et des personnages (3D, ou tracking 2D en post) : *dans un champ / contrechamp, les signes des regards doivent être opposés*. Utile en phase 2 pour un agent qui monte des plans Blender ou des rushes avec métadonnées.
Limites : personnages centrés (x = 0,5), sans aire de regard ; pas de test de la règle des 30 % ni du franchissement « propre » (travelling qui traverse, plan dans l'axe). À faire.

## Outil généralisé : `sauts_regard.py` (session 8, BACKLOG 48) — [TESTÉ EN LABO]
`python3 sauts_regard.py <edl.json> <mesures.json>` : liste, pour chaque version d'un montage, les coupes où deux personnages différents regardent du même côté de l'écran. Plans à deux personnages ignorés ; un plan en mouvement fournit `<plan>_debut` / `<plan>_fin`.
Validation sur l'atelier 11 (`mesures_atelier11.json`) : v1 0 saut, **v2 et v4 : 1 saut à 7,6 s** (le franchissement voulu), v3 0 (travelling). Test d'un franchissement **partiel** (`edl_test_partiel.json` : A1 → B2 → A1 → B1) : **2 sauts** (aller et retour), là où le franchissement complet n'en fait qu'un : la différence entre l'erreur et le parti pris est comptable.
Usage phase 2 : un agent qui monte des plans Blender (positions connues) ou des rushes trackés peut lancer ce contrôle avant export et signaler chaque saut non voulu.
