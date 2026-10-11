#!/bin/zsh
# QC d'un fichier livré (phase 2, session 6, après les projets Studio F42 : cinq fichiers sur cinq au-dessus de -1 dBTP).
# Usage : qc_livraison.sh FICHIER [cible_LUFS=-14]
# Mesure sur le fichier ENCODÉ : image (codec, taille, cadence, tags couleur), pistes son (nombre, canaux),
# loudness intégrée, LRA, true peak, crêtes décodées (au-dessus de 0 dBFS = saturation à la lecture),
# noir au début et à la fin (un petit logo sur noir compte comme du noir : regarder l'image). Signale ce qui sort des repères de montage-loudness-livraison.
F="$1"; CIBLE="${2:--14}"
[ -f "$F" ] || { echo "fichier introuvable : $F"; exit 1; }
echo "== $F"
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,color_primaries,color_transfer -of compact=p=0 "$F"
NA=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$F" | wc -l | tr -d ' ')
ffprobe -v error -select_streams a -show_entries stream=index,codec_name,channels,sample_rate -of compact=p=0 "$F"
[ "$NA" -gt 1 ] && echo "ATTENTION : $NA pistes son (la plupart des lecteurs ne jouent que la première)"
R=$(ffmpeg -nostats -hide_banner -i "$F" -map 0:a:0 -af ebur128=peak=true,astats=metadata=0 -f null - 2>&1)
I=$(echo "$R" | awk '/Integrated loudness/{f=1} f&&/I:/{print $2; exit}')
LRA=$(echo "$R" | awk '/Loudness range/{f=1} f&&/LRA:/{print $2; exit}')
TP=$(echo "$R" | awk '/True peak/{f=1} f&&/Peak:/{print $2; exit}')
SP=$(echo "$R" | awk '/Overall/{f=1} f&&/Peak level dB/{print $NF; exit}')
echo "loudness intégrée $I LUFS (cible $CIBLE) ; LRA $LRA LU ; true peak $TP dBTP ; crête décodée $SP dBFS"
awk -v i="$I" -v c="$CIBLE" 'BEGIN{d=i-c; if (d>1||d<-1) printf "ATTENTION : %+.1f LU par rapport à la cible\n", d}'
awk -v t="$TP" 'BEGIN{if (t>-1) printf "ATTENTION : true peak %s dBTP > -1 (limiteur à -1 dBTP)\n", t}'
awk -v s="$SP" 'BEGIN{if (s>0) printf "ATTENTION : crêtes décodées au-dessus de 0 dBFS (%s) : saturation à la lecture\n", s}'
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F")
ffmpeg -nostats -hide_banner -i "$F" -map 0:v:0 -vf "scale=320:-2,blackdetect=d=0.3:pix_th=0.10" -an -f null - 2>&1 | grep -o "black_start:[0-9.]* black_end:[0-9.]* black_duration:[0-9.]*" | \
  awk -v d="$D" '{split($1,a,":"); split($2,b,":"); split($3,c,":"); w=""; if (a[2]<0.05) w=" (début)"; if (b[2]>d-0.2) w=" (fin)"; print "noir " a[2] "-" b[2] " s (" c[2] " s)" w}'
