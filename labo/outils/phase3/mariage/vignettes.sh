#!/bin/zsh
# vignettes.sh CHEMIN_RUSH : images clés (une par GOP, ~0,96 s), 384x216, LUT S-Log3 -> 709, dans _travail/vignettes/<nom>/k_####.jpg
T="/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"; f="$1"; n=$(basename "$f" .MP4); O="$T/vignettes/$n"
[[ -f "$O/fini" ]] && exit 0
mkdir -p "$O"
ffmpeg -v quiet -y -skip_frame nokey -hwaccel videotoolbox -i "$f" -vf "scale=384:216,format=yuv444p10le,lut3d=$T/lut/SL3SG3Ctos709.cube" -fps_mode passthrough -q:v 4 "$O/k_%04d.jpg" && \
ffprobe -v quiet -select_streams v -skip_frame nokey -show_entries frame=pts_time -of default=nw=1:nk=1 "$f" | grep . | sort -n > "$O/temps.txt" && touch "$O/fini"
