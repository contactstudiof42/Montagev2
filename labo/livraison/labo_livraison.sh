#!/usr/bin/env bash
# Labo livraison vidéo : source test 1920x1080 25p 10 s + audio, master H.264 web,
# version verticale 1080x1920, vérification ffprobe.
# Usage : bash labo_livraison.sh [dossier_rendus]
set -euo pipefail
R="${1:-$(dirname "$0")/../rendus/livraison}"
mkdir -p "$R"
FF="ffmpeg -hide_banner -nostdin -y -loglevel error"
t() { local d=$(date +%s.%N); "$@"; echo "  temps: $(echo "$(date +%s.%N) - $d" | bc) s"; }

echo "== 1. Source test (ProRes 422 HQ + PCM, tags BT.709) =="
t $FF -f lavfi -i "testsrc2=size=1920x1080:rate=25:duration=10" \
  -f lavfi -i "sine=frequency=440:sample_rate=48000:duration=10" \
  -filter_complex "[1:a]volume=-12dB,aformat=channel_layouts=stereo[a]" -map 0:v -map "[a]" \
  -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -c:a pcm_s24le "$R/source_1080p25.mov"

echo "== 2. Master web H.264 16:9 (CRF 18, High, yuv420p, faststart, AAC 48k) + loudnorm -14 =="
t $FF -i "$R/source_1080p25.mov" \
  -vf "scale=1920:1080:flags=lanczos,format=yuv420p" \
  -c:v libx264 -preset slow -crf 18 -profile:v high -level:v 4.1 \
  -g 50 -bf 2 -x264-params "keyint=50:min-keyint=25" \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000" \
  -c:a aac -b:a 320k -ar 48000 -ac 2 \
  -movflags +faststart "$R/master_web_1080p.mp4"

echo "== 3. Débit cible 2 passes (8 Mb/s, maxrate 10M) =="
t $FF -i "$R/source_1080p25.mov" -vf format=yuv420p -c:v libx264 -preset medium -b:v 8M -maxrate 10M -bufsize 16M \
  -profile:v high -pass 1 -passlogfile "$R/x264pass" -an -f null /dev/null
t $FF -i "$R/source_1080p25.mov" -vf format=yuv420p -c:v libx264 -preset medium -b:v 8M -maxrate 10M -bufsize 16M \
  -profile:v high -pass 2 -passlogfile "$R/x264pass" \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$R/master_web_8M.mp4"
rm -f "$R"/x264pass*

echo "== 4. Vertical 1080x1920 : recadrage centre (crop) =="
t $FF -i "$R/source_1080p25.mov" \
  -vf "crop=ih*9/16:ih,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p" \
  -c:v libx264 -preset slow -crf 19 -profile:v high -level:v 4.2 -g 50 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000" -c:a aac -b:a 256k -ar 48000 \
  -movflags +faststart "$R/vertical_crop_1080x1920.mp4"

echo "== 5. Vertical 1080x1920 : fond flou + 16:9 au centre =="
t $FF -i "$R/source_1080p25.mov" -filter_complex \
  "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2[bg];\
[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[v]" \
  -map "[v]" -map 0:a -c:v libx264 -preset slow -crf 19 -profile:v high -level:v 4.2 -g 50 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$R/vertical_flou_1080x1920.mp4"

echo "== 6. Vérifications ffprobe =="
for f in "$R"/master_web_1080p.mp4 "$R"/master_web_8M.mp4 "$R"/vertical_*.mp4; do
  echo "--- $(basename "$f")"
  ffprobe -v error -select_streams v:0 -show_entries \
    stream=codec_name,profile,level,width,height,pix_fmt,sample_aspect_ratio,r_frame_rate,color_range,color_space,color_transfer,color_primaries,bit_rate \
    -of default=nw=1 "$f" | tr '\n' ' '; echo
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels,bit_rate -of default=nw=1 "$f" | tr '\n' ' '; echo
  ffprobe -v error -show_entries format=bit_rate,duration -of default=nw=1 "$f" | tr '\n' ' '; echo
  # faststart : l'atome moov doit précéder mdat
  python3 - "$f" <<'PY'
import sys, struct
d = open(sys.argv[1], 'rb').read(1 << 20); i = 0; order = []
while i + 8 <= len(d):
    size, typ = struct.unpack('>I4s', d[i:i+8]); order.append(typ.decode('latin1'))
    if size == 1: size = struct.unpack('>Q', d[i+8:i+16])[0]
    if size < 8: break
    i += size
print('  atomes:', ' '.join(order), '-> faststart OK' if 'moov' in order and (('mdat' not in order) or order.index('moov') < order.index('mdat')) else '-> faststart ABSENT')
PY
  echo -n "  loudness: "; ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true:framelog=quiet -f null - 2>&1 \
    | awk '/Summary/{s=1} s&&/I:|Peak:/{printf "%s ", $0} END{print ""}' | tr -s ' '
done
