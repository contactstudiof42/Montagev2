---
name: montage-blender
description: Blender pour la vidéo et le motion design — rendu en ligne de commande (blender -b -P script.py), scripts Python bpy, plans 3D pour un montage, caméras multiples, Cycles contre Eevee, motion blur, AgX, lumières motivées, éléments émissifs, animation par keyframes calculées, plans « produit » ou objets dans le noir, packshot 3D, rendus de test rapides. Mots d'un réalisateur ou d'un motion designer : « on fait ce plan en 3D », « il me faut des plans d'insert », « on n'a pas tourné ce plan », « rendu trop long », « ça fait CG », « le chrome est tout noir », « la boule sort du cadre ».
---

# Blender pour la vidéo

Marqueurs : **[SOURCÉ]** lu dans une source datée · **[TESTÉ EN LABO]** fait technique mesuré (temps de rendu, scripts, pixels) · **[ÉPROUVÉ EN MAQUETTE]** principe tiré d'une maquette Blender/Pillow/ffmpeg, hypothèse à confirmer sur de vraies images en phase 2 · **[THÉORIQUE]** doc ou pratique, jamais exécuté.

**Fait foi sur** : la fabrication de plans 3D dans Blender (scripts bpy, rendu, réglages). Pour la méthode générale de pilotage par MCP : `montage-pilotage-mcp` ; pour l'intention couleur : `montage-couleur-et-intention`. Détail des recettes et mesures : [details.md](details.md).

## 1. Quand et pourquoi
- **Plans impossibles ou trop chers à tourner** (macro d'objets, réaction en chaîne, packshot dans le noir), **plans d'insert** pour un montage rapide, **décors de typographie**.
- **Contrôle total du temps** : on calcule la position d'un objet à l'image près, donc on peut caler un événement visuel sur un son, ou une réaction en chaîne sur une règle du temps (atelier 02 : le pendule frotte l'allumette à l'apogée, image 200) [ÉPROUVÉ EN MAQUETTE].
- **Quand l'éviter** [THÉORIQUE] : visage humain, matière organique (feu, eau, tissu) sans temps de simulation, ou quand le « look CG » trahirait le sujet. Un vrai plan tourné, même modeste, bat souvent un rendu propre et vide.

## 2. Méthode d'atelier [TESTÉ EN LABO]
1. **Une scène, plusieurs caméras** : un seul script construit le plateau, une caméra par « plan » (pendule, cube, sphères, allumette, large). Le montage choisit des fenêtres `(caméra, image source, durée)` : c'est une **liste de plans (EDL) en JSON**.
2. **Ne rendre que les images utilisées** : regrouper les images demandées par caméra en plages contiguës, rendre avec `bpy.ops.render.render(animation=True)` par plage, garder un **cache** `caméra_image.png`. Ne supprimer du cache que les caméras dont le plateau a changé. (`atelier/02-etincelle/montage.py`.)
3. **Tester 1 image par caméra avant tout rendu long** (stills côte à côte avec `hstack`) : c'est là que se voient le chrome noir, le sujet hors cadre, l'allumette « sucette ».
4. **Choisir les fenêtres de source depuis la cinématique**, pas au compteur. Un pendule de 2,45 m qui balaie ±32° devant un 45 mm sort du cadre 4 images après le passage au point bas : une fenêtre doit commencer **une image avant** le passage (atelier 02, v3). Planche de toutes les images d'une caméra pour diagnostiquer (`-pattern_type glob`, `tile`).
5. **Planche contact de la 1re image de chaque plan** du montage : chaque vignette doit se lire seule.

## 3. Réglages qui ont marché (Blender 4.2.3 LTS, CPU, VM 4 cœurs) [TESTÉ EN LABO]
- Installation : `curl` de `blender-4.2.3-linux-x64.tar.xz` + `tar xf` ≈ 30 s.
- Cycles CPU, 270×480, **12 échantillons + débruitage** (OIDN) : ~0,7-1,5 s par image ; 260 images ≈ 4-5 min. Agrandir ×2 en lanczos avec ffmpeg pour une maquette 540×960.
- `view_transform = "AgX"`, look « AgX - Punchy » : les hautes lumières (flamme, reflets) restent lisibles sans brûler, mieux que Standard [ÉPROUVÉ EN MAQUETTE] ; revers : AgX plafonne le blanc (≈ 222/255), d'où un « blanc clinique » impossible sans courbe de point blanc à l'étalonnage [TESTÉ EN LABO] (pièce 22 v3, détail dans [details.md](details.md)).
- Motion blur `shutter = 0.5` : un objet qui traverse en 1 à 2 images ne se voit plus du tout [ÉPROUVÉ EN MAQUETTE] (atelier 02 v1-v3) → **ralentir l'objet ou rapprocher la caméra**, pas augmenter l'échantillonnage.
- **Le chrome reflète son environnement** : dans un monde noir, il est noir. Ajouter des bandes émissives **invisibles à la caméra** (`visible_camera = False`) qui ne servent qu'aux reflets. C'est la technique des softbox de packshot.
- Feu/flamme : un cône émissif + une lampe ponctuelle à énergie animée (scintillement aléatoire 120 ± 25 W) suffit pour la *lumière* du feu sur le décor ; la flamme elle-même reste graphique (limite connue : simulation Mantaflow ou plan tourné à prévoir).
- Valeurs d'émission animées : `inputs["Emission Strength"].keyframe_insert("default_value", frame=f)`.

## 4. Couleur et lumière (intention)
- Lumière **motivée** [THÉORIQUE] : une grande source froide rasante + un liseré ; la chaleur n'existe que si une source chaude est dans le plan (règle Deakins, goût Joker/Ziak : `montage-couleur-et-intention`).
- **Vérifier la règle couleur par la mesure** [TESTÉ EN LABO] sur le MP4 : % de pixels chauds par image (atelier 02 v4 : ≤ 0,25 % avant l'événement, 6,3 % après).

## 5. À vérifier en phase 2 (Mac)
- Temps de rendu GPU Metal contre CPU cloud ; Eevee Next en rendu final pour des maquettes (non testé en headless ici).
- Le pilotage par MCP (`PLAN-TESTS-MCP.md`, test 13) : refaire `atelier/02-etincelle/scene.py` et comparer les planches.

## 6. Autres leçons (résumé ; détail dans [details.md](details.md))
- **Simuler plutôt qu'animer quand la causalité est l'argument** (chute, collision, réaction en chaîne) : la simulation donne les images de contact exactes, utiles pour placer les sons et choisir où couper [ÉPROUVÉ EN MAQUETTE]. Corps rigides **déterministes** (Blender 4.2.3, CPU) : monter sur les contacts calculés une fois, rendre caméra par caméra [TESTÉ EN LABO]. Piège : `transform_apply(location=False, rotation=False, scale=True)`, sinon la collision explose.
- **Plan immobile = une seule image rendue**, répétée au montage (rendu 4× plus rapide) [TESTÉ EN LABO].
- **Caméra portée crédible** : 2-3 sinus lents par axe (0,9 à 3 Hz, < 1°), pas de bruit blanc [ÉPROUVÉ EN MAQUETTE].
- **Rendre un mouvement une fois, le placer plusieurs fois** par une courbe temps → paramètre au montage ; densifier le rendu là où la courbe ralentit [ÉPROUVÉ EN MAQUETTE] (pièce 22).
- **Chercher le cadrage en image fixe** (3 à 5 candidats en planche) avant de lancer l'animation [ÉPROUVÉ EN MAQUETTE].
- **Vérifier la caméra et les poses à la 1re et à la dernière image** (caméra sous l'eau, tasse enfoncée dans le sol) [TESTÉ EN LABO].
- **Eevee sans écran dans la VM** : plus lent que Cycles (OpenGL logiciel) ; à réévaluer sur GPU [TESTÉ EN LABO].
