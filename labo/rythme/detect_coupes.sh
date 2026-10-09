#!/usr/bin/env bash
# Test : fabrique un montage synthétique aux durées connues, puis retrouve les coupes avec scdet.
# Usage : ./detect_coupes.sh [dossier_sortie]
set -euo pipefail
OUT=${1:-../rendus/rythme}; mkdir -p "$OUT"
# durées (images à 25 i/s) : rythme « montée puis respiration »
DUR=(50 40 30 20 12 8 8 6 75)
SRC=(testsrc2 mandelbrot smptebars rgbtestsrc testsrc2 mandelbrot smptebars rgbtestsrc testsrc2)
HUE=(0 0 0 0 90 0 0 0 200)
L=""; i=0
for d in "${DUR[@]}"; do
  ffmpeg -loglevel error -y -f lavfi -i "${SRC[$i]}=s=320x180:r=25" -frames:v $d -vf "hue=h=${HUE[$i]}" -pix_fmt yuv420p "$OUT/p$i.mp4"
  L+="file 'p$i.mp4'"$'\n'; i=$((i+1))
done
printf "%s" "$L" > "$OUT/liste.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$OUT/liste.txt" -c copy "$OUT/montage.mp4"
# coupes attendues (en secondes)
acc=0; echo -n "attendu : "; for d in "${DUR[@]::${#DUR[@]}-1}"; do acc=$((acc+d)); printf "%.2f " $(echo "$acc/25" | bc -l); done; echo
echo -n "scdet   : "
ffmpeg -hide_banner -i "$OUT/montage.mp4" -vf "scdet=threshold=10,metadata=print:key=lavfi.scd.time:file=-" -f null - 2>/dev/null \
  | grep -o "lavfi.scd.time=[0-9.]*" | cut -d= -f2 | tr '\n' ' '; echo
