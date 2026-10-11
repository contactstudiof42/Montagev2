# MISSION — PHASE 3 (LOCAL, SUPERVISÉE) : MONTER DE VRAIS PROJETS DANS RESOLVE

Tu tournes sur le Mac de Diego, dans une session **qu'il lance lui-même** et qu'il regarde. Jamais en routine. Si tu as un doute qui peut abîmer quelque chose (projet Resolve, fichier, rendu), demande-lui ; pour le reste, décide et note.

## Le but
En phase 1 tu as appris le métier sur des textes et des maquettes, en phase 2 tu as appris à regarder de vraies vidéos. Ici tu fais le travail : à partir de **rushes, son et brief**, livrer dans DaVinci Resolve (par le MCP) une version **presque finie**, que Diego n'aurait plus qu'à peaufiner.
La mesure : **le nombre et la gravité des retours** dont Diego aurait besoin pour livrer ta version, comparés à ceux d'un Claude sans formation qui monte le même projet.

## Ce qui est nouveau pour toi (ne fais pas semblant de savoir)
- Tu n'as jamais piloté Resolve : les skills `montage-resolve` et `montage-pilotage-mcp` sont [THÉORIQUE]. Tout geste validé passe en **[TESTÉ EN CONDITIONS RÉELLES] (date)**.
- Tu n'as jamais vu de rushes : choisir la prise, le moment dans la prise, ce qu'on jette, c'est le cœur du métier et c'est neuf.
- Tu n'as jamais traduit un brief en choix de montage.
- Tu n'entends pas le son : tout jugement sonore est mesuré, et ta note de livraison dit ce que Diego doit vérifier à l'oreille.

## Règles de sécurité (priment sur tout)
1. **Resolve** : ne crée que des projets dont le nom commence par `P3-`. N'ouvre, ne modifie, ne supprime aucun autre projet de la base de Diego. Enregistre le projet avant de finir.
2. **Médias** : les rushes et sons sont en lecture seule, qu'ils soient dans `videos/phase-3/<projet>/` ou dans un dossier source externe indiqué par `brief.md` (ex. `/Volumes/SSD FAST/SONY copy/`). Dans un dossier source externe, tu n'écris rien, nulle part (pas même dans son `EXPORT/`). Ne les déplace pas, ne les renomme pas, ne les réencode pas sur place. Copies légères et fichiers de travail : `videos/phase-3/<projet>/_travail/`. Rendus : `videos/phase-3/<projet>/rendus/`.
3. **Test à l'aveugle** : ne cherche jamais la version finale de Diego (ni sur le disque, ni dans `videos/projets-f42/`, ni ailleurs) avant qu'il la dépose lui-même dans `videos/phase-3/<projet>/final-diego/` à l'étape de comparaison. Si le projet test fait partie des projets déjà analysés en phase 2, dis-le à Diego dès le début : le test serait biaisé.
4. **Code arbitraire** : préfère les outils dédiés du MCP. `run_script_unsafe` seulement si aucun autre outil ne le permet, jamais pour supprimer un fichier ou toucher hors de `P3-*`, et chaque usage est noté dans le journal.
5. Rien de payant en plus, aucun compte créé, rien de publié (règles de `CLAUDE.md`). **Banques de sons et de musique** : tu peux chercher et télécharger toi-même des SFX (et des musiques si le brief le demande) sur Artlist, ou sur une autre banque que Diego indique, avec le compte de Diego déjà connecté dans Chrome (extension Claude in Chrome). Rien d'acheté, aucun abonnement modifié, pas plus de 100 SFX par jour (limite de la licence Artlist). Range chaque son dans `videos/phase-3/<projet>/sfx/` et note-le dans `sfx.md` (nom, banque, lien, usage prévu). Tu n'entends pas les sons : choisis sur le nom, les mots-clés et la forme d'onde, et signale dans la note de livraison ceux que Diego doit écouter.

## Étape 0 — Session 0 : apprendre l'outil (une seule fois)
1. Diagnostic : `get_resolve_status`, version, `get_whats_new` depuis ta date de connaissance, `get_scripting_docs` / `get_scripting_api` / `search_scripting_api`. Résume dans `labo/mcp/resolve-mcp.md` ce que le serveur sait faire et ce qu'il ne sait pas.
2. Bac à sable : projet `P3-BAC-A-SABLE`, avec 3 ou 4 courts extraits de `videos/clips/` copiés dans `videos/_travail/p3-bac-a-sable/` (jamais l'original). Teste, **un geste puis une image de contrôle** à chaque fois :
   importer des médias · créer une timeline (résolution, cadence) · poser des plans avec points d'entrée et de sortie à l'image près · couper, raccourcir, déplacer · poser une musique et régler un niveau · un fondu son · un texte · un nœud d'étalonnage simple et une LUT · rendre un H.264 · relire le rendu (ffprobe, `qc_livraison.sh`, planche).
   Puis les gestes qu'exige le premier projet (Sony, kinetic vertical) : timeline 1080x1920 à 25 i/s à partir de rushes UHD 16:9 à 50 i/s (recadrage et position par plan) · synchroniser un son externe (micro HF ou perche) avec le son caméra · un flash blanc d'une ou deux images · un changement de vitesse (ralenti, rampe) · un détourage (Magic Mask ou masque de Fusion) · un texte dans une police installée sur le Mac · un SFX posé à l'image près · un plan de fin fourni (fichier ProRes avec alpha) en surimpression. Enfin, le navigateur : `/chrome` (ou les outils Claude in Chrome) disponible dans la session, recherche d'un SFX sur Artlist, téléchargement d'un seul son, puis déplacement du fichier téléchargé vers le dossier `sfx/` du bac à sable. Pour chacun : faisable par le MCP, faisable seulement à la main, ou impossible.
3. Pour chaque geste : réussi, échoué ou contourné, avec l'appel exact. Résultats dans `PLAN-TESTS-MCP.md` (tests Resolve) et dans les skills `montage-resolve` et `montage-pilotage-mcp`, marqués [TESTÉ EN CONDITIONS RÉELLES] (date).
4. Fin de session 0 : la liste « ce que je peux faire seul / ce que je ne peux pas faire / ce que Diego devra faire à la main ». Commit, push.

## Étapes 1 à 5 — Monter un projet (`videos/phase-3/<projet>/`)
Le dossier contient `brief.md`, et soit `rushes/` et `son/`, soit les chemins d'un dossier source externe (lis-les dans `brief.md`). Tes fichiers texte vont dans le dépôt, dans `projets-phase-3/<projet>/` (commités), jamais les médias.

1. **Préparer** : relis `brief.md`, `GOUTS.md`, la synthèse de `RAPPORT.md`, `montage-formats`, `montage-regard`, et les skills du genre demandé. Si un élément du brief manque (durée, format, destination), choisis et note ton choix.
2. **Dérusher** → `derush.md` : inventaire (ffprobe, durées, cadences), copies légères, transcription de toute parole, planches. Pour chaque rush : ce qu'il contient, les bons moments avec timecodes, les prises à écarter et pourquoi (flou, jeu, son, raccord). C'est l'étape la plus importante : prends le temps.
3. **Plan de montage** → `plan.md` : intention en une phrase, durée et format, structure minutée (ouverture, développement, sommet, fin), musique et calage, références de ton corpus qui guident, critères mesurables de réussite (durée, loudness, lisibilité muette, premier écran net avant 2 s…). En mode test, tu n'attends pas de validation. Plus tard, sur un vrai projet, Diego validera ce plan avant le montage.
4. **Monter dans Resolve** : projet `P3-<projet>-agent`, timeline au format du brief. Un geste, une image de contrôle. Journal de chaque appel dans `journal.md`. Son : niveaux, fondus, ambiance continue sous la parole. Couleur : équilibre et raccord, look seulement si le brief ou les références le demandent. Textes et sous-titres si le format l'exige (lisibilité sur téléphone).
5. **Juger et corriger** : rends la V1 dans `rendus/`, puis regarde-la comme en phase 2 (planche, courbes, `qc_livraison.sh`, grille de `montage-regard`). Écris `autocritique.md` (ce qui ne va pas, par ordre de gravité), corrige, rends la V2. Deux ou trois versions au plus. Termine par `note-de-livraison.md` : ce que tu as fait, tes choix, ce que Diego doit vérifier (surtout à l'oreille), ce que tu n'as pas su faire dans Resolve.

## Étape 6 — Comparaison (quand Diego a déposé sa version et ses notes)
Diego dépose sa version dans `final-diego/` et note les versions dans `RETOURS-DIEGO.md`. Alors seulement :
- Compare ta version, celle de Claude nu (`rendus-nu/`) et celle de Diego : durée, structure, prises choisies, rythme, son, couleur, textes. Mesure ce qui se mesure.
- `comparaison.md` : ce que Diego a fait que tu n'as pas fait, et pourquoi c'était mieux ; ce que Claude nu a fait mieux que toi, s'il y en a ; l'apport réel de ta formation.
- Reverse les leçons dans les skills (avec la date) et dans « Leçons de phase 3 » ci-dessous. Un principe confirmé par la version de Diego passe en [TESTÉ EN CONDITIONS RÉELLES].
- Bilan court dans `RAPPORT.md`.

## Leçons de phase 3 (à enrichir à chaque projet)
- **Sony LinkBuds (2026-10-11, avant la comparaison avec Diego)** : lire rotation et gamma des rushes avant tout proxy ; dérusher en planches verticales de 8 vignettes par rush (25 min pour 252 rushes, 40 min de matière) ; le dérush trouve ce que le brief ne dit pas (les rushes donnent les oreilles et les bijoux, pas le geste de mettre l'écouteur ; un changement de lumière au rouge qui porte le sommet ; le décompte de la coach, un son sans besoin de sous-titre) ; la musique décide de la structure (un extrait continu de 60 s existait dans le morceau, avec un silence numérique avant le drop) ; rendre la V0 tôt, la mesurer (loudness, luminance par plan), corriger.

## Chaque session
1. Démarrage de `CLAUDE.md` (git pull, retours, boîte à références).
2. Reprends où `PROGRESS.md` s'est arrêté. 50 minutes au maximum ; enregistre le projet Resolve et le journal avant de finir.
3. Commit et push à chaque étape terminée (fichiers texte seulement, `git status` avant).
4. Fin : `PROGRESS.md` (où reprendre), synthèse de `RAPPORT.md`, commit, push.
