# Labo : vitesses, arrêts sur image, inversions et fondus dans l'aller-retour EDL / XML / OTIO (session 10, 2026-10-10) — [TESTÉ EN LABO, côté fichiers]

BACKLOG 15 (« tester vitesses, recadrages, nests… dans l'aller-retour »). Outil : `vitesses.py sortie/`. OpenTimelineIO 0.18.1 + `otio-fcp-adapter` + `otio-cmx3600-adapter` (pip, 6 s).
Timeline de test à 25 i/s, 2 pistes : A normal, B ralenti 50 %, C accéléré 200 %, D arrêt sur image, E inversé (−100 %), fondu de 12 images E→F, F ralenti 40 % ; en V2 un titre incrusté. Fichiers écrits : `vitesses_25p.otio`, `.xml` (FCP7), `.edl` (CMX 3600, V1 seule) ; comparaison : `resultats.json`.

| | Coupes et positions | Vitesses | Arrêt sur image | Inversion | Fondu | Pistes |
|---|---|---|---|---|---|---|
| **OTIO JSON** | exactes | conservées | conservé | conservée | conservé | noms conservés |
| **FCP7 XML** (adaptateur OTIO) | exactes | **toutes perdues** (aucun effet de vitesse écrit) | **perdu** | **perdue** | conservé (Cross Dissolve) | **noms de pistes perdus** |
| **EDL CMX 3600** | exactes à la représentation près (le fondu centré 6/6 devient un fondu qui démarre 6 images avant la coupe : même image à l'écran) | lignes M2 écrites justes (12,5 / 50 / 0 / −25 / 10 i/s) mais **point de sortie source faux** (voir 2) ; **la vitesse du plan entrant d'un fondu (F, 40 %) est perdue à la relecture** | conservé (M2 0.0 + commentaire FREEZE FRAME) | conservée | conservé (`D 012`) | une seule piste ; **timecode d'enregistrement à 00:00:00:00** alors que la timeline démarre à 01:00:00:00 |

## Ce que ça montre
1. **Une vitesse ne voyage pas** : le XML FCP7 produit par l'outil d'échange libre la jette sans prévenir, l'EDL la garde à moitié. Seul l'OTIO natif la porte, et peu de logiciels l'importent.
2. **Un aller-retour réussi par le même outil ne prouve pas que le fichier est juste.** Dans l'EDL, le ralenti à 50 % (2 s à l'écran) déclare 4 s de source au lieu de 1 s, l'accéléré 200 % déclare 1 s au lieu de 4 s : la durée source est divisée par la vitesse au lieu d'être multipliée. La relecture par le même adaptateur se recale sur la durée d'enregistrement, donc tout paraît exact. Un conformateur qui lit les points source (et non la ligne M2) tirera la mauvaise quantité de média : **les poignées et les médias consolidés seront trop courts pour les accélérés**.
3. Le timecode de départ (01:00:00:00, convention de diffusion) n'est pas écrit dans l'EDL : décalage d'une heure à l'import chez l'étalonneur si personne ne le vérifie.

## Ce que j'en retiens pour le métier [TESTÉ EN LABO pour les fichiers ; comportement à l'import dans Premiere / Resolve / Avid = phase 2, PLAN-TESTS 46]
- **Avant un envoi à l'étalonnage ou aux VFX, aplatir les vitesses** : soit les rendre (plan rendu au ralenti, nouveau média, nom explicite `B_ralenti50_rendu`), soit envoyer les médias à vitesse native avec **une liste des changements de vitesse** et **une vidéo de référence** (le montage exporté avec timecode incrusté), contre laquelle on vérifie chaque plan.
- Un ralenti **interpolé** (Optical Flow, RIFE) se rend toujours avant l'envoi : l'interpolation ne se recalcule pas à l'identique chez un autre logiciel.
- **Vérifier l'EDL à l'œil** : point source de sortie cohérent avec la vitesse (source = durée × vitesse), timecode de départ, vitesse des plans entrants dans un fondu.
- Artistiquement : un ralenti qu'on a « réglé à l'oreille » dans le montage est une décision de rythme ; s'il se perd en route, le film revient à l'étalonnage avec un autre rythme sans que personne le voie. C'est la vidéo de référence qui protège la décision.

## Vérificateur d'EDL (`../verif_edl.py fichier.edl cadence [départ]`, BACKLOG 58) — [TESTÉ EN LABO]
- Sur `vitesses_25p.edl` (écrite par OTIO) : **4 alertes**, toutes réelles : départ à 00:00:00:00 au lieu de 01:00:00:00 ; B (50 %) 100 images source au lieu de 25 ; C (200 %) 25 au lieu de 100 ; **F (40 %, plan entrant du fondu) 56 images source pour 56 enregistrées** — l'adaptateur ignore la vitesse sur l'événement de fondu (deuxième défaut, distinct de l'inversion).
- Sur `juste_25p.edl` (écrite à la main, source = enregistrement × vitesse, départ 01:00:00:00) : **aucune alerte** (pas de faux positif).
- Limites : une seule convention vérifiée (source = enregistrement × vitesse) ; certains logiciels écrivent la source sans tenir compte de la vitesse : l'alerte dit alors « à vérifier », pas « faux ». Fondus : l'événement de départ de longueur nulle est ignoré. Pas de lecture des effets de recadrage (absents du CMX 3600).
