---
name: montage-workflows
description: Passer un montage d'un logiciel à l'autre et tenir le pipeline — formats d'échange (EDL, XML FCP7, FCPXML, AAF, OTIO), Dynamic Link, conformation, envoi à l'étalo et au mixage, VFX pulls avec poignées, codecs intermédiaires (ProRes, DNxHR), fabrication des proxies, rushes VFR de téléphone, caler les horloges de plusieurs caméras, interpolation et ralentis, pipeline type par format. Mots d'un monteur : « on envoie à l'étalo », « fais-moi un XML », « l'EDL ne tombe pas juste », « exporte l'AAF pour le mixeur », « il faut des poignées », « ça a perdu les effets », « le son du téléphone se décale », « les caméras ne sont pas à la même heure ».
---

# Workflows et pipelines

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Savoir et recettes (pourquoi un pipeline, passages entre logiciels, codecs, proxies, VFR, horloges par corrélation audio, ralentis et interpolation, pipelines types, mesures du labo) : [details.md](details.md). Version d'avant : `archives/audit-2/skills/montage-workflows/`._

**Fait foi sur** : les échanges entre logiciels (ce qui passe et ce qui se perd), la conformation, les proxies, les rushes VFR, la synchro de plusieurs caméras, l'interpolation et les codecs intermédiaires. Procédures dans chaque logiciel : `montage-premiere`, `montage-resolve`, `montage-after-effects`, `montage-blender` ; specs de livraison : `montage-loudness-livraison`.

## 1. Formats d'échange : lequel pour quoi
| Format | Transporte | Perd | Usage |
|---|---|---|---|
| **EDL CMX 3600** | coupes, fondus, 1 piste vidéo, noms de bobines (8 car.), commentaires | **la cadence** (absente du fichier), effets, vitesses complexes, pistes multiples | conformation simple, étalonneur qui veut les points de coupe [TESTÉ EN LABO] |
| **XML FCP7 (xmeml)** | pistes, coupes, noms, marqueurs, certains effets de base, vitesses simples | effets propriétaires, titres, étalonnage | **le plus sûr pour Premiere ↔ Resolve** [fichier TESTÉ EN LABO ; import THÉORIQUE] |
| **FCPXML** | timeline Final Cut Pro, rôles | dépend du logiciel qui l'importe | FCP ↔ Resolve [THÉORIQUE] |
| **AAF** | montage + audio avec **poignées**, niveaux, pistes | effets vidéo | **envoi au mixeur** (Pro Tools, Fairlight) [TESTÉ EN LABO, fichier seulement] |
| **OTIO** | tout ce que les autres portent, ouvert, scriptable | peu d'imports natifs | pivot de conversion par script [TESTÉ EN LABO] |

Toujours mettre la cadence dans le nom du fichier (`film_v6_30p.edl`) : une EDL relue à la mauvaise cadence donne de faux timecodes, et un logiciel peut l'accepter en silence. [TESTÉ EN LABO]

## 2. Ce qui se perd dans l'aller-retour [TESTÉ EN LABO côté fichiers ; imports dans les logiciels à éprouver]
- **Un fichier d'échange transporte des coupes, pas des réglages** : vitesses, arrêts sur image, inversions, recadrages et images clés sont perdus sans avertissement dès que la timeline est reconstruite (XML FCP7 via OTIO : 7 réglages sur 7) ; l'EDL inverse la durée source des ralentis et ne garde aucun recadrage ; les nests sont relus vides ; une stéréo éclatée G/D perd un canal.
- **Donc** : aplatir avant l'envoi (rendre ralentis, nests, recadrages), ou envoyer médias natifs + liste des vitesses et recadrages (`labo/workflows/recadrages/liste_recadrages.py`) + vidéo de référence à timecode incrusté ; à l'arrivée, compter plans, pistes et canaux. Avant tout envoi d'EDL : `python3 labo/workflows/verif_edl.py film.edl 25`. Au mixeur : l'AAF exporté directement par le logiciel de montage, ou des stems.

## 3. Checklist d'envoi (à chaque passage)
1. Cadence, résolution, espace couleur notés dans le nom du fichier ou un fichier joint.
2. Vidéo de référence avec timecode incrusté.
3. Poignées (son : 2-5 s ; VFX : 8-16 images).
4. Relire l'échange dans un projet neuf **avant** de l'envoyer et comparer les coupes à la référence.
5. Ne jamais livrer depuis des proxies.

## 4. Ralentis : la technique pure, et l'œil de Diego
Repère de Diego (2026-10-12) : ×2 en natif depuis du 50 i/s, ×4 avec flux optique, au-delà « ça devient bizarre ». Sur la technique pure, ma veille doit aller plus loin que ce repère (hiérarchie du goût, `CLAUDE.md`), et tout ralenti interpolé se montre image par image à 200 % ; interpoler plan par plan, jamais à travers une coupe ; sur l'eau, le feuillage, une foule, un simple fondu peut battre l'interpolation ([details.md](details.md)).
