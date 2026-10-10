#!/bin/sh
# planche.sh VIDEO OUT.png : 12 images à intervalle régulier (grille 4×3, 240 px de large) + médiane de luminance
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1")
ffmpeg -v error -y -i "$1" -vf "fps=12/$d,scale=240:-1,tile=4x3" -frames:v 1 "$2"
ffmpeg -v error -i "$1" -vf "fps=2,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-" -f null - | grep -o 'YAVG=[0-9.]*' | cut -d= -f2 | sort -n | awk '{a[NR]=$1} END{print "YAVG médiane (plage limitée 16-235):", a[int(NR/2)+1]}'
