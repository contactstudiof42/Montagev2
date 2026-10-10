#!/bin/sh
# Pièce 12 : trois plans fixes + grain vivant + air de pièce. Usage : montage.sh L1.png F.png L2.png d1 d2 d3 sortie.mp4
L1=$1; F=$2; L2=$3; D1=$4; D2=$5; D3=$6; OUT=$7
T=$(python3 -c "print($D1+$D2+$D3)")
ffmpeg -loglevel error -y -loop 1 -t $D1 -i $L1 -loop 1 -t $D2 -i $F -loop 1 -t $D3 -i $L2 \
  -f lavfi -t $T -i "anoisesrc=color=pink:amplitude=0.02:seed=5" \
  -filter_complex "[0][1][2]concat=n=3:v=1:a=0,fps=25,noise=alls=7:allf=t,format=yuv420p[v];[3]lowpass=f=900,volume=${GAIN:-12}dB[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 20 -c:a aac -b:a 128k $OUT
