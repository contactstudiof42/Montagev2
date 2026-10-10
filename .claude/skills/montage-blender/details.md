# Blender : détail des recettes et mesures (annexe de SKILL.md)

Déplacé de `SKILL.md` le 2026-10-10 (audit de fin de phase 1). Les en-têtes ont perdu leur numéro de session ; les références de pièces restent. Marqueurs : voir `SKILL.md`.

## Eau, objet qui tombe, ombre d'un personnage invisible (ateliers 04 et 06)
- Eau = simple plan animé en Z + Principled (IOR 1,33, transmission, bump d'ondes) : crédible en 8 échantillons + débruitage, ~1,2 s/image en 480×270 CPU [TESTÉ EN LABO]. Sous incidence rasante, l'eau est un **miroir** (Fresnel) : rien ne se devine sous la surface, quelle que soit la transmission [ÉPROUVÉ EN MAQUETTE] (atelier 04).
- **Vérifier que la caméra reste hors de l'eau** (ou de tout objet animé) à chaque image : tester images 1 et N, pas seulement le milieu.
- Plan de sol de 200 m + SUBSURF simple niveau 8 + DISPLACE (texture Wood band noise) = rides de sable ; un estran presque plat se découvre d'un coup quand l'eau passe sous sa hauteur moyenne (effet utile) [ÉPROUVÉ EN MAQUETTE].
- Paramétrer la scène par un JSON (caméra, courbe d'eau, plage d'images) pour ne rendre que les images utiles de chaque caméra (`atelier/04-maree-decouvre/v3-*.json`).
- Lancer plusieurs rendus en parallèle n'accélère rien sur CPU partagé ; `pkill -f motif` peut tuer le shell qui le lance (le motif figure dans sa propre ligne de commande) [TESTÉ EN LABO].
- **Objet qui tombe** (atelier 06) [TESTÉ EN LABO] : chute keyframée image par image (bascule de 6 images autour du bord, puis z = z0 - ½·g·t² à 25 i/s, impact calculé et imprimé par le script) ; **vérifier la pose de repos** : une rotation finale de -180° avec l'origine décalée a enfoncé la tasse dans le sol. Pour des variantes comparables : `cycles.seed` fixe et **aucune modification du script entre deux rendus** d'une même série.
- **Ombre portée d'un personnage invisible** [TESTÉ EN LABO] : un volume noir `visible_camera = False`, `visible_glossy = False` entre la source et le décor projette une ombre sans apparaître. 2 sources surfaciques, 480×270, 16 échantillons + débruiteur ≈ 2,5 s/image sur 4 cœurs.

## Corps rigides et Eevee sans écran (atelier 07)
- **Quand simuler plutôt qu'animer à la main** : quand la causalité est l'argument (chaîne à la « Cog », chute, collision). Une simulation est vraie dans le fichier ; elle donne les **images de contact exactes**, qui servent à placer les sons et à choisir où couper [ÉPROUVÉ EN MAQUETTE].
- Recette [TESTÉ EN LABO] : `bpy.ops.rigidbody.world_add()` ; `substeps_per_frame = 40`, `solver_iterations = 30` pour de petits objets (dominos de 9 cm, bille de 2,2 cm) ; formes `BOX` / `SPHERE` / `CYLINDER` ; `collision_margin = 0.001` ; frottement 0,7-0,8 pour que les dominos basculent au lieu de glisser. Lire les positions avec `sc.frame_set(f)` image par image depuis la 1re (JSON), puis `bpy.ops.ptcache.bake_all(bake=True)` avant le rendu. Une plage de rendu partielle se règle **après** le bake. Simulation de 200 images ≈ 1 s.
- **Piège n°1** : `transform_apply(scale=True)` applique aussi position et rotation par défaut ; l'origine part à (0, 0, 0), la forme `BOX` se centre dessus, les dominos se superposent et explosent. Toujours `transform_apply(location=False, rotation=False, scale=True)`.
- **Piège n°2** : un objet actif posé à moins de ~1 cm d'un autre part tout seul à l'image 2. Laisser du jeu, vérifier les premières images.
- **Réglage par lots** : la simulation seule (`mode: sim`) est quasi gratuite ; balayer 3 configurations et lire les images d'événements (`contacts.py`) avant de rendre.
- **Eevee en ligne de commande dans la VM** : plante sans `libEGL.so.1` ; après `apt-get install -y libegl1`, rend en OpenGL logiciel à **~7 s/image** en 480×270, plus lentement que Cycles (8 échantillons + débruitage : ~2 s/image seul, ~6-8 s à 6 rendus sur 4 cœurs). À réévaluer sur GPU (phase 2).
- **Amortir sans tricher** : `angular_damping = 1` dès le début empêche aussi la bascule (pièce 07 v2 : la tasse tombait debout, lu comme un trucage [ÉPROUVÉ EN MAQUETTE]). Mettre l'amortissement en clé **à partir de l'impact** (`rb.keyframe_insert("angular_damping", frame=f)`), testé en v3.
- Rendre plusieurs caméras en parallèle (un processus par caméra) : 4 images fixes de contrôle en 9 s.

## Déterminisme, plan immobile, caméra portée (ateliers 07-08)
- **La simulation est déterministe** (Blender 4.2.3, Bullet, CPU) [TESTÉ EN LABO] : `atelier/07-causalite/scene.py` en mode `sim` lancé 3 fois en parallèle donne trois `sim.json` identiques à l'octet (8 912 valeurs) ; événements identiques sur une autre VM. On peut monter sur les images de contact calculées une fois, puis rendre caméra par caméra. À revérifier sur le Mac (test 36 du `PLAN-TESTS-MCP.md`).
- **Plan immobile = une image** (pièce 08) : rendu 4 fois plus rapide ; le présent figé au pixel peut devenir un choix (temps arrêté), sinon ajouter un grain fin au montage.
- **Caméra portée crédible** [ÉPROUVÉ EN MAQUETTE] : somme de 2-3 sinus lents par axe (0,9 à 3 Hz, 0,6 à 0,9°), clé toutes les 2 images ; pas de bruit blanc (« séisme »). Zoom lent sur `data.lens` (38 → 56 mm sur 70 images). `atelier/08-souvenir/scene.py`.

## Un mouvement rendu une fois, placé plusieurs fois (pièce 22)
- Rendre le mouvement de caméra à **paramètre u régulier** (64-96 images), puis construire chaque version au montage par une **courbe temps → u** (`atelier/22-a-la-maniere-d-ego/montage.py`) : trois placements contre la voix pour le coût d'un rendu (~3 s/image, Cycles 8 échantillons, 480×270, 63 000 chaises par 2 modificateurs Array) [TESTÉ EN LABO].
- Limite : un palier lent étire peu d'images (saccades si u avance de moins d'une image rendue toutes les 2-3 images de sortie) ; densifier le rendu là où la courbe est lente [ÉPROUVÉ EN MAQUETTE]. Équivalent AE : remappage temporel (PLAN-TESTS 64).
- Brume par la passe Mist mélangée à la couleur du monde en compositing : le champ « se perd » au lieu de s'arrêter, sans volumétrie [ÉPROUVÉ EN MAQUETTE].

## AgX plafonne le blanc ; cadrage en image fixe ; moiré (pièce 22 v3)
- **Symptôme** : un monde « blanc clinique » reste gris malgré plus de lumière. **Diagnostic** [TESTÉ EN LABO] : pixel MAX (numpy) identique partout, ciel compris (222-225 / 255 avec AgX + « Base Contrast », exposition +1) → le plafond vient de la **transformée de vue**. AgX compresse les hautes lumières et n'atteint le blanc qu'à des valeurs de scène très hautes.
- **Correction** : à l'étalonnage. Courbe de point blanc (`curves=all='0/0 0.5/0.52 0.87/0.985 1/1'`) : YAVG médiane 199 → 226, ombres gardées. Resolve : gain / point blanc après la transformée ; Blender seul : look « Punchy » / « High Contrast » ou courbes RGB du compositor. Ne pas pousser l'exposition à +3 (on brûle les objets). Fond blanc 100 % sans grader : view transform « Standard » (hautes lumières qui clippent durement).
- **Cadrage d'un plan final** : 3 à 5 candidats en image fixe (7 s chacun, caméra en paramètre `--cam x,y,z,tx,ty,tz`), planche, choix, PUIS l'animation (3 min). Le choix est d'intention (où est le vide ? vers où regarde le sujet ?) [ÉPROUVÉ EN MAQUETTE].
- **Moiré** : un champ d'objets réguliers plus fins que le pixel moire en fin de recul (8 échantillons). La brume l'efface ; un fond noir à lumière rasante le révèle. Remèdes : échantillons ×4 sur ces images, brume plus proche, ou défocus léger [ÉPROUVÉ EN MAQUETTE].
