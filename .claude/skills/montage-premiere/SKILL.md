---
name: montage-premiere
description: Adobe Premiere (ex-Premiere Pro, renommé « Premiere » en version 26, janvier 2026) — organiser un projet (Productions, bins, auto-save), proxies et ingest, multicam, monter sur la musique (marqueurs, Remix), sous-titres (Speech to Text, SRT, incrustés, légendes animées), Lumetri et gestion des couleurs (Direct Rec.709, Wide Gamut, tone mapping, log), Generative Extend, Media Intelligence, export (Media Encoder, H.264 adaptatif, normalisation loudness), raccourcis de trim (ripple, roll, slip, slide), scripting ExtendScript / UXP. Mots d'un monteur : « ça rame, fais des proxies », « synchro multicam », « recaler sur la musique », « sous-titres pour les réseaux », « l'image est délavée dans Premiere », « exporte pour Insta », « il me manque deux secondes de plan ».
---

# Premiere — le logiciel de montage au quotidien

Statut : **[THÉORIQUE]**, recherche du 2026-10-10 (pages d'aide Adobe lues par extraits, sources dans `sources/premiere-2026.md`). Rien n'est exécuté : Premiere n'est pas installable dans la VM. Les points marqués `[INCERTAIN]` sont à vérifier en phase 2 (`PLAN-TESTS-MCP.md`, test 14 et suivants).

## Quand Premiere, et pourquoi (le regard d'abord)
- **Premiere pour monter** : c'est l'outil du récit (structure, rythme, dialogue, musique). On y décide l'ordre et la durée des plans, pas le look final.
- **Pas Premiere pour finir l'image** quand l'enjeu couleur est fort (pub, clip, fiction) : étalonnage dans Resolve (`montage-resolve`). Lumetri suffit pour du corporate, du social, une normalisation de rushes.
- **After Effects pour l'animation qui compte** (`montage-after-effects`) ; Premiere pour un titre simple ou un MOGRT.
- Règle de DA : on ne cherche pas l'effet dans Premiere avant que le montage « off-line » tienne en plans nus. Un montage qui ne marche pas sans effets ne marchera pas avec.

## Version et nouveautés (datées)
- **Version 26.0 (janvier 2026)** : le logiciel s'appelle « Adobe Premiere » (le « Pro » disparaît) ; numérotation alignée sur l'année. 25.x = dernière branche « Premiere Pro ». [SOURCÉ]
- 26.0 : masquage d'objets par IA avec suivi en un clic, masques repensés. 26.2 (avril 2026) : effets et transitions Film Impact intégrés, Content Credentials à l'export. 26.3 (juin 2026) : **légendes animées mot à mot** (style réseaux). **26.5 (sept. 2026)** : Generative Media Tool (vidéo et SFX générés depuis un texte, dans la timeline), **Paper Edit** (monter depuis le texte de la transcription). [SOURCÉ, dates à confirmer]
- Depuis 25.2 (avril 2025) : Generative Extend, Media Intelligence (recherche en langage naturel, en anglais), traduction des sous-titres, nouvelle gestion des couleurs. [SOURCÉ]
- **Color mode** (espace d'étalonnage 32 bits flottants, distinct de Lumetri) : bêta publique NAB 2026, sortie stable non confirmée ; ne pas mélanger avec Lumetri sur un même clip. [INCERTAIN]

## Organisation de projet
- Arborescence disque fixe avant d'importer : `01_RUSHES / 02_SON / 03_GRAPHISMES / 04_MUSIQUE / 05_EXPORTS / 06_PROJET`. Ne jamais déplacer un média après import (médias hors ligne).
- Bins miroirs de cette arborescence + bin `SEQUENCES` avec versions datées (`PUB30_v03_2026-10-10`). Une séquence = une version : on duplique avant chaque grosse modification.
- **Productions** pour les gros projets (bobines, épisodes) : sous-projets liés, médias partagés sans doublon ; tout faire depuis le panneau Production, rien d'autre dans son dossier ; stockage partagé en SMB, même nom de volume partout, cache local, pas de Dropbox/Drive, verrouillage de projet activé. [SOURCÉ]
- Auto-save par défaut : 5 min, 20 versions. [SOURCÉ] → descendre à 3 min sur un projet client ; garder une copie hors du disque de travail.

## Proxies (quand ça rame)
- Ingest à l'import (Media Browser, case Ingest : Copy / Transcode / Create Proxies / Copy and Create Proxies) ou après coup : clic droit > Proxy > Create Proxies ; encodage par Media Encoder. Bascule par le bouton **Toggle Proxies** (à ajouter au moniteur). **L'export utilise toujours la pleine résolution.** [SOURCÉ]
- Format : ProRes Proxy (ou un intra-image léger) ; **jamais de H.264 Long GOP en proxy** (lourd à décoder en lecture arrière et au scrub). [SOURCÉ, guide Frame.io]
- Le proxy doit garder **le même ratio, la même cadence et les mêmes canaux audio** que l'original, sinon la bascule casse.

## Multicam
- Sélection des clips > Clip > Create Multi-Camera Source Sequence ; synchro par timecode, audio ou points d'entrée. Puis New Sequence from Clip, vue Multi-Camera dans le moniteur Programme, coupe en direct aux touches numériques, retouche à l'outil Roll (N). [SOURCÉ]
- Régler les canaux audio (mono) avant la synchro. [SOURCÉ, tiers]
- Regard : le multicam rend la coupe facile, donc paresseuse. Un premier passage en direct donne l'énergie, un second passage plan par plan donne le sens (qui écoute, qui réagit : cf. `montage-grammaire`).

## Monter sur la musique
- Marqueurs (M) posés pendant la lecture sur les temps forts et **sur l'arrangement** (entrée de basse, break, refrain) : cf. `montage-rythme`, le calage au temps est la texture, la densité par section est la forme.
- **Pas de détection de beats native sur desktop** selon les sources (elle existe sur Premiere mobile) [INCERTAIN] : alternative fiable, mesurer les temps hors Premiere (onset/BPM en Python) et importer les marqueurs.
- **Remix** (Essential Sound ou outil du groupe Ripple) : rallonge ou raccourcit une musique à une durée cible en recousant ses segments ; précision ~1 s (jusqu'à 5). [SOURCÉ] Écouter chaque raccord : le Remix ignore le sens des paroles.
- Poser les coupes sur l'image la plus proche du marqueur, jamais en tapant des durées (dérive mesurée dans l'atelier 03).

## Sous-titres
- Transcription (Speech to Text) > Create Captions (preset « Subtitle Default »). Export : fichier séparé (SRT) ou **incrusté** (Burn Captions Into Video, non désactivable). [SOURCÉ]
- Réseaux : incrustés (lecture sans son), 1 à 3 mots par carton pour un format kinetic, 2 lignes max sinon ; zone sûre verticale (ni en bas, ni à droite sous les boutons). Légendes animées mot à mot natives depuis 26.3. Broadcast / plateformes : SRT séparé.
- Traduction des sous-titres par modèles tiers : relire, surtout les noms propres et l'humour.

## Couleur dans Premiere
- Presets de séquence : **Direct Rec.709 (SDR, défaut)** — le log et la gamme large sont « tone mappés » à l'entrée ; Direct HLG / PQ ; **Wide Gamut** (Tone Mapped / Minimal / No Tone Mapping) ; ou gestion désactivée. [SOURCÉ]
- **Ne jamais changer l'espace de travail une fois l'étalonnage commencé** ; l'espace de sortie peut changer. [SOURCÉ]
- Log détecté automatiquement seulement pour certaines caméras : sinon assigner l'espace du clip à la main (sinon image délavée). Diagnostic « délavé / trop contrasté » : cf. `montage-couleur-pipeline`.
- Tags couleur écrits dans le fichier exporté : [INCERTAIN] → toujours vérifier avec `ffprobe` (color_primaries, transfer, matrix).

## Generative Extend et IA (2026-10)
- Rallonger un plan de quelques secondes (respiration avant une coupe, fin de plan trop courte) : sources 360p à 4K, 12 à 60 i/s ; **sortie 8 bits SDR, 30 i/s max**, passage par le cloud, consomme des crédits. [SOURCÉ] → acceptable pour du social ; **à éviter sur un master 10 bits / HDR / 24p cinéma** (rupture de qualité visible à l'étalonnage). Toujours dire au client quel plan est généré (cf. `montage-ia-generative`).
- Media Intelligence : chercher un plan par description (en anglais), « Search Similar Frames ». Utile pour dérusher un documentaire.

## Export
- Réseaux : H.264 « Match Source – Adaptive High Bitrate » recommandé par Adobe. [SOURCÉ] Les specs précises et la vérification : `montage-loudness-livraison` (yuv420p, faststart, AAC 48 kHz, BT.709, -14 LUFS pour le web).
- **Loudness Normalization** à l'export (onglet Effects) : ATSC A/85, EBU R128, ITU BS.1770 (cible réglable), limiteur true peak. [SOURCÉ, page ancienne] Mon labo a montré qu'une normalisation peut comprimer : mesurer l'export avec `ebur128` (test 8 du plan MCP).
- Master : ProRes 422 HQ (ou DNxHR HQX 10 bits) en pleine qualité, puis dérivés.

## Raccourcis de trim (défauts)
Ripple B · Roll N · Slide U · Slip Y · Ripple Delete Maj+Suppr. [SOURCÉ] J/K/L, I/O, C (cutter), Cmd/Ctrl+K (Add Edit), Q/W (ripple trim vers la tête de lecture), M, F (match frame) : défauts usuels [INCERTAIN, à vérifier].
Le trim est l'endroit où le montage se joue à l'image près : roll pour déplacer une coupe sans changer la durée, slip pour changer le moment du plan sans toucher au rythme.

## Scripting et automatisation
- **UXP** sorti de bêta dans 25.6 (décembre 2025), proche de la parité avec ExtendScript/CEP ; ExtendScript annoncé jusqu'à septembre 2026, statut actuel [INCERTAIN]. Pour un agent : préférer UXP ou un MCP (`montage-pilotage-mcp`) ; ne rien écrire en ExtendScript neuf.

## Pièges
- Séquence créée « à la main » aux mauvais réglages : toujours créer la séquence depuis un clip représentatif, puis vérifier cadence et ratio.
- Proxy à cadence différente → désynchronisation. Média déplacé → hors ligne.
- Effets empilés sur 200 clips : passer par un calque d'effets (adjustment layer).
- Export « Match Source » d'une séquence 25p vers une plateforme 30p : laisser à 25 (jamais de conversion de cadence à l'export sans raison).
