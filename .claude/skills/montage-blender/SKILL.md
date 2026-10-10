---
name: montage-blender
description: Blender pour la vidéo et le motion design — rendu en ligne de commande (blender -b -P script.py), scripts Python bpy, plans 3D pour un montage, caméras multiples, Cycles contre Eevee, motion blur, AgX, lumières motivées, éléments émissifs, animation par keyframes calculées, plans « produit » ou objets dans le noir, packshot 3D, rendus de test rapides. Mots d'un réalisateur ou d'un motion designer : « on fait ce plan en 3D », « il me faut des plans d'insert », « on n'a pas tourné ce plan », « rendu trop long », « ça fait CG », « le chrome est tout noir », « la boule sort du cadre ».
---

# Blender pour la vidéo

## 1. Quand et pourquoi
- **Plans impossibles ou trop chers à tourner** (macro d'objets, réaction en chaîne, packshot dans le noir), **plans d'insert** pour un montage rapide, **décors de typographie**.
- **Contrôle total du temps** : on calcule la position d'un objet à l'image près, donc on peut caler un événement visuel sur un son, ou une réaction en chaîne sur une règle du temps (atelier 02 : le pendule frotte l'allumette à l'apogée, image 200).
- **Quand l'éviter** : visage humain, matière organique (feu, eau, tissu) sans temps de simulation, ou quand le « look CG » trahirait le sujet. Un vrai plan tourné, même modeste, bat souvent un rendu propre et vide.

## 2. Méthode d'atelier [TESTÉ EN LABO]
1. **Une scène, plusieurs caméras** : un seul script construit le plateau, une caméra par « plan » (pendule, cube, sphères, allumette, large). Le montage choisit des fenêtres `(caméra, image source, durée)` : c'est une **liste de plans (EDL) en JSON**.
2. **Ne rendre que les images utilisées** : regrouper les images demandées par caméra en plages contiguës, rendre avec `bpy.ops.render.render(animation=True)` par plage, garder un **cache** `caméra_image.png`. Ne supprimer du cache que les caméras dont le plateau a changé. (`atelier/02-etincelle/montage.py`.)
3. **Tester 1 image par caméra avant tout rendu long** (stills côte à côte avec `hstack`) : c'est là que se voient le chrome noir, le sujet hors cadre, l'allumette « sucette ».
4. **Choisir les fenêtres de source depuis la cinématique**, pas au compteur. Un pendule de 2,45 m qui balaie ±32° devant un 45 mm sort du cadre 4 images après le passage au point bas : une fenêtre doit commencer **une image avant** le passage (atelier 02, v3). Planche de toutes les images d'une caméra pour diagnostiquer (`-pattern_type glob`, `tile`).
5. **Planche contact de la 1re image de chaque plan** du montage : chaque vignette doit se lire seule.

## 3. Réglages qui ont marché (Blender 4.2.3 LTS, CPU, VM 4 cœurs) [TESTÉ EN LABO]
- Installation : `curl` de `blender-4.2.3-linux-x64.tar.xz` + `tar xf` ≈ 30 s.
- Cycles CPU, 270×480, **12 échantillons + débruitage** (OIDN) : ~0,7-1,5 s par image ; 260 images ≈ 4-5 min. Agrandir ×2 en lanczos avec ffmpeg pour une maquette 540×960.
- `view_transform = "AgX"`, look « AgX - Punchy » : les hautes lumières (flamme, reflets) restent lisibles sans brûler en blanc, mieux que Standard.
- Motion blur `shutter = 0.5` : les objets rapides deviennent des traînées ; si un objet traverse en 1 à 2 images, on ne le voit plus du tout (sphères de l'atelier 02 v1-v3) → **ralentir l'objet ou rapprocher la caméra**, pas augmenter l'échantillonnage.
- **Le chrome reflète son environnement** : dans un monde noir, il est noir. Ajouter des bandes émissives **invisibles à la caméra** (`visible_camera = False`) qui ne servent qu'aux reflets. C'est la technique des softbox de packshot.
- Feu/flamme : un cône émissif + une lampe ponctuelle à énergie animée (scintillement aléatoire 120 ± 25 W) suffit pour la *lumière* du feu sur le décor ; la flamme elle-même reste graphique (limite connue : simulation Mantaflow ou plan tourné à prévoir).
- Valeurs d'émission animées : `inputs["Emission Strength"].keyframe_insert("default_value", frame=f)`.

## 4. Couleur et lumière (intention)
- Lumière **motivée** : une grande source froide rasante + un liseré ; la chaleur n'existe que si une source chaude est dans le plan (règle Deakins, goût Joker/Ziak : `montage-couleur-et-intention`).
- **Vérifier la règle couleur par la mesure** sur le MP4 : % de pixels chauds par image (atelier 02 v4 : ≤ 0,25 % avant l'événement, 6,3 % après).

## 5. À vérifier en phase 2 (Mac)
- Temps de rendu GPU Metal contre CPU cloud ; Eevee Next en rendu final pour des maquettes (non testé en headless ici).
- Le pilotage par MCP (`PLAN-TESTS-MCP.md`, test 13) : refaire `atelier/02-etincelle/scene.py` et comparer les planches.

## Leçons de l'atelier 04 « marée » (session 4) [TESTÉ EN ATELIER]
- Eau = simple plan animé en Z + Principled (IOR 1,33, transmission, bump d'ondes) : crédible en 8 échantillons + débruitage, ~1,2 s/image en 480×270 CPU. Sous incidence rasante, l'eau est un **miroir** (Fresnel) : rien ne se devine sous la surface, quelle que soit la transmission.
- **Vérifier que la caméra reste hors de l'eau** (ou de tout objet animé) à chaque image : tester images 1 et N, pas seulement le milieu.
- Plan de sol de 200 m + SUBSURF simple niveau 8 + DISPLACE (texture Wood band noise) = rides de sable ; un estran presque plat se découvre d'un coup quand l'eau passe sous sa hauteur moyenne (effet utile).
- Paramétrer la scène par un JSON (caméra, courbe d'eau, plage d'images) permet de rendre seulement les images utiles de chaque caméra pour un montage multi-plans (`atelier/04-maree-decouvre/v3-*.json`).
- Lancer plusieurs rendus en parallèle n'accélère rien sur CPU partagé ; et `pkill -f motif` peut tuer le shell qui le lance (le motif figure dans sa propre ligne de commande).
- **Objet qui tombe (atelier 06, session 5)** [TESTÉ EN ATELIER] : chute keyframée image par image (bascule de 6 images autour du bord, puis z = z0 - ½·g·t² à 25 i/s, impact calculé par le script et imprimé) ; **vérifier la pose de repos** : une rotation finale de -180° avec l'origine décalée a enfoncé la tasse dans le sol (invisible dans le montage, coupé avant l'impact, mais faux). Pour des variantes comparables, `cycles.seed` fixe et **aucune modification du script entre deux rendus** d'une même série (les nouveaux paramètres doivent garder par défaut le comportement exact).
- **Ombre portée d'un personnage invisible** : un volume noir avec `visible_camera = False` et `visible_glossy = False` entre la source et le décor projette une ombre sans apparaître. Temps : 2 sources surfaciques, 480×270, 16 échantillons + débruiteur ≈ 2,5 s/image sur 4 cœurs.

## Simulation de corps rigides et Eevee sans écran (session 6, atelier 07) [TESTÉ EN LABO]
- **Quand simuler plutôt qu'animer à la main** : quand la causalité est l'argument (chaîne à la « Cog », chute, collision). Une simulation est vraie dans le fichier, donc le spectateur ne peut douter que du montage ; elle donne en plus les **images de contact exactes**, qui servent à placer les sons et à choisir où couper.
- Recette : `bpy.ops.rigidbody.world_add()` ; `substeps_per_frame = 40`, `solver_iterations = 30` pour des petits objets (dominos de 9 cm, bille de 2,2 cm) ; formes `BOX` / `SPHERE` / `CYLINDER` ; `collision_margin = 0.001` ; frottement 0,7-0,8 pour que les dominos basculent au lieu de glisser. Lire les positions avec `sc.frame_set(f)` image par image depuis la 1re (écrit dans un JSON), puis `bpy.ops.ptcache.bake_all(bake=True)` avant le rendu. Une plage de rendu partielle se règle **après** le bake (la simulation doit partir de l'image 1). Coût : simulation de 200 images ≈ 1 s.
- **Piège n°1** : `transform_apply(scale=True)` applique aussi la position et la rotation par défaut. L'origine part à (0, 0, 0) et la forme de collision `BOX` se centre sur l'origine : le plateau collisionne au niveau du sol, les dominos se superposent et explosent. Toujours écrire `transform_apply(location=False, rotation=False, scale=True)`.
- **Piège n°2** : un objet actif posé trop près d'un autre au départ (moins de ~1 cm) part tout seul à l'image 2. Laisser du jeu et vérifier sur les premières images que rien ne bouge avant la cause.
- **Réglage par lots** : la simulation seule (`mode: sim`) est quasi gratuite. Balayer 3 configurations à la fois et lire les images d'événements (`contacts.py`) avant de rendre quoi que ce soit.
- **Eevee en ligne de commande dans la VM** : il plante sans `libEGL.so.1`. Après `apt-get update && apt-get install -y libegl1` (10 s), il rend en OpenGL logiciel à **~7 s/image** en 480×270, donc **plus lentement que Cycles** (8 échantillons + débruitage : ~2 s/image seul, ~6-8 s quand 6 rendus se partagent 4 cœurs). Dans la VM, Cycles reste le bon choix ; Eevee est à réévaluer sur le Mac (GPU, phase 2).
- **Amortir sans tricher** : `angular_damping = 1` dès le début empêche aussi l'objet de basculer (pièce 07 v2 : la tasse tombait debout, lu comme un trucage). Les propriétés de corps rigide s'animent : mettre l'amortissement en clé **à partir de l'impact** (`rb.keyframe_insert("angular_damping", frame=f)`), testé en v3.
- Rendre plusieurs caméras **en parallèle** (un processus par caméra) : 4 images fixes de contrôle en 9 s au total.
