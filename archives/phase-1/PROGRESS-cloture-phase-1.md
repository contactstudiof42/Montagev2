# PROGRESS — état actuel

_Lire en premier. Ne garde que l'état présent ; l'historique des sessions 1 à 25 et les anciens « reprendre ici » sont dans `archives/phase-1/PROGRESS-historique.md`._

## État (2026-10-10, après la session de clôture n°1)
- **Phase 1 terminée** (apprentissage sans vraie vidéo ni logiciel piloté). Synthèse : `RAPPORT.md`. Backlog trié phase 2 / phase 3 / abandonné : `BACKLOG.md`.
- **Phase 2 à venir** : analyse de vraies vidéos. Ce que j'attends de l'utilisateur : `PHASE-2-BESOINS.md`.
- **Phase 3** : pilotage des logiciels par MCP, plan dans `PLAN-TESTS-MCP.md`.
- Consigne durable : culture YouTube / internet au niveau du cinéma et du clip (voir `montage-youtube`).

## Règles de session encore valables
- Relever `date -u` au début et le relire avant de clôturer : **l'horloge de la machine est juste** (vérifié par l'utilisateur, session 23). Mon estimation du temps « au ressenti » surestime la durée d'un facteur 3 à 8 : ne jamais clôturer sans regarder l'heure.
- Jamais d'identifiant personnel (adresse e-mail…) dans un en-tête de requête.
- Le serveur `HIGGSFIELD_MCP` est présent ; ses outils de génération peuvent consommer des crédits payants : rien générer sans accord explicite.

## Installation (temps mesurés)
- `python3 -m pip install -q numpy pillow` (~10 s) ; + `scipy opentimelineio otio-fcp-adapter` si besoin (~20 s).
- `apt-get install -y espeak-ng tesseract-ocr tesseract-ocr-fra` (~15 s).
- Blender 4.2.3 : `curl -sSL -o /tmp/blender.tar.xz https://download.blender.org/release/Blender4.2/blender-4.2.3-linux-x64.tar.xz && tar xf /tmp/blender.tar.xz -C /tmp` (~30 s). Cycles CPU 480×270, 32 échantillons : ~9 s par image.
- Préinstallés : ffmpeg 6.1.1, Python 3, Node 22, Chromium (Playwright).

## Pièges d'environnement encore vrais
- `pkill -f motif` tue le shell appelant, et `pgrep -f motif` dans une boucle se trouve lui-même : tuer et attendre par PID.
- Une commande lancée avec `&` survit à la fin de l'appel Bash : utiliser `run_in_background`.
- tesseract multi-fils bloque : `OMP_THREAD_LIMIT=1`. L'OCR ne mesure pas la lisibilité d'une miniature : juger à l'œil.
- ffmpeg en `yuv*` = plage limitée (noir = 16). PIL lit un PNG 16 bits en 8 bits.
- **YouTube est illisible depuis la VM** (IP de datacenter : « confirmez que vous n'êtes pas un robot »), même dans Chromium. Ne pas contourner avec des cookies de compte. Les vidéos arrivent par lien de fichier (Dropbox, Drive, WeTransfer) ou en phase 2 sur le Mac.
- helpx.adobe.com renvoie 403 au WebFetch ; les pages Google passent.
- Eevee sans écran est plus lent que Cycles dans la VM.
