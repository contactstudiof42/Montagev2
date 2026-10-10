#!/bin/sh
# B2 : 3 sonneries téléphone seul, la main entre (0,5 s réelle) et se pose ; elle reste posée 2 sonneries ; puis décroche (réel).
F=$1; O=$2
mkdir -p $O/arrivee $O/levee
i=0; for k in $(seq 0 3 41); do cp $F/f$(printf %04d $k).png $O/arrivee/f$(printf %04d $i).png; i=$((i+1)); done
i=0; for k in $(seq 42 3 119); do cp $F/f$(printf %04d $k).png $O/levee/f$(printf %04d $i).png; i=$((i+1)); done
T=$(python3 -c "print(0.5+3*5-0.6+1.6+1.5)")
ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='(0.5*sin(2*PI*880*t)+0.3*sin(2*PI*1320*t))*(0.5+0.5*sin(2*PI*20*t))*lt(mod(t-0.5\,3)\,1.2)*gte(t\,0.5)*lt(t\,15.5)*0.4':s=48000:d=$T" -ac 2 $O/sonneB2.wav
# tenue téléphone seul jusqu'à 8,9 s ; arrivée de la main 0,56 s ; main posée jusqu'à 14,9 s ; levée ; 1,5 s de fin
ffmpeg -loglevel error -y -loop 1 -t 8.9 -framerate 25 -i $F/f0000.png -framerate 25 -i $O/arrivee/f%04d.png \
  -loop 1 -t 5.44 -framerate 25 -i $F/f0041.png -framerate 25 -i $O/levee/f%04d.png -i $O/sonneB2.wav \
  -f lavfi -t $T -i "anoisesrc=color=brown:amplitude=0.01:seed=3" \
  -filter_complex "[0]fps=25,format=yuv420p[a];[1]fps=25,format=yuv420p[b];[2]fps=25,format=yuv420p[c];[3]fps=25,format=yuv420p,tpad=stop_mode=clone:stop_duration=1.5[d];[a][b][c][d]concat=n=4:v=1:a=0,noise=alls=5:allf=t[v];[4][5]amix=inputs=2:normalize=0[s]" \
  -map "[v]" -map "[s]" -c:v libx264 -crf 20 -c:a aac -b:a 128k -t $T $O/B2.mp4
