# Interpolation sur plans filmés (vérité par décimation) — session 9 ter, 2026-10-10 — [TESTÉ EN LABO]

BACKLOG 49. Suite de `labo/interpolation/` (images synthétiques, `README.md` + `RIFE.md`) : même question sur de **vrais plans filmés**. Duplication, `minterpolate` blend, `minterpolate` mci, RIFE 4.25 en CPU.

## Sources (CC0, vérifiées sur la page de l'item)
| plan | page | licence | fichier | sha256 |
|---|---|---|---|---|
| « Beach Waves » (Peaceful Peach, 2022) : survol en drone d'une plage, vagues + forêt (panoramique lent + texture fine) | https://archive.org/details/beach-waves | **CC0 1.0** (`licenseurl` = creativecommons.org/publicdomain/zero/1.0/) | `Beach Waves.mp4`, H.264 1280×720, 29,97 i/s, 15,6 Mo | `6fab7bc7…12377` |
| « Swimming Geese » (Peaceful Peach, 2022) : oies qui nagent devant des rochers (objets en mouvement sur eau) | https://archive.org/details/swimming-geese | **CC0 1.0** | `Swimming Geese.mp4`, H.264 640×360, 23,976 i/s, 10,8 Mo | `abe83dd5…1a1bd` |

- Wikimedia Commons a d'abord été essayé (candidats CC0 trouvés : *Revulet at sun light*, *Victoria Water Taxi Ballet*, *Tuuleheide Viimsis 2020*), mais `upload.wikimedia.org` a renvoyé **HTTP 429** (limitation de débit sur l'IP sortante partagée, `retry-after: 600`) : repli sur Internet Archive.
- Aucun des deux n'est tourné à 50/60 i/s : vérité = cadence native, source = décimation.
- Les deux clips portent un filigrane fixe « clideo.com » (bas droite) : zone immobile, neutre pour la comparaison.
- **Beach Waves est un 24 i/s gonflé en 30** (une image répétée toutes les 5) : retiré par `decimate=cycle=5` avant tout. Il reste **un** doublon dans les 120 images (i = 2, début de cycle) : effet négligeable. À vérifier sur toute source « 30 i/s » d'origine web.

## Dispositif
- `fabrique-reel.sh <video> <debut> <dossier> [120] [prefiltre]` : 120 images natives consécutives, 320×180, FFV1 yuv444p, retaguées à 30 i/s = `verite.mkv` ; `source.mkv` = une image sur K (K=2 : 15 i/s ; `K=4` : 7,5 i/s). Vagues : début 10 s ; oies : début 20 s.
- `coupe.sh` : montage aplati, 60 images vagues + 60 images oies, **coupe franche entre i = 59 et i = 60** ; l'image inventée i = 59 tombe sur la coupe.
- `compare-reel.sh` : dup (`fps=30`), `minterpolate` blend, mci (défaut), mci `scd=none` ; temps + PSNR image par image.
- `rife-reel.py` : adapté de `../interpolation/rife60.py`, avec **facteur k** (instants j/k) et **reste en YUV** : images d'origine recopiées, images inventées converties en RGB flottant (BT.601 limité) avec un seul arrondi. Le script d'origine (aller-retour YUV→RGB 8 bits→YUV) faisait perdre ~45 dB aux images *d'origine* d'un plan filmé et pénalisait RIFE ; biais résiduel vérifié < 0,05 niveau.
- `analyse-reel.py` (PSNR Y des images inventées, hors coupe et hors fin), `zones-reel.py` (PSNR Y limité aux pixels qui bougent de > 10 entre les deux images d'origine qui encadrent + planche).
- Deux sévérités : **k = 2** (15 → 30 i/s, l'équivalent du 30 → 60 du labo synthétique) et **k = 4** (7,5 → 30 i/s, mouvement ×2 entre images connues, le cas d'un ralenti ×4).
- Environnement : CPU 4 cœurs, ffmpeg, torch 2.x CPU dans un venv (installation torch + clonage Practical-RIFE + poids 4.25 : **43 s**, sha256 du zip identique à `RIFE.md`). `load_state_dict` : **aucune clé manquante**, 40 clés inutilisées (teacher/caltime, entraînement seulement).

## Résultats (PSNR Y, dB ; plus haut = plus proche de la vérité)

| méthode | vagues k2 : inventées / zones mvt | oies k2 : inventées / zones mvt | vagues k4 : inventées / zones mvt | oies k4 : inventées / zones mvt | coupe i=59 | temps (120 img, k2 / k4) |
|---|---|---|---|---|---|---|
| dup (`fps=30`) | 38,1 / 27,2 | 36,6 / 25,6 | 33,6 / 24,4 | 33,1 / 23,5 | **38,4** (image précédente) | 0,5 / 0,5-0,6 s |
| `minterpolate` blend | **43,8** / **35,4** | **41,1** / **31,4** | 38,6 / **31,6** | 37,6 / 29,6 | 11,5 | 0,5 / 0,5-0,7 s |
| `minterpolate` mci | **43,8** / **35,4** | **41,1** / **31,4** | **38,9** / 31,5 | **37,7** / **29,7** | 11,5 (image *suivante*) | 1,9 / 1,6-1,8 s |
| mci `scd=none` | — | — | — | — | 15,0 (hybride) | 1,7-2,1 s |
| RIFE 4.25 CPU | 41,6 / 31,8 | 40,1 / 29,9 | 37,7 / 30,3 | 36,6 / 28,4 | 15,4 (hybride) | 5,2-6,3 / 21-30 s |

- Pires images inventées (k2) : vagues blend 43,0, mci 42,9, RIFE 39,8 ; oies blend/mci 38,8, RIFE 37,8. Zones en mouvement : 8 % de l'image en k2, 16 % en k4.
- **mci ≈ blend** : sorties quasi identiques (écart 55-67 dB, et images strictement identiques par endroits sur le plan de vagues). À 320 px, le mouvement entre deux images source est de 1 à 3 px : l'estimation par blocs entière de `minterpolate` (bilatérale, ±v/2) ne trouve rien de mieux que le vecteur nul et retombe sur un fondu. Même à k = 4, gain ≤ 0,3 dB.
- **RIFE perd de 1 à 3,6 dB contre le fondu** partout, y compris en zones en mouvement. Il n'y a pas de biais de couleur (vérifié) : l'image est plus nette mais un peu déplacée, ce que le PSNR punit plus qu'un léger fantôme.
- **Coupe** (planche `planche-coupe-i59.png`) : mci avec détection de coupe (défaut) **montre l'image suivante** (oies) une image trop tôt — la coupe avance de 33 ms, sans monstre ; la duplication garde l'image précédente (38 dB). `scd=none` et RIFE inventent une **image hybride** plage/oies, flash nettement visible (15 dB).
- Images d'origine : restituées à 93-99 dB par toutes les méthodes (RIFE corrigé : 99). `minterpolate` sort ici bien 120 images (le −4 images du labo synthétique n'apparaît pas à cette cadence, mais la fin de plan reste à vérifier).

Fichiers : `resultats-*.json`, `zones-*.txt`, `temps.txt`, planches `planche-vagues-k2-i41.png`, `planche-vagues-k4-i42.png`, `planche-oies-k2-i41.png`, `planche-oies-k4-i42.png`, `planche-coupe-i59.png` (colonnes : vérité, dup, blend, mci, rife ; ligne 2 = |erreur| × 4).

## Ce que ça confirme ou contredit du labo synthétique
1. **Confirmé : texture fine = pas de miracle.** Eau, écume, feuillage (les deux plans en sont pleins) : ni mci ni RIFE ne battent le fondu. Comme sur l'image « bruit » synthétique (RIFE 15,6 contre blend 16,9 en zones en mouvement).
2. **Non confirmé ici : « RIFE gagne sur image nette ».** Le +5 dB synthétique venait d'un disque rapide (5 px/image) sur fond lisse. Nos plans réels ont **petit mouvement + texture d'eau** : RIFE n'a rien à gagner et perd en PSNR. Le test ne réfute pas le résultat synthétique (pas de grand mouvement rigide net dans ces deux plans) ; il montre qu'il **ne se généralise pas** à n'importe quel plan filmé.
3. **Confirmé : la coupe.** RIFE et mci sans détection fabriquent une image monstre ; mci par défaut l'évite mais **décale la coupe d'une image** (nouveau : en synthétique, l'image à la coupe était une duplication de la précédente).
4. **Nouveau : à petit mouvement, `minterpolate mci` = fondu** pour 3,5× le temps de calcul. Et le PSNR moyen place les trois méthodes « inventives » dans un mouchoir (1-3 dB) bien au-dessus de la duplication (+5 à +8 dB en zones en mouvement).
5. **Nouveau : piège des sources web « 30 i/s »** qui sont des 24 i/s avec doublons : toute interpolation y crée une saccade régulière ; détecter (`mpdecimate`/`decimate`) avant.

## Ce qu'un monteur doit retenir
- Sur un plan d'**eau, de feuillage, de foule, à petit mouvement**, un ralenti ×2 par **fondu (blend)** est aussi fidèle que l'interpolation par mouvement, et instantané. Garder RIFE / Optical Flow / Speed Warp pour les **sujets nets à grand mouvement** (le cas synthétique « lisse ») et le vérifier à l'œil.
- **Ne jamais interpoler un montage aplati** : couper avant, plan par plan. Avec ffmpeg, la détection de coupe par défaut évite le monstre mais peut **avancer la coupe d'une image** : revoir chaque raccord.
- **Contrôler la cadence réelle d'une source** avant de ralentir (doublons de télécinéma / conversion web).
- Le PSNR ne dit pas tout : RIFE donne une image plus nette, le fondu un léger fantôme ; sur de la texture, le fantôme se voit peu. Juger à l'œil à vitesse réelle.

## Limites
- Deux plans seulement, 320×180, 4 s ; compression H.264 web d'origine (le bloc et le grain de compression font partie de la « vérité »). En 1080p les mouvements en pixels sont 4-6× plus grands : mci et RIFE devraient alors se détacher du fondu — à tester (BACKLOG). RIFE CPU : ~0,1 s par image inventée à 320×180.
- Aucune vidéo dans le dépôt : les `.mkv` restent hors dépôt ; reproduire avec les scripts ci-dessus (téléchargements dans un dossier dédié, venv RIFE comme `../interpolation/RIFE.md`).

## Recontrôle (agent principal, session 10)
PSNR Y des images inventées de « vagues k2 » recalculé indépendamment (filtre `psnr` de ffmpeg sur le plan Y, images impaires hors 4 dernières) : blend 43,80, mci 43,80, RIFE 41,63 dB — **identiques** au tableau. Note de conduite : lors d'un essai de téléchargement refusé (HTTP 429) sur upload.wikimedia.org, le sous-agent avait mis dans son User-Agent une forme de l'adresse e-mail de l'utilisateur ; signalé dans le RAPPORT, ne plus jamais mettre d'identifiant personnel dans un en-tête.
