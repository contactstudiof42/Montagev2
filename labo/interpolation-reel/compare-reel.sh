#!/bin/sh
# 15 -> 30 i/s par plusieurs méthodes ffmpeg ; temps de calcul ; PSNR image par image contre verite.mkv.
# Usage : compare-reel.sh <dossier>   (écrit <nom>.mkv, <nom>.psnr, temps.txt)
R=$1; : > $R/temps.txt
run() { nom=$1; vf=$2
  t0=$(date +%s.%N); ffmpeg -y -v error -i $R/source.mkv -vf "$vf" -c:v ffv1 -pix_fmt yuv444p $R/$nom.mkv
  echo "$nom $(echo "$(date +%s.%N) - $t0" | bc) s" | tee -a $R/temps.txt
  ffmpeg -v error -i $R/$nom.mkv -i $R/verite.mkv -lavfi "[0][1]psnr=stats_file=$R/$nom.psnr" -f null - ; }
run dup       "fps=30"
run blend     "minterpolate=fps=30:mi_mode=blend"
run mci       "minterpolate=fps=30:mi_mode=mci"
run mci_noscd "minterpolate=fps=30:mi_mode=mci:scd=none"
