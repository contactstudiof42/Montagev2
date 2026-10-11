# Autocritique — Sony LinkBuds Clip, V3

_2026-10-11. Autocritique de la V2 : `archives/phase-3/sony-linkbuds/autocritique-V2.md`. Regardé : planches à 5 images par seconde, 6 images en pleine résolution à côté des références (`images/V3_6images.jpg`, `images/look_D.jpg`), courbes des zooms relues image par image, `tremblement.py`, `qc_livraison.sh`, `flash_check.py`. **Rien n'a été écouté.** Question posée à chaque image : « un monteur pro livrerait-il ça ? »_

## Mesures du rendu final (`rendus/sony_linkbuds_V3.mp4`)
| | V2 | V3 | Claude nu | Références réseaux |
|---|---|---|---|---|
| Durée | 59,6 s | **44,6 s** | 54,9 s | 12-43 s |
| Plans | 68 | **91** | 83 | — |
| Flashs | 6 | 28 | ≈ 60 | — |
| SFX | 19 | **64** | ≈ 55 | — |
| Impacts / poussées / secousses | 4 / 1 / 1 | **19 / 11 / 2** (+ 1 punch-in) | ≈ 30 en tout | — |
| Détourages | 0 | **3** | 3 | — |
| Noirs (5e centile de luma) | 17 | **9** | 19 | 5-11 |
| Contraste (95e − 5e centile) | 137 | **167** | 117 | 121-170 |
| Saturation moyenne | 113 | 100 | 143 | 79-158 (médiane 115) |
| Loudness / true peak | −14,5 / −1,4 | **−14,1 / −1,1** | −13,2 / −2,0 (crête) | — |
| Photosensibilité (pire seconde) | 3 | 3 | non mesuré | — |
| Tremblement des packshots (moyenne) | 4,3-4,7 px | **0,7-2,7 px** | ≈ tremble aussi | plan fixe < 1,5 |

## Ce qui ne va pas encore, par ordre de gravité
1. **Le son n'a pas été écouté.** 64 SFX choisis sur leur nom et leur forme d'onde, une coupure musicale (125,736 → 133,236 s) calée par la phase des temps forts : à valider à l'oreille avant tout. C'est le risque principal de la V3.
2. **Packshot rose (C6725) : 2,7 px de tremblement moyen** après ma stabilisation (5,5 avant), au-dessus de mon seuil de 2 px ; pic 4,7 px. Il dure 1 s et commence sur un flash. Gyroflow ferait mieux s'il obtient l'accès au dossier.
3. **Halo jaune autour des cheveux sur le premier détourage** (C6594, 281-293) : la carte de profondeur hésite sur les mèches éclairées par le néon. Visible sur image fixe ; sur 12 images en plein rythme, probablement pas. Le contour blanc ne suit pas une mèche.
4. **Le titre est juste propre, pas remarquable.** SST Pro Roman qui monte sous un masque et dont l'interlettrage se resserre : c'est le geste standard d'une marque tech, sans idée propre au film. Mieux qu'un grossissement, en deçà des titres de mes références (darius, équipe de France). Alternative à juger par Diego : pas de titre (le plan de fin Sony suffit).
5. **Le dernier packshot tient 3 s** (995-1072) avec une poussée lente et le titre : la plus longue tenue du film, voulue comme conclusion, mais après 40 s de rafales elle peut paraître longue.
6. **Rupture de lumière salle rouge → packshots de jour.** Assumée (flash blanc, « après la séance, l'objet »), mais c'est un autre monde ; les boîtiers dans la salle noire (C6506-C6508) gardaient l'unité, en tremblant beaucoup plus (travellings rapides).
7. **Look jugé seul.** D2 a le niveau de densité des références (noirs 9, contraste 167) ; la lumière des rushes reste une lumière d'ambiance, sans les contre-jours sculptés de mes références. Grain posé en Overlay à 35 %, à doser à l'œil sur un vrai écran.
8. Les arrêts sur image et les détourages alourdissent le rendu (carte de profondeur par IA) : un rendu complet prend environ 1 min 30 au lieu de 15 s.

## Ce qui marche (vérifié)
- L'ouverture K-O-R-E : quatre lettres au même point du cadre, une par temps, puis le mot. On sait où l'on est en 2 s.
- Les rafales reviennent quatre fois (199, 421, 609, 784), séparées par des plans tenus et des arrêts détourés : contraste vitesse / arrêt, ce que Diego avait aimé vers 15 s dans la V2.
- Les détourages : propres sur C6566 et C6657, orange / noir / rouge, contour blanc net, figés pour de bon.
- Les courbes de zoom : départ rapide, freinage long, flou de bougé ; relues image par image (1,25 → 1,008 dès la 2e image puis 1,0).
- Aucune transition intégrée de type glissement, poussée ou volet.
- Ordre des plans : chaque bloc a sa raison écrite dans `plan.md`.
