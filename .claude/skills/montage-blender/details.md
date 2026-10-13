Annexe de `SKILL.md` : recettes bpy, mesures et pièges de montage-blender, éprouvés en VM Linux (Blender 4.2.3, CPU), jamais encore sur le Mac (Blender 5.2.2) ; le SKILL.md fait foi. Réglages, couleur et autres leçons déplacés du SKILL.md à l'audit 2 (2026-10-13).

## Réglages qui ont marché, texte complet de l'ancien SKILL.md (Blender 4.2.3 LTS, CPU, VM 4 cœurs) [TESTÉ EN LABO]
- Installation : `curl` de `blender-4.2.3-linux-x64.tar.xz` + `tar xf` ≈ 30 s.
- Cycles CPU, 270×480, **12 échantillons + débruitage** (OIDN) : ~0,7-1,5 s par image ; 260 images ≈ 4-5 min. Agrandir ×2 en lanczos avec ffmpeg pour une maquette 540×960.
- `view_transform = "AgX"`, look « AgX - Punchy » : les hautes lumières (flamme, reflets) restent lisibles sans brûler, mieux que Standard [ÉPROUVÉ EN MAQUETTE] ; revers : AgX plafonne le blanc (≈ 222/255), d'où un « blanc clinique » impossible sans courbe de point blanc à l'étalonnage [TESTÉ EN LABO] (pièce 22 v3, détail dans [details.md](details.md)).
- Motion blur `shutter = 0.5` : un objet qui traverse en 1 à 2 images ne se voit plus du tout [ÉPROUVÉ EN MAQUETTE] (atelier 02 v1-v3) → **ralentir l'objet ou rapprocher la caméra**, pas augmenter l'échantillonnage.
- **Le chrome reflète son environnement** : dans un monde noir, il est noir. Ajouter des bandes émissives **invisibles à la caméra** (`visible_camera = False`) qui ne servent qu'aux reflets. C'est la technique des softbox de packshot.
- Feu/flamme : un cône émissif + une lampe ponctuelle à énergie animée (scintillement aléatoire 120 ± 25 W) suffit pour la *lumière* du feu sur le décor ; la flamme elle-même reste graphique (limite connue : simulation Mantaflow ou plan tourné à prévoir).
- Valeurs d'émission animées : `inputs["Emission Strength"].keyframe_insert("default_value", frame=f)`.

## Couleur et lumière (intention)
- Lumière **motivée** [THÉORIQUE] : une grande source froide rasante + un liseré ; la chaleur n'existe que si une source chaude est dans le plan (règle Deakins, goût Joker/Ziak : `montage-couleur`).
- **Vérifier la règle couleur par la mesure** [TESTÉ EN LABO] sur le MP4 : % de pixels chauds par image (atelier 02 v4 : ≤ 0,25 % avant l'événement, 6,3 % après).

## Autres leçons (résumé de l'ancien SKILL.md ; détail plus bas)
- **Simuler plutôt qu'animer quand la causalité est l'argument** (chute, collision, réaction en chaîne) : la simulation donne les images de contact exactes, utiles pour placer les sons et choisir où couper [ÉPROUVÉ EN MAQUETTE]. Corps rigides **déterministes** (Blender 4.2.3, CPU) : monter sur les contacts calculés une fois, rendre caméra par caméra [TESTÉ EN LABO]. Piège : `transform_apply(location=False, rotation=False, scale=True)`, sinon la collision explose.
- **Plan immobile = une seule image rendue**, répétée au montage (rendu 4× plus rapide) [TESTÉ EN LABO].
- **Caméra portée crédible** : 2-3 sinus lents par axe (0,9 à 3 Hz, < 1°), pas de bruit blanc [ÉPROUVÉ EN MAQUETTE].
- **Rendre un mouvement une fois, le placer plusieurs fois** par une courbe temps → paramètre au montage ; densifier le rendu là où la courbe ralentit [ÉPROUVÉ EN MAQUETTE] (pièce 22).
- **Chercher le cadrage en image fixe** (3 à 5 candidats en planche) avant de lancer l'animation [ÉPROUVÉ EN MAQUETTE].
- **Vérifier la caméra et les poses à la 1re et à la dernière image** (caméra sous l'eau, tasse enfoncée dans le sol) [TESTÉ EN LABO].
- **Eevee sans écran dans la VM** : plus lent que Cycles (OpenGL logiciel) ; à réévaluer sur GPU [TESTÉ EN LABO].

# Blender : détail des recettes et mesures

Déplacé de `SKILL.md` le 2026-10-10 (audit de fin de phase 1). Marqueurs : voir `SKILL.md`.

## Eau, objet qui tombe, ombre d'un personnage invisible (ateliers 04 et 06)
- Eau = simple plan animé en Z + Principled (IOR 1,33, transmission, bump d'ondes) : crédible en 8 échantillons + débruitage, ~1,2 s/image en 480×270 CPU [TESTÉ EN LABO]. Sous incidence rasante, l'eau est un **miroir** (Fresnel) : rien ne se devine sous la surface, quelle que soit la transmission [ÉPROUVÉ EN MAQUETTE] (atelier 04).
- Plan de sol de 200 m + SUBSURF simple niveau 8 + DISPLACE (texture Wood band noise) = rides de sable ; un estran presque plat se découvre d'un coup quand l'eau passe sous sa hauteur moyenne (effet utile) [ÉPROUVÉ EN MAQUETTE].
- Paramétrer la scène par un JSON (caméra, courbe d'eau, plage d'images) pour ne rendre que les images utiles de chaque caméra (`atelier/04-maree-decouvre/v3-*.json`).
- Lancer plusieurs rendus en parallèle n'accélère rien sur CPU partagé ; `pkill -f motif` peut tuer le shell qui le lance (le motif figure dans sa propre ligne de commande) [TESTÉ EN LABO].
- **Objet qui tombe** (atelier 06) [TESTÉ EN LABO] : chute keyframée image par image (bascule de 6 images autour du bord, puis z = z0 - ½·g·t² à 25 i/s, impact calculé et imprimé par le script). Pose de repos : une rotation finale de -180° avec l'origine décalée a enfoncé la tasse dans le sol. Pour des variantes comparables : `cycles.seed` fixe et **aucune modification du script entre deux rendus** d'une même série.
- **Ombre portée d'un personnage invisible** [TESTÉ EN LABO] : un volume noir `visible_camera = False`, `visible_glossy = False` entre la source et le décor projette une ombre sans apparaître. 2 sources surfaciques, 480×270, 16 échantillons + débruiteur ≈ 2,5 s/image sur 4 cœurs.

## Corps rigides et Eevee sans écran (atelier 07)
- Recette [TESTÉ EN LABO] : `bpy.ops.rigidbody.world_add()` ; `substeps_per_frame = 40`, `solver_iterations = 30` pour de petits objets (dominos de 9 cm, bille de 2,2 cm) ; formes `BOX` / `SPHERE` / `CYLINDER` ; `collision_margin = 0.001` ; frottement 0,7-0,8 pour que les dominos basculent au lieu de glisser. Lire les positions avec `sc.frame_set(f)` image par image depuis la 1re (JSON), puis `bpy.ops.ptcache.bake_all(bake=True)` avant le rendu. Une plage de rendu partielle se règle **après** le bake. Simulation de 200 images ≈ 1 s.
- **Piège n°1, pourquoi** : `transform_apply(scale=True)` applique aussi position et rotation par défaut ; l'origine part à (0, 0, 0), la forme `BOX` se centre dessus, les dominos se superposent et explosent.
- **Piège n°2** : un objet actif posé à moins de ~1 cm d'un autre part tout seul à l'image 2. Laisser du jeu, vérifier les premières images.
- **Réglage par lots** : la simulation seule (`mode: sim`) est quasi gratuite ; balayer 3 configurations et lire les images d'événements (`contacts.py`) avant de rendre.
- **Eevee en ligne de commande dans la VM** : plante sans `libEGL.so.1` ; après `apt-get install -y libegl1`, rend en OpenGL logiciel à **~7 s/image** en 480×270, contre ~2 s/image seul pour Cycles (8 échantillons + débruitage ; ~6-8 s à 6 rendus sur 4 cœurs). À réévaluer sur GPU (phase 3).
- **Amortir sans tricher** : `angular_damping = 1` dès le début empêche aussi la bascule (pièce 07 v2 : la tasse tombait debout, lu comme un trucage [ÉPROUVÉ EN MAQUETTE]). Mettre l'amortissement en clé **à partir de l'impact** (`rb.keyframe_insert("angular_damping", frame=f)`), testé en v3.
- Rendre plusieurs caméras en parallèle (un processus par caméra) : 4 images fixes de contrôle en 9 s.

## Déterminisme, plan immobile, caméra portée (ateliers 07-08)
- **Déterminisme** [TESTÉ EN LABO] (Blender 4.2.3, Bullet, CPU) : `atelier/07-causalite/scene.py` en mode `sim` lancé 3 fois en parallèle donne trois `sim.json` identiques à l'octet (8 912 valeurs) ; événements identiques sur une autre VM. À revérifier sur le Mac (exercice E4 de `PLAN-TESTS.md`).
- **Plan immobile** (pièce 08) : le présent figé au pixel peut devenir un choix (temps arrêté) ; sinon ajouter un grain fin au montage pour faire vivre l'image (rien à voir avec la protection des noirs à l'encodage, que le grain n'assure pas : voir `montage-loudness-livraison`).
- **Caméra portée** [ÉPROUVÉ EN MAQUETTE] : amplitudes 0,6 à 0,9°, clé toutes les 2 images. Zoom lent sur `data.lens` (38 → 56 mm sur 70 images). `atelier/08-souvenir/scene.py`.

## Un mouvement rendu une fois, placé plusieurs fois (pièce 22)
- Rendre le mouvement de caméra à **paramètre u régulier** (64-96 images), puis construire chaque version au montage par une courbe temps → u (`atelier/22-a-la-maniere-d-ego/montage.py`) : trois placements contre la voix pour le coût d'un rendu (~3 s/image, Cycles 8 échantillons, 480×270, 63 000 chaises par 2 modificateurs Array) [TESTÉ EN LABO].
- Seuil de saccade : u qui avance de moins d'une image rendue toutes les 2-3 images de sortie [ÉPROUVÉ EN MAQUETTE]. Équivalent AE : remappage temporel (PLAN-TESTS 64).
- Brume par la passe Mist mélangée à la couleur du monde en compositing : le champ « se perd » au lieu de s'arrêter, sans volumétrie [ÉPROUVÉ EN MAQUETTE].

## AgX plafonne le blanc ; cadrage en image fixe ; moiré (pièce 22 v3)
- **Symptôme** : un monde « blanc clinique » reste gris malgré plus de lumière. **Mesure** [TESTÉ EN LABO] : pixel MAX (numpy) identique partout, ciel compris (222-225 / 255 avec AgX + « Base Contrast », exposition +1) → le plafond vient de la transformée de vue. C'est le seul fait mesuré sur AgX ici ; l'explication (AgX compresse les hautes lumières et n'atteint le blanc qu'à des valeurs de scène très hautes) est [THÉORIQUE]. AgX ne « blanchit » pas les couleurs froides : hypothèse réfutée (pièce 10 v4, `montage-couleur/intention.md`).
- **Correction** : à l'étalonnage. Courbe de point blanc (`curves=all='0/0 0.5/0.52 0.87/0.985 1/1'`) : YAVG médiane 199 → 226, ombres gardées. Resolve : gain / point blanc après la transformée ; Blender seul : look « Punchy » / « High Contrast » ou courbes RGB du compositor. Ne pas pousser l'exposition à +3 (on brûle les objets). Fond blanc 100 % sans grader : view transform « Standard » (hautes lumières qui clippent durement).
- **Cadrage en image fixe** : 7 s par candidat (caméra en paramètre `--cam x,y,z,tx,ty,tz`) contre 3 min pour l'animation ; le choix est d'intention (où est le vide ? vers où regarde le sujet ?) [ÉPROUVÉ EN MAQUETTE].
- **Moiré** : un champ d'objets réguliers plus fins que le pixel moire en fin de recul (8 échantillons). La brume l'efface ; un fond noir à lumière rasante le révèle. Remèdes : échantillons ×4 sur ces images, brume plus proche, ou défocus léger [ÉPROUVÉ EN MAQUETTE].
