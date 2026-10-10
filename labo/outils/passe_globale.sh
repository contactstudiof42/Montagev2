#!/bin/zsh
# Passe globale d'un film (phase 2) : copie légère 480p, sous-titres, coupes, loudness, vignettes / 10 s.
# Usage : passe_globale.sh FILM.mkv DOSSIER_SORTIE [index_piste_audio_VO=0] [index_sous-titre=-1]
# Tout part dans DOSSIER_SORTIE (sous videos/_travail/, jamais dans Git).
set -e
FILM="$1"; OUT="$2"; A="${3:-0}"; S="${4:--1}"
RACINE="${0:A:h}/../.."
mkdir -p "$OUT/vignettes"
t0=$(date +%s)
# 1. Copie légère (VideoToolbox) + son VO stéréo
[ -f "$OUT/proxy.mp4" ] || ffmpeg -v error -y -i "$FILM" -map 0:v:0 -map 0:a:$A -vf "scale=-2:480" \
  -c:v h264_videotoolbox -b:v 1200k -c:a aac -ac 2 -b:a 128k "$OUT/proxy.mp4"
echo "proxy: $(( $(date +%s)-t0 )) s"
# 2. Sous-titres
[ "$S" -ge 0 ] && ffmpeg -v error -y -i "$FILM" -map 0:s:$S "$OUT/sous-titres.srt" || true
# 3. Loudness : courbe court terme (S, 3 s) toutes les 100 ms + intégré
ffmpeg -nostats -hide_banner -i "$OUT/proxy.mp4" -map 0:a -af ebur128=framelog=verbose -f null - 2> "$OUT/ebur128.log"
echo "loudness: $(( $(date +%s)-t0 )) s"
# 4. Vignettes toutes les 10 s
ffmpeg -v error -y -i "$OUT/proxy.mp4" -vf "fps=1/10,scale=192:-2" -q:v 4 "$OUT/vignettes/v%05d.jpg"
echo "vignettes: $(( $(date +%s)-t0 )) s"
# 5. Coupes (PySceneDetect adaptatif, réduit)
"$RACINE/.venv/bin/scenedetect" -i "$OUT/proxy.mp4" -o "$OUT" -d 2 detect-adaptive list-scenes -q
echo "coupes: $(( $(date +%s)-t0 )) s"
