# Court métrage IA « cyberpunk atmosphérique » — plan de travail

- **Genre** : court métrage de fiction entièrement généré, ton atmosphérique (ambiance avant action). **Durée** : 30 s. **Destination** : à préciser par Diego.
- **Médias** : `/Volumes/SSD FAST/CM TEST /` (attention à l'espace en fin de nom). Textes et prompts : ici (versionnés).
- **Statut au 2026-10-23** : stratégie choisie, dossier créé. Pas encore de synopsis, de DA ni de génération.

## Contraintes (Diego, 2026-10-23)
- Pas de Higgsfield. **Budget de génération : 25 $ sur Oxen** (Seedance 2.5). Clé API d'Oxen fournie plus tard.
- Images de référence faites dans GPT (hors budget Oxen).
- La référence Blender sert au **mouvement de caméra et au déplacement des sujets**, pas aux visages (Diego).

## Stratégie retenue : Blender → GPT → Seedance 2.5 (Oxen)
1. **Synopsis et découpage** : 6 à 7 plans de 4 à 5 s. Des plans séparés, pas un plan-séquence (voir leçon 3).
2. **Bible de look** : palette, focale, un seul type de mouvement, et le parti pris qui évite le cliché cyberpunk.
3. **Blender** : décor en volumes gris + caméra + sujets en boîtes de couleur (code couleur écrit dans le prompt). Rendu vidéo de chaque plan → `03_blender/previz/`.
4. **GPT** : une plaque par plan, faite à partir d'une image du rendu Blender (cadrage et disposition seulement), sans personnage ; une fiche personnage (face, profil, dos, tenue). Les enseignes lisibles se font ici, pas dans la vidéo.
5. **Seedance 2.5 Reference to Video** (Oxen) : `@Video1` = la previz, `@Image` = la plaque et la fiche personnage. Audio généré **gardé** comme base (Diego, 2026-10-23) : ambiance et bruitages dans le prompt, « no music, no subtitles » ; musique et éléments ajoutés en post.
6. **Son** : le son généré sert de base ; une nappe d'ambiance continue posée en post sous tous les plans (chaque prise a son propre son, les coupes sauteraient sinon), musique, renforts de bruitages ; séparation des pistes si une prise mélange trop. Coût du son sur Oxen : à vérifier (non documenté).
7. **Topaz Video AI 7.1.4** (local, gratuit) pour l'upscale ; étalonnage commun, grain et halation dans Resolve (projet `P3-`). Son dans Resolve/Fairlight.

## Budget (prix Oxen lus le 2026-10-23 ; estimations à tenir dans un `journal.md`)
| Résolution | Prix | 25 $ donnent |
|---|---|---|
| 480p (et brouillon) | 0,12 $/s | 208 s |
| 720p | 0,26 $/s | 96 s |
| 1080p (ou brouillon finalisé) | 0,65 $/s | 38 s |

Répartition prévue : calibrage 2 × 5 s en 480p (1,20 $) · brouillons 480p, environ 2,5 essais par plan (≈ 10,50 $) · finals en 720p, 7 × 5 s (≈ 9,10 $) · réserve ≈ 4 $. **Le 1080p est hors budget**, sauf pour un plan héros. Le finalisé 1080p d'un brouillon (`draft_task_id`) coûte 0,65 $/s ; un final en 720p est une nouvelle prise, pas celle du brouillon.
À tester sur un plan avant de décider : 480p + Topaz contre 720p + Topaz, comparés en pleine résolution.

## Leçons reprises du projet « studiof42-rise » (2026-10-05/06, même chaîne Blender → plaques → Seedance 2.5 sur Oxen) [projet : studiof42-rise]
1. Sans fiche personnage, les visages changent d'un plan à l'autre (Diego).
2. « Real 35mm film footage, scanned, organic grain » en tête du prompt a rendu l'image « moins IA » (Diego).
3. Un plan-séquence de 20 s avec beaucoup d'actions : le modèle en oublie (le clap), ajoute un étage en trop (« pur slop »), change de vitesse et ne suit plus la référence (Diego). V4 : une action principale par étage, prompt réduit de 2 600 à 900 mots.
4. Objets en surnombre dans les plaques = slop (posters, comics) ; le décor nu à une seule source de lumière a été retenu (Diego).
5. Pas de noms de marques dans les prompts d'images : décrire la forme. Phrase « Do not reproduce any reference 1:1 ».
6. Plaques faites depuis le rendu Blender (cadrage et disposition seulement, couleurs et lumière ignorées).

## Gabarit des prompts Seedance (repris des films du festival Higgsfield, annexe `montage-ia-generative/prompts-seedance-pros.md`)
Un prompt par plan, en anglais, dans cet ordre : SCENE CONTEXT · ACTIVE REFERENCES (pour chaque `@`, ce qu'on en prend et ce qu'on n'en prend pas ; la previz Blender : trajectoire, vitesse, positions des sujets, jamais les matières grises, la lumière ni les visages) · LOCATION MAP · FIRST FRAME AND SPATIAL BLOCKING · OPTICS (angle de champ, distance et hauteur de caméra lus dans Blender) · ACTION TIMING (minuté, une action par segment) · PHYSICS · LIGHTING (une source nommée, pas de lumière de cinéma ajoutée) · STYLE (pellicule de nuit, palette en proportions et en codes hexadécimaux) · POSITIVE CONSTRAINTS (compter personnages et objets ; aucun texte hors des enseignes voulues). Section AUDIO : ambiance et bruitages voulus, « no music, no dialogue » sauf réplique écrite. Prompts versionnés (`LOCK v01`…) et rangés ici.
Ratio observé chez eux : 3 à 5 secondes générées par seconde gardée, soit 90 à 150 s pour nos 30 s ; cohérent avec le budget ci-dessus.
Piste de DA à discuter : le cyberpunk sans néon (tubes fluorescents verdâtres, comme un des films de nuit du festival) pour sortir du cliché.

## Moyens
- Clé API Oxen : à venir (Diego). En attendant, Diego génère dans le Workbench d'Oxen.
- GPT : Diego génère, ou je passe par son profil Chrome « robot » s'il y est connecté (à confirmer).
- Blender 5.2.2 par MCP, Topaz Video AI 7.1.4, Resolve Studio : en place.

## Prochaine étape
Synopsis et découpage en 6-7 plans avec Diego, puis `da.md` (bible de look) avant tout Blender.
