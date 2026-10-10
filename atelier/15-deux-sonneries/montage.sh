#!/bin/sh
# Pièce 15 : monte A, B, C, D à partir des images à 75 i/s (dossier $1) ; sortie dans $2.
# A : 3 sonneries + décroché réel ; B : 5 sonneries + réel ; C : 3 + ralenti x3 interpolé (mci) depuis 25 i/s ; D : 3 + ralenti x3 vrai.
F=$1; O=$2; mkdir -p $O/s25
i=0; for k in $(seq 0 3 119); do cp $F/f$(printf %04d $k).png $O/s25/f$(printf %04d $i).png; i=$((i+1)); done
ffmpeg -loglevel error -y -framerate 25 -i $O/s25/f%04d.png -c:v ffv1 $O/reel25.mkv
ffmpeg -loglevel error -y -i $O/reel25.mkv -vf "minterpolate=fps=75:mi_mode=mci,setpts=3*PTS,fps=25" -c:v ffv1 $O/ralenti_interp.mkv
ffmpeg -loglevel error -y -framerate 25 -i $F/f%04d.png -c:v ffv1 $O/ralenti_vrai.mkv
# sonnerie : timbre de cloche (sinus 880 + 1320, trille 20 Hz), 1,2 s de son / 1,8 s de silence
sonne() { # $1 = nombre de sonneries, $2 = durée totale
  ffmpeg -loglevel error -y -f lavfi -i "aevalsrc='(0.5*sin(2*PI*880*t)+0.3*sin(2*PI*1320*t))*(0.5+0.5*sin(2*PI*20*t))*lt(mod(t-0.5\,3)\,1.2)*gte(t\,0.5)*lt(t\,0.5+3*$1)*0.4':s=48000:d=$2" -ac 2 $O/sonne$1.wav; }
for v in A B C D; do
  case $v in A|C|D) N=3;; B) N=5;; esac
  H=$(python3 -c "print(0.5+3*$N-0.6)")
  case $v in A|B) L=$O/reel25.mkv; LD=1.6;; C) L=$O/ralenti_interp.mkv; LD=4.8;; D) L=$O/ralenti_vrai.mkv; LD=4.8;; esac
  T=$(python3 -c "print($H+$LD+1.5)")
  sonne $N $T
  ffmpeg -loglevel error -y -loop 1 -t $H -framerate 25 -i $F/f0000.png -i $L -i $O/sonne$N.wav \
    -f lavfi -t $T -i "anoisesrc=color=brown:amplitude=0.01:seed=3" \
    -filter_complex "[0]fps=25,format=yuv420p[a];[1]fps=25,format=yuv420p,tpad=stop_mode=clone:stop_duration=1.5[b];[a][b]concat=n=2:v=1:a=0,noise=alls=5:allf=t[v];[2][3]amix=inputs=2:normalize=0[s]" \
    -map "[v]" -map "[s]" -c:v libx264 -crf 20 -c:a aac -b:a 128k -t $T $O/$v.mp4
  echo "$v : tenue $H s, décroché $LD s, total $T s"
done
