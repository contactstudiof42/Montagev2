---
name: montage-after-effects
description: Faire bouger juste dans After Effects — easing, Graph Editor (courbes de vitesse et de valeur), influence des clés, Easy Ease (F9), anticipation, overshoot, rebond, expressions (wiggle, loopOut, valueAtTime, posterizeTime, time remap, compteur), rigs à sliders, organisation de comp (précomps, nulls). Mots d'un motion designer : « ça fait amateur », « ça manque de poids », « c'est mou », « trop linéaire », « ça claque pas », « boucle propre », « ça rebondit trop », « fais-le trembler ». Quoi animer et pourquoi : `montage-motion-design-principes`.
---

# After Effects : le mouvement d'abord

Annexe des recettes : [expressions.md](expressions.md). Preuves du labo : `labo/ae-expressions/RESULTATS.md`. Sources : `sources/after-effects.md`.

Marqueurs : **[SOURCÉ]** lu dans une source datée · **[TESTÉ EN LABO]** fait technique mesuré ; ici **syntaxe et maths vérifiées sous Node avec un faux environnement, pas dans AE** · **[ÉPROUVÉ EN MAQUETTE]** principe tiré d'une maquette Blender/Pillow/ffmpeg, hypothèse à confirmer sur de vraies images en phase 2 · **[THÉORIQUE]** doc ou pratique, jamais exécuté.

**Fait foi sur** : la technique du mouvement dans AE (courbes, expressions, rigs). Pour quoi animer : `montage-motion-design-principes` ; pour piloter AE par MCP : `montage-pilotage-mcp` ; saccade dans Premiere ou Resolve : `montage-premiere`, `montage-resolve`. Détail des recettes, saccade et liste des vérifications de phase 2 : [expressions.md](expressions.md).

**Avant de régler une courbe** : choisir *quoi* animer (le paramètre qui porte le sens, un seul signe) avec `montage-motion-design-principes`. Ce skill-ci dit *comment* le faire bouger. La plus belle courbe sur le mauvais paramètre (échelle d'un mot) reste un « pulse » de logo [ÉPROUVÉ EN MAQUETTE] (atelier 01).

## 1. Quand s'en servir

- Dès qu'une animation « marche » mais ne convainc pas : elle est juste dans le temps, mais elle n'a pas de matière.
- Pour animer un titre, un logo, une interface ou un habillage, et pour construire un rig réutilisable (sliders, nulls, contrôleurs).
- Pour diagnostiquer : « pourquoi ça fait cheap ? ». La réponse est presque toujours dans le graphe de vitesse.

## 2. Pourquoi : ce que le mouvement raconte

**Le mouvement est une description de la matière.** Deux objets qui font le même trajet en 12 images ne pèsent pas la même chose si leur courbe diffère. Le spectateur ne voit pas les clés, il **sent** la masse, la raideur, l'intention.

- **Le poids, c'est l'accélération.** Un objet lourd démarre lentement (inertie) et s'arrête lentement. Un objet léger démarre sec. Une sortie de clé très tirée (forte influence) donne du poids ; une sortie courte donne de la nervosité.
- **L'anticipation prépare l'œil.** 2 à 4 images de recul (quelques pixels, quelques %) avant un départ rapide. Sans elle, un départ brutal paraît être une erreur de montage ; avec elle, il paraît voulu.
- **L'overshoot dit la matière.** Dépasser la cible puis revenir, c'est dire « j'ai de l'élan et je suis élastique ». Fréquence haute et amortissement fort : métal, plastique dur, UI. Fréquence basse, peu amorti : gélatine, cartoon. **Pas d'overshoot** : verre, pierre, luxe, sobriété. Choisir l'overshoot, c'est choisir un matériau.
- **L'Easy Ease par défaut trahit l'amateur.** F9 pose une vitesse nulle avec une influence d'environ 33 % des deux côtés : une courbe symétrique, molle, que tout le monde reconnaît. Ce n'est pas faux, c'est **sans opinion**. Un pro part de F9 puis tire les poignées (60 à 90 % d'influence côté arrivée est courant pour un arrêt « luxe »).
- **L'asymétrie entrée/sortie.** Les mouvements vivants ne sont presque jamais symétriques : départ vif, arrivée longue (UI, apparition), ou départ lent, arrivée sèche (impact, chute). Régler l'influence de sortie de la clé A **différemment** de l'influence d'entrée de la clé B.
- **Le ralenti avant l'arrêt.** C'est la dernière phase qui est la plus lue. Les 30 à 40 % finaux d'un mouvement d'arrivée doivent porter la décélération. Un arrêt net sur une vitesse non nulle, c'est un « bug » à l'œil (sauf impact voulu).
- **Courbe de vitesse vs courbe de valeur.** *Graphe de vitesse* : on règle **comment** on va (accélération, poids). *Graphe de valeur* : on voit **où** on est, et c'est le seul qui montre un overshoot ou un rebond, en séparant X et Y (Séparer les dimensions). Règle de pro : timing et poids dans la vitesse, trajectoires, dépassements et arcs dans la valeur. Une courbe de valeur en S propre, sans plateau ni marche, c'est le signe d'un mouvement sain.
- **Le temps de lecture.** Un mouvement qui finit doit laisser au moins 0,5 à 1 s de tenue avant le suivant, sinon le texte n'est pas lu.

### Durées types à 25 i/s (points de départ, à juger à l'œil)

| Usage | Durée | Remarque |
|---|---|---|
| Micro-interaction UI (bouton, toggle) | 4 à 8 i (160 à 320 ms) | Au-delà, l'UI paraît lente |
| Apparition d'un panneau / carte UI | 8 à 12 i | Sortie plus courte que l'entrée (≈ 70 %) |
| Lettre par lettre (décalage entre lettres) | 1 à 2 i | 3 i et plus : effet « machine à écrire » |
| Entrée d'un mot ou d'une ligne de titre | 10 à 18 i | Décaler les lignes de 3 à 5 i |
| Lower third (entrée) | 12 à 20 i, tenue ≥ 3 s | La tenue doit permettre deux lectures du nom |
| Révélation de logo | 30 à 75 i (1,2 à 3 s) | Plus le logo est « premium », plus l'arrivée est longue et sans overshoot |
| Anticipation | 2 à 4 i | Rarement plus de 15 % de l'amplitude |
| Overshoot / rebond qui se pose | 8 à 20 i | Au-delà, ça devient du cartoon |
| Transition plein cadre | 8 à 16 i | Sur le temps fort de la musique |

Ces chiffres sont des **conventions de métier**, pas des normes. Pour l'UI, ils rejoignent les guides de motion des systèmes de design (100 à 500 ms).

## 3. Méthode de travail (le geste du motion designer)

1. **Poser les clés en Linéaire et régler le timing d'abord** (blocking) : positions et instants justes, sans easing. Si c'est faux en linéaire, l'easing ne sauvera rien.
2. **F9 partout, puis passer au graphe de vitesse** (Maj+F3 ouvre l'éditeur de graphiques). Tirer les poignées : arrivée longue, départ court, ou l'inverse selon la matière.
3. **Vérifier dans le graphe de valeur** : pas de dépassement involontaire (Bézier spatial qui « boucle »), pas de plateau parasite.
4. **Ajouter la vie** : anticipation, overshoot, décalage entre éléments (2 à 4 i). Jamais tout en même temps.
5. **Flou de mouvement** activé sur tout ce qui va vite : un mouvement rapide sans flou paraît saccadé à 25 i/s.
6. **Relire à vitesse réelle**, pas image par image, puis une fois en boucle, et une fois le son coupé.

Pour les clés : Alt+double-clic (Option sur Mac) sur une clé ouvre la **Vitesse de l'image clé**, où l'on tape vitesse et influence au chiffre près (utile pour copier un réglage d'un projet à l'autre).

## 4. Recettes

Code complet et commentaires : [expressions.md](expressions.md). Fichiers : `labo/ae-expressions/NN-*.js`.

| # | Recette | Usage motion | Statut |
|---|---|---|---|
| 01 | `wiggle(freq, amp)` piloté par deux sliders | Caméra à l'épaule, tremblement, flottement | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** (bornes vérifiées avec un faux wiggle) |
| 02 | `loopOut("cycle")` | Boucle de fond, rotation infinie, GIF | **[TESTÉ EN LABO, syntaxe uniquement]** (le comportement testé est celui du mock) |
| 03 | `loopOut("pingpong")` | Balancier, respiration simple | **[TESTÉ EN LABO, syntaxe uniquement]** |
| 04 | Boucle manuelle `valueAtTime(t0 + (time - t1) % d)` | Boucler une portion choisie | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 05 | Overshoot inertiel (principe Dan Ebberts) | Arrivée élastique sur n'importe quelle propriété | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** : pic à 107 pour une cible de 100, posé en 3 s |
| 06 | Écho / suiveur `valueAtTime(time - retard)` | Traînées, cascades, essaims | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 07 | `ease(p, 20, 60, 0, 100)` | Piloter une propriété par une autre (« progression ») | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** (courbe exacte d'`ease` non reproduite) |
| 08 | Time remap à vitesse constante | Ralenti/accéléré propre d'un clip | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 09 | Compteur de texte avec séparateur de milliers | Chiffres clés, data, infographie | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 10 | `posterizeTime(8)` + wiggle | Effet stop motion, image par image dessinée | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 11 | Rig respiration asymétrique (inspiration/rétention/expiration/pause) | Logo vivant, attente, ambiance | **[TESTÉ EN LABO, syntaxe/logique Node uniquement]** |
| 12 | Rebond avec gravité (bounce back, Ebberts) | Objet qui tombe et rebondit | **[THÉORIQUE]** |
| 13 | `loopOut("offset")` / `("continue")` | Escalier qui monte, mouvement qui continue sur sa lancée | **[THÉORIQUE]** |
| 14 | Animateur de texte + sélecteur de plage « Expression » | Décalage lettre par lettre piloté | **[THÉORIQUE]** |

### Réglages qui comptent

- **Overshoot (05)** : `freq` règle la raideur, `decay` la rapidité de stabilisation. L'amplitude n'est pas un réglage : elle vient de **la vitesse d'arrivée** (vitesse ÷ 2π·freq). Pour plus de rebond, on arrive plus vite ou on baisse `freq`. Les clés doivent arriver **avec de la vitesse** (sortie linéaire ou peu amortie) : une clé en Easy Ease arrive à vitesse nulle, donc il n'y a pas d'overshoot.
- **Wiggle (01)** : fréquence 0,5 à 2 pour un flottement, 3 à 8 pour une caméra à l'épaule, au-delà c'est une vibration. Amplitude caméra : 2 à 8 px en HD. Sur une seule dimension : séparer les dimensions, ou ne garder qu'un axe du résultat.
- **pingpong (03)** : au retour, l'easing est inversé. Une arrivée longue devient un départ long. Si l'asymétrie compte, faire un cycle complet et utiliser `cycle`.
- **cycle (02)** : la dernière clé doit avoir la même valeur que la première, avec des tangentes compatibles, sinon un « hoquet » apparaît à chaque tour.

- **Saccade (step-printing)** : régulière = `posterizeTime(8);` sur le Time Remap d'une précomp [THÉORIQUE] ; **choisie** = Time Remap en clés maintenues (Hold) sur les images voulues, Frame Blending coupé. La saccade régulière laisse le hasard choisir les images et rate le coup de lumière [ÉPROUVÉ EN MAQUETTE] (pièce 20 v1). Recette tableau, pièges et traînée : [expressions.md](expressions.md#saccade).

## 5. Organisation de projet et rigs

- **Arborescence** : `00_COMPS_FINALES`, `01_PRECOMPS`, `02_RIGS`, `03_ASSETS` (sous-dossiers IMG, VID, AUDIO, AI), `99_ARCHIVES`. Les noms des comps finales portent le format et la version : `TITRE_16x9_v03`.
- **Un calque `CTRL` (null ou calque d'effets)** porte tous les sliders, cases et couleurs du rig. Les expressions pointent vers `thisComp.layer("CTRL").effect("…")`. On renomme les sliders en français clair, sans fautes : les expressions les appellent par leur nom.
- **Les nulls parents** portent le mouvement global ; les enfants portent le détail (règle « un mouvement, un calque ») : la position sur le null, la rotation sur l'enfant. On évite d'empiler trois animations sur la même propriété.
- **Les précomps** pour isoler un élément réutilisable (logo, carte) ; exposer les réglages utiles via les **Propriétés essentielles** (Essential Graphics) si le rig doit partir en MOGRT vers Premiere.
- **Couleurs de calques** par fonction (contrôleurs, textes, formes, adjustment) et **marqueurs de comp** nommés sur les temps forts de la musique.
- **Le timing global** se règle par des précomps qu'on peut caler sur la musique : déplacer une précomp, c'est déplacer tout un geste sans casser l'easing interne.

## 6. Pièges

- **Moteur JavaScript vs ExtendScript hérité.** Depuis AE 16.0 (CC 2019), le moteur par défaut est **JavaScript** (ECMAScript 2018), plus rapide. L'ancien moteur **ExtendScript hérité** suit ECMAScript 3. Le choix se fait par projet : Fichier > Paramètres du projet > onglet Expressions. Les projets enregistrés dans d'anciennes versions s'ouvrent en ExtendScript hérité. Erreurs classiques en passant à JavaScript : `if/else` sur une ligne sans accolades, raccourci `this()` (utiliser `thisLayer`), syntaxe en snake_case (`this_comp`, à remplacer par `thisComp`), `sourceText` qui doit parfois être lu en `.value`. Écrire pour le moteur JavaScript, avec accolades et points-virgules, et ne pas dépendre de la « dernière valeur » d'un `if` sans `else`.
- **Expressions lentes.** Toute expression est réévaluée à chaque image, et `valueAtTime` ou `sampleImage` en boucle multiplient le coût. `sampleImage()` (lire la couleur d'un calque) est la plus coûteuse : à réserver à un pixel ou une petite zone, et sur peu de calques. Les échos en cascade (06) sur 50 calques et des boucles `for` sur `numKeys` ralentissent l'aperçu. Remèdes : **Convertir l'expression en images clés** (Animation > Assistant d'images clés) une fois le réglage figé, `posterizeTime` pour les valeurs qui n'ont pas besoin de 25 i/s, la vue « Expressions désactivées » (raccourci d'aperçu) pour travailler l'animation.
- **`exp()` qui explose.** Dans un overshoot, `Math.exp(decay * t)` devient `Infinity` après quelques minutes ; d'où la coupure (`t < 3`) dans la recette 05 (point signalé par Dan Ebberts).
- **Vitesse d'arrivée nulle = pas d'overshoot.** Voir 05 : c'est la cause n° 1 de « mon expression ne fait rien ».
- **Bézier spatial non voulu.** Par défaut, les trajectoires de position sont courbes : le calque peut faire une boucle ou dépasser **dans l'espace**. Clic droit > Interpolation spatiale > Linéaire si le chemin doit être droit.
- **Séparer les dimensions** change ce que montre le graphe de vitesse (vitesse par axe et non vitesse le long du chemin). L'overshoot sur Position 2D non séparée dépasse sur les deux axes à la fois, proportionnellement à leurs vitesses (vérifié en labo).
- **Wiggle et duplication.** Le tirage aléatoire de `wiggle` varie d'un calque à l'autre ; pour contrôler ou figer un tirage, on utilise `seedRandom()`. Le comportement exact à la duplication n'a pas été vérifié ici : voir la phase 2.
- **Fréquence d'overshoot et cadence.** À 25 i/s, un overshoot très rapide (freq > 6) peut tomber entre les images et paraître sauter (voir l'incident en labo). Juger à l'œil à 25 i/s, pas à 50.
- **Période qui varie dans un `sin` = mouvement qui se fige.** `Math.sin(2*Math.PI*time/P)` avec `P` animé (un bercement qui ralentit, une respiration qui s'apaise) ne donne pas la fréquence 1/P : la fréquence réelle est 1/P − t·P'/P² et tombe presque à zéro (mesuré : 0,02 Hz au lieu de 0,31 à 0,63 Hz, `labo/ae-expressions/bercement/test.js`) : le geste **hésite et repart**, l'inverse du calme voulu. Intégrer la phase (recette « bercement qui ralentit » dans `expressions.md`). Même piège dans un `wiggle(freq, …)` à `freq` animée. [TESTÉ EN LABO] (sous Node)
- **Moteur et compatibilité.** Un projet partagé avec un poste en ExtendScript hérité peut afficher des erreurs d'expression en série. Fixer le moteur dans le cahier des charges.

## 7. À vérifier en phase 2

La liste des 11 vérifications dans AE (expressions sur de vrais calques, pic d'overshoot, courbe d'`ease`, F9, `posterizeTime` à 25 i/s, `seedRandom`…) est dans [expressions.md](expressions.md#phase-2).
