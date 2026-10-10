# Labo : recadrages, nests et audio multipiste dans l'aller-retour XML FCP7 / EDL / AAF via OTIO (session 11, 2026-10-10) — [TESTÉ EN LABO, côté fichiers]

BACKLOG 15 (suite de `../vitesses/`). Versions : Python 3.11, OpenTimelineIO 0.18.1, otio-fcp-adapter 1.0.0, otio-cmx3600-adapter 1.0.0, otio-aaf-adapter 2.0.0, pyaaf2 1.7.1 (pip, gratuits).
Deux vérités terrain à 25 i/s, départ 01:00:00:00 :
- `verite_fcp7.xml`, **XML FCP7 écrit à la main** comme un export Premiere : A zoom 150 % + rotation 10° + centre décalé + Crop (5/5/12/12) ; B Ken Burns (échelle 100→130 en images clés) ; un **nest** à 3 plans sur 2 pistes, lui-même zoomé à 120 % ; audio : une **paire stéréo éclatée** (G/D sur 2 pistes, −6 dB), une piste mono avec un niveau en images clés et un **fondu audio** Cross Fade (+3 dB).
- `natif_25p.otio`, **la même chose construite en OTIO** : effet générique `Transform`, nest = `Stack` dans un `Track`, 3 pistes audio, effet `AudioLevels`, fondu audio.
`recadrages.py` exporte, relit et compare champ par champ (relevé XML direct, sans OTIO, des deux côtés) → `resultats.json`.

## Résultats

| | Échelle / position / rotation / Crop | Images clés (Ken Burns, niveau) | Nest (séquence imbriquée) | Stéréo éclatée G/D | Pistes mono, niveaux de clip | Fondu audio |
|---|---|---|---|---|---|---|
| **XML FCP7 → OTIO → XML FCP7** (`aller_retour_fcp7.xml`) | **survit**, mais seulement comme métadonnées brutes `fcp_xml` recopiées telles quelles (OTIO n'en comprend rien : `Effect` sans valeurs exploitables) | survivent (même voie) | **perdu : nest relu vide** (0 plan sur 3) ; le plan nest devient une coquille | **canal droit perdu** (3 → 2 pistes audio) ; la piste restante se déclare encore « stéréo, 2 pistes éclatées » | survivent (via métadonnées) | survit ; clips adjacents réécrits en `start/end = -1` (convention FCP7, équivalent) |
| **Même timeline, métadonnées `fcp_xml` retirées** (cas d'une timeline modifiée par un script ou venue d'un autre format) (`otio_propre_fcp7.xml`) | **tout perdu** : l'adaptateur n'écrit **aucun `<filter>`** à partir des `Effect` OTIO | perdues | perdu (vide) | canal droit perdu, n° de canal source perdu | **niveaux perdus**, n° de canal source perdu | survit |
| **OTIO natif → XML FCP7** | perdu (aucun filtre écrit) | — | **plantage** si le `Stack` n'a pas de `source_range` ; avec, les 3 plans sont **écrits** (`natif_nest_borne.xml`) mais **relus vides** | n/a | **gain perdu** ; **noms de pistes perdus** | survit |
| **EDL CMX 3600** (`recadrages_*.edl`, `natif_2audio.edl`) | **perdu** (aucune trace, même pas en commentaire) | perdues | **nest supprimé sans avertissement** (événement absent) | **pistes audio non écrites** ; > 2 pistes audio : refus (`NotSupportedError`) | perdus | n/a |
| **AAF (otio-aaf-adapter)** | **non testable en labo** : l'écriture exige des MobID d'origine Avid (`Cannot find mob ID`) et des métadonnées AAF sur chaque fondu | — | — | — | — | refus (`AAFValidationError`) |

Chiffres clés : sur 7 plans de la vérité XML, l'aller-retour garde 6 plans (canal D perdu), 3 → 2 pistes audio, nest 3 → 0 plan intérieur ; sans métadonnées d'origine, 7 filtres sur 7 perdus ; EDL : 2 événements sur 3 vidéo (nest effacé), 0 audio. Timecode de départ : conservé dans le XML (01:00:00:00), toujours **perdu dans l'EDL** (00:00:00:00, cf. `../vitesses/`).

## Ce que ça montre
1. **Un recadrage « survit » à OTIO seulement s'il n'a pas été touché** : l'adaptateur recopie le XML d'origine qu'il a mis de côté. Dès que la timeline passe par un autre format, un script, ou est reconstruite, le recadrage disparaît sans message. OTIO n'a pas de schéma de transformation standard en 0.18 : un `Effect("Transform")` n'est écrit par aucun adaptateur.
2. **Les nests ne traversent pas** : bug de lecture de l'adaptateur FCP7 (il cherche les pistes directement sous `<sequence>` au lieu de `<sequence><media>`), donc tout nest venant de Premiere est relu vide ; l'EDL les supprime.
3. **La stéréo éclatée est fusionnée en une piste** à la lecture (seul le canal « primaire » est gardé) : au retour, il manque le canal droit. Les niveaux et fondus audio passent par le XML d'origine, jamais par l'EDL.

## Parades pratiques
- **Recadrages** : avant l'envoi, soit **les rendre** (plan recadré exporté en nouveau média), soit envoyer les médias pleins + **liste des recadrages en CSV** (`liste_recadrages.py fichier.xml > recadrages.csv`, voir `verite_recadrages.csv` : TC, plan, fichier, effet, paramètre, valeur ou images clés) + **vidéo de référence** avec TC incrusté. Ne jamais faire transiter un XML Premiere → Resolve par un script OTIO qui le modifie.
- **Nests** : **aplatir** (décomposer le nest dans la timeline principale) ou le rendre en un seul média avant tout échange ; contrôler le nombre de plans avant/après.
- **Audio multipiste** : pour le mixeur, **AAF exporté directement par le logiciel de montage** (pas via OTIO) ou **stems / WAV polyphoniques** ; vérifier le nombre de pistes et de canaux à l'arrivée. L'EDL ne sert qu'à l'image.

## Règles pour un monteur
1. Un fichier d'échange transporte des **coupes**, pas des **réglages** : recadrage, nest, gain et canal se vérifient à chaque passage, contre une vidéo de référence.
2. **Aplatir avant d'envoyer** : nests décomposés, recadrages rendus ou listés en CSV, vitesses rendues (`../vitesses/`).
3. **Compter à l'arrivée** : nombre de plans, de pistes audio, de canaux par plan ; un écart d'un seul = on arrête et on cherche.
4. **Audio : AAF natif du logiciel de montage, ou stems** ; jamais d'EDL ni de XML retouché par un outil tiers pour le mixage.
5. Artistiquement : un recadrage est un **cadrage décidé au montage** (un gros plan fabriqué dans un plan large) ; s'il se perd, l'étalonneur reçoit un autre plan que celui qu'on a monté. La liste CSV + la référence protègent cette décision.

## Ce qui reste à vérifier (phase 2, logiciels réels — PLAN-TESTS 46)
- Import direct (sans OTIO) d'un XML Premiere avec Basic Motion / Crop / nest dans **Resolve** : mapping zoom/position/rotation/rognage, nests en Compound Clips ? Et l'inverse Resolve → Premiere.
- `aller_retour_fcp7.xml` dans Premiere : la piste « stéréo éclatée » orpheline s'importe-t-elle en mono G seul ?
- AAF Premiere → Pro Tools / Resolve Fairlight : pistes, canaux, niveaux, fondus. Non mesurable ici (pas de médias Avid ; l'adaptateur AAF n'écrit que des timelines venues d'un AAF).
- Coordonnées : Basic Motion FCP7 (centre −1…1, échelle %) ≠ Resolve (zoom ×, position en pixels) : conversion à vérifier sur image.

## Rejouer
```
python3 -m pip install -q opentimelineio otio-fcp-adapter otio-cmx3600-adapter otio-aaf-adapter pyaaf2
python3 recadrages.py .                                     # réécrit les fichiers d'échange + resultats.json
python3 liste_recadrages.py verite_fcp7.xml > verite_recadrages.csv
```
