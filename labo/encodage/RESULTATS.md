# Labo encodage — bandes dans les dégradés sombres (session 2, 2026-10-09)

Script : `banding.py` (relançable, ~1 min). Mesures : `banding_resultats.json`.
Source : dégradé vertical cyan-vert, luma 4 → 34/255 (fond nocturne type Ziak / pièce 02), 540×960, 48 images.
Critère : profil vertical central après flou σ = 3 px (l'œil intègre le grain), **indice de marches** = max|dérivée| / moyenne|dérivée|
(≈ 1-2 lisse, > 4 marches nettes) + palier plat max (px). Mesure sur une seule image (n° 24) : indicatif, pas une métrique normalisée.

## Contrôle du critère (sans perte, qp 0)
| Variante | Indice | Palier max |
|---|---|---|
| 8 bits quantifié brut | 5,32 | 81 px |
| 8 bits tramé ±1 niveau (TPDF) | **1,92** | 52 px |
→ le critère voit bien les bandes et l'effet du tramage.

## Résultats (H.264 / HEVC, preset medium)
| Variante | Indice | Palier | Ko (1,6 s) |
|---|---|---|---|
| A 8 bits brut CRF 20 | 5,31 | 81 | 25 |
| B 8 bits tramé CRF 20 | 5,32 | 72 | 25 |
| C tramé CRF 20 `-tune grain` | 5,34 | 64 | 16 |
| D tramé CRF 16 `-tune grain` | 5,25 | 68 | 92 |
| E tramé CRF 23 | 5,32 | 57 | 14 |
| H 16 bits → 8 bits, `-aq-mode 3` | 5,34 | 64 | 30 |
| **F 10 bits x264 CRF 20** | **1,56** | 19 | 15 |
| G 10 bits x265 CRF 22 | 2,78 | 25 | 8 |
| F ré-encodé 8 bits CRF 23 (simulation plateforme) | 5,25 | 64 | 17 |
| grain σ = 1 niveau (a2) CRF 20 grain | 5,00 | 64 | 25 |
| **grain σ = 2 niveaux, grain fin (a4 t1)** CRF 20 grain | **2,83** | 8 | 308 |
| idem, ré-encodé 8 bits CRF 23 | **3,19** | 46 | 57 |
| grain σ = 2, gros grain 2 px (a4 t2), ré-encodé | 2,88 | 33 | 125 |
| grain σ = 3, gros grain (a6 t2), ré-encodé | 4,01* | 13 | 411 |
*le gros grain fort laisse du bruit après le flou de mesure : l'indice monte sans que ce soient des bandes.

## Ce que ça apprend
1. **Le tramage classique (±1 niveau) ne survit pas à x264**, même à CRF 16 et `-tune grain` : dans les zones sombres et plates, l'encodeur lisse ce bruit trop faible et les marches reviennent (5,3 comme sans tramage). Corrige ma piste de la session 1 (« CRF / tune grain » suffiraient) : **faux**.
2. **Le 10 bits règle le problème à la source** (1,56) et coûte moins cher (15 Ko) : c'est le bon format de master et d'échange (ProRes, DNxHR HQX, H.264/HEVC 10 bits).
3. **Mais la plateforme ré-encode en 8 bits** : le 10 bits ne protège plus (5,25 après ré-encode simulé). Pour une livraison réseaux sociaux d'images sombres, seul un **grain volontaire d'environ 2 niveaux d'écart-type, fin** tient après ré-encode (3,2 au lieu de 5,2), au prix d'un débit ~10× plus élevé à notre encodage.
4. Artistiquement : le grain n'est pas qu'un cache-misère. Dans une image basse et dense (Joker, Ziak), il donne une **matière** au noir. Le doser à l'image, pas en post-it : visible à 100 %, invisible comme « effet ».

## Recette [TESTÉ EN LABO]
- Master / échange : 10 bits partout (`-pix_fmt yuv420p10le` ou ProRes 422 HQ).
- Livraison réseaux d'un film sombre : ajouter un grain monochrome fin σ ≈ 2/255 **avant** l'encodage final 8 bits (Resolve : Film Grain ; AE : Add Grain ; ffmpeg : `noise=c0s=4:allf=t` sur la luma seule (calibré : bruit uniforme ±s → σ = s/√3 ; c0s=4 → σ 2,3 ; c0s=6 → 3,6 ; mesuré sur gris 20/255)), encoder en CRF 18-20 `-tune grain`, débit plus élevé accepté.
- Ne pas compter sur le tramage ±1 niveau ni sur `-aq-mode 3` seuls.
- À vérifier : le vrai ré-encodage d'Instagram/TikTok (inconnu, simulé ici par x264 CRF 23) → phase 2 (export test privé ? interdit de publier : à faire par l'utilisateur).
