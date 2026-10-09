# Labo livraison vidéo : résultats (2026-10-09)

Environnement : ffmpeg 6.1.1 (libx264, encodeur AAC natif), CPU seulement.
Script : `labo_livraison.sh`. Rendus dans `labo/rendus/livraison/`.
Durée totale : 1 min 29 s (temps réel) pour 10 s de vidéo.

## Commandes qui marchent [TESTÉ EN LABO]

### Source test (ProRes 422 HQ 10 bits + PCM 24 bits, tags BT.709), 24 s
```bash
ffmpeg -f lavfi -i "testsrc2=size=1920x1080:rate=25:duration=10" -f lavfi -i "sine=frequency=440:sample_rate=48000:duration=10" \
  -filter_complex "[1:a]volume=-12dB,aformat=channel_layouts=stereo[a]" -map 0:v -map "[a]" \
  -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -c:a pcm_s24le source_1080p25.mov
```

### Master web 16:9 en CRF, 18 s
```bash
ffmpeg -i source.mov -vf "scale=1920:1080:flags=lanczos,format=yuv420p" \
  -c:v libx264 -preset slow -crf 18 -profile:v high -level:v 4.1 -g 50 -bf 2 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000" -c:a aac -b:a 320k -ar 48000 -ac 2 \
  -movflags +faststart master_web_1080p.mp4
```
(Ici le loudnorm d'une seule passe suffit car la source est un sinus stable. Sur un vrai mix, normaliser l'audio à part, voir `labo/loudness/`.)

### Débit cible en 2 passes (8 Mb/s, maxrate 10M, bufsize 16M), 4 s + 11 s
```bash
ffmpeg -y -i source.mov -vf format=yuv420p -c:v libx264 -preset medium -b:v 8M -maxrate 10M -bufsize 16M -profile:v high -pass 1 -an -f null /dev/null
ffmpeg -i source.mov -vf format=yuv420p -c:v libx264 -preset medium -b:v 8M -maxrate 10M -bufsize 16M -profile:v high -pass 2 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -c:a aac -b:a 256k -ar 48000 -movflags +faststart master_web_8M.mp4
```

### Vertical 1080x1920, recadrage au centre, 13 s
```bash
-vf "crop=ih*9/16:ih,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p" -c:v libx264 -crf 19 -profile:v high -level:v 4.2 ...
```

### Vertical 1080x1920, fond flou + image 16:9 au centre, 14 s
```bash
-filter_complex "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2[bg];[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[v]"
```

## Vérification ffprobe (sorties réelles)

| Fichier | Profil / niveau | pix_fmt | Tags couleur (range/space/trc/prim) | Débit vidéo | Audio | faststart | Loudness |
|---|---|---|---|---|---|---|---|
| master_web_1080p.mp4 (CRF 18) | High / 4.1 | yuv420p | tv / bt709 / bt709 / bt709 | 8.33 Mb/s | AAC 48 kHz 2 canaux, 231 kb/s | moov avant mdat, OK | -14.0 LUFS, TP -13.1 |
| master_web_8M.mp4 (2 passes) | High / 4.0 | yuv420p | idem | 7.90 Mb/s (cible 8) | AAC 48k, 183 kb/s | OK | -33.8 LUFS (non normalisé, voulu) |
| vertical_crop_1080x1920.mp4 | High / 4.2 | yuv420p | idem | 3.49 Mb/s | AAC 48k, 240 kb/s | OK | -14.0 LUFS |
| vertical_flou_1080x1920.mp4 | High / 4.2 | yuv420p | idem | 2.53 Mb/s | AAC 48k, 183 kb/s | OK | -33.8 LUFS (non normalisé) |

Commandes de vérification :
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,level,width,height,pix_fmt,sample_aspect_ratio,r_frame_rate,color_range,color_space,color_transfer,color_primaries,bit_rate -of default=nw=1 F.mp4
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels,bit_rate -of default=nw=1 F.mp4
ffprobe -v error -show_entries format=bit_rate,duration -of default=nw=1 F.mp4
```
Le faststart se vérifie en lisant l'ordre des atomes MP4 (script Python intégré à `labo_livraison.sh`). On obtient `ftyp moov free mdat`.

## Observations, pièges

- **Les tags couleur sont à écrire explicitement.** ffmpeg ne les déduit pas d'une source testsrc. Sans `-color_primaries/-color_trc/-colorspace`, ffprobe affiche `unknown`, et certains lecteurs ou plateformes interprètent alors mal les couleurs (décalage gamma, rendu « délavé » sur Mac/QuickTime). Ce test n'a pas comparé l'affichage réel : c'est à faire en phase 2.
- **Le débit AAC demandé n'est pas le débit obtenu.** On a demandé 320k et 256k, ffprobe indique 231k et 183k. L'encodeur AAC natif consomme moins sur un sinus pur. Ce n'est pas un défaut, mais il ne faut pas « vérifier » le débit audio sur une mire.
- Le CRF 18 sur testsrc2 (mire très détaillée et animée) donne environ 8.3 Mb/s. Sur des images réelles, le débit varie beaucoup : le CRF garantit une qualité et non une taille.
- Le 2 passes `-b:v 8M` atterrit à 7.90 Mb/s, soit -1.2 %, ce qui est conforme.
- `-level` doit être compatible avec la résolution et le débit : 4.1 pour du 1080p25, 4.2 pour du 1080x1920 en vertical (x264 a choisi le niveau indiqué sans erreur).
- `setsar=1` est indispensable après un crop ou un scale, sinon le SAR hérité peut déformer l'image sur la plateforme (ici SAR = 1:1, vérifié).
- La source ProRes HQ 1080p de 10 s pèse 84 Mo : en labo, on garde des sources courtes.
