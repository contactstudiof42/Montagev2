# RAPPORT — Phase 1 (cloud)

## SYNTHÈSE (réécrite à chaque session — dernière : session 1, 2026-10-09)

### Mon point de vue artistique actuel
Je défends un travail **réduit à une idée** (un concept, un signe — Saul Bass), où **le mouvement a une cause** et porte sur le paramètre qui raconte, pas sur le premier venu (échelle, opacité). J'arbitre par l'émotion avant la continuité (Murch), et je règle le rythme sur l'état intérieur, pas sur l'action (Schoonmaker). J'évite la symétrie mécanique, le carton centré qui zoome, le *drone* de tension, le look « bande-annonce » de l'IA.
Ce qui a changé cette session : en atelier, j'ai corrigé un excès (v1 : un « pulse » de 22 %) par un manque (v2 : 6 %, invisible). La vraie correction a été de **déplacer** le mouvement vers un autre paramètre (l'interlettrage qui se resserre : un corps qui retient son souffle). C'est ma leçon la plus nette.

### Niveau par domaine (confiance : faible / moyenne / bonne)
| Domaine | Niveau | Confiance | Commentaire |
|---|---|---|---|
| Regard / autocritique | méthode écrite, appliquée 4 fois | moyenne | grille éprouvée sur une seule pièce |
| Direction artistique | méthode écrite | faible | pas encore d'examen |
| Culture montage / title design | 10 fiches + 1 fiche IA | moyenne | sources secondaires surtout, faits incertains listés en fin de fiche |
| Rythme | principes + mesure des coupes | moyenne | pas encore d'exercice d'atelier |
| Motion design | principes + 1 pièce en 4 versions | moyenne | |
| Son | principes + 1 design sonore synthétique | faible | je ne peux pas écouter : jugement par forme d'onde |
| Loudness / livraison | recettes testées en labo | bonne | méthode mesure + gain validée à 0,0-0,2 LU |
| After Effects | expressions testées (syntaxe/logique Node) | moyenne | comportement réel AE non vérifié |
| IA générative | état de l'art daté 2026-10 | moyenne | rien testé, info volatile |
| Blender | rendu en ligne de commande maîtrisé pour l'atelier | moyenne | pas encore de skill dédié |
| Couleur, Resolve, Premiere, tournage VFX | — | — | à venir |

### Œuvres et auteurs analysés (fiches dans `culture/`)
- **Walter Murch** (*In the Blink of an Eye*) : l'émotion gagne les arbitrages ; couper à la fin d'une pensée ; le son porte le raccord.
- **Thelma Schoonmaker** (*Raging Bull*, *Goodfellas*) : le rythme suit l'état intérieur ; retirer le son avant l'impact.
- **Saul Bass** (génériques) : un concept, un signe, animé sur la musique.
- **Kyle Cooper** (*Se7en*) : montrer le processus plutôt que le personnage.
- **Edgar Wright** : montage « hip-hop » d'une routine ; la transition comme gag ; la synchro musicale se fabrique au tournage.
- **Michel Gondry** (*Star Guitar*) : chaque couche sonore a une famille visuelle stable ; la synchro tombe sur des événements dans l'image, pas sur les coupes, et le public apprend la règle.
- **Jonathan Glazer** (Guinness *Surfer*) : quand le message parle du temps, faire réellement attendre ; deux blocs de cadence contrastés, une seule bascule.
- **Sally Menke** (Tarantino) : faire durer la tension tant que le rapport de force n'a pas basculé ; la résolution est bien plus courte que l'attente.
- **Kirk Baxter et Angus Wall** (*The Social Network*) : une situation-cadre (déposition) comme pivot de montage, avec des raccords question/réponse entre présent et passé.
- **Patrick Clair** (générique de *True Detective*) : le décor devient le contenu du personnage ; les défauts d'un traitement poussé à l'extrême deviennent la matière.
- **IA** (`culture/ia-oeuvres-remarquables.md`) : *Total Pixel Space*, *Ancestra*, *The Hardest Part* (Washed Out / Paul Trillo), contre-exemple Coca-Cola : l'IA convainc quand le procédé est le sujet.

### Atelier
- **Pièce 01 « Respiration »** (`atelier/01-respiration/`) : carton-titre d'apnée, 4 versions. Planches : `v1-planche.png` → `v2-planche.png` → `v3-planche.png` → `v4-planche.png` (+ `v4-onde.png` pour le son). Critiques notées dans `CRITIQUE.md`. Progression : pulse mécanique et bug d'apparition (v1) → asymétrie mais mouvement invisible (v2) → mouvement déplacé sur l'interlettrage, fond en profondeur (v3) → police choisie et son (v4).

### Dernier examen créatif
Aucun pour l'instant (premier prévu en session 2 ou 3).

### Skills (voir le sommaire dans `.claude/skills/montage-expert/SKILL.md`)
`montage-expert`, `montage-regard`, `montage-direction-artistique`, `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion` (artistiques, v1) ; `montage-loudness-livraison` (testé en labo), `montage-after-effects` (testé en syntaxe et logique Node, pas dans AE), `montage-ia-generative` (théorique, daté).

### État de l'art IA générative (au 2026-10-09, sources dans `sources/ia-generative-2026-10.md`, rien testé)
- Vidéo : Veo 3.1 (MAJ janv. 2026 : 9:16 natif, upscale 4K), Kling 3.0 (févr. 2026, jusqu'à 15 s avec son), Seedance 2.0 (févr. 2026), Runway Gen-4.5 (déc. 2025). **Sora arrêté** selon la page officielle OpenAI (app fermée le 26/04/2026, API annoncée pour le 24/09/2026 ; retrait effectif connu par une seule source secondaire).
- Logiciels : Premiere 26 (masque/suivi d'objet IA, Firefly Boards multi-modèles ; Generative Extend limité à 2 s, 8 bits SDR), Resolve 21 / 21.1 (CineFocus, Magic Mask 2.0).
- Droit : AI Act art. 50 (transparence, deepfakes) applicable depuis le 02/08/2026 — à confirmer sur le texte officiel. Musique IA : Suno sous licence Warner (nov. 2025) ; Udio fermé à l'export.

### Phase 2 : priorités du `PLAN-TESTS-MCP.md`
1. Lire l'état des hôtes et les skills fournis par le serveur Higgsfield avant toute action (une liste de noms d'outils `ae_`, `pr_`, `bl_` a été **observée** dans l'environnement le 2026-10-09, non appelée).
2. AE : comp de test, texte, clés avec easing, export d'images ; puis coller les 11 expressions du labo et comparer aux valeurs Node.
3. Premiere / Resolve : loudness mesuré par le logiciel contre ffmpeg sur les mêmes WAV (écart attendu ≤ 0,5 LU) ; normalisation à l'export = gain ou compression ?
4. Blender : refaire la pièce 01 via MCP et comparer aux planches.

### Questions sur vos goûts (pour remplir `GOUTS.md`, actuellement absent)
1. Trois films, clips ou pubs dont le **montage** vous a marqué ? Et un que vous trouvez surcoté ?
2. Plutôt **retenue** (plans longs, silence, peu d'effets) ou **énergie** (montage serré, typo qui bouge, synchro musicale) ? Les deux selon les projets ?
3. Des studios de motion design ou des génériques de référence (Elastic, Buck, ManvsMachine, Saul Bass, autre) ?
4. Le grain, les défauts, l'argentique : vous aimez, ou vous préférez une image nette et propre ?
5. L'IA générative dans vos projets : visible et assumée, invisible (raccords), ou à éviter ?
6. Quels formats faites-vous le plus (pub, réseaux verticaux, corporate, clip) ? C'est là que je concentrerai mes examens.
7. Une typographie ou une palette que vous détestez ?

### Autres questions et prochaines priorités
- Questions : quelles normes de loudness pour vos livraisons TV (charte PAD de quelle chaîne) ? Avez-vous des rushes libres de droits à me donner pour l'atelier ?
- Prochaines priorités : examen créatif n°1 ; `montage-couleur-et-intention` + labo couleur (OCIO/colour-science) ; pièce 02 « spectaculaire » (contraste avec la 01) ; skill `montage-references` à partir de ~10 fiches ; exercice de rythme (même matériau sur trois tempos).

---

## JOURNAL

### Session 1 — 2026-10-09, 22:48 → (fin indiquée plus bas) UTC
