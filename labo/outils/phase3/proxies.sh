#!/bin/zsh
# Proxy 360x640 (rushes verticaux : rotation 90 appliquée par ffmpeg) 25p converti S-Log3 -> 709 (LUT Sony LC-709 TypeA) + audio 16 kHz mono, depuis un rush en lecture seule.
# Usage : proxies.sh RUSH.MP4 (lancé depuis _travail/, qui contient slog3_709A.cube)
f=$1; n=${${f:t:r}#20260929_}
[[ -s proxy/$n.mp4 ]] || ffmpeg -v error -y -hwaccel videotoolbox -i "$f" -vf "fps=25,scale=640:640:force_original_aspect_ratio=decrease:force_divisible_by=2,lut3d=slog3_709A.cube" -c:v h264_videotoolbox -b:v 1500k -c:a aac -ac 1 -b:a 96k proxy/$n.mp4
[[ -s a16k/$n.wav ]] || ffmpeg -v error -y -i "$f" -vn -ac 1 -ar 16000 a16k/$n.wav
