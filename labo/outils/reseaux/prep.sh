#!/bin/zsh
# prep.sh SRC NOM : proxy, sons, coupes image par image, demucs, whisper, loudness
R="/Volumes/SSD FAST/Montage-IA"; SRC="$1"; N="$2"; D="$R/videos/_travail/reseaux/$N"
mkdir -p "$D"; cd "$D"
ffmpeg -v error -y -i "$SRC" -vf "scale='if(gt(iw,ih),640,-2)':'if(gt(iw,ih),-2,640)',format=yuv420p" -c:v libx264 -crf 16 -preset fast -c:a aac -b:a 192k proxy.mp4
ffmpeg -v error -y -i "$SRC" -vn -ac 2 -ar 44100 audio.wav
ffmpeg -v error -y -i "$SRC" -vn -ac 1 -ar 16000 audio16k.wav
"$R/.venv/bin/scenedetect" -q -i proxy.mp4 -m 1 -o . detect-adaptive list-scenes -f scenes_adapt >/dev/null 2>&1
"$R/.venv/bin/scenedetect" -q -i proxy.mp4 -m 1 -o . detect-content -t 22 list-scenes -f scenes_content >/dev/null 2>&1
"$R/.venv/bin/python" -I -c "
import csv,json
def lire(f):
    rows=list(csv.reader(open(f)))[2:]
    return [float(r[3]) for r in rows[1:]]
a=lire('scenes_adapt.csv'); c=lire('scenes_content.csv')
json.dump({'coupes':a},open('coupes.json','w')); json.dump({'coupes':c},open('coupes_content.json','w'))
print('$N adapt',len(a),'content',len(c))
"
ffmpeg -nostats -i audio.wav -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|LRA:|Peak:" | tr -s ' ' | tr '\n' ' ' > loudness.txt; echo >> loudness.txt
"$R/.venv/bin/python" -I -m demucs --two-stems vocals -o sep audio.wav >/dev/null 2>&1
whisper-cli -m ~/.cache/whisper-cpp/ggml-large-v3-turbo.bin -l auto -osrt -mc 0 -of transcript -f audio16k.wav >/dev/null 2>&1
echo "$N fini"; cat loudness.txt
