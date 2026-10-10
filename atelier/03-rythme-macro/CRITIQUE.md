# Critique — Atelier 03 « Rythme macro »

Rendus : `build.py <dossier> v1|v2|v3` (≈ 1 min en tout ; vidéos non versionnées). Planches « timeline » : **1 vignette = 1 temps, 1 ligne = 1 mesure** (14 lignes = 14 mesures). On lit donc la musique en lisant la planche de haut en bas.

## v1 (A micro, B macro) — `v1-A-timeline.png`, `v1-B-timeline.png`
- **Défaut technique, mesuré au scdet** : à 25 i/s, un temps à 140 BPM dure 10,71 images. En rendant chaque segment avec sa durée en secondes, ffmpeg arrondit chaque plan à l'image entière **et l'erreur s'accumule** : A coupe toutes les 0,84 s au lieu de 0,857 s, et la dernière coupe arrive à 22,68 s au lieu de 23,14 s (**−460 ms, plus d'un temps de retard**). B dérive de −250 ms. Sur la planche, la coupure de B commence un temps trop tard. Un monteur humain ne voit pas ce bug dans un logiciel de montage (la timeline est en images) ; un agent qui fabrique un montage par script, si.
- **Défaut de couleur** : le plan « braise » sortait magenta/violet (rotation de teinte d'un mandelbrot déjà coloré). Un accent chaud qui n'est pas chaud ne fait pas son travail.
- La palette « acier » laissait passer trop de vert.

## v2 (corrections) — `v2-A-timeline.png`, `v2-B-timeline.png`
- Coupes calculées en **numéros d'image absolus** (`round(t_fin*fps) - round(t_début*fps)`) : écart max mesuré **17 ms** au temps le plus proche (moins d'une demi-image, le minimum possible à 25 i/s), aucune dérive sur 24 s.
- Braise obtenue par désaturation puis mélange de canaux (orange vrai) ; acier plus désaturé (s=0,06).
- **Lecture de A** : la planche est un **motif périodique** (rotation de 6 plans toutes les 3 mesures). L'intro clairsemée et le couplet chargé sont **visuellement identiques** : l'image n'entend que le métronome, pas la musique. Le plan orange revient 4 fois à intervalles réguliers : c'est devenu du papier peint, il ne signifie plus rien.
- **Lecture de B** : la structure du morceau se lit sur la planche (4 lignes tenues = intro, densité qui monte, une ligne orange = coupure, retour au plan d'ouverture = reprise). Critère 1 atteint. 100 % des coupes sur une mesure ou une demi-mesure (critère 2). Le plan chaud n'apparaît qu'une fois, sur le silence (critère 3) : **l'événement visuel le plus fort tombe sur l'absence sonore la plus forte**. C'est le moment du montage.
- **Faiblesses de B** : 6,9 s d'intro sur un seul zoom abstrait, c'est long pour une matière qui n'a pas de sujet (un visage, une action tiendraient ; une fractale non). Le couplet en une coupe par mesure est sage pendant 4 mesures : l'image est « au-dessus » du beat, mais sans tension propre (la seconde horloge à 0,6 s est trop discrète à +6 % pour être perçue sur une planche ; à vérifier en lecture).

## v3 (C hybride) — `v3-C-timeline.png`
- Structure macro (intro tenue, coupure chaude, reprise) + énergie micro **seulement dans le couplet** (coupe tous les 2 temps, puis tous les temps sur les 2 dernières mesures avant la coupure). 23 plans, écart max 17 ms.
- **C'est la meilleure des trois pour un usage réseaux / pub** : on garde le plaisir du calage (la montée finale en coupes au temps prépare la coupure comme un roulement de batterie), mais l'image a encore une forme d'ensemble. Le contraste de densité (0 coupe pendant 6,9 s, puis 21 coupes en 13,7 s, puis 1 plan tenu) **est** le rythme ; le calage n'en est que la texture.
- B reste le choix pour un clip au ton grave (Ziak) : C est plus séduisant, B plus menaçant.

## Ce que j'en retiens (reversé dans les skills)
1. **Le calage sur les temps est une texture, la densité par section est la forme.** Un montage qui coupe au même pas de bout en bout est un métronome, même calé parfaitement. → `montage-rythme`.
2. **Un accent ne vaut que par sa rareté** : un plan ou une couleur d'exception utilisé une fois au bon endroit (le silence) ; quatre fois, c'est un motif. → `montage-rythme`, `montage-couleur-et-intention`.
3. **Événement visuel fort sur l'absence sonore** : la coupure musicale est le meilleur emplacement pour l'image la plus singulière. → `montage-son-et-emotion`.
4. **Technique** : en montage scripté, poser les coupes sur des numéros d'image absolus, jamais en additionnant des durées arrondies ; vérifier au scdet. À 25 i/s, un tempo de 140 BPM ne tombe pas juste : l'erreur de ±½ image est incompressible et inaudible (≤ 20 ms). → `montage-rythme` (recette `[TESTÉ EN LABO]`).
5. Une matière abstraite sans sujet ne tient pas un plan long : la durée qu'un plan supporte dépend de ce qu'il y a à lire dedans (cf. Murch, densité d'information).

## Pistes pour une v4
- Remplacer la banque abstraite par des plans Blender avec un sujet (un objet industriel qu'on démonte, cf. Ziak) et voir si l'intro tenue de B devient tenable.
- Seconde horloge plus forte (+15 %) et mesurer si elle se perçoit sans gêner.
- Ajouter la version A **avec SFX** (kinetic) : le vrai concurrent de B dans les goûts de l'utilisateur.
