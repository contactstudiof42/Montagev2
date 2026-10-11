# Look — Sony LinkBuds Clip (V4)

_2026-10-11, après la note de Diego sur la V3 : « bouillie de pixels », « encore trop pâté de couleurs », « toujours pas assez pro », plans d'écouteurs surexposés. Look V3 : `archives/phase-3/sony-linkbuds/look-V3.md`. Planche finale : `images/V4_6images.jpg` (ouverture, écouteur, collage, sommet rouge, écran partagé, titre)._

## Diagnostic de la V3 (mesuré sur une image en pleine résolution, OkLCh)
Tout tombait dans la même teinte : joue 41°, chouchou rose 28° (devenu saumon), écouteur 32° avec une chroma de 0,137 (il devait être presque neutre), fond flou 37°. Une seule couleur ambre, saturée (×1,3) : c'est le « pâté ». S'y ajoutait l'encodage H.264 à 11 Mb/s.

## Chaîne V4 (`labo/couleur/look_sony_v4.py`, une LUT par lumière, un seul nœud)
1. **Balance avant le tirage** (gains linéaires R 0,79 / V 1,065 / B 0,97 pour la salle) : la lumière tungstène était gardée trop chaude **et trop magenta** (refroidir seul rendait la peau plus rose : 41 → 33°). Gains trouvés par recherche sur des points témoins (peau vers 50°, écouteur vers le crème).
2. S-Log3 → tirage Kodak 2383 (comme la V3), saturation ramenée de 1,3 à 1,05.
3. **Séparation en OkLCh** : chroma réduite dans les tons sombres (le décor recule), hautes lumières désaturées (écouteurs, néons, boîtiers propres), peau plafonnée en douceur (chroma 0,085) et ramenée vers 55°, ambre du décor réduit (×0,6), ombres à peine froides.
4. Trois LUT : **salle**, **jour** (hall, packshots : sans la balance de salle), **rouge** (plans C6657 à C6681 : sans refroidissement, saturation 1,35, +0,15 diaph, pour que la bascule au rouge se lise). Plus **rouge négatif** (1 − rouge) pour les images d'inversion de la rafale 4.

## Résultat (mesuré)
| | V3 | V4 |
|---|---|---|
| Peau (joue, OkLCh) | 41°, C 0,109 | **50°, C 0,085** |
| Noirs (luma < 20), RVB moyen 8 bits | brun | **10,8 / 10,5 / 11,6** (neutres) |
| Noirs (5e centile) / contraste | 9 / 167 | 9 / 174 |
| Encodage | H.264 11 Mb/s | **H.265 Main 10, 39 Mb/s** ; PSNR 40,7 dB contre la même image rendue en PNG 16 bits, aucun bloc visible en noirs amplifiés ×6 |

Vérifications : mon banc Python reproduit Resolve à 1 % près (moyennes 0,887 contre 0,875 sur le même packshot) ; chaque LUT jugée sur 8 images témoins (dont une peau foncée, C6628) à côté des références réseaux.

## Erreur faite puis corrigée
Premier rendu V4 : noirs **bleu canard** (R 5, V 13, B 21 sur 43 % des pixels d'un plan), parce que j'avais cumulé deux refroidissements (ombres de `look_sony.py` + ombres de la séparation). Vu seulement en amplifiant les noirs ×6 : à l'œil, sur une vignette, l'image paraissait juste. Corrigé (froid 0,006, ombres 0,2). Leçon : mesurer la couleur des noirs, pas seulement leur luminance.

## Exposition des packshots (comment je l'ai mesurée)
Sur l'image rendue en pleine résolution : histogramme de luma du boîtier (zone du produit) et part des pixels ≥ 97 % (équivalent fausses couleurs « blanc brûlé ») et ≥ 250 / 255 sur l'image entière. V3 : ~10 % du boîtier au-dessus de 97 %. V4 : décalage CDL de −0,8 diaph (−0,081 en S-Log3) sur les trois packshots → **0 à 1,8 % de pixels ≥ 250**, uniquement des reflets ponctuels ; le 95e centile plafonne à 245-249 grâce à l'épaule du 2383 : le boîtier garde son modelé et sa couleur.

## Écart restant
La lumière de la salle reste une lumière d'ambiance tungstène, sans contre-jours sculptés : le look la rend propre et séparée, pas sculptée. Le rouge reste un rouge-orangé (la lumière réelle) plutôt qu'un rouge pur.
