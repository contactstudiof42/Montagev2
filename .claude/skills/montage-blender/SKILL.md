---
name: montage-blender
description: Blender pour la vidéo et le motion design, piloté par script ou par MCP — rendu en ligne de commande (blender -b -P script.py), scripts Python bpy, plans 3D pour un montage, caméras multiples, Cycles contre Eevee, motion blur, AgX, lumières motivées, éléments émissifs, animation par keyframes calculées, simulation, plans « produit » ou objets dans le noir, packshot 3D, rendus de test rapides. Mots d'un réalisateur ou d'un motion designer : « on fait ce plan en 3D », « il me faut des plans d'insert », « on n'a pas tourné ce plan », « rendu trop long », « ça fait CG », « le chrome est tout noir », « la boule sort du cadre ».
---

# Blender pour la vidéo

_Réécrit le 2026-10-13 (audit 2). **Statut honnête** : la méthode et les réglages ci-dessous ont été éprouvés en VM Linux, Blender 4.2.3, sur CPU (34 pièces d'atelier) ; **jamais sur le Mac**, où sont installés Blender 5.2.2 LTS et un GPU : API, identifiants de moteur et temps de rendu à revérifier (exercice E0 de `PLAN-TESTS.md`). Recettes bpy, mesures et pièges : [details.md](details.md). Version d'avant : `archives/audit-2/skills/montage-blender/`._

**Fait foi sur** : la fabrication de plans 3D dans Blender (scripts bpy, rendu, réglages). Méthode générale de pilotage : `montage-pilotage-mcp` ; intention couleur : `montage-couleur`.

## 1. Quand et pourquoi
- **Plans impossibles ou trop chers à tourner** (macro d'objets, réaction en chaîne, packshot dans le noir), plans d'insert, décors de typographie.
- **Contrôle total du temps** : la position d'un objet se calcule à l'image près, donc un événement visuel se cale sur un son. [ÉPROUVÉ EN MAQUETTE]
- **Quand l'éviter** : visage humain, matière organique (feu, eau, tissu) sans temps de simulation, ou quand le look « CG » trahirait le sujet ; un vrai plan tourné, même modeste, bat souvent un rendu propre et vide. [THÉORIQUE]

## 2. Méthode [TESTÉ EN LABO]
1. **Une scène, plusieurs caméras** : un seul script construit le plateau, une caméra par plan ; le montage choisit des fenêtres (caméra, image source, durée) dans une liste de plans en JSON.
2. **Ne rendre que les images utilisées**, par plages contiguës, avec un cache par caméra.
3. **Une image par caméra avant tout rendu long** (images fixes côte à côte) : c'est là que se voient le chrome noir, le sujet hors cadre, l'objet mal proportionné. (Gagnée : chrome noir, sujet hors cadre, allumette « sucette » en atelier.)
4. **Vérifier la caméra et les poses à la première et à la dernière image** de chaque plan animé, pas seulement au milieu. (Gagnée : une caméra sous l'eau pendant 97 images, une tasse enfoncée dans le sol.)
5. **Choisir les fenêtres de source depuis la cinématique**, pas au compteur (un pendule sort du cadre 4 images après le point bas : la fenêtre commence une image avant).
6. **Planche de la première image de chaque plan** du montage : chaque vignette doit se lire seule.

## 3. Réglages gagnés (à remesurer sur le Mac)
- **Le chrome reflète son environnement** : dans un monde noir, il est noir. Ajouter des bandes émissives **invisibles à la caméra** (`visible_camera = False`) qui ne servent qu'aux reflets : la technique des softbox de packshot. [ÉPROUVÉ EN MAQUETTE]
- **AgX** garde lisibles les hautes lumières (flamme, reflets) mieux que Standard ; mais il plafonne le blanc vers 222/255 (pixel max mesuré partout, ciel compris, en « Base Contrast ») : un blanc clinique se pose ensuite au grade (courbe de point blanc). [TESTÉ EN LABO] À reconfirmer sur Blender 5.2 (exercice E3).
- **Flou de bougé** (`shutter = 0.5`) : un objet qui traverse le cadre en 1 à 2 images disparaît ; ralentir l'objet ou rapprocher la caméra, pas augmenter l'échantillonnage. [ÉPROUVÉ EN MAQUETTE]
- **Simuler plutôt qu'animer quand la causalité est l'argument** (chute, collision, réaction en chaîne) : la simulation donne les images de contact exactes, pour placer les sons et choisir où couper ; corps rigides déterministes à paramètres égaux. Piège : `transform_apply(location=False, rotation=False, scale=True)`, sinon la collision explose. [TESTÉ EN LABO, Blender 4.2.3]
- Temps de rendu sur la VM (Cycles CPU, 270×480, 12 échantillons + débruitage : 0,7 à 1,5 s par image) : sans valeur pour le Mac, à remesurer en E0.
