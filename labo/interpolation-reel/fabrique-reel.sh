#!/bin/sh
# Vérité terrain à partir d'un plan filmé : N images natives consécutives, 320x180, FFV1, retaguées à 30 i/s ;
# source = une image sur K (défaut 2 : 15 i/s ; K=4 : 7,5 i/s, variable d'env. K). Usage : fabrique-reel.sh <video> <debut_s> <dossier> [nb_images=120] [pre_filtre, ex. decimate=cycle=5 pour retirer
# les doublons d'un 24 i/s gonflé en 30 i/s (1 image sur 5 répétée)]
V=$1; T=$2; R=$3; N=${4:-120}; P=${5:+$5,}; mkdir -p $R
ffmpeg -y -v error -ss $T -i "$V" -vf "${P}scale=320:180:flags=area,setpts=N/30/TB" -frames:v $N -r 30 -an -c:v ffv1 -pix_fmt yuv444p $R/verite.mkv
ffmpeg -y -v error -i $R/verite.mkv -vf "select=not(mod(n\,${K:-2})),setpts=N*${K:-2}/30/TB" -r 30/${K:-2} -c:v ffv1 -pix_fmt yuv444p $R/source.mkv
echo "$R : verite $(ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of csv=p=0 $R/verite.mkv) img, source $(ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of csv=p=0 $R/source.mkv) img"
