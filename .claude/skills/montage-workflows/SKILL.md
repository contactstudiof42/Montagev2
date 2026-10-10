---
name: montage-workflows
description: Passer un montage d'un logiciel à l'autre et tenir le pipeline — formats d'échange (EDL, XML FCP7, FCPXML, AAF, OTIO), Dynamic Link, conformation, envoi à l'étalo et au mixage, VFX pulls avec poignées, codecs intermédiaires (ProRes, DNxHR), fabrication des proxies, rushes VFR de téléphone, interpolation et ralentis, pipeline type par format. Mots d'un monteur : « on envoie à l'étalo », « fais-moi un XML », « l'EDL ne tombe pas juste », « exporte l'AAF pour le mixeur », « il faut des poignées », « ça a perdu les effets », « le son du téléphone se décale ».
---

# Workflows transversaux et pipelines

Marqueurs : **[SOURCÉ]** lu dans une source datée · **[TESTÉ EN LABO]** fait technique mesuré (fichiers d'échange, ffmpeg, scripts ; les imports dans les logiciels restent à faire en phase 3) · **[ÉPROUVÉ EN MAQUETTE]** principe tiré d'une maquette Blender/Pillow/ffmpeg, hypothèse à confirmer sur de vraies images · **[THÉORIQUE]** doc ou pratique, jamais exécuté.

**Fait foi sur** : les échanges entre logiciels (ce qui passe et ce qui se perd), la conformation, les proxies (règles et fabrication), les rushes VFR, l'interpolation et les codecs intermédiaires. Procédures dans chaque logiciel : `montage-premiere`, `montage-resolve`, `montage-after-effects`, `montage-blender` ; specs de livraison et loudness : `montage-loudness-livraison`. Mesures détaillées : [details.md](details.md).

## 1. Pourquoi c'est un sujet artistique
Un pipeline n'est pas de la logistique : il décide **quand une décision devient irréversible**. Tant que le montage vit dans un seul
logiciel, tout reste discutable ; chaque passage (vers l'étalo, le mixage, les VFX) fige quelque chose. Le bon pipeline garde ouvertes
les décisions qui ne sont pas encore mûres (le rythme, la fin) et ferme vite celles qui le sont (le format, la cadence, l'espace couleur).
Règle : **verrouiller le montage image avant d'envoyer à l'étalonnage et au mixage**, et noter ce qui reste ouvert (plans VFX, titres).

## 2. Formats d'échange : lequel pour quoi
| Format | Transporte | Perd | Usage |
|---|---|---|---|
| **EDL CMX 3600** | coupes, fondus, 1 piste vidéo, noms de bobines (8 car.), commentaires | **la cadence** (absente du fichier), effets, vitesses complexes, pistes multiples, majuscules des marqueurs | conformation simple, étalonneur qui veut les points de coupe [TESTÉ EN LABO, `labo/workflows/`] |
| **XML FCP7 (xmeml)** | pistes, coupes, noms, marqueurs, certains effets de base, vitesses simples | effets propriétaires, titres, étalonnage | **le plus sûr pour Premiere ↔ Resolve** [fichier TESTÉ EN LABO ; import THÉORIQUE] |
| **FCPXML** | timeline Final Cut Pro, rôles | dépend du logiciel qui l'importe | FCP ↔ Resolve [THÉORIQUE] |
| **AAF** | montage + audio avec **poignées**, niveaux, pistes | effets vidéo | **envoi au mixeur** (Pro Tools, Fairlight) ; écriture par script testée [TESTÉ EN LABO, fichier seulement] |
| **OTIO** | tout ce que les autres portent, ouvert, scriptable | peu d'imports natifs | pivot de conversion par script (Python `opentimelineio`) [TESTÉ EN LABO] |

Pièges vérifiés : une EDL relue à la mauvaise cadence donne de faux timecodes (relue à 24 au lieu de 30 : échec net en script,
mais un logiciel peut l'accepter en silence). **Toujours mettre la cadence dans le nom du fichier** (`film_v6_30p.edl`).

## 3. Passages entre logiciels (règles d'usage) [THÉORIQUE sauf mention]
- **Premiere → After Effects** : Dynamic Link pour un plan qui bouge encore (le montage peut changer) ; **rendu intermédiaire** (ProRes 4444 avec alpha) dès que le plan est validé, car le Dynamic Link ralentit la timeline et casse quand on déplace les projets.
- **Premiere / montage → Resolve (étalonnage)** : XML + rushes originaux (pas les proxies !). Avant l'export : aplatir les nests, retirer les effets inutiles, mettre les plans sur le minimum de pistes, noter les recadrages et vitesses (souvent mal traduits). Alternative robuste : un **fichier « référence » du montage** (export plein cadre) à superposer dans Resolve pour vérifier la conformation plan à plan.
- **Montage → mixage** : AAF avec **poignées** (2 à 5 s), pistes rangées par famille (dialogues, ambiances, SFX, musique), + vidéo de référence avec timecode incrusté, + liste des intentions (où le silence, où la musique arrache).
  - **AAF par script** [TESTÉ EN LABO, 2026-10-10] : `labo/workflows/aaf_pistes.py` écrit avec `pyaaf2` 1.7.1 un AAF à 3 pistes nommées par famille (DIAL / MUS / SFX), essence WAV embarquée, blancs en `Filler` ; relu par pyaaf2 **et** par OpenTimelineIO (otio-aaf-adapter) : positions, débuts dans la source et durées identiques à l'image près (`labo/workflows/aaf_resultats.json`). Taille : ~3,3 Mo pour 30 s de mono 48 kHz (essence embarquée). Non vérifié : import réel dans Pro Tools / Fairlight (phase 3), poignées, niveaux et fondus (non écrits par ce script).
- **Plans VFX (pull)** : exporter les plans concernés en EXR ou DPX, dans l'espace couleur d'origine (log), **avec poignées de 8 à 16 images**, nommés par plan (`SH010_v001`), et une liste (EDL ou tableau) qui dit où ils retournent. Retour en EXR/ProRes 4444, même nom, version incrémentée.
- **Blender → compositing / montage** : séquence d'images (PNG pour l'atelier, EXR multicouche pour un vrai compositing), jamais une vidéo compressée en sortie de rendu (un plantage perd tout, une image ratée se re-rend seule). [ÉPROUVÉ EN MAQUETTE] (séquences PNG + montage ffmpeg, pièces 01-04)
- **Grille de musique → montage** : marqueurs générés hors logiciel en XML FCP7 (`labo/marqueurs/beats_xml.py`) [détection TESTÉ EN LABO].

## 4. Codecs intermédiaires et proxies (choix) [THÉORIQUE, specs à vérifier sur les pages Apple/Avid]
- **ProRes 422 HQ** : master de montage 10 bits ; **ProRes 4444 (XQ)** : alpha, VFX, titres ; **DNxHR HQX / 444** : équivalents Avid, plus faciles sous Windows.
- **Proxies** [TESTÉ EN LABO pour la fabrication ; rattachement dans les logiciels THÉORIQUE] : ProRes Proxy (`prores_ks -profile:v 0`) ou H.264 **tout-intra** (`-g 1`), jamais de long-GOP (lourd au scrub) ; **même nom, même durée, même cadence, même rapport d'image (1/2 ou 1/4 exact), mêmes pistes audio** (`-map 0:v -map 0:a` : par défaut ffmpeg n'en garde qu'une), timecode recopié ; vérifier chaque lot avec `labo/proxies/verif_proxy.py`. Le proxy sert au rythme, jamais à juger couleur ou netteté. Pourquoi c'est artistique : un montage qui saccade fait couper trop tôt.
- **Rushes de téléphone en cadence variable (VFR)** [TESTÉ EN LABO] : repérer avec `ffprobe` (`r_frame_rate` ≠ `avg_frame_rate`) ; lus à la cadence nominale, ils dérivent (−400 ms à 5 s, ≈ 1 s à 10 s). **Conformer une fois, à l'ingest, à la cadence du projet** (`-fps_mode cfr -r 25`, intermédiaire ProRes/DNxHR + PCM) : synchro exacte, au prix d'images doublées dans les passages sombres. Choix [THÉORIQUE] : saccade franche pour un document, fondu seulement pour une ambiance sans visage. Comportement de Premiere / Resolve face au VFR : phase 3.
- **Ralentis et interpolation** [TESTÉ EN LABO] : interpoler **plan par plan** (à travers une coupe, une image hybride des deux plans apparaît). Sur image lisse à grands mouvements, `minterpolate=mi_mode=mci` bat le fondu et RIFE 4.25 bat `mci` ; **sur texture fine et sur de vrais plans d'eau ou de feuillage à petit mouvement, le simple fondu égale `mci` et bat RIFE** (43,8 contre 41,6 dB). Ne pas généraliser un gain mesuré sur un type d'image. Quand l'interpolation casse, assumer la duplication (saccade) ou le fondu plutôt que livrer des artefacts ; tourner en haute cadence si le ralenti est prévu. Optical Flow, Speed Warp, Pixel Motion : THÉORIQUE.

## 5. Pipelines types par format
Chaque ligne : ce qui est verrouillé tôt (●) et ce qui reste ouvert longtemps (○).

| Format | Pipeline | Verrouillé tôt | Ouvert longtemps |
|---|---|---|---|
| **Pub 30 s / 15 s / 6 s** | ingest + proxies → montage Premiere (30 s d'abord, déclinaisons ensuite) → VFX / AE (packshot, titres) → étalo Resolve (XML) → mixage (AAF) → masters par diffuseur (PAD TV -23, web -14/-16) | ● durée, format, packshot, mentions légales | ○ ordre des plans du milieu, musique (droits !) |
| **Vertical réseaux** | souvent tout dans un logiciel (Premiere ou Resolve) ; sous-titres incrustés ; export par plateforme | ● 9:16, zones de sécurité, sous-titres | ○ le hook des 2 premières secondes (tester 2-3 versions) |
| **Clip** | montage sur la musique définitive (grille de marqueurs) → effets → étalo → export (la musique est déjà mixée : pas de mixage, mais vérifier la loudness du master) | ● la musique, la synchro labiale | ○ la structure (macro ou micro, cf. `montage-rythme`) |
| **Corporate** | dérush transcrit (Speech to Text) → montage papier (paper edit) → montage → titres AE → étalo léger → mixage voix → versions longue / capsules | ● le message validé par le client avant le montage fin | ○ les images d'illustration |
| **Documentaire** | dérush et transcription → séquences par thème → bout à bout long → structure → affinage → étalo, mixage, sous-titres, archives (droits) | ● rien avant la structure | ○ la structure elle-même, longtemps (Varda : la voix s'écrit après le montage) |
| **Fiction courte** | proxies et synchro du son → montage scène par scène → montage image verrouillé → conformation → VFX → étalo → mixage → DCP / master | ● le montage image avant l'étalo et le mixage | ○ les VFX, la musique originale |

## 6. Checklist d'envoi (à chaque passage)
1. Cadence, résolution, espace couleur notés dans le nom du fichier ou un fichier texte joint.
2. Vidéo de référence avec timecode incrusté.
3. Poignées (son : 2-5 s ; VFX : 8-16 images).
4. Relire l'échange dans un projet neuf **avant** de l'envoyer (aller-retour de contrôle) et comparer les coupes à la référence.
5. Ne jamais livrer depuis des proxies.

Voir aussi : `montage-premiere`, `montage-resolve`, `montage-after-effects`, `montage-blender`, `montage-loudness-livraison`, `montage-couleur-pipeline`.

## 7. Ce qui se perd dans l'aller-retour [TESTÉ EN LABO côté fichiers ; imports en phase 3 ; détail : [details.md](details.md)]
- **Un fichier d'échange transporte des coupes, pas des réglages.** Vitesses, arrêts sur image, inversions, recadrages et images clés : **perdus sans avertissement** dès que la timeline est reconstruite (XML FCP7 via OTIO : 7 réglages sur 7) ; l'EDL inverse la durée source des ralentis et ne garde aucun recadrage. **Nests relus vides**, stéréo éclatée G/D réduite à un canal.
- Règle : **aplatir avant l'envoi** (rendre ralentis, nests, recadrages) ou envoyer médias natifs + liste des vitesses et recadrages (`labo/workflows/recadrages/liste_recadrages.py`) + **vidéo de référence à TC incrusté** ; à l'arrivée, compter plans, pistes et canaux. Avant tout envoi d'EDL : `python3 labo/workflows/verif_edl.py film.edl 25`. Au mixeur : **AAF exporté directement par le logiciel de montage** ou stems, jamais d'EDL ni de XML retouché par un outil tiers.
- Pourquoi c'est artistique : un recadrage perdu, c'est un autre plan (le gros plan redevient plan moyen) ; un canal droit perdu, c'est une ambiance qui se rétrécit sans que personne ne l'entende avant le mixage.
