#!/bin/sh
# Vérité terrain à partir d'un plan filmé : N images natives consécutives, 320x180, FFV1, retaguées à 30 i/s ;
# source = une image sur deux (15 i/s). Usage : fabrique-reel.sh <video> <debut_s> <dossier> [nb_images=120]
V=$1; T=$2; R=$3; N=${4:-120}; mkdir -p $R
ffmpeg -y -v error -ss $T -i "$V" -vf "scale=320:180:flags=area,setpts=N/30/TB" -frames:v $N -r 30 -an -c:v ffv1 -pix_fmt yuv444p $R/verite.mkv
ffmpeg -y -v error -i $R/verite.mkv -vf "select=not(mod(n\,2)),setpts=N/15/TB" -r 15 -c:v ffv1 -pix_fmt yuv444p $R/source.mkv
echo "$R : verite $(ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of csv=p=0 $R/verite.mkv) img, source $(ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of csv=p=0 $R/source.mkv) img"
