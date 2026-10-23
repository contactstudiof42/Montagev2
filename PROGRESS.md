# PROGRESS — état actuel

_Lire en premier. Seul l'état présent compte ici. Historique : `archives/` (clôture de la phase 1, sessions 1 à 25, phase 2, état d'avant l'audit 2 dans `archives/audit-2/racine/PROGRESS.md`). Chaîne d'analyse d'une vraie vidéo et leçons de méthode : `.claude/skills/montage-nouvelle-reference/methode-analyse.md` ; outils installés et contrôles : `labo/OUTILS.md` ; inventaire du corpus : `REFERENCES.md`._

## OÙ REPRENDRE (2026-10-13, après l'audit 2)
- **Audit 2 appliqué** (`AUDIT-2.md`, décisions de Diego en tête) : `CLAUDE.md` commence par la carte des sens et la hiérarchie du goût ; une seule liste de contrôle avant rendu (`montage-regard`) ; skills réduits aux règles gagnées par une erreur ou portant un mot de Diego, le savoir et les recettes en annexe ; `montage-expert` archivé ; `montage-couleur` remplace les deux skills de couleur ; plus aucun nom de client ou de personne filmée dans les skills. État d'avant : tag `avant-audit-2` et copie intégrale dans `archives/audit-2/`.
- **Nouveau principe de Diego** (2026-10-13, `CLAUDE.md`) : ne pas se brider faute d'outil ; la liste des moyens au début de chaque session, Diego valide, j'installe (achat, compte et autorisation de macOS : Diego).
- **E0 fait le 2026-10-13** (résultat : `PLAN-TESTS.md` 6.8, table 6.7) : Blender marche par les trois voies (MCP ouvert, ligne de commande, MCP en arrière-plan grâce au lanceur `/opt/homebrew/bin/blender`), rendus identiques ; After Effects marche par `osascript` + ExtendScript + `aerender` (contourné : pas de modèle PNG, rendu TIFF converti ; pièges notés : Inter remplacée en silence par Helvetica, capitales héritées du panneau Caractère) ; Resolve répond. **Le MCP de Higgsfield n'est pas branché** : la table 6.7 est remplie d'après le code du plugin seulement. **Prochaine étape : E1, dans une nouvelle session**, après que Diego a branché le connecteur Higgsfield (et, s'il veut, créé le modèle PNG d'AE) : d'abord vérifier les outils Higgsfield un par un (6.7, colonne « réellement fait »), écrire `labo/outils/courbe_mouvement.py`, puis l'exercice. Règles de Diego pour Higgsfield inchangées : aucun crédit de génération sans lui demander (coût estimé), aucun fichier de client envoyé, que de la matière créée pour l'occasion ; références Swile POW A et A, restées sur le Mac.

- **Veille IA du 2026-10-23** (demande de Diego : quel workflow pour un court métrage IA de 30 s « cyberpunk atmosphérique ») : annexe § 6 de `montage-ia-generative` (Kling 4.0 sorti le 15/10, Seedance 2.5 brouillon puis finalisation, Genjutsu, Oxen). Moyens constatés : Higgsfield 0 crédit (plan gratuit) ; Oxen 46 $ ; profil Chrome « robot » de Diego pour Instagram (connecté). **Projet lancé le 2026-10-23** : `projets-phase-3/cm-cyberpunk/plan.md` (sans Higgsfield, 25 $ d'Oxen ; Blender → GPT → Seedance 2.5) ; médias dans `/Volumes/SSD FAST/CM TEST /`. Méthode éprouvée par Diego le 05/10 dans `/Users/diego/Claude Work/studiof42-rise/`.

- **Livre *Story* de Robert McKee lu en entier le 2026-10-23** (PDF fourni par Diego) : ressource consultable `culture/livres/mckee-story/` (README : « Je cherche… », sommaire, glossaire ; une fiche par chapitre, avec les pages) et nouveau skill `montage-ecriture-scenario` (aucune règle gagnée encore ; savoir transposé aux formats du studio, [THÉORIQUE]). Texte OCR et PDF hors Git dans `videos/livres/mckee-story/`. Prochaine étape possible : un premier script réel pour éprouver le skill ; d'autres sources (écriture publicitaire, documentaire) à demander à Diego.

## Projets de la phase 3
- **Projet 1, film de marque kinetic (Sony LinkBuds)** : V5 livrable à 80-85 %, clos le 2026-10-12. Leçons [projet] : `projets-phase-3/sony-linkbuds/lecons.md`, `retours-V5.md`.
- **Projet 2, film de mariage (mariage-jo)** : V3b 10 %, V4 25 % (« le DA, c'est pas mal, il y a du mieux » ; « le mariage, c'est trop d'émotion pour un robot »), clos le 2026-10-13. Rendu V4 : `videos/phase-3/mariage-jo/rendus/mariage_jo_V4.mp4`, timeline `MARIAGE_JO_V4` du projet Resolve `P3-mariage-jo-agent`. Leçons classées par portée : `projets-phase-3/mariage-jo/lecons.md`.
- Accords de Diego encore valables : `PROMPT-PHASE-3.md`. Pièges de Resolve : `montage-resolve` (SKILL.md et `recettes.md`).

## Règles de session encore valables
- Relever `date` au début de la session et le relire avant de clôturer : estimée « au ressenti », la durée écoulée est surévaluée d'un facteur 3 à 8.
- Jamais d'identifiant personnel (adresse e-mail…) dans un en-tête de requête.
- Un serveur MCP de génération (comme `HIGGSFIELD_MCP`) peut consommer des crédits payants : ne rien générer sans accord explicite.
- `pkill -f motif` tue le shell appelant : tuer par PID. Les calculs longs se lancent avec `run_in_background`, pas avec `&`.
- ffmpeg Homebrew sans `drawtext` (pas de texte sur les tuiles) : annoter avec Pillow. L'option `framelog=verbose` d'ebur128 ne sort rien sans `-v verbose` : utiliser `ebur128` simple.
- ffmpeg en `yuv*` = plage limitée (noir = 16). PIL lit un PNG 16 bits en 8 bits.
- Ne jamais modifier un script zsh pendant qu'une exécution le lit (zsh lit au fil de l'eau). Sortie `ffprobe -of csv=p=0` : peut finir par une virgule ; préférer `-of default=nw=1:nk=1`.
- zsh : `====` en début de mot déclenche une erreur (« = not found ») ; écrire des séparateurs entre guillemets. zsh ne découpe pas une commande rangée dans une variable : passer par une fonction shell.
- Un `cd` dans une commande déplace le répertoire de travail des commandes suivantes : préférer les chemins absolus, ou `git -C`.
- Le Python système (3.15 rc) est trop récent pour librosa : lancer les scripts avec `.venv/bin/python -I` ; WhisperX dans `.venv-whisperx`.
