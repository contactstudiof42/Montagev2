# Labo proxies (session 8, 2026-10-10)

But : fabriquer des proxies avec ffmpeg qui se rattachent à leurs originaux. Critères vérifiés par `verif_proxy.py` : même cadence, même nombre d'images, même rapport d'image, même nombre de pistes et de canaux audio, même timecode de départ. Ces critères viennent de la doc Adobe (« Attach Proxies ») et de la pratique Resolve : **le comportement réel des logiciels est [THÉORIQUE] ici**, à vérifier en phase 2 (PLAN-TESTS 42).

Original synthétique : 1920×1080, 25 i/s, 10 s, ProRes 422 HQ, **2 pistes audio** (mono + stéréo), TC 10:00:00:00 (86 Mo).

| proxy | commande (essentiel) | Mo | temps VM | verdict |
|---|---|---|---|---|
| p1 H.264 « naïf » | `-vf scale=960:540 -c:v libx264 -c:a aac` | 1,4 | 5,1 s | **ÉCART : 1 seule piste audio** |
| p2 ProRes Proxy | `-map 0:v -map 0:a -c:v prores_ks -profile:v 0 -c:a pcm_s16le` | 13,0 | 5,8 s | OK |
| p3 H.264 tout-intra | `-map 0:v -map 0:a -c:v libx264 -g 1 -c:a aac` (.mov) | 4,8 | 3,4 s | OK |
| p4 mauvais rapport | `scale=1024:540` | 13,4 | 6,8 s | **ÉCART : rapport** |
| p5 ProRes sans `-timecode` | idem p2 sans l'option | 13,0 | 6,7 s | OK (TC recopié) |

Leçons :
1. **Piège n°1 : ffmpeg ne garde qu'une piste audio par défaut** (sélection automatique d'un seul flux par type). Toujours `-map 0:v -map 0:a` pour un proxy : sinon le rattachement échoue ou, pire, le son de l'ambiance disparaît du montage.
2. Le timecode de départ est recopié par défaut (même en .mp4) ; le forcer reste une ceinture de sécurité.
3. Garder exactement le rapport d'image (1/2 ou 1/4 de la définition) ; un proxy « arrondi » (1024×540) est refusé.
4. Tout-intra (`-g 1`) : plus léger que ProRes Proxy (4,8 contre 13 Mo ici) et rapide à encoder ; le long-GOP (p1) est le plus léger mais le plus lourd à décoder en scrub : à éviter pour un proxy.
5. Mesures sur une mire synthétique : les rapports de taille changent avec de vraies images (bruit, grain).
