# RAPPORT — Phase 1 (cloud)

## SYNTHÈSE (réécrite à chaque session — dernière : session 1, 2026-10-09)

### Mon point de vue artistique actuel
Je défends un travail **réduit à une idée** (un concept, un signe — Saul Bass), où **le mouvement a une cause** et porte sur le paramètre qui raconte, pas sur le premier venu (échelle, opacité). J'arbitre par l'émotion avant la continuité (Murch), et je règle le rythme sur l'état intérieur, pas sur l'action (Schoonmaker). J'évite la symétrie mécanique, le carton centré qui zoome, le *drone* de tension, le look « bande-annonce » de l'IA.
Ce qui a changé cette session : j'ai appris à me méfier de mes impressions sur une planche réduite (un faux diagnostic de bruit, démenti par la mesure). En atelier, j'ai corrigé un excès (v1 : un « pulse » de 22 %) par un manque (v2 : 6 %, invisible). La vraie correction a été de **déplacer** le mouvement vers un autre paramètre (l'interlettrage qui se resserre : un corps qui retient son souffle). C'est ma leçon la plus nette.

### Niveau par domaine (confiance : faible / moyenne / bonne)
| Domaine | Niveau | Confiance | Commentaire |
|---|---|---|---|
| Regard / autocritique | méthode écrite, appliquée 4 fois | moyenne | grille éprouvée sur une seule pièce |
| Direction artistique | méthode écrite, éprouvée par l'examen n°1 (13/20) | faible à moyenne | audace insuffisante, clichés de catégorie non vus → méthode corrigée |
| Culture montage / title design / couleur | 10 fiches + 3 fiches couleur + 1 fiche IA | moyenne | sources secondaires surtout, faits incertains listés en fin de fiche |
| Rythme | principes + mesure des coupes | moyenne | pas encore d'exercice d'atelier |
| Motion design | principes + 1 pièce en 4 versions | moyenne | |
| Son | principes + 1 design sonore synthétique | faible | je ne peux pas écouter : jugement par forme d'onde |
| Loudness / livraison | recettes testées en labo | bonne | méthode mesure + gain validée à 0,0-0,2 LU |
| After Effects | expressions testées (syntaxe/logique Node) | moyenne | comportement réel AE non vérifié |
| IA générative | état de l'art daté 2026-10 | moyenne | rien testé, info volatile |
| Blender | rendu en ligne de commande maîtrisé pour l'atelier | moyenne | pas encore de skill dédié |
| Couleur (intention) | principes + 3 fiches | moyenne | pas encore éprouvé en atelier |
| Couleur (pipeline) | conversions et LUT testées (colour-science 0.4.7, OCIO 2.6) | moyenne à bonne | pas de vrai rush log testé |
| Resolve, Premiere, tournage VFX | — | — | à venir |

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
- **Vittorio Storaro** : une couleur = un état, qui évolue avec le récit ; le noir est un outil.
- **Christopher Doyle / Wong Kar-wai** : la couleur dit ce que les personnages taisent ; un seul rouge saturé porté par le décor.
- **Roger Deakins** : une couleur par lieu ou chapitre, une source crédible pour chaque teinte, la retenue.
- **IA** (`culture/ia-oeuvres-remarquables.md`) : *Total Pixel Space*, *Ancestra*, *The Hardest Part* (Washed Out / Paul Trillo), contre-exemple Coca-Cola : l'IA convainc quand le procédé est le sujet.

### Atelier
- **Pièce 01 « Respiration »** (`atelier/01-respiration/`) : carton-titre d'apnée de 10 s, 5 versions. Planches : `v1-planche.png` → `v2-planche.png` → `v3-planche.png` → `v4-planche.png` (+ `v4-onde.png` pour le son) → `v5-planche.png`. Critiques notées dans `CRITIQUE.md`. Progression :
  - v1 : pulse mécanique de 22 % et bug d'apparition (mot noir sur fond bleu) ;
  - v2 : asymétrie juste, mais mouvement devenu invisible ;
  - v3 : mouvement **déplacé** sur l'interlettrage (le mot se resserre pendant l'apnée), fond en profondeur ;
  - v4 : police choisie (EB Garamond) et design sonore synthétique ;
  - v5 : interlettrage adapté à la police, inspiration plus lisible ;
  - v6 : j'ai corrigé un « bruit de rendu »… qui n'existait pas. La mesure a montré que les taches venaient de l'encodage H.264 du dégradé (`v5-v6-detail-fond.png`).
  Leçon : mesurer avant de corriger. Version de référence : v6 avec le son « silence ».

### Dernier examen créatif
**N°1 — spot 30 s + vertical 15 s pour une mutuelle (offre jeunes parents)** : `examens/01-mutuelle-jeunes-parents.md`. Recommandation : montage de gestes de nuit en très gros plans, puis bascule vers un plan long de 9 s (le soulagement). **Autocritique : 13/20.**
- Deux directions sur trois étaient trop proches (réalistes, nocturnes).
- Deux clichés de catégorie m'ont échappé (la boîte à musique, le montage de gestes du quotidien).
- Je n'ai vérifié ni la faisabilité ni le réglementaire.

`montage-direction-artistique` est corrigé en conséquence : une direction doit changer de registre, et j'ajoute un test du cliché, la version muette, la faisabilité et les contraintes du secteur.

### Skills (voir le sommaire dans `.claude/skills/montage-expert/SKILL.md`)
Artistiques (v1) : `montage-expert`, `montage-regard`, `montage-direction-artistique` (corrigé après examen), `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`.
Techniques : `montage-grammaire` (théorique), `montage-loudness-livraison` (testé en labo), `montage-couleur-pipeline` (testé en labo), `montage-after-effects` (testé en syntaxe et logique Node, pas dans AE), `montage-ia-generative` (théorique, daté).

### État de l'art IA générative (au 2026-10-09, sources dans `sources/ia-generative-2026-10.md`, rien testé)
- Vidéo : Veo 3.1 (MAJ janv. 2026 : 9:16 natif, upscale 4K), Kling 3.0 (févr. 2026, jusqu'à 15 s avec son), Seedance 2.0 (févr. 2026), Runway Gen-4.5 (déc. 2025). **Sora arrêté** selon la page officielle OpenAI (app fermée le 26/04/2026, API annoncée pour le 24/09/2026 ; retrait effectif connu par une seule source secondaire).
- Logiciels : Premiere 26 (masque/suivi d'objet IA, Firefly Boards multi-modèles ; Generative Extend limité à 2 s, 8 bits SDR), Resolve 21 / 21.1 (CineFocus, Magic Mask 2.0).
- Droit : AI Act art. 50 (transparence, deepfakes) applicable depuis le 02/08/2026 — à confirmer sur le texte officiel. Musique IA : Suno sous licence Warner (nov. 2025) ; Udio fermé à l'export.

### Phase 2 : priorités du `PLAN-TESTS-MCP.md`
1. Lire l'état des hôtes et les skills fournis par le serveur Higgsfield avant toute action (une liste de noms d'outils `ae_`, `pr_`, `bl_` a été **observée** dans l'environnement le 2026-10-09, non appelée).
2. AE : comp de test, texte, clés avec easing, export d'images ; puis coller les 11 expressions du labo et comparer aux valeurs Node.
3. Premiere / Resolve : loudness mesuré par le logiciel contre ffmpeg sur les mêmes WAV (écart attendu ≤ 0,5 LU) ; normalisation à l'export = gain ou compression ?
4. Blender : refaire la pièce 01 via MCP et comparer aux planches.

### Vos goûts (`GOUTS.md`, créé le 2026-10-09 à votre demande)
- **Interstellar**, pour le rythme (`culture/interstellar-rythme.md`) : poser une règle du temps et la faire entendre ; un son qui arrache d'une scène à la suivante ; des segments de montage parallèle qui raccourcissent jusqu'au climax. Intégré à `montage-rythme`.
- **Joker**, pour la couleur et l'image (`culture/joker-couleur-image.md`) : la dominante verte gardée, la peau protégée, une couleur forte méritée. Intégré à `montage-couleur-et-intention`.
- **Ziak, « Même pas un grincement »** (Bleu Désert ; montage Antonin Brones, étalonnage Arthur Paux) : **analysé sur le fichier que vous m'avez donné** (`culture/ziak-meme-pas-un-grincement.md`, graphique `culture/ziak-chronologie-mesures.png`). Le clip compte 88 plans (médiane 1,7 s) sur une drill à 143,6 BPM, et **aucune coupe n'est calée sur le beat** : le montage suit l'arrangement (26 coupes/min avec la basse, 13 sans, un plan long et immobile dans chaque creux). Les éclairs des tirs battent leur propre mesure (15 images) contre la musique. 88 % de l'image est presque noire, une seule couleur chaude (le feu) occupe 0,16 % de l'image, et la révélation n'arrive qu'à 3:24. La forme incarne le titre : une machine sans effort visible, sans transition voyante, une menace contenue.
- **Kinetic editing** : nouveau skill `montage-kinetic-editing` et labo de synchronisation des SFX (impacts calés à 2 ms près ; -14,3 LUFS / -1,1 dBTP). La démo est un test technique, pas encore une pièce.

### Questions sur vos goûts (pour compléter `GOUTS.md`)
0. Ziak contre le kinetic editing : le clip de Ziak fait l'inverse du kinetic (rien n'est calé sur le beat, aucun SFX surligné). Aimez-vous les deux pour des usages différents (réseaux contre clip ou film de marque), ou y a-t-il un point commun que je ne vois pas ? Mon analyse de Ziak correspond-elle à ce que vous ressentez ?
1. Un film, un clip ou une pub que vous trouvez surcoté ?
2. Plutôt **retenue** (plans longs, silence, peu d'effets) ou **énergie** (montage serré, typo qui bouge, synchro musicale) ? Les deux selon les projets ?
3. Des studios de motion design ou des génériques de référence (Elastic, Buck, ManvsMachine, Saul Bass, autre) ?
4. Le grain, les défauts, l'argentique : vous aimez, ou vous préférez une image nette et propre ?
5. L'IA générative dans vos projets : visible et assumée, invisible (raccords), ou à éviter ?
6. Quels formats faites-vous le plus (pub, réseaux verticaux, corporate, clip) ? C'est là que je concentrerai mes examens.
7. Une typographie ou une palette que vous détestez ?

### Autres questions et prochaines priorités
- Questions : quelles normes de loudness pour vos livraisons TV (charte PAD de quelle chaîne) ? Avez-vous des rushes libres de droits à me donner pour l'atelier ?
- Prochaines priorités :
  - atelier « direction A dans le noir » (la piste audacieuse de l'examen) ;
  - clôture de la pièce 01 ;
  - pièce 02 spectaculaire et verticale ;
  - skill `montage-grammaire` ;
  - atelier couleur « même plan, trois étalonnages » ;
  - exercice de rythme (même matériau sur trois tempos).

---

## JOURNAL

### Session 1 — 2026-10-09
- **Heure** : 22:48 → 23:25 UTC environ. Démarrage : la branche n'existait pas, je l'ai créée. `GOUTS.md` est absent.
- **Méthode** : j'ai fait moi-même le regard et la création (atelier, examen, synthèse `montage-references`, skills socles). J'ai confié en parallèle à des sous-agents la recherche documentaire et les labos, dont je relis les résultats.
- **Œuvres analysées (14 fiches)** :
  - montage et title design : Murch, Schoonmaker, Saul Bass, Kyle Cooper, Edgar Wright, Gondry (*Star Guitar*), Glazer (Guinness *Surfer*), Sally Menke, Baxter et Wall (*The Social Network*), Patrick Clair (*True Detective*) ;
  - couleur : Storaro, Doyle et Wong Kar-wai, Deakins ;
  - IA : *Total Pixel Space*, *Ancestra*, *The Hardest Part*, pub Coca-Cola.
- **Pièce créée** : 01 « Respiration », v1 → v6. Blender 4.2.3 en ligne de commande (Cycles CPU), ffmpeg, son synthétisé avec numpy, police EB Garamond (OFL).
- **Tests réussis** :
  - loudness : la mesure ebur128 puis un gain atterrit à 0,0-0,2 LU de la cible ; loudnorm en 2 passes rate 2 fois sur 4 (bascule silencieuse en mode dynamique) ;
  - livraison H.264, master et vertical : conformes ;
  - scdet : 8 coupes franches sur 8 détectées ;
  - expressions AE sous Node : 32 tests sur 32 ;
  - couleur : allers-retours exacts, LUT ffmpeg identique au calcul Python (0,0017 code d'écart).
- **Tests ratés ou limites, avec leur cause** :
  - scdet ne voit pas les fondus enchaînés ;
  - le passage mono → stéréo avec `-ac 2` perd 3 dB (il faut `pan`) ;
  - le fetch d'une police sur github.com est bloqué hors périmètre (jsDelivr fonctionne) ;
  - les taches sur le fond clair de la v5 ne venaient pas de Cycles, comme je le croyais, mais de l'encodage H.264 du dégradé : diagnostic faux, corrigé par la mesure ;
  - je ne peux ni voir le mouvement ni entendre le son : je juge par planches et par mesures.
- **Skills créés** : les 13 listés plus haut, dont `montage-direction-artistique` corrigé après l'examen n°1.
- **Observation** : un serveur `HIGGSFIELD_MCP` est visible dans l'environnement. Je ne l'ai pas appelé et j'ai noté les noms d'outils dans `PLAN-TESTS-MCP.md` comme hypothèses.
- **Sources principales** : `sources/culture-session1.md`, `sources/loudness-livraison.md`, `sources/after-effects.md`, `sources/ia-generative-2026-10.md`, `sources/couleur-pipeline.md`. Les faits non vérifiés sont listés en fin de chaque fiche.
