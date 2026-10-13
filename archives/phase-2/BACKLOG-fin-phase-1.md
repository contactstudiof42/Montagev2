# BACKLOG — trié à la fin de la phase 1

_Trié le 2026-10-10 (session de clôture n°1). Le backlog complet de la phase 1 (sujets faits, traces, réalimentations Y0-Y52 et 0-79) est archivé dans `archives/phase-1/BACKLOG-phase-1.md` ; les numéros entre parenthèses y renvoient. Plus aucun sujet de « maquette seule » : la phase 1 est close._

## Phase 2 — demande de voir de vraies images ou d'écouter un vrai son
### Vos références (priorité 1)
- **Ziak, Interstellar, Joker, EGO** : revoir les extraits avec le son ; confronter mes fiches (`culture/`) et les principes que j'en ai tirés (Y0, pièces 29, 31, 22).
- **Kinetic editing** : mesurer de vrais edits (densité de coupes, SFX par minute, calage au beat ou non) et juger à l'oreille (67, 68).
### Vérifier les principes `[ÉPROUVÉ EN MAQUETTE]` sur de vraies images
- Micro-sauts de jump cut et seuil de durée retirée sur un vrai rush face caméra (Y17, Y50, Y16).
- Cécité au changement, saillance, « la coupe va où le regard est déjà » : test spectateur des pièces 12 et 13 (33, 47, 50 ; PLAN-TESTS 44-45, 47).
- Le fond raccorde, fond = monde / lumière = corps, sur un vrai champ-contrechamp (47).
- Montage alterné à deux vitesses : tic libre contre tic sur les retours, sur un spectateur (Y39).
- Réaction tenue, bouton, timing comique sur de vraies scènes (Y28, Y30, Y48).
- Lecture d'un corps : posture selon l'axe, focale, mains qui parlent (Y41, 73, 76) — sur de vrais corps, plus sur un pantin.
- « Laisser chercher » (Haneke) : taille d'un détail à l'écran salle / téléphone (Y49) — sur un vrai plan large.
- Densité d'événements et relances sur de vraies vidéos YouTube (Y23, `labo/youtube/densite.py`).
- Shorts narratifs : cadre fixe contre coupes, la 1re seconde sans le son (Y43).
### Écouter
- Son et émotion : même image, trois bandes son (13) ; silences, ambiances, SFX jugés à l'oreille, pas sur forme d'onde.
- Le son d'un strobe, d'un claquement, d'une goutte : comparer mes designs synthétiques à de vrais sons (77, Y43).
### Vrais rushes techniques
- Un vrai rush log (LogC, S-Log3) : conversions et LUT du labo (2, 41).
- Un vrai rush VFR de téléphone (labo `vfr/`), de vrais plans pour l'interpolation et le keying (14, 49).
- Un rush à strobe réel (84 dans l'archive) ; photosensibilité sur de vrais exports (37).
- Plan sombre en mouvement téléversé en non répertorié : ce que la plateforme rend (PLAN-TESTS 52).
### Culture à revoir en images
- Fiches écrites de mémoire ou sans vidéo : Kolder, drill FR, Freeze Corleone, génériques de séries, Shorts narratifs (29, 38, 74).
- Culture YouTube encore de seconde main : regarder des extraits par genre (Y5).

## Phase 3 — demande les logiciels (plan détaillé : `PLAN-TESTS-MCP.md`)
- Lire l'état des hôtes et les skills d'entrée du serveur Higgsfield (`ae-clean-rig`, `blender-scene`) avant toute action.
- After Effects : coller les expressions du labo et comparer aux valeurs Node ; saccade choisie (PLAN-TESTS 61).
- Premiere : loudness et normalisation à l'export contre ffmpeg ; tags couleur ; détection de beats ; remonter une pièce depuis sa liste de plans ; écran de fin et chapitres (10, PLAN-TESTS 11-17, 63).
- Resolve : arbre de nodes de l'atelier 05, rendu en lot, Fusion et Fairlight par script, retime (8, 30).
- Échanges : importer les XML, EDL et AAF du labo (vitesses, recadrages, nests, stéréo) dans Premiere et Resolve ; vraies EDL exportées dans `coupes.py` et `verif_edl.py` (15, 27, 58, Y42 ; PLAN-TESTS 46, 48).
- Blender : buée animée par matériau et vrai modèle de voiture (pièce 34) ; refaire les pièces 01 et 02 via MCP ; Eevee contre Cycles sur GPU (PLAN-TESTS 36-37, 75).
- Proxies et rattachement dans les logiciels (PLAN-TESTS 40-42).
- Revérifier l'état public des ponts MCP (12 : information volatile).
- Garde-fou : aucune génération payante sans votre accord explicite.

## Abandonné (avec la raison)
- **Veille IA à chaque session (Y11)** : quotidienne, elle ne trouvait plus rien de neuf depuis quatre sessions. Remplacée par une veille ponctuelle avant un projet qui utilise l'IA, et après Adobe MAX (novembre 2026).
- **Nouvelles pièces de maquette** (pièce 02 v6 flamme, 03 v4, 04 sous-marin, 17 v6, 19 v9 rig à coude, 22 v4, 25 voix, 26 larges, 28 v4, 30 main, 34 v7-v8, écho de poses en mouvement Y19, Y16, Y52…) : la maquette a donné ce qu'elle pouvait ; la suite se juge sur de vraies images.
- **Ateliers jamais faits « Spirale » (25), « trois tempos » (6), « teaser 15 s » (51), « plan-séquence de marche » (72), réutiliser la table de la pièce 06 (31)** : à reprendre seulement sur un vrai projet, plus en maquette.
- **Examens réguliers** : 13 examens faits ; en phase 2, les vrais projets du studio remplacent les briefs fictifs.
- **Relectures de sources bloquées en 403** (TD1008, Ofcom, Creative Review, entretiens ASC) : à relire seulement si un projet en dépend.
- **Saillance par modèle appris (52)** : le spectateur réel de la phase 2 est une meilleure mesure.
- **OCR pour juger la lisibilité d'une miniature** : réfuté en labo (non monotone avec la taille).
- **Fusion des skills artistiques (19, 42)** : faite par l'audit de la session de clôture.
