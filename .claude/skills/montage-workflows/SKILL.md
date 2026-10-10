---
name: montage-workflows
description: Workflows transversaux et pipelines de post-production — passer un montage d'un logiciel à l'autre (Premiere, After Effects, Resolve, Blender, Fairlight / Pro Tools), formats d'échange (EDL CMX 3600, XML FCP7, FCPXML, AAF, OpenTimelineIO), Dynamic Link, conformation, envoi à l'étalonnage et au mixage, VFX pulls (EXR/DPX avec poignées), codecs intermédiaires (ProRes, DNxHR), proxies, et pipeline type de bout en bout par format (pub, vertical réseaux, clip, corporate, documentaire, fiction). Mots d'un monteur : « on envoie à l'étalo », « fais-moi un XML », « l'EDL ne tombe pas juste », « exporte l'AAF pour le mixeur », « il faut des poignées », « on conforme sur les rushes », « je passe le plan en AE », « round-trip Resolve », « ça a perdu les effets ».
---

# Workflows transversaux et pipelines

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
  - **AAF par script** [TESTÉ EN LABO, 2026-10-10] : `labo/workflows/aaf_pistes.py` écrit avec `pyaaf2` 1.7.1 un AAF à 3 pistes nommées par famille (DIAL / MUS / SFX), essence WAV embarquée, blancs en `Filler` ; relu par pyaaf2 **et** par OpenTimelineIO (otio-aaf-adapter) : positions, débuts dans la source et durées identiques à l'image près (`labo/workflows/aaf_resultats.json`). Taille : ~3,3 Mo pour 30 s de mono 48 kHz (essence embarquée). Non vérifié : import réel dans Pro Tools / Fairlight (phase 2), poignées, niveaux et fondus (non écrits par ce script).
- **Plans VFX (pull)** : exporter les plans concernés en EXR ou DPX, dans l'espace couleur d'origine (log), **avec poignées de 8 à 16 images**, nommés par plan (`SH010_v001`), et une liste (EDL ou tableau) qui dit où ils retournent. Retour en EXR/ProRes 4444, même nom, version incrémentée.
- **Blender → compositing / montage** : séquence d'images (PNG pour l'atelier, EXR multicouche pour un vrai compositing), jamais une vidéo compressée en sortie de rendu (un plantage perd tout, une image ratée se re-rend seule). [TESTÉ en atelier : séquences PNG + montage ffmpeg, pièces 01-04]
- **Grille de musique → montage** : marqueurs générés hors logiciel en XML FCP7 (`labo/marqueurs/beats_xml.py`) [détection TESTÉE EN LABO].

## 4. Codecs intermédiaires et proxies (choix) [THÉORIQUE, specs à vérifier sur les pages Apple/Avid]
- **ProRes 422 HQ** : master de montage 10 bits ; **ProRes 4444 (XQ)** : alpha, VFX, titres ; **DNxHR HQX / 444** : équivalents Avid, plus faciles sous Windows.
- **Proxies** : ProRes Proxy ou H.264 basse résolution **au même nom et même durée** que l'original (sinon la reconnexion échoue). Le proxy sert au rythme, jamais au jugement de la couleur ni de la netteté.
- **Rushes de téléphone en cadence variable (VFR)** [TESTÉ EN LABO, session 8, `labo/vfr/`] : un faux rush à vérité terrain (30 i/s, puis 3-8 s « basse lumière » à ~24 i/s avec gigue, flash et clic à 5,000 s) :
  - **Repérer** : `ffprobe` donne `r_frame_rate` ≠ `avg_frame_rate` (30/1 contre ~27) et des intervalles d'images inégaux (`mesure_vfr.py`).
  - **Lire les images à la cadence nominale** (ce que fait un logiciel qui ignore les horodatages) : **−400 ms de désynchro à 5 s**, et l'écart grandit (≈ 1 s à 10 s, calculé : 271 images lues à 30 i/s = 9,03 s pour 10 s de son).
  - **Convertir en cadence fixe à l'ingest** (`-fps_mode cfr -r 25`/`30`, ou `-vf fps=25` ; en intermédiaire ProRes/DNxHR + PCM) : **synchro exacte** (0 ms), au prix d'images doublées là où le téléphone n'a rien capturé (25 doublons sur 10 s à 30 i/s) : saccade visible dans les passages sombres. `minterpolate=mi_mode=blend` réduit les doublons (2) mais fond les images entre elles (traînées).
  - **Le choix artistique** : on ne peut pas inventer les images que le téléphone n'a pas prises. Saccade franche pour un rush documentaire (vérité du document), interpolation par mélange seulement pour un plan d'ambiance sans visage ni geste net, interpolation par IA (à tester) pour un plan qui doit être fluide. Toujours conformer **une fois, à l'ingest, à la cadence du projet** (25 en Europe), jamais dans la timeline.
  - Comportement de Premiere / Resolve face au VFR : [THÉORIQUE], à vérifier en phase 2 (`PLAN-TESTS-MCP.md`).

- **Ralentis et changements de cadence par interpolation** [TESTÉ EN LABO, session 9, `labo/interpolation/` ; Optical Flow de Premiere, Speed Warp de Resolve, Pixel Motion d'AE : THÉORIQUE] : 30 → 60 i/s contre une vérité terrain. Sur une image lisse aux grands mouvements, l'interpolation par mouvement (`minterpolate=mi_mode=mci`) bat le fondu de 3 dB en zones en mouvement ; **sur une texture fine, elle ne vaut pas mieux qu'un fondu** ; elle casse partout sur les objets fins qui tournent, les bords d'occlusion et les petits objets rapides. **Interpoler plan par plan** : à travers une coupe sans détection de changement de plan (`scd=none`), une image de mélange des deux plans apparaît (flash). `minterpolate` raccourcit le plan de 2 images source (−67 ms à 30 i/s). **RIFE 4.25** (IA libre, MIT, CPU, `labo/interpolation/RIFE.md`) : +5 dB sur `mci` en zones en mouvement sur l'image lisse (le meilleur outil libre testé pour un ralenti de plan net, famille de Speed Warp / Topaz), aucun gain sur la texture fine, et lui aussi invente une image hybride sur une coupe. Choix artistique : quand l'interpolation casse, assumer la duplication (saccade de *step-printing*) ou le fondu (traînée) plutôt que livrer des artefacts ; et tourner en haute cadence si le ralenti est prévu.

- **Fabriquer des proxies avec ffmpeg** [TESTÉ EN LABO, session 8, `labo/proxies/` ; rattachement dans les logiciels THÉORIQUE] : `-map 0:v -map 0:a` obligatoire (**par défaut ffmpeg ne garde qu'une piste audio** : proxy refusé ou ambiance perdue), même cadence, même rapport d'image (1/2 ou 1/4 exact), timecode recopié. ProRes Proxy (`prores_ks -profile:v 0`) ou H.264 tout-intra (`-g 1`, 3× plus léger ici) ; jamais de long-GOP pour scrubber. Vérifier chaque lot avec `labo/proxies/verif_proxy.py`. Pourquoi ça compte artistiquement : un montage qui saccade fait couper trop tôt (on n'ose pas laisser vivre un plan qu'on ne voit pas en temps réel).

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

## Vitesses dans l'aller-retour (session 10, `labo/workflows/vitesses/RESULTATS.md`) [TESTÉ EN LABO côté fichiers ; imports en phase 2]
- XML FCP7 via OTIO : **vitesses, arrêts sur image et inversions perdus sans avertissement** ; EDL : lignes M2 justes mais **durée source inversée** (ralenti = trop de source déclarée, accéléré = pas assez) et vitesse du plan entrant d'un fondu perdue à la relecture ; timecode de départ 01:00:00:00 non écrit.
- Règle : **aplatir les vitesses avant l'envoi** (rendre les ralentis, surtout interpolés) ou envoyer médias natifs + liste des vitesses + **vidéo de référence avec timecode incrusté**. Un aller-retour qui se relit sans erreur par le même outil ne prouve rien.

