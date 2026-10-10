# Labo interpolation d'images (ralenti, 30 → 60 i/s) — session 9, 2026-10-10 — [TESTÉ EN LABO]

BACKLOG 46. Question : que vaut l'interpolation par mouvement de ffmpeg (`minterpolate`) contre la duplication et le fondu, et où casse-t-elle ? Équivalents logiciels : Premiere « Optical Flow », Resolve « Optical Flow / Speed Warp », AE « Pixel Motion » (non testés ici, phase 2).

## Dispositif
- `fabrique.py <dossier> [bruit|lisse]` : vérité terrain à 60 i/s (240 images, 320×180) — fond qui panote (20 px/s), disque rapide (~300 px/s, 5 px par image à 60), barre qui tourne (0,8 tr/s), carré qui passe devant le disque (occlusion), **coupe franche à 2,0 s**. `source30.mkv` = une image sur deux. FFV1 sans perte.
  - « bruit » : textures aléatoires en blocs de 4 px, disque camouflé dans le fond (cas hostile).
  - « lisse » : fond flou contrasté, disque en dégradé avec une bande sombre (plus proche d'une image filmée).
- `compare.sh <dossier>` : 5 méthodes, temps de calcul, PSNR image par image contre la vérité.
- `analyse.py` : PSNR Y des images **inventées** (impaires) hors coupe, image inventée à travers la coupe (i = 119).
- `zones.py` : PSNR restreint aux **zones en mouvement** + planche (ligne 1 : vérité, dup, blend, mci, aobmc ; ligne 2 : |erreur| × 4).

## Résultats (PSNR Y, dB ; plus haut = plus proche de la vérité)

| méthode | lisse : inventées | lisse : zones en mvt | bruit : inventées | bruit : zones en mvt | coupe (lisse / bruit) | temps (240 img) |
|---|---|---|---|---|---|---|
| `fps=60` (duplication) | 31,2 | 10,4 | 28,2 | 14,3 | 30,2 / 22,5 | 0,7-1,0 s |
| `minterpolate mi_mode=blend` | 34,2 | 13,4 | 29,9 | 16,9 | 30,2 / 22,5 | 0,7-1,1 s |
| `minterpolate mi_mode=mci` (défaut : obmc, bilat) | **37,2** | **16,3** | 29,6 | 16,1 | 30,2 / 22,5 | 3,9-4,7 s |
| `mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1` | 37,0 | 16,0 | **30,7** | **17,3** | 30,2 / 22,5 | 7,4-8,1 s |
| `mci:scd=none` | 37,2 | 16,3 | 29,6 | 16,1 | **17,8 / 18,3** | 4,6 s |

Fichiers : `analyse-lisse.txt`, `analyse-bruit.txt`, `zones-*.txt`, `resultats-*.json`, planches `planche-lisse-i63.png`, `planche-bruit-i63.png`.

## Ce que ça montre
1. **Sur une image lisse avec de grands mouvements simples, l'interpolation par mouvement gagne nettement** (+3 dB sur le fondu, +6 sur la duplication en zones en mouvement).
2. **Sur une texture fine (feuillage, foule, eau, grain fort), elle ne vaut pas mieux qu'un fondu** (29,6 contre 29,9) : l'estimation de mouvement se trompe de bloc. Le mode `aobmc + bidir` récupère un peu (+1 dB) pour deux fois le temps de calcul.
3. **Ce qui casse partout** (planches, ligne 2) : la **barre qui tourne** (objet fin en rotation : hélices, rayons, baguettes), le **bord d'occlusion** (carré devant le disque), le **petit objet rapide** (5 px/image). Aucune méthode n'invente correctement ce qui était caché.
4. **Coupe** : avec la détection de changement de plan par défaut (`scd=fdiff`), l'image inventée à la coupe est une duplication (inoffensive) ; **sans elle, une image de mélange des deux plans** (17,8 dB) apparaît sur la coupe — un flash visible. **Interpoler plan par plan, jamais un montage aplati.**
5. **Durée** : `minterpolate` sort 236 images au lieu de 240 (les 2 dernières images source ne sont pas prolongées) : **−67 ms en fin de plan**. Sur un conformage, prévoir des poignées ou vérifier la durée.
6. Les images d'origine ne sont pas restituées à l'identique (≈ 78-81 dB, écart infime, dû au passage YUV) : sans conséquence visible.

## Quand l'utiliser (point de vue de monteur)
- **Ralenti fluide** acceptable : panoramique, travelling, dérive lente, grand sujet sur fond uni ou flou. À refuser : mains, cheveux, rayons, hélices, eau, foule, tout ce qui passe devant autre chose.
- **Le fondu (blend) et la duplication sont des choix esthétiques, pas des pis-aller** : la duplication donne le saccadé du *step-printing* (Wong Kar-wai / Doyle, `culture/christopher-doyle-wong-kar-wai.md`), le fondu une traînée de rêve. Quand l'interpolation casse, assumer l'un des deux plutôt que livrer des artefacts de mouvement.
- Toujours **filmer en haute cadence** si un ralenti est prévu (`montage-preparation-tournage-vfx`) : l'interpolation répare, elle ne remplace pas.

## Limites et suite
- Images synthétiques ; PSNR ne mesure pas la gêne perçue (un fondu « fantôme » peut avoir un bon PSNR et se voir). RIFE 4.25 testé en CPU : voir `RIFE.md` (+5 dB sur mci en zones en mouvement sur l'image lisse, aucun gain sur la texture fine, image hybride sur la coupe). Recontrôlé par l'agent principal avec `analyse.py` : chiffres identiques. FILM, Topaz, Speed Warp non testés.
