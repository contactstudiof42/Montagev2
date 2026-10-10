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
| **AAF** | montage + audio avec **poignées**, niveaux, pistes | effets vidéo | **envoi au mixeur** (Pro Tools, Fairlight) [THÉORIQUE] |
| **OTIO** | tout ce que les autres portent, ouvert, scriptable | peu d'imports natifs | pivot de conversion par script (Python `opentimelineio`) [TESTÉ EN LABO] |

Pièges vérifiés : une EDL relue à la mauvaise cadence donne de faux timecodes (relue à 24 au lieu de 30 : échec net en script,
mais un logiciel peut l'accepter en silence). **Toujours mettre la cadence dans le nom du fichier** (`film_v6_30p.edl`).

## 3. Passages entre logiciels (règles d'usage) [THÉORIQUE sauf mention]
- **Premiere → After Effects** : Dynamic Link pour un plan qui bouge encore (le montage peut changer) ; **rendu intermédiaire** (ProRes 4444 avec alpha) dès que le plan est validé, car le Dynamic Link ralentit la timeline et casse quand on déplace les projets.
- **Premiere / montage → Resolve (étalonnage)** : XML + rushes originaux (pas les proxies !). Avant l'export : aplatir les nests, retirer les effets inutiles, mettre les plans sur le minimum de pistes, noter les recadrages et vitesses (souvent mal traduits). Alternative robuste : un **fichier « référence » du montage** (export plein cadre) à superposer dans Resolve pour vérifier la conformation plan à plan.
- **Montage → mixage** : AAF avec **poignées** (2 à 5 s), pistes rangées par famille (dialogues, ambiances, SFX, musique), + vidéo de référence avec timecode incrusté, + liste des intentions (où le silence, où la musique arrache).
- **Plans VFX (pull)** : exporter les plans concernés en EXR ou DPX, dans l'espace couleur d'origine (log), **avec poignées de 8 à 16 images**, nommés par plan (`SH010_v001`), et une liste (EDL ou tableau) qui dit où ils retournent. Retour en EXR/ProRes 4444, même nom, version incrémentée.
- **Blender → compositing / montage** : séquence d'images (PNG pour l'atelier, EXR multicouche pour un vrai compositing), jamais une vidéo compressée en sortie de rendu (un plantage perd tout, une image ratée se re-rend seule). [TESTÉ en atelier : séquences PNG + montage ffmpeg, pièces 01-04]
- **Grille de musique → montage** : marqueurs générés hors logiciel en XML FCP7 (`labo/marqueurs/beats_xml.py`) [détection TESTÉE EN LABO].

## 4. Codecs intermédiaires et proxies (choix) [THÉORIQUE, specs à vérifier sur les pages Apple/Avid]
- **ProRes 422 HQ** : master de montage 10 bits ; **ProRes 4444 (XQ)** : alpha, VFX, titres ; **DNxHR HQX / 444** : équivalents Avid, plus faciles sous Windows.
- **Proxies** : ProRes Proxy ou H.264 basse résolution **au même nom et même durée** que l'original (sinon la reconnexion échoue). Le proxy sert au rythme, jamais au jugement de la couleur ni de la netteté.
- Ne jamais monter des fichiers à GOP long à cadence variable (téléphone) sans les transcoder en cadence fixe : désynchro du son garantie. [THÉORIQUE ; à tester avec ffmpeg]

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
