# Labo keying — distance au fond vert, réglage du key, despill (session 2, 2026-10-10)

Scripts : `scene_vert.py` (Blender : sphère grise + 9 tiges de 8 mm = « cheveux », devant un fond vert émissif diffus à 0,3 / 1 / 3 m ; un 2e rendu transparent donne **l'alpha de vérité terrain**), `mesure_key.py` (ffmpeg `chromakey` ± `despill`, comparaison à la vérité). Mesures : `resultats.json`. Durée totale : ~1 min.

| Distance sujet-fond | Débordement vert sur le sujet (G − max(R,B), /255) | Trous dans le sujet (key 0,12) | Erreur alpha moyenne | Erreur alpha sur les bords |
|---|---|---|---|---|
| 0,3 m | 9,6 | 4,7 % | 1,8 % | 43 % |
| 1 m | 7,5 | 2,6 % | 1,5 % | 42 % |
| 3 m | **3,7** | **0,8 %** | **1,0 %** | 41 % |

- **La distance divise le débordement par 2,6 entre 0,3 et 3 m** et les trous dans le sujet par 6. Confirme la règle de plateau « 2 à 3 m au moins » ([TESTÉ EN LABO] en synthèse 3D ; réserve : dans ma scène, le fond proche reçoit aussi plus de lumière de la key, ce qui le délave, deux causes mêlées).
- **Un fond surexposé se délave et le keyer mange le sujet** : mon fond était écrêté (G = 255, R = 92 à 156). Avec une tolérance de 0,20 au lieu de 0,12, 86 à 92 % du sujet gris disparaît. Le fond doit être **saturé, pas brillant** : exposer le vert au niveau du gris moyen, comme le dit la pratique.
- **`despill=type=green`** ramène le vert résiduel du sujet de 3,7-9,6 à 0, sans toucher l'alpha.
- **Les « cheveux » fins sont perdus quelle que soit la distance** (≈ 41-43 % d'erreur sur les bords) : `chromakey` est un key de chrominance quasi binaire. Pour les cheveux, il faut un keyer qui travaille en alpha doux (Keylight, Resolve 3D Keyer, Delta Keyer) et un contre-jour au tournage : à mesurer en phase 2 avec le même protocole (vérité terrain Blender).
