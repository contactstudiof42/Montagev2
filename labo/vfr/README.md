# Labo VFR (cadence variable des téléphones) — session 8, 2026-10-10

- `fabrique_vfr.py <dossier>` : faux rush VFR à vérité terrain (270 images sur 10 s ; 30 i/s, puis 3-8 s entre 1/30 et 1/20 s avec gigue, puis 30 i/s ; flash sur l'image horodatée 5,004 s, clic audio à 5,000 s). Astuce : concat demuxer avec `duration` par image **et** `option framerate 90000` (sinon les horodatages sont arrondis au 1/25 s du démultiplexeur image) et `-safe 0`.
- `mesure_vfr.py fichiers…` : cadence nominale et moyenne, intervalles min/max, instant du flash (image la plus claire via `signalstats`), instant du clic, décalage, images identiques consécutives (approximation par YAVG égal).
- Résultats (`mesures.jsonl`) :

| fichier | conversion | images | décalage flash/clic | doublons |
|---|---|---|---|---|
| vfr.mp4 | source | 271 | +3,9 ms (vérité +4) | — |
| A_cfr30 | `-fps_mode cfr -r 30` | 301 | 0 | 25 |
| B_fps25 | `-vf fps=25` | 251 | 0 | 11 |
| C_naif30 | `setpts=N/30/TB` (lecture à la cadence nominale) | 271 | **−400 ms** | 1 |
| D_prores30 | `fps=30` → ProRes 422 LT + PCM | 301 | 0 | 37 |
| E_blend30 | `minterpolate=fps=30:mi_mode=blend` | 300 | 0 | 2 (images fondues) |

- Erreur rencontrée : `-r` avec `-fps_mode passthrough` est refusé par ffmpeg 6.1 (« contradictory »).
- Limites : un seul rush synthétique ; le comportement des logiciels de montage n'est pas testé ici (phase 2).
