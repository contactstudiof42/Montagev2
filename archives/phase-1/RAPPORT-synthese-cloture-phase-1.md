# RAPPORT — synthèse à la fin de la phase 1

_Réécrit d'un seul tenant le 2026-10-10 (session de clôture n°1). L'historique complet (journal des 25 sessions, anciennes synthèses, anciennes questions) est dans `archives/phase-1/RAPPORT-journal.md`._

## Ce qu'a été la phase 1
25 sessions sans vraie vidéo ni logiciel piloté : 22 skills, 79 fiches de culture (`culture/`), 34 pièces d'atelier (`atelier/`, maquettes fabriquées avec Blender, Python et ffmpeg), une vingtaine de labos techniques (`labo/`) et 13 examens de direction artistique (`examens/`, notes de 13 à 15 sur 20, moyenne 14,4). Tout ce que je sais vient donc de **lectures**, de **mesures sur des fichiers fabriqués** et de **maquettes** que j'ai regardées image par image. Aucune vidéo réelle n'a été vue en mouvement avec le son, sauf le clip de Ziak que vous m'avez donné.

## Mon point de vue artistique
Je défends un travail **réduit à une idée**, où **le mouvement a une cause** et où chaque plan est relié au suivant par autre chose que le tempo. J'arbitre par l'émotion avant la continuité (Murch). Je cherche d'abord **l'image propre au sujet** (la marée qui découvre ce qui était caché, la buée qui ferme une voiture à mesure qu'on s'approche) avant d'appeler une référence. Je sais faire moins quand c'est plus juste : quand le corps, la voix ou la variation de vitesse du sujet portent le sens, le montage se retire.
Mes défauts connus, relevés par les examens : **recommander mon propre système** (« une seule chaleur méritée », « le même cadre qui revient »), **écarter une direction audacieuse sans l'avoir maquettée**, recommander des hybrides par prudence, et régler la forme sans écrire le contenu (aucun gag écrit dans un divertissement). Je les contrôle par des cases bloquantes dans `montage-direction-artistique`.

## Niveau par domaine
| Domaine | Niveau atteint | Confiance |
|---|---|---|
| Direction artistique (brief → directions) | méthode écrite, éprouvée par 13 examens | moyenne |
| Regard / autocritique | méthode + 28 règles, appliquées sur des dizaines de versions | moyenne à bonne |
| Rythme | principes + mesures + ateliers (montage alterné, densité, gags) | moyenne à bonne |
| Grammaire (raccords, axe, jump cut) | mesures dans Blender, maquettes | moyenne |
| Couleur et intention | principes + maquettes mesurées | moyenne |
| Couleur technique (log, LUT, ACES) | conversions testées en labo | moyenne à bonne |
| Son et émotion | principes, jugés sur forme d'onde : je n'ai jamais **écouté** | faible à moyenne |
| Loudness et livraison | recettes mesurées avec ffmpeg | bonne |
| Motion design | principes + maquettes Pillow ; rien dans After Effects | moyenne |
| Kinetic editing / YouTube / Shorts | skills sourcés + maquettes ; culture de seconde main | moyenne |
| Culture (cinéma, clip, pub, génériques, YouTube) | 79 fiches, presque toutes tirées de textes | moyenne |
| Blender | rendus en ligne de commande, simulations | bonne |
| After Effects, Premiere, Resolve | documentation et expressions testées hors logiciel | faible à moyenne |
| Échanges de fichiers (EDL, XML, AAF, OTIO) | testés côté fichiers ; imports dans les logiciels non vérifiés | moyenne |
| IA générative | état de l'art sourcé au 2026-10-10 ; seule l'interpolation (RIFE) testée | moyenne |
| Pilotage par MCP | méthode écrite ; aucun appel | nulle en pratique |

## Les 10 principes les plus solides de la phase 1
Chacun a été vérifié au moins sur une maquette ; tous restent **à confirmer sur de vraies images** (marqueur `[ÉPROUVÉ EN MAQUETTE]` dans les skills).
1. **Le rythme est la variation des durées, pas la vitesse.** Un montage calé au temps de bout en bout devient un papier peint ; la forme, c'est la densité de coupes par section, et un accent ne vaut que par sa rareté.
2. **On ne coupe pas dans la preuve.** Dans une chaîne causale ou un gag mécanique, on coupe dans les respirations ; couper sur le contact escamote ce qu'on veut montrer.
3. **Une coupe invisible n'existe que si le regard est déjà au bon endroit.** Une anomalie à travers une coupe passe inaperçue si le plan précédent n'a pas posé le regard là où elle apparaît (cécité au changement).
4. **Un détail se dimensionne à l'écran, pas dans la scène.** Une secousse « réaliste » de 0,6 pixel n'existe pas ; un changement d'échelle a besoin d'un témoin qui reste dans le cadre.
5. **Le fond est attribué au monde, la lumière au corps.** Un mur qui bleuit isole un personnage sans le refroidir ; c'est le fond qui raccorde, pas le sujet.
6. **L'œil lit l'énergie du cadre, pas le nombre de sources.** Éteindre trois lampadaires lointains ne se voit pas ; éteindre autour du personnage se voit toujours. Mesurer avant de corriger, et corriger à l'étage où le défaut naît (tournage, rendu ou étalonnage).
7. **La courbe d'une lumière qui change dit qui agit** : coupure sèche = la physique, fondu = un régisseur, clignement = la panne. Une coupure sèche a besoin d'une cause montée juste avant.
8. **Une attente doit être habitée.** Un temps vide ne dilate rien ; une main posée sur le combiné qui ne décroche pas, si. De loin, un silence a besoin d'un acte visible des personnages.
9. **Un jump cut minuscule est pire qu'un jump cut franc**, et le punch-in est une hiérarchie, pas un cache-coupe. Couper juste après que les yeux se rouvrent.
10. **Une direction écartée sans maquette n'a pas été jugée**, et une technique que je n'ai pas vue en mouvement ne se recommande pas. Deux fois, la direction écartée a donné la meilleure image.

## État des skills
22 skills dans `.claude/skills/`, sommaire dans `montage-expert`. Chaque principe porte un marqueur de statut : `[SOURCÉ]` (lu dans une source citée), `[TESTÉ EN LABO]` (fait technique mesuré), `[ÉPROUVÉ EN MAQUETTE]` (vu sur une maquette Blender, Pillow ou ffmpeg : hypothèse pour la phase 2), `[THÉORIQUE]` (déduit, jamais vérifié). La session de clôture a audité chaque skill (doublons, contradictions, concision, descriptions) : voir le détail plus bas.

## Priorités de la phase 2
1. **Regarder vos références pour de vrai** (Ziak, Interstellar, Joker, EGO, kinetic) et confronter mes fiches écrites de mémoire ou d'après des textes.
2. **Vérifier les 10 principes ci-dessus sur de vraies images**, en priorité ceux qui viennent seulement de maquettes (micro-sauts, cécité au changement, lumière et fond).
3. **Écouter** : le son est mon domaine le plus faible ; il faut des couples image + son réels.
4. **Apprendre de vos projets** : couples rushes + montage final, et vos commentaires sur ce qui marche.
5. Préparer la phase 3 : `PLAN-TESTS-MCP.md` (tests d'import, d'export et de mesure dans les logiciels).
La liste des vidéos à me fournir, les questions sur vos goûts et ma méthode d'analyse sont dans `PHASE-2-BESOINS.md`.

## Audit de la session de clôture (2026-10-10)
- **Tailles** : RAPPORT 616 → 70 lignes (168 → 10 Ko) ; PROGRESS 115 → 29 lignes ; BACKLOG 223 → 50 lignes ; les 22 SKILL.md 336 → 221 Ko (chacun entre 6 et 14 Ko, moins de 150 lignes). Le détail est parti dans des annexes (`details.md`, `regles-atelier.md`, `veilles-2026-10.md`…), qui gardent le texte d'origine : le total des skills avec annexes a donc grossi (419 → 489 Ko), mais seul le SKILL.md se charge à chaque fois.
- **Marqueurs** après audit (occurrences) : 227 `[SOURCÉ]`, 96 `[TESTÉ EN LABO]`, 168 `[ÉPROUVÉ EN MAQUETTE]`, 93 `[THÉORIQUE]`, 6 `[À TRANCHER EN PHASE 2]`. Plus aucun `[TESTÉ EN ATELIER]`. Plusieurs principes perceptifs passés de « labo » à « maquette » (cécité au changement, 180°, échos de mouvement, flou optique, punch-in, captions, miniatures, motion blur).
- **Erreurs ancrées corrigées** :
  - « l'horloge de la VM est peu fiable » (fausse, a écourté les sessions 16 à 23) : retirée de PROGRESS ; la règle « regarder `date -u` » la remplace ;
  - « finir vers 40 min à cause de l'anti-doublon » : retiré (consigne obsolète) ;
  - `montage-rythme` et `montage-grammaire` se disaient « non encore éprouvés » ; plusieurs skills se disaient « version 1 » après 20 enrichissements ; `montage-direction-artistique` annonçait `montage-references` « à venir » et « aucune bibliothèque par format » ;
  - « AgX blanchit le froid » (réfuté en session 8) réécrit en hypothèse réfutée ; « le grain protège le noir » remplacé par « le grain n'est pas une protection universelle » ;
  - Kolder « une transition kinetic se tourne » : seule la forme nuancée reste (un point commun aux deux plans, tourné ou trouvé) ;
  - « une relance est un pic » aligné sur « un coup qualitatif, pas une rafale » ; contradiction kinetic / youtube sur le punch-in tranchée (« changer d'échelle seulement là où l'on veut l'emphase ») ;
  - Resolve : recette `TimelineItem.SetLUT` (dépréciée) remplacée par le graphe de nodes ; « Magic Mask 2.0 / IntelliTrack en 21.1 » déclaré faux ; workflows : « proxy H.264 » contre « jamais de long-GOP » tranché en « H.264 tout-intra » ;
  - Premiere 26.5 et la sortie 8 bits de Generative Extend : marqués `[À TRANCHER EN PHASE 2]` (une seule source) ;
  - `PLAN-TESTS-MCP.md` s'appelait « phase 2 » : renommé phase 3.
- **Doublons fusionnés** : grammaire fait foi sur le raccord mouvement et les J/L-cut ; rythme sur le temps et la musique ; son-et-émotion sur le silence ; couleur-et-intention sur le sens, couleur-pipeline sur la technique ; formats sur les Shorts narratifs ; youtube sur le face caméra ; direction-artistique sur le test « mon propre système ». Tableau complet : sommaire de `montage-expert`.
- **Doutes non tranchés** : seuil de durée retirée pour un jump cut et seuil des micro-sauts (2 %) ; « un geste naturel suffit en plan taille » ; whoosh 3 à 6 images avant la coupe ; loudness corporate hors plateformes ; vraie version de Premiere ; scripting dans Resolve gratuit. Chevauchements restants, signalés mais acceptables : Resolve ↔ couleur-pipeline (RCM), loudness ↔ kinetic / youtube (specs d'envoi), workflows ↔ formats (pipelines).

## Session de clôture n°2 (2026-10-10)
- **Annexes des skills** : doublons retirés (268 → 202 Ko d'annexes ; SKILL.md inchangés à 220 Ko). Corrections de la clôture n°1 propagées dans les annexes (AgX, grain, recette Resolve, Magic Mask, proxies tout-intra, punch-in, relance, Kolder) ; chaque annexe dit que son SKILL.md fait foi.
- **Erreur ancrée trouvée au sondage** : 36 renvois « à vérifier en phase 2 » visaient des tests dans les logiciels (Resolve, After Effects, Premiere, Blender sur GPU, imports d'échange) : passés en « phase 3 ». « Phase 2 » ne désigne plus que les vraies vidéos.
- **19 fiches de culture écrites en partie de mémoire** vérifiées sur le web (158 → 190 Ko, sources datées ajoutées ; 102 mentions `[NON VÉRIFIÉ]` dans `culture/`). Corrections notables : Cog ≈ 100 prises (pas 606) ; *In the Blink of an Eye* paru en 1992 ; ouverture de *The Social Network* ≈ 7 min ; ralentis de *Raging Bull* à 48/72/96/120 i/s et silence avant un coup dans le combat contre Dauthuille (pas Robinson) ; Kurzgesagt : deux événements distincts (oct. 2025, juil. 2026) qui étaient fusionnés. Aucun principe invalidé ; deux exemples à remplacer (Schoonmaker, logo de *Scott Pilgrim*) et un principe McLaren sans source tant qu'un chapitre en 403 n'est pas relu.
