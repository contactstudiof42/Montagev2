# Autocritique — Sony LinkBuds Clip, V4

_2026-10-11. Autocritique V3 : `archives/phase-3/sony-linkbuds/autocritique-V3.md`. Regardé : planche de toute la vidéo (une image sur 8), 6 images en pleine résolution (`images/V4_6images.jpg`), chaque effet rendu par plage et relu image par image, titre comparé en pleine résolution à la DA Sony (`images/V4_titre_vs_ref.png`), flash cut comparé à l'exemple d'eyecannndy (vu moi-même). **Rien n'a été écouté.**_

## Mesures du rendu (`rendus/sony_linkbuds_V4.mp4`)
| | V3 | V4 | Cible |
|---|---|---|---|
| Durée | 44,6 s | 44,6 s | ≤ 60 s |
| Plans issus des rushes | 90 | 83 (63 rushes) | — |
| **Doublons** (même moment d'un rush deux fois) | **11** | **0** | 0 |
| Encodage | H.264, 11 Mb/s | **HEVC Main 10, yuv420p10le, 39 Mb/s**, BT.709 | Diego |
| Loudness / true peak | −14,1 / −1,1 | **−14,0 LUFS / −1,1 dBTP**, LRA 3,1 | −14 ±1 / ≤ −1 |
| Photosensibilité (pire seconde) | 3 | 3 (35 flashs ou inversions) | ≤ 3 |
| Noirs (p5) / contraste / couleur des noirs | 9 / 167 / brun | 9 / 174 / **neutre** | — |
| Tremblement des lettres K-O-R-E (rendu) | ~1,3-1,7 px | **0,18-0,34 px** | < 1,5 |
| Packshot rose C6725 | 2,7 px | **0,89 px** (geste gardé) | < 2 |
| Packshot C6723 (deux passages) | 0,7 / 1,8 px | **1,1 / 1,6 px** | < 2 |
| SFX | 64, peu de familles | **63, une famille par technique**, hauteurs variées | varié |

## Ce qui ne va pas encore, par ordre de gravité
1. **Le son n'a pas été écouté.** 63 sons placés sur la crête, 25 nouveaux sons d'Artlist jamais entendus, variantes de hauteur fabriquées (tic de verre, armement argentique, glitch). Risques : un son « cheap » que les mots-clés ne révèlent pas (la clameur à 32 s, le carillon non utilisé), une densité trop forte entre 26 et 28 s (néon, Polaroid, rewind, drop).
2. **Le flash cut des oreilles (6,1-7,2 s) n'est pas à échelle constante.** L'exemple d'eyecannndy (cartes de baseball) garde la même pose, la même place et la même échelle ; le mien garde la place de l'écouteur mais grossit d'une participante à l'autre (crescendo). Choix assumé (les plans moyens zoomés ×3 seraient sous la résolution native), mais c'est une variante, pas la technique pure. Les deux dernières macros (C6561, C6559) sont un peu molles.
3. **Rafale 2 (16,8-18,7 s) : le plan C6571 (jambes sombres et floues) est faible**, et le step-print rend la descente un peu illisible sur les plans sombres. Remplaçable par C6587 plus longtemps.
4. **Rafale 1 : C6624 revient deux fois** (7 s puis 17 s du rush) : la règle est respectée (moments différents), mais le cadrage identique peut se lire comme une répétition.
5. **Les collages sont pré-calculés** (Python, ProRes 4444) : propres, mais non modifiables dans Resolve. Le collage C (photo sur fond inversé) est le plus « effet » des trois.
6. **Le rouge** reste rouge-orangé : c'est la lumière réelle, mais moins spectaculaire que dans la V3 (où tout était rouge, y compris la peau).
7. Les compositions (carte de profondeur supprimée, écran partagé, zoom infini) restent légères : un rendu complet prend 60 s.

## Ce qui marche (vérifié)
- **Ouverture** : K, O, R, E épinglées au même point et à la même hauteur (0,2-0,3 px de résidu), puis un vrai zoom infini du E au mot KORE (alignement SIFT, recul exponentiel freiné, bord fondu, 7 images) : aucun rectangle visible, aucun flou de transition.
- **Une technique par moment** : zoom infini, flash cut aligné, rafale qui monte, step-print qui descend, écran partagé, inversions dans le rouge, trois collages différents. Aucune n'est répétée.
- **Couleur séparée** : peau naturelle, écouteur crème, décor qui recule, noirs neutres ; le packshot garde le détail du boîtier.
- **Titre** : dessin de la DA Sony (Medium + Light, espace 0,3 em), apparition sobre ; écart restant : la graisse exacte de la référence (entre Medium et Bold, image floue).
- **Stabilisation** : Gyroflow synchronisé partout où il est utilisé, puis fixe (lettres) ou rail (packshots) selon l'intention du cadreur.
