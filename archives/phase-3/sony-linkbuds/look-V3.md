# Look — Sony LinkBuds Clip (V3)

_2026-10-11, étape 3 bis de `PROMPT-PHASE-3.md`. Décidé seul, sans validation de Diego (« à toi de te corriger seul »). Planche : `images/look_D.jpg` (rangée du haut : les 6 images du film avec le look ; rangée du bas : 3 images des références réseaux, équipe de France, Nike de dariusbuesch, yungchillyboy). Fichiers de travail : `videos/phase-3/sony-linkbuds/_travail/look/`._

## Intention
Une salle noire où seuls les corps sont éclairés : **noirs francs, peau chaude et dense, blancs des écouteurs propres**, la couleur du lieu (tungstène, néons, passage au rouge) gardée parce qu'elle raconte le lieu. Un tirage film (le goût de Diego par défaut), pas un filtre : pas de dominante ajoutée, pas de teal & orange plaqué.

## Chaîne (une seule LUT, un seul nœud)
`labo/couleur/look_sony.py` cuit tout en un `.cube` de 33 points : S-Log3 → linéaire, S-Gamut3.Cine → 709 (compression douce du gamut) → +0,25 diaph → **Cineon log → émulation de tirage Kodak 2383 D65 de Resolve** (`LUT/Film Looks/`) → saturation 1,1 des tons moyens (ombres non saturées) → **pied de courbe 0,08** (noirs écrasés) → **ombres neutralisées puis légèrement froides**. Installée : `LUT/P3/P3_sony_look_film_D.cube`. Réglage par plan : décalage CDL sur le log avant la LUT (1 diaph = 0,077 en S-Log3), par exemple −0,04 pour les packshots de jour.

## Itérations (jugées en pleine résolution, à côté des références)
| Version | Réglage | Verdict |
|---|---|---|
| V2 | LUT Sony LC-709 TypeA | sépia, laiteux, noirs gris-brun (p5 de luma 34 sur le plan C6507) ; à vignette réduite elle paraissait correcte : **la vignette ment** |
| A | 2383 pure, expo 0 | peau et couleurs plus riches, mais noirs encore bruns (t-shirt noir gris), blancs brûlés au packshot |
| B, C | 2383 dosée à 80-85 %, +0,3 à +0,5 diaph, saturation 1,1-1,15 | plus claires, retombent vers le laiteux |
| **D (retenue)** | 2383 pleine, +0,25 diaph, saturation 1,1, pied 0,08, ombres neutres | noirs francs avec texture, peau dense, écouteur blanc net, bijoux qui brillent ; rouge sombre mais lisible ; le niveau des références dans le style du brief |
| E | D plus clair (+0,4, pied 0,12) | proche de D, un peu moins dense |

## Écart restant avec les références (honnête)
- Les références sculptent la lumière au tournage (contre-jours, visage découpé sur noir) : un look ne crée pas cette lumière. Ici les rushes sont en lumière d'ambiance ; D les rend denses, pas sculptés.
- Pas de grain dans la LUT : grain posé à la finition par une couche dédiée (voir `plan.md`), désactivable.
- Les plans de jour (hall, packshots) n'ont pas la même lumière que la salle : même LUT, exposition par plan ; le passage salle → packshot reste une rupture voulue (flash).
