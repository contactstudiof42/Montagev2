# Prompts Seedance 2.5 des films sélectionnés au Higgsfield Global Film Festival (lu le 2026-10-23)

Annexe de `SKILL.md` : du savoir (recettes observées), pas des règles gagnées. Tout ce qui suit a été **lu** dans les données ; l'efficacité de chaque tournure est **[NON VÉRIFIÉ]**, tant qu'un essai de notre côté ne l'a pas montrée.

## Source et limites
- Demande de Diego (2026-10-23) : s'inspirer des workflows et prompts « professionnels » visibles sur higgsfield.ai/community/contests.
- Les projets du festival sont publics. Liste de la sélection (126 films, vote du public clos le 15/10, palmarès « dernière semaine d'octobre ») ; chaque projet a un dossier (`snapshot_folder_id`) dont les générations se lisent sans compte : `https://fnf-api-gw.higgsfield.ai/fnf/folders/<id>/items/v2?ordering=asc&include_subfolders=true&size=50&cursor=<cursor>`. Script : `labo/outils/higgsfield_projets.py`.
- Échantillon : 23 films de la sélection (les mieux placés dans la liste, plus ceux de science-fiction ou de nuit), 10 902 générations (plafond de 600 par film), dont 3 482 Seedance 2.5.
- Limites : on voit **toutes** les générations, pas celles qui sont dans le film ; le palmarès n'est pas encore connu ; beaucoup de ces comptes ont des générations illimitées (ce qui change le ratio et la résolution).

## Chiffres [SOURCÉ, données du 2026-10-23]
| Mesure | Valeur |
|---|---|
| Modèle vidéo | Seedance 2.5 : 88 % des vidéos. Kling 3.0, Wan 3.0, MiniMax : marginaux |
| Modèles d'image | Seedream 5 Pro 1 760 · Nano Banana 2 1 288 · GPT Image 2 / 2.5 1 229 · Soul (Higgsfield) environ 1 100 |
| Durée demandée | 30 s : 19 % · 20 s : 16 % · 10 s : 11 % · 4 à 8 s : 23 % |
| Résolution | 720p 52 % · 1080p 37 % · 480p 11 % ; mode brouillon jamais utilisé |
| Format | 16:9 55 % · 21:9 41 % |
| Références par génération | aucune : 34 % · 1 à 3 images : le plus fréquent · une vidéo de référence : 22 % · un son : 11 % |
| Secondes générées par seconde du film | 2,6 (LEAK) · 3,3 (POWER) · 5,0 (Morek) · 5,1 (Carried) ; un cas à 14,5 |
| Longueur des prompts vidéo (médiane par film) | 600 à 23 000 caractères ; la plupart entre 3 000 et 9 000 |
| Son | audio natif activé presque toujours (dialogues), mais « no music » dans 20 films sur 23 et « no subtitles » dans 15 |

## La structure qui revient (sections du prompt, par fréquence)
`SCENE CONTEXT` (une ou deux phrases) → `ACTIVE REFERENCES` (chaque référence et son rôle) → `LOCATION MAP` (la géographie, ce qui existe et ce qui n'existe pas) → `FIRST FRAME AND SPATIAL BLOCKING` (l'état exact de la première image) → `FORMAT MODE` (nombre de temps, coupes ou non, temps réel) → `OPTICS` / `CAMERA` → `ACTION TIMING` (minuté) → `PHYSICS` → `LIGHTING` → `AUDIO` → `CHARACTER ACTING` → `STYLE` → `POSITIVE CONSTRAINTS`.
Cette grille identique d'un film à l'autre vient probablement de l'assistant de prompts de Higgsfield [NON VÉRIFIÉ] ; elle se recopie telle quelle sur Oxen (les références y sont `@Image1`, `@Video1` au lieu de `<<<id>>>`).

## Les tournures, et ce qu'elles cherchent à empêcher
1. **Chaque référence a un rôle, ce qu'on en prend et ce qu'on n'en prend pas.** « A VIDEO REFERENCE, AND THE AUTHORITATIVE SOURCE FOR THE COMPOSITION OF THIS SHOT. Read from it: […] Do NOT read from it: the action, the performance, […] the lighting » (CONTROL). Variante avec portée dans le temps : TAKE / REJECT / SCOPE: 2.0s–6.0s (MAINTENANCE), et une note « anti-conflation » quand deux images montrent la même chose sous deux angles.
2. **Plaque de décor en lumière plate, à rééclairer** : « for location reference — take only the geography and the materials. Do not use as a starting frame […] it is a neutral base plate » (Soulless). La plaque sert à la géographie ; la lumière est décrite dans le prompt.
3. **Compter les objets et les personnes** : « Exactly one instance of him exists in this frame », répété plan par plan (contre les doublons et les objets qui apparaissent).
4. **Décrire la première image** : la position exacte de chacun à 0:00 ; « no empty establishing frame, no delayed reveal » (Random Access).
5. **Minutage seconde par seconde, une action par segment, « Hold » entre deux actions** (Soulless, 500YEN). Un seul verbe de mouvement par temps.
6. **L'optique en mesures physiques** : « 21 degree diagonal field of view […] camera 2.2 meters from the subject », hauteur de caméra en mètres (Random Access) ; focale en mm, ouverture en T (POWER : 28 mm anamorphique, T2.8).
7. **Un paragraphe de physique** : poids, inertie, ombres de contact, « no floating props ».
8. **Une seule source de lumière nommée, et pas de lumière de cinéma ajoutée** : « No fill, no rim light, no softbox » (POWER) ; « Underexposed one stop, crushed blacks with detail » (The Breach).
9. **La palette en proportions et en codes hexadécimaux** : « 60:30:10 », des couleurs en `#8E1E28`, et l'exclusion explicite d'un cliché (« No teal-orange grade, no neon », POWER).
10. **Le look pellicule** : 35 mm (19 films sur 23), grain (17), Arri (21), halation (14), anamorphique (12), obturateur à 180° et 24 i/s ; Kodak Vision3 500T (la pellicule tungstène de nuit) dans 5 films. Et l'exclusion « no 3D render, no game engine, no CGI cleanliness ».
11. **Contre le cliché de la nuit urbaine** : un film de nuit à Tokyo (500YEN) demande des tubes fluorescents verdâtres qui grésillent, « no neon, no colorful LED strips ». Le néon n'apparaît que dans 9 films sur 23.
12. **Gauche et droite anatomiques, et ce qui ne doit pas déborder** : côté conducteur, épaule blessée gauche ; « Rain is on the glass, not inside the car » (TOKYO 4:17).
13. **Des prompts versionnés et rattachés au storyboard** : « LOCK v03 », plans K25 à K30, durée cible au montage (TOKYO 4:17).
14. **Deux façons de découper** : une génération = un plan (le plus courant), ou une génération de 30 s avec des coupes internes de 3 à 5 s (The Breach). Les plans trop courts se rallongent par extension avant ou arrière (The Breach : 84 extensions arrière).
15. **Raccorder plusieurs générations en un faux plan continu** (défi « Impossible Camera », 21-28/10) : cacher les coupes dans le noir, derrière un objet qui passe, dans un changement d'échelle ou un filé.

## Images de référence
- Fiches personnage : vues de face, trois-quarts, profil, dos, sur fond blanc uni, parfois une grille d'expressions, « no text » (500YEN).
- Plaques de décor : « no people » (509 prompts d'images), longues descriptions de l'usure et des sources de lumière réelles ; une plaque de base sert « d'autorité » pour la géométrie et la couleur des plaques suivantes (A Long Lunch).

## Ce que j'en tire pour la chaîne Blender → images → Seedance (hypothèses à tester)
- Blender fournit tout seul les chiffres de la section OPTICS (angle de champ, distance, hauteur de caméra) : à écrire depuis la scène, pas à la main.
- La previz Blender en `@Video1` avec le gabarit « Read from it : trajectoire et vitesse de caméra, positions et déplacements des sujets / Do NOT read from it : matières grises, couleurs, lumière, visages ».
- Plaques en lumière plate (géographie et matières), lumière décrite dans le prompt.
- Ratio de 3 à 5 secondes générées par seconde gardée : c'est la base d'un budget.
