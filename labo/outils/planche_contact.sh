#!/bin/bash
# Planche contact avec grille à partir d'un dossier d'images (ffmpeg requis, sans drawtext).
# Usage : planche_contact.sh <dossier_images> <dossier_sortie> [colonnes=6] [lignes=2] [largeur_vignette=216] [hauteur_vignette=384]
# Ajoute une grille jaune tous les 10 % de la hauteur pour aider à choisir le cadrage.
# Affiche l'ordre des images : case 1 = en haut à gauche, lecture ligne par ligne.
set -e
IN="$1"; OUT="$2"; C="${3:-6}"; R="${4:-2}"; W="${5:-216}"; H="${6:-384}"
mkdir -p "$OUT/vignettes"
files=( $(cd "$IN" && ls *.jpg *.png 2>/dev/null | sort) )
for f in "${files[@]}"; do
  ffmpeg -nostdin -loglevel error -y -i "$IN/$f" \
    -vf "scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2,drawgrid=w=iw:h=ih/10:t=1:c=yellow@0.6" \
    "$OUT/vignettes/${f%.*}.jpg"
done
N=$((C*R)); i=0; g=0
while [ $i -lt ${#files[@]} ]; do
  ffmpeg -nostdin -loglevel error -y -framerate 1 -start_number 0 \
    -pattern_type glob -i "$OUT/vignettes/*.jpg" -vf "select='between(n\,$i\,$((i+N-1)))',tile=${C}x${R}" \
    -frames:v 1 "$OUT/planche_$g.jpg"
  echo "planche_$g.jpg :"; printf '  %s\n' "${files[@]:$i:$N}"
  i=$((i+N)); g=$((g+1))
done
