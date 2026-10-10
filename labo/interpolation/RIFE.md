# RIFE (interpolation par IA) contre minterpolate — session 9 bis, 2026-10-10 — [TESTÉ EN LABO]

BACKLOG 46b. Même vérité terrain que `README.md` (320×180, 30 → 60 i/s, coupe à 2,0 s), en CPU (4 cœurs, sans GPU).

## Installation
- `pip install torch --index-url https://download.pytorch.org/whl/cpu` : torch 2.14.1+cpu, **46 s**, **769 Mo** sur disque (numpy déjà présent ; opencv inutile).
- Code : `git clone https://github.com/hzwer/Practical-RIFE` (licence **MIT**, © 2021 hzwer) — seul `model/warplayer.py` sert.
- Poids : **RIFE 4.25** (recommandé par défaut), zip de 22,9 Mo sur Google Drive (id `1ZKjcbmt1hypiFprJPIKW0Tt0lr_2i7bg`), récupéré sans compte par
  `curl -L "https://drive.usercontent.google.com/download?id=<id>&export=download&confirm=t"` (sha256 `e63d481b…de5b4`).
  Contenu : `train_log/flownet.pkl` + `IFNet_HDv3.py`. Le README du dépôt indique que les poids sont **sous la même licence MIT** (usage commercial possible).
- Aucun échec : Google Drive a répondu directement, pas besoin d'alternative Hugging Face.

## Commande
Script maison `rife60.py` (versé au dépôt par l agent principal ; `load_state_dict(strict=False)` : les résultats prouvent que les poids sont chargés, mais vérifier le retour « missing keys » avant tout usage) : décode `source30.mkv` en RGB par ffmpeg, charge `IFNet` + `flownet.pkl` (`torch.load(..., weights_only=True)`), complète l'image à un multiple de 64 (320×192), appelle `net(x, 0.5, [16, 8, 4, 2, 1])` pour chaque paire, garde les images d'origine, puis encode en `ffv1 -pix_fmt yuv444p` → `rife.mkv`. PSNR comme `compare.sh` :
`ffmpeg -i rife.mkv -i verite60.mkv -lavfi "[0][1]psnr=stats_file=rife.psnr" -f null -`
- **240 images** comme la vérité : 120 d'origine + 119 inventées + la dernière image dupliquée (minterpolate en sort 236).
- Pas de détection de coupe (RIFE brut ; `inference_video.py` du dépôt en a une, par SSIM, non utilisée ici).

## Résultats (PSNR Y, dB ; plus haut = mieux)

| méthode | lisse : inventées | lisse : zones en mvt | bruit : inventées | bruit : zones en mvt | coupe i=119 (lisse / bruit) | temps (240 img) |
|---|---|---|---|---|---|---|
| `fps=60` (duplication) | 31,2 | 10,4 | 28,2 | 14,3 | 30,2 / 22,5 | 0,7-1,0 s |
| `minterpolate` blend | 34,2 | 13,4 | 29,9 | **16,9** | 30,2 / 22,5 | 0,7-1,1 s |
| `minterpolate` mci | 37,2 | 16,3 | 29,6 | 16,1 | 30,2 / 22,5 | 3,9-4,7 s |
| **RIFE 4.25 (CPU)** | **41,2** | **21,2** | **30,3** | 15,6 | **20,5 / 21,3** | 12-24 s (92 s au 1er lancement à froid) |

- Pire image inventée : lisse 32,8 (mci 33,2), bruit 24,2 (blend 27,6, mci 25,7) : RIFE gagne en moyenne mais a des ratés ponctuels.
- Images d'origine restituées à l'identique (99 dB, contre ≈ 79-81 avec minterpolate).
- Planches (colonnes : vérité, dup, blend, mci, rife ; ligne 2 = |erreur| × 4) : `planche-rife-lisse-i63.png`, `planche-rife-bruit-i63.png`.

## Lecture
1. **Image lisse (proche du filmé) : RIFE écrase minterpolate** : +4 dB sur les inventées, **+5 dB dans les zones en mouvement** (21,2 contre 16,3). Le disque rapide et le bord d'occlusion sont nettement mieux reconstruits.
2. **Texture fine (bruit) : pas de miracle** : un peu mieux en moyenne (30,3), mais moins bon que le fondu dans les zones en mouvement (15,6 contre 16,9) ; la barre qui tourne et le disque camouflé restent faux.
3. **Coupe (i=119) : RIFE invente une image hybride** des deux plans (fond mélangé, carré rouge dédoublé, disque fantôme) : flash visible, 20-21 dB. C'est le même piège que `mci:scd=none` : **toujours interpoler plan par plan** (ou activer la détection de coupe du script officiel).
4. **Coût** : 3 à 20 fois plus lent que mci en CPU sur 320×180 ; le temps croît avec la surface (≈ 30× plus de pixels en 1080p : prévoir des minutes par seconde de film sans GPU).

## Conclusion pour un monteur
- Pour un **ralenti de plan filmé net** (sujet qui bouge sur fond lisible), RIFE est clairement le meilleur outil libre testé : à préférer à `minterpolate`, et c'est la famille de Resolve « Speed Warp » / Topaz.
- Sur **feuillage, eau, foule, grain fort, objets fins en rotation**, il ne sauve rien : assumer duplication ou fondu (voir `README.md`).
- **Couper avant d'interpoler**, vérifier l'image autour de chaque raccord, garder une poignée en fin de plan.
- Installation légère (≈ 800 Mo, < 2 min) ; licences MIT code et poids : utilisable en production. En pratique, préférer une intégration prête (rife-ncnn-vulkan, vs-rife, Flowframes) à un script maison.
