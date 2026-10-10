#!/bin/sh
# Montage aplati : 60 premières images de <A>/verite.mkv puis 60 premières de <B>/verite.mkv (coupe franche entre i=59 et i=60).
# Usage : coupe.sh <dossierA> <dossierB> <dossier_coupe>
A=$1; B=$2; R=$3; mkdir -p $R
ffmpeg -y -v error -i $A/verite.mkv -i $B/verite.mkv -filter_complex "[0]trim=end_frame=60,setpts=PTS-STARTPTS[a];[1]trim=end_frame=60,setpts=PTS-STARTPTS[b];[a][b]concat=n=2,setpts=N/30/TB" -r 30 -c:v ffv1 -pix_fmt yuv444p $R/verite.mkv
ffmpeg -y -v error -i $R/verite.mkv -vf "select=not(mod(n\,2)),setpts=N/15/TB" -r 15 -c:v ffv1 -pix_fmt yuv444p $R/source.mkv
