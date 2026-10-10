# labo/outils — regarder et mesurer un montage autour de ses coupes (session 24, 2026-10-10)

Réponse à Y23 (lire un vrai découpage), Y26 (activité hors coupes, robuste au grain), Y29 (bande-film générale).
Outil : `coupes.py` (Python 3, numpy, Pillow, ffmpeg ; `opentimelineio` pour l'OTIO, `pip install` 14 s).
Banc : `fabrique_test.py` fabrique une vidéo de 9 plans (8 à 75 images, plans fixes et animés, un son par plan,
un plan sur trois presque muet) avec l'EDL CMX3600 et l'OTIO exacts, et une variante à grain fort
(`noise=alls=40:allf=t`). Durée de fabrication : 2 s. Mesure complète : ~3 s pour 11 s de vidéo 320×180.

## Résultats [TESTÉ EN LABO]
| Test | Résultat |
|---|---|
| EDL CMX3600 (record in, timeline à 01:00:00:00, `* LOC:` = marqueurs) | 8/8 coupes, 2/2 marqueurs |
| OTIO (piste vidéo, marqueurs de piste) | 8/8, identique à l'EDL |
| scdet seuil 10, image propre | 8/8, 1 fausse alerte (c+1 entre deux plans fixes) |
| scdet seuil 10, grain fort | 8/8, **5 fausses alertes** : image 1 et c+1 |
| scdet seuil 5, grain fort | 8/8, 9 fausses alertes (toutes à c+1 ou image 1) |
| scdet + fusion des détections à 1 image d'écart (corrigé dans l'outil) | **8/8, 0 fausse alerte** propre et grain |

Activité visuelle hors coupes (vérité = la vidéo propre) :
| Mesure | propre | grain fort | erreur due au grain |
|---|---|---|---|
| YDIF plein cadre (signalstats) | 10,08 | 30,34 | **×3,0** |
| YDIF image /8 + flou 3×3 | 0,895 | 1,635 | +83 % |
| idem /16 | 0,533 | 0,893 | +68 % |
| idem /32 | 0,377 | 0,579 | +54 % |
| /8, moins le plancher (5e centile), linéaire | 0,895 | 0,506 | −43 % (surcorrige) |
| /8, soustraction **quadratique** du plancher, image par image | 0,895 | 1,061 | **+19 %** (retenu) |

## Ce que j'en retiens
- **Ne jamais mesurer « ça bouge » en plein cadre sur un rush granuleux ou un film à grain ajouté** : le grain triple la mesure. Réduire l'image ne suffit pas (le grain de `alls=40` survit à /32).
- Le grain s'ajoute en quadrature, pas linéairement : retirer le plancher mesuré sur les plans fixes par `√(a² − p²)`. Condition : le film contient au moins 5 % d'images sans mouvement (sinon le plancher est surestimé : le noter).
- **scdet double les coupes sur image granuleuse** (c et c+1) : toujours fusionner les détections voisines d'une image. Une EDL ou un OTIO valent mieux qu'une détection : la détection sert à vérifier un export, pas à le remplacer.
- La bande-film (6 images de part et d'autre, enveloppe du son sous chaque image, marqueurs en rouge) suffit pour juger un raccord à l'image près sans lecteur : c'est l'outil à lancer en phase 2 sur chaque export Premiere / Resolve (EDL ou OTIO) avant de le montrer.

## Fondus enchaînés dans l'EDL (2e passe, même session) [TESTÉ EN LABO]
- Banc : 3 plans, fondu `xfade` de 12 images (44 → 56) puis coupe sèche à 94 ; EDL CMX3600 écrite à la main avec la ligne de départ à durée nulle et la ligne `D    012`.
- Piège corrigé : sur une ligne `D 012` (ou `W001 012`), la durée **décale les timecodes d'un champ** ; l'ancien parseur lisait le TC source à la place du record in. Et la ligne de départ (record in = record out) ne doit pas compter comme une coupe.
- Résultat : coupes [50, 94] (le fondu compté en son milieu), fondus [[44, 12]] ; **scdet manque le fondu** (1/2) et voit la coupe sèche : un détecteur de coupe ne voit pas un fondu, il faut l'EDL (ou `labo/fondus/variance.py`).

## Limites
- EDL : événements vidéo `V` seulement ; un fondu compte comme une coupe en son milieu (décision arbitraire, notée dans le JSON sous `fondus`). Pas de pondération des événements (un rire ≠ un bruitage : reste dans `labo/youtube/densite.py`).
- Pas encore testé sur un vrai export Premiere / Resolve (phase 2, PLAN-TESTS 73).

## Pulsations et cadence (`tempos.py`, Y45) [TESTÉ EN LABO, calcul exact en fractions]
- BPM entiers dont la noire tombe sur des images entières : **25 i/s → 60, 75, 100, 125, 150** ; **24 i/s → 60, 72, 80, 90, 96, 120, 144, 160, 180** ; 30 i/s → 60, 72, 75, 90, 100, 120, 150, 180 ; 50 i/s → 60, 75, 100, 120, 125, 150 ; **23,976 et 29,97 : aucun**.
- **Piège** : à 25 i/s, 120 BPM = 12,5 images par temps. Couper « toutes les 12 images » dérive de **16 images (0,64 s) en 8 mesures** ; 128 BPM en coupant toutes les 12 : −9 images. Il faut couper sur la grille arrondie de chaque temps (12, 13, 12, 13…), jamais répéter une durée fixe. L'erreur d'arrondi par temps reste ≤ ½ image (invisible).
- Le tic de 1,25 s (48 BPM) tombe pile à 24 i/s (30 images), pas à 25 (31,25) : c'est ce que la pièce 29 a rencontré.
