# PROGRESS — état d'avancement

_Lire en premier. Mis à jour à chaque fin de session._

## Où on en est (après la session 6, 2026-10-10 ~04:05 UTC)
- **Skills (21)** : enrichis en session 6 : `montage-son-et-emotion` (hors champ, Chion, règles pour les arrières), `montage-loudness-livraison` (§5 bis livraison 5.1, RT 040, pièges ffmpeg), `montage-references` (Aftersun, Les Revenants), `montage-blender` (corps rigides, Eevee sans écran), `montage-regard` et `montage-rythme` (leçons de l'atelier 07).
- **Culture** : 32 fiches. Nouveau en session 6 : *Aftersun* (Wells / McClendon), *Les Revenants* (Gobert), clips de rap français (PNL, Kekra, Ziak).
- **Atelier** : 01 à 06 inchangés ; **07 « Causalité »** (chaîne bille → 9 dominos → tasse, simulée en corps rigides ; montages A plan unique / B coupe sur les contacts / C coupe dans les respirations ; v2 ratée (tasse debout), v3 = référence ; son tiré de la simulation). Scripts : `scene.py` (modes sim / render / still, caméras large, livre, dominos, tasse, chaine, sol), `contacts.py`, `son.py`, `montage.py`, `edl-*.json`.
- **Sources** : + `surround-hors-champ-2026-10.md` (ITU BS.775 / BS.1770, RT 040, France TV 2023, Chion ; 8 commandes ffmpeg testées).
- **Examens** : n°1 (13/20), n°2 (14/20), n°3 (15/20), n°4 (14/20). **N°5 en session 8.**

## Reprendre ici (session 7)
1. Démarrage normal. Blender : `curl -sSL -o blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf blender.tar.xz` dans le scratchpad (30 s). `python3 -m pip install -q numpy pillow` (numpy n'est plus préinstallé pour ce Python en session 6).
2. Pièges : **ne jamais lancer `pkill -f motif` quand le motif apparaît dans la commande du shell lui-même** (tue le shell, code 144) : couper le motif (`"f_liv""re"`) ou passer par un script. `transform_apply` sans arguments applique aussi la position (voir `montage-blender`). Vérifier le cadre de chaque caméra par une image fixe **à l'image du contact** avant le rendu (session 6 : caméra sous le plan de la table = contact caché). 6 rendus Cycles pour 4 cœurs : ~8-10 s/image chacun ; préférer 4 à la fois.
3. Atelier 07 : v3 = référence (`params-v3.json`, `edl-C3.json`) ; v4 proposée dans `CRITIQUE.md`. Les rendus ne sont pas conservés : relancer `scene.py` par caméra avec `rendu=[a,b]` (≈ 3 s/image, 4 processus à la fois).
4. Puis BACKLOG : 32 « souvenir » (Aftersun), 33 « inquiétude calme » (Revenants), 34 surround sur un vrai mix, pièce 04 (sous-marin, 9:16), « Spirale ».
5. Sous-agents de recherche en parallèle (4 en session 6, fiables) ; relire leurs fiches et revérifier un chiffre clé en labo avant de les verser (fait pour le -4,5 LU du surround).

## Environnement constaté
- ffmpeg 6.1.1, Python 3, Node 22 préinstallés (numpy à installer en session 6). `apt-get update` puis `apt-get install libegl1` possible (10 s). Blender 4.2.3 LTS : téléchargement + décompression 30 s.
- Rendu Cycles CPU 640×360, 4 échantillons, scène texte + plan : ~1 image/s (250 images ≈ 3,5-4 min) quand d'autres tâches tournent.
- Un serveur MCP nommé `HIGGSFIELD_MCP` est listé dans l'environnement : non appelé (consigne phase 1). Noms observés dans `PLAN-TESTS-MCP.md`.

## Historique
- Session 6 — 2026-10-10 03:29 → ~04:05 UTC : fiches Aftersun et Les Revenants, recherche surround et hors champ (vérifiée en labo), atelier 07 « Causalité » (corps rigides, A/B/C), Eevee sans écran mesuré, PLAN-TESTS 36-37.
- Session 5 — 2026-10-10 02:29 → 03:05 UTC : atelier 05 « Trois étalonnages » (6 versions + scintillement), atelier 06 « Versions » (v1-v3), examen n°4 (14/20), API Resolve 19-21.1, fiches Elastic, ManvsMachine, Buck, Åkerlund, Gavras, état public des MCP (tests 21-32), AAF par familles.
- Session 4 — 2026-10-10 01:30 → 02:10 UTC : loudness hors plateformes, atelier 04 (v1-v4/v5), fondus 3/4, marqueurs XML, `montage-workflows` + OTIO, fiches Marker, Morris, Burtt, Rydstrom, vérification IA.
- Session 3 — 2026-10-10 00:30 → ~00:50 UTC : `montage-pilotage-mcp`, atelier 03 « rythme macro » (3 versions), labo fondus (résultat négatif), `montage-premiere`, fiches Varda et Jonze, examen n°3 (15/20), `montage-formats`.
- Session 2 — 2026-10-09 23:52 → 2026-10-10 00:30 UTC : pièce 02 « Étincelle » (6 versions), labo encodage, `montage-blender`, `montage-resolve`, fiches Murai et Honda « Cog », examen n°2 (14/20).
- Session 1 — 2026-10-09 22:48 → ~23:25 UTC : démarrage, structure, 13 skills, 14 fiches, atelier 01 (6 versions), 5 labos, examen n°1.
