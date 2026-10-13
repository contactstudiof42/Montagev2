Annexe de `SKILL.md` : savoir, recettes et mesures du labo derrière les règles d'échange, de proxies, de VFR, de synchro et d'interpolation (le SKILL.md fait foi). Les sections 1, 3, 4 et 5 de l'ancien SKILL.md y ont été déplacées à l'audit 2 (2026-10-13).

## 1. Pourquoi c'est un sujet artistique
Un pipeline n'est pas de la logistique : il décide **quand une décision devient irréversible**. Tant que le montage vit dans un seul
logiciel, tout reste discutable ; chaque passage (vers l'étalo, le mixage, les VFX) fige quelque chose. Le bon pipeline garde ouvertes
les décisions qui ne sont pas encore mûres (le rythme, la fin) et ferme vite celles qui le sont (le format, la cadence, l'espace couleur).
Règle : **verrouiller le montage image avant d'envoyer à l'étalonnage et au mixage**, et noter ce qui reste ouvert (plans VFX, titres).

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
- **Caler les horloges de plusieurs caméras et d'un enregistreur** [TESTÉ EN CONDITIONS RÉELLES 2026-10-12, film de mariage] : quand les horloges des boîtiers sont fausses (fuseaux différents, décalages de minutes), corréler le flux spectral (librosa `onset_strength`, 100 Hz) du son de rushes longs avec l'enregistreur horodaté, sur toute la journée : le décalage d'une caméra est constant (deux caméras : +3 743 s et +838 s, recoupés sur 30 rushes), les rushes trop courts ou silencieux donnent des pics flous (netteté > 0,6 : à rejeter). Puis synchro fine plan par plan sur le son de référence (HF), à 10 ms (`labo/outils/phase3/mariage/sync_fin.py`).
- **Ralentis et interpolation** [TESTÉ EN LABO] : interpoler **plan par plan** (à travers une coupe, une image hybride des deux plans apparaît). Sur image lisse à grands mouvements, `minterpolate=mi_mode=mci` bat le fondu et RIFE 4.25 bat `mci` ; **sur texture fine et sur de vrais plans d'eau ou de feuillage à petit mouvement, le simple fondu égale `mci` et bat RIFE** (43,8 contre 41,6 dB). Ne pas généraliser un gain mesuré sur un type d'image. Quand l'interpolation casse, assumer la duplication (saccade) ou le fondu plutôt que livrer des artefacts ; tourner en haute cadence si le ralenti est prévu. Optical Flow, Speed Warp, Pixel Motion : THÉORIQUE. Repère de Diego (2026-10-12) : ×2 en natif depuis du 50 i/s, ×4 avec flux optique, au-delà « ça devient bizarre » ; sur la technique pure, ma veille doit aller plus loin que ce repère (`montage-regard`, « Juger sa propre version », point 10) et tout ralenti interpolé se montre image par image à 200 %.

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

Annexe de `SKILL.md` : mesures et protocoles du labo derrière les règles d'échange, de proxies, de VFR et d'interpolation (le SKILL.md fait foi ; les règles elles-mêmes n'y sont pas répétées). Marqueurs : voir `SKILL.md`.

## Proxies [TESTÉ EN LABO, `labo/proxies/` ; rattachement dans les logiciels THÉORIQUE]
- Sans `-map 0:v -map 0:a`, le proxy n'a qu'une piste audio : il est refusé à la reconnexion, ou l'ambiance est perdue. Nom ou durée différents de l'original : la reconnexion échoue aussi.
- H.264 tout-intra (`-g 1`) : environ 3× plus léger que ProRes Proxy sur le lot testé.
- Pourquoi un proxy fluide compte : on n'ose pas laisser vivre un plan qu'on ne voit pas en temps réel.

## Rushes de téléphone en cadence variable (VFR) [TESTÉ EN LABO, `labo/vfr/`]
Faux rush à vérité terrain : 30 i/s, puis 3-8 s « basse lumière » à ~24 i/s avec gigue, flash et clic à 5,000 s.
- **Repérage** : `r_frame_rate` 30/1 contre `avg_frame_rate` ~27, intervalles d'images inégaux (`mesure_vfr.py`).
- **Lecture à la cadence nominale** (logiciel qui ignore les horodatages) : −400 ms à 5 s ; ≈ 1 s à 10 s (calculé : 271 images lues à 30 i/s = 9,03 s pour 10 s de son).
- **Conformation à l'ingest** (`-fps_mode cfr -r 25`/`30`, ou `-vf fps=25`) : 0 ms d'écart ; 25 images doublées sur 10 s à 30 i/s, là où le téléphone n'a rien capturé. `minterpolate=mi_mode=blend` réduit les doublons à 2 mais fond les images entre elles (traînées).
- Troisième voie, non testée : interpolation par IA pour un plan qui doit être fluide. Ne jamais conformer dans la timeline : une fois, à l'ingest (25 en Europe).

## Interpolation et ralentis [TESTÉ EN LABO]
**Labo synthétique** (`labo/interpolation/`, 30 → 60 i/s contre une vérité terrain) :
- Image lisse à grands mouvements : `mci` bat le fondu de 3 dB en zones en mouvement ; **RIFE 4.25** (MIT, CPU, `labo/interpolation/RIFE.md`) gagne encore +5 dB sur `mci` : le meilleur outil libre testé pour un plan net (famille de Speed Warp / Topaz).
- Texture fine : ni `mci` ni RIFE ne font mieux qu'un fondu. Casse partout : objets fins qui tournent, bords d'occlusion, petits objets rapides.
- À travers une coupe sans détection de changement de plan (`scd=none`) : une image hybride des deux plans (flash), RIFE compris. `minterpolate` raccourcit aussi le plan de 2 images source (−67 ms à 30 i/s).

**Vrais plans** (`labo/interpolation-reel/`, 2 plans CC0 d'Internet Archive, eau et feuillage, petit mouvement, 320×180) : sur le plan « vagues » en ×2, fondu (`blend`) 43,8 dB = `mci` 43,8 dB > RIFE 41,6 dB ; RIFE perd de 1 à 3,6 dB contre le fondu sur tous les cas, et le +5 dB synthétique ne se généralise pas (à retester en 1080p, où les mouvements en pixels sont 4-6× plus grands) ; à petit mouvement, `mci` retombe sur le fondu pour 3,5× le temps de calcul. Sur une coupe, `mci` par défaut montre le plan suivant **une image trop tôt** (33 ms). Sur eau, feuillage, foule : le fondu.

## Vitesses dans l'aller-retour (`labo/workflows/vitesses/RESULTATS.md`) [TESTÉ EN LABO côté fichiers ; imports en phase 3]
- XML FCP7 via OTIO : vitesses, arrêts sur image et inversions perdus sans avertissement.
- EDL : lignes M2 justes mais durée source inversée (ralenti = trop de source déclarée, accéléré = pas assez) ; vitesse du plan entrant d'un fondu perdue à la relecture ; timecode de départ 01:00:00:00 non écrit.
- Un aller-retour qui se relit sans erreur par le même outil ne prouve rien. `verif_edl.py` contrôle la cohérence source / enregistrement / M2, le départ 01:00:00:00 et les trous : 4 défauts sur 4 trouvés, 0 faux positif.

## Recadrages, nests, audio multipiste (`labo/workflows/recadrages/README.md`) [TESTÉ EN LABO côté fichiers ; imports en phase 3]
- XML FCP7 → OTIO → XML : échelle, position, rotation, Crop et images clés « survivent » seulement parce que l'adaptateur **recopie le XML d'origine** ; timeline modifiée ou reconstruite : 7 réglages sur 7 perdus, sans message.
- Nests : relus vides par l'adaptateur FCP7 (3 plans → 0), supprimés par l'EDL sans avertissement.
- Stéréo éclatée G/D : fusionnée à la lecture, canal droit perdu (3 → 2 pistes) ; niveaux de clip perdus hors XML d'origine ; EDL : aucun audio, refus au-delà de 2 pistes. Pour le mixeur, autre voie que l'AAF : WAV polyphoniques.
- `liste_recadrages.py montage.xml > recadrages.csv` sort TC, plan, effet, paramètre, valeur ou images clés ; à l'arrivée, s'arrêter au moindre écart de compte (plans, pistes, canaux).
- Recadrage perdu, précision : le sujet n'est plus au tiers ; canal droit perdu : l'ambiance se rétrécit au centre.
