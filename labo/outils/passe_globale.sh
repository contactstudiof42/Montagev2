#!/bin/zsh
# Passe globale d'un film (phase 2) : copie légère 480p, sous-titres, coupes, loudness, vignettes / 10 s.
# Usage : [HDR=1] passe_globale.sh FILM.mkv DOSSIER_SORTIE [index_piste_audio_VO=0] [index_sous-titre=-1]
# Tout part dans DOSSIER_SORTIE (sous videos/_travail/, jamais dans Git).
set -e
FILM="$1"; OUT="$2"; A="${3:-0}"; S="${4:--1}"
RACINE="${0:A:h}/../.."
mkdir -p "$OUT/vignettes"
t0=$(date +%s)
# 1. Copie légère (VideoToolbox) + son VO stéréo
# Source HDR (PQ / HLG) : HDR=1 → décodage et conversion en SDR BT.709 par VideoToolbox (scale_vt). Sans cela, l'image
# PQ lue comme du SDR est grise et délavée (le ffmpeg Homebrew n'a ni zscale ni libplacebo). Testé sur Whiplash (session 2).
if [ "${HDR:-0}" = 1 ]; then
  [ -f "$OUT/proxy.mp4" ] || ffmpeg -v error -y -hwaccel videotoolbox -hwaccel_output_format videotoolbox_vld -i "$FILM" \
    -map 0:v:0 -map 0:a:$A -vf "scale_vt=w=-2:h=480:color_matrix=bt709:color_primaries=bt709:color_transfer=bt709,hwdownload,format=p010le,format=yuv420p" \
    -c:v h264_videotoolbox -b:v 1200k -c:a aac -ac 2 -b:a 128k "$OUT/proxy.mp4"
else
  [ -f "$OUT/proxy.mp4" ] || ffmpeg -v error -y -i "$FILM" -map 0:v:0 -map 0:a:$A -vf "scale=-2:480" \
    -c:v h264_videotoolbox -b:v 1200k -c:a aac -ac 2 -b:a 128k "$OUT/proxy.mp4"
fi
echo "proxy: $(( $(date +%s)-t0 )) s"
# 2. Sous-titres
[ "$S" -ge 0 ] && ffmpeg -v error -y -i "$FILM" -map 0:s:$S "$OUT/sous-titres.srt" || true
# 3. Loudness : courbe court terme (S, 3 s) toutes les 100 ms + intégré
ffmpeg -nostats -hide_banner -i "$OUT/proxy.mp4" -map 0:a -af ebur128 -f null - 2> "$OUT/ebur128.log"
echo "loudness: $(( $(date +%s)-t0 )) s"
# 4. Vignettes toutes les 10 s
ffmpeg -v error -y -i "$OUT/proxy.mp4" -vf "fps=1/10,scale=192:-2" -q:v 4 "$OUT/vignettes/v%05d.jpg"
echo "vignettes: $(( $(date +%s)-t0 )) s"
# 5. Coupes (PySceneDetect adaptatif, réduit)
"$RACINE/.venv/bin/scenedetect" -i "$OUT/proxy.mp4" -o "$OUT" -d 2 detect-adaptive list-scenes -q
echo "coupes: $(( $(date +%s)-t0 )) s"
