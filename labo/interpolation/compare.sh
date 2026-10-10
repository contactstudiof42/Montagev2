#!/bin/sh
# Interpole source30 -> 60 i/s par plusieurs méthodes et mesure le PSNR image par image contre verite60.
# Usage : compare.sh <dossier_rendus>
R=$1
run() { nom=$1; vf=$2
  t0=$(date +%s.%N); ffmpeg -y -v error -i $R/source30.mkv -vf "$vf" -c:v ffv1 -pix_fmt yuv444p $R/$nom.mkv
  echo "$nom $(echo "$(date +%s.%N) - $t0" | bc) s"
  ffmpeg -v error -i $R/$nom.mkv -i $R/verite60.mkv -lavfi "[0][1]psnr=stats_file=$R/$nom.psnr" -f null - ; }
run dup      "fps=60"
run blend    "minterpolate=fps=60:mi_mode=blend"
run mci      "minterpolate=fps=60:mi_mode=mci"
run mci_aobmc_bidir "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"
run mci_noscd "minterpolate=fps=60:mi_mode=mci:scd=none"
