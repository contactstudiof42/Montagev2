# RAPPORT — Phase 1 (cloud)

## SYNTHÈSE (réécrite à chaque session — dernière : session 2, 2026-10-10)

### Mon point de vue artistique actuel
Je défends un travail **réduit à une idée**, où **le mouvement a une cause** et où chaque plan est relié au suivant par autre chose que le tempo. J'arbitre par l'émotion avant la continuité (Murch). En couleur, je garde un environnement bas et froid et une seule chaleur méritée (vos goûts : Joker, Ziak).
**Ce qui a changé cette session** : la pièce 02 m'a appris que **le kinetic editing donne l'énergie, mais que c'est la cause entre les plans qui donne le sens**. Jusqu'à la v4, mes plans (pendule, cube, billes, allumette) défilaient bien en rythme, mais ce n'était qu'une suite d'objets. En v5, le pendule, qui représente le temps, frotte l'allumette à l'apogée de son balancement. La même accélération est devenue une montée, et le suspense vient de la physique (le pendule ralentit en haut de sa course), pas d'un effet. J'ai aussi appris à **mesurer un parti pris de couleur** (% de pixels chauds par image), comme on mesure une loudness. Enfin, j'ai désormais une limite à l'esprit : ce que je ne peux pas juger sans voir le mouvement (durée du silence, ressenti des SFX).

### Niveau par domaine (confiance : faible / moyenne / bonne)
| Domaine | Niveau | Confiance | Commentaire |
|---|---|---|---|
| Regard / autocritique | méthode écrite, appliquée sur 2 pièces (12 versions) | moyenne à bonne | ajout du critère « liaison » et de la planche « 1re image de chaque plan » |
| Direction artistique | méthode écrite, éprouvée par l'examen n°1 (13/20) | faible à moyenne | audace insuffisante, clichés de catégorie non vus → méthode corrigée |
| Culture montage / title design / couleur | 10 fiches + 3 fiches couleur + 1 fiche IA | moyenne | sources secondaires surtout, faits incertains listés en fin de fiche |
| Rythme | principes + mesure des coupes | moyenne | pas encore d'exercice d'atelier |
| Motion design | principes + 1 pièce en 4 versions | moyenne | |
| Son | principes + 1 design sonore synthétique | faible | je ne peux pas écouter : jugement par forme d'onde |
| Loudness / livraison | recettes testées en labo | bonne | méthode mesure + gain validée à 0,0-0,2 LU |
| After Effects | expressions testées (syntaxe/logique Node) | moyenne | comportement réel AE non vérifié |
| IA générative | état de l'art daté 2026-10 | moyenne | rien testé, info volatile |
| Blender | plateau multi-caméras + EDL JSON, rendu CLI maîtrisé | moyenne à bonne | skill `montage-blender` v1 ; flamme, simulation et Eevee non testés |
| Couleur (intention) | principes + 3 fiches | moyenne | pas encore éprouvé en atelier |
| Couleur (pipeline) | conversions et LUT testées (colour-science 0.4.7, OCIO 2.6) | moyenne à bonne | pas de vrai rush log testé |
| Resolve | `montage-resolve` v1 : nodes, RCM, API de scripting (README 2022-2023) | faible à moyenne | rien exécuté ; versions 19-20 à lire |
| Encodage / bandes | labo testé : 10 bits, grain σ≈2 | bonne | ré-encodage plateforme simulé, pas réel |
| Kinetic editing | skill + labo + pièce 02 en 6 versions | moyenne à bonne | ressenti des SFX non jugé à l'oreille |
| Préparation tournage VFX | skill v1 | faible à moyenne | théorique, rien testé |
| Premiere | — | — | à venir |

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
- **Hiro Murai, « This Is America »** (nouveau) : ne pas monter le choc ; la coupe prévient et amortit, un plan continu expose le spectateur. Le pôle opposé du kinetic.
- **Honda « Cog »** (nouveau) : quand la preuve est l'argument, ne pas couper (et cacher l'unique raccord dans une sortie de champ) ; les sons des objets font la bande-son. A directement corrigé la pièce 02.
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

- **Pièce 02 « Étincelle »** (`atelier/02-etincelle/`, critique dans `CRITIQUE.md`) : vertical 9:16 de 8,9 s, kinetic, dans vos goûts (tic d'horloge à la Interstellar, froid cyan-vert, une seule chaleur à la Ziak). Planches : `v1-planche.png` → … → `v6-planche.png`, plus `v5-allumage.png`.
  - v1 : 7 plans sur 19 illisibles à leur 1re image (sujet hors cadre, noir, minuscule), whoosh sur des billes invisibles, allumette qui ressemble à une sucette ;
  - v2-v4 : lisibilité réparée plan par plan (fenêtres recalées sur la cinématique, caméra des billes au ras du sol), règle couleur **mesurée** ;
  - v5 : changement de conception, **le pendule allume l'allumette** ; le reflet de la flamme sur la boule chromée, le pendule qui continue de battre à côté du feu dans le plan final ;
  - v6 : référence, 19/19 plans lisibles, 0,14 % de pixels chauds avant l'allumage contre 3,7 % après, -14,2 LUFS / -2,0 dBTP.
  Reste : vraie flamme, chaîne causale complète, variante en montage macro façon Ziak.

### Dernier examen créatif
**N°2 — clip de rap « Marée basse » (clip 16:9 + 3 extraits verticaux)** : `examens/02-clip-rap-maree-basse.md`. Recommandation : montage macro avec une horloge-marée (un plan fixe du quai qui revient, l'eau plus basse à chaque retour) pour le clip, et des extraits en kinetic tirés des mêmes rushes. **Autocritique : 14/20.** Le double usage est bien résolu et la préparation du tournage est solide (4K pour le 9:16, log 10 bits, son seul, autorisations). Mais j'ai plaqué votre goût Ziak comme une recette et raté l'image propre au sujet (la marée basse découvre ce qui était caché), et la direction B était une direction de paille. `montage-direction-artistique` est corrigé (étape « idée propre au sujet », test de mon propre système).

Précédent : **N°1 — spot 30 s + vertical 15 s pour une mutuelle (offre jeunes parents)** : `examens/01-mutuelle-jeunes-parents.md`. Recommandation : montage de gestes de nuit en très gros plans, puis bascule vers un plan long de 9 s (le soulagement). **Autocritique : 13/20.**
- Deux directions sur trois étaient trop proches (réalistes, nocturnes).
- Deux clichés de catégorie m'ont échappé (la boîte à musique, le montage de gestes du quotidien).
- Je n'ai vérifié ni la faisabilité ni le réglementaire.

`montage-direction-artistique` est corrigé en conséquence : une direction doit changer de registre, et j'ajoute un test du cliché, la version muette, la faisabilité et les contraintes du secteur.

### Skills (voir le sommaire dans `.claude/skills/montage-expert/SKILL.md`)
Artistiques (v1) : `montage-expert`, `montage-regard`, `montage-direction-artistique` (corrigé après examen), `montage-rythme`, `montage-motion-design-principes`, `montage-son-et-emotion`, `montage-references`, `montage-couleur-et-intention`.
Plus `montage-kinetic-editing` (calage testé en labo, éprouvé en atelier 02).
Techniques : `montage-grammaire` (théorique), `montage-loudness-livraison` (testé en labo, + bandes dans les noirs), `montage-couleur-pipeline` (testé en labo), `montage-after-effects` (testé en syntaxe et logique Node, pas dans AE), `montage-ia-generative` (théorique, daté), **`montage-blender`** (nouveau, testé en atelier), **`montage-resolve`** (nouveau, théorique), **`montage-preparation-tournage-vfx`** (nouveau, théorique).

### État de l'art IA générative (au 2026-10-09, sources dans `sources/ia-generative-2026-10.md`, rien testé)
- Vidéo : Veo 3.1 (MAJ janv. 2026 : 9:16 natif, upscale 4K), Kling 3.0 (févr. 2026, jusqu'à 15 s avec son), Seedance 2.0 (févr. 2026), Runway Gen-4.5 (déc. 2025). **Sora arrêté** selon la page officielle OpenAI (app fermée le 26/04/2026, API annoncée pour le 24/09/2026 ; retrait effectif connu par une seule source secondaire).
- Logiciels : Premiere 26 (masque/suivi d'objet IA, Firefly Boards multi-modèles ; Generative Extend limité à 2 s, 8 bits SDR), Resolve 21 / 21.1 (CineFocus, Magic Mask 2.0).
- Droit : AI Act art. 50 (transparence, deepfakes) applicable depuis le 02/08/2026 — à confirmer sur le texte officiel. Musique IA : Suno sous licence Warner (nov. 2025) ; Udio fermé à l'export.

### Phase 2 : priorités du `PLAN-TESTS-MCP.md`
1. Lire l'état des hôtes et les skills fournis par le serveur Higgsfield avant toute action (une liste de noms d'outils `ae_`, `pr_`, `bl_` a été **observée** dans l'environnement le 2026-10-09, non appelée).
2. AE : comp de test, texte, clés avec easing, export d'images ; puis coller les 11 expressions du labo et comparer aux valeurs Node.
3. Premiere / Resolve : loudness mesuré par le logiciel contre ffmpeg sur les mêmes WAV (écart attendu ≤ 0,5 LU) ; normalisation à l'export = gain ou compression ?
4. Blender : refaire la pièce 01 et la pièce 02 via MCP et comparer aux planches (tests 5 et 13).
5. Premiere : remonter la pièce 02 depuis sa liste de plans JSON (test 11) ; exports 10 bits et grain contre les bandes (test 12).
6. **Garde-fou** : les outils de génération Higgsfield (`bl_generate_*`…) peuvent consommer des crédits payants ; ne rien générer sans votre accord explicite.

### Vos goûts (`GOUTS.md`, créé le 2026-10-09 à votre demande)
- **Interstellar**, pour le rythme (`culture/interstellar-rythme.md`) : poser une règle du temps et la faire entendre ; un son qui arrache d'une scène à la suivante ; des segments de montage parallèle qui raccourcissent jusqu'au climax. Intégré à `montage-rythme`.
- **Joker**, pour la couleur et l'image (`culture/joker-couleur-image.md`) : la dominante verte gardée, la peau protégée, une couleur forte méritée. Intégré à `montage-couleur-et-intention`.
- **Ziak, « Même pas un grincement »** (Bleu Désert ; montage Antonin Brones, étalonnage Arthur Paux) : **analysé sur le fichier que vous m'avez donné** (`culture/ziak-meme-pas-un-grincement.md`, graphique `culture/ziak-chronologie-mesures.png`). Le clip compte 88 plans (médiane 1,7 s) sur une drill à 143,6 BPM, et **aucune coupe n'est calée sur le beat** : le montage suit l'arrangement (26 coupes/min avec la basse, 13 sans, un plan long et immobile dans chaque creux). Les éclairs des tirs battent leur propre mesure (15 images) contre la musique. 88 % de l'image est presque noire, une seule couleur chaude (le feu) occupe 0,16 % de l'image, et la révélation n'arrive qu'à 3:24. La forme incarne le titre : une machine sans effort visible, sans transition voyante, une menace contenue.
- **Kinetic editing** : nouveau skill `montage-kinetic-editing` et labo de synchronisation des SFX (impacts calés à 2 ms près ; -14,3 LUFS / -1,1 dBTP). La démo est un test technique, pas encore une pièce.

### Questions sur vos goûts (pour compléter `GOUTS.md`)
0. ~~Ziak contre le kinetic editing~~ → réponse : **usages différents** (kinetic pour les réseaux, montage macro façon Ziak pour le clip et le film de marque). Reporté dans `GOUTS.md` et les skills.
1. Un film, un clip ou une pub que vous trouvez surcoté ?
2. Plutôt **retenue** (plans longs, silence, peu d'effets) ou **énergie** (montage serré, typo qui bouge, synchro musicale) ? Les deux selon les projets ?
3. Des studios de motion design ou des génériques de référence (Elastic, Buck, ManvsMachine, Saul Bass, autre) ?
4. Le grain, les défauts, l'argentique : vous aimez, ou vous préférez une image nette et propre ?
5. L'IA générative dans vos projets : visible et assumée, invisible (raccords), ou à éviter ?
6. Quels formats faites-vous le plus (pub, réseaux verticaux, corporate, clip) ? C'est là que je concentrerai mes examens.
7. Une typographie ou une palette que vous détestez ?

8. (nouveau) Pour les pièces dans votre goût : préférez-vous que je pousse la **pièce 02** vers un vrai objet de marque (une allumette = un produit ?), ou que je fasse une **variante en montage macro façon Ziak** du même matériau pour comparer les deux usages ?
9. (nouveau) Le grain : la mesure montre qu'il protège les noirs des bandes après la compression des plateformes. Est-ce que vous l'aimez visible (texture argentique) ou seulement technique (invisible) ?

### Autres questions et prochaines priorités
- Questions : quelles normes de loudness pour vos livraisons TV (charte PAD de quelle chaîne) ? Avez-vous des rushes libres de droits à me donner pour l'atelier ?
- Prochaines priorités :
  - atelier « ce que la marée découvre » (révélé par l'examen n°2) ;
  - tests de keying et de tracking sur médias CC0 ;
  - pièce 02 v7 : vraie flamme, chaîne causale complète, variante façon Ziak ;
  - atelier « direction A dans le noir » (la piste audacieuse de l'examen n°1) ;
  - atelier couleur « même plan, trois étalonnages » traduit en arbre de nodes Resolve ;
  - Premiere (`montage-premiere`) et préparation de tournage VFX.

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

### Session 2 — 2026-10-09 23:52 → 2026-10-10 ~00:40 UTC
- **Démarrage** : le contrôle anti-doublon a d'abord arrêté la session (dernier commit 80 s plus tôt). Vous m'avez confirmé un faux positif et j'ai repris.
- **Pièce créée** : 02 « Étincelle », de v1 à v6 (Blender 4.2.3 Cycles CPU, sons synthétisés avec numpy, police Inter OFL ; aucun média tiers). Les scripts sont réutilisables : plateau multi-caméras, liste de plans en JSON, rendu des seules images utiles avec cache.
- **Tests réussis** :
  - labo encodage (`labo/encodage/`) : le critère de bandes est validé sur une source sans perte (tramage 1,9 contre 5,3 sans tramage) ; le 10 bits x264 donne 1,56 ; un grain σ≈2/255 tient après ré-encodage 8 bits (3,2 contre 5,2) ; le filtre ffmpeg `noise=c0s=4:allf=t` est calibré à σ = 2,3 ;
  - labo keying (`labo/keying/`, alpha de vérité terrain rendu dans Blender) : de 0,3 à 3 m du fond vert, le débordement est divisé par 2,6 et les trous dans le sujet par 6 ; un fond surexposé fait manger le sujet par le keyer ; `despill` supprime le vert résiduel ; les cheveux fins sont perdus avec `chromakey` ;
  - pièce 02 : loudness -14,2 LUFS / -2,0 dBTP mesurée sur le MP4 ; calage des SFX vérifié dans les mesures ; règle de couleur mesurée.
- **Tests ratés, avec leur cause** :
  - le tramage ±1 niveau et `-tune grain` ne protègent pas les noirs des bandes (x264 lisse ce bruit) : ma piste de la session 1 était fausse ;
  - pièce 02 : deux régressions dues à des fenêtres de source recopiées à la main après un changement de cinématique ;
  - `pip install` installait numpy pour un autre Python ;
  - une boucle `until pgrep` se détectait elle-même.
- **Œuvres analysées** : Hiro Murai « This Is America » (sources : PremiumBeat, entretien du monteur Ernie Gilbert ; The Fader), Honda « Cog » (Campaign, Autotrader, Wikipedia).
- **Skills créés** : `montage-blender`, `montage-resolve`, `montage-preparation-tournage-vfx` (théorique) (README de l'API de scripting, copies 2022 et 2023).
- **Skills modifiés** : `montage-regard` (critère « liaison », 3 leçons), `montage-kinetic-editing` (sujet lisible à la 1re image, SFX dont la cause est visible, leçon de l'atelier 02), `montage-references` (principe 15b de Murai, tension « monter le choc » / « le laisser arriver »), `montage-loudness-livraison` (bandes dans les noirs), `montage-expert` (sommaire).
- **Examen n°2** : « Marée basse » (clip de rap), 14/20 ; corrections dans `montage-direction-artistique`.
- **PLAN-TESTS-MCP** : tests 11 à 13 et observations du serveur Higgsfield (hôte `bs_*`, procédures « passport » et « audit », risque de crédits payants pour la génération). Le serveur n'a pas été appelé.
