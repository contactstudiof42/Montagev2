# Annexe : loudness et livraison (détails)

Complète `SKILL.md`. Tout ce qui est marqué [TESTÉ EN LABO] a été exécuté le 2026-10-09 avec ffmpeg 6.1.1 ; voir `labo/loudness/RESULTATS.md` et `labo/livraison/RESULTATS.md`.

## 1. Vocabulaire

- **LUFS / LKFS** : la même unité (ITU-R BS.1770, pondération K, gating). L'Europe dit LUFS, les États-Unis LKFS. 1 LU = 1 dB.
- **Intégré (I)** : loudness moyenne de tout le programme, avec deux gates : un absolu à -70 LUFS et un relatif à -10 LU (BS.1770-2 et suivantes). Les silences ne comptent donc pas.
- **Dialogue-gated** : on ne mesure que les passages de dialogue (algorithme Dolby, BS.1770-1). Utilisé par Netflix. ffmpeg ne sait pas le faire.
- **Short-term (S, 3 s) / Momentary (M, 400 ms)** : servent au mix et à surveiller les pics de sensation. Certaines chartes TV limitent le short-term maximal.
- **LRA (Loudness Range)** : étendue de dynamique perçue, du 10e au 95e percentile du short-term. Ordres de grandeur : pub 3 à 6 LU, magazine TV 5 à 10, fiction 10 à 20 et plus.
- **True peak (dBTP)** : crête reconstruite après sur-échantillonnage (×4 dans BS.1770), qui capte les crêtes entre échantillons. Elle est toujours ≥ au pic échantillon (dBFS).

## 2. Cibles détaillées et nuances

### Broadcast
- **EBU R128 (v5, novembre 2023)** : -23 LUFS ±0.5 LU (±1 LU si l'imprévisible l'impose, comme en direct), TP max -1 dBTP en production. Documents liés : Tech 3341 (compteur), 3342 (LRA), 3343 (guide de production), 3344 (distribution). R128 s1 couvre les spots courts (pubs, bandes-annonces) et s2 les plateformes de streaming.
- **France** : les chaînes appliquent R128 à travers leurs chartes PAD (prêt-à-diffuser). Ces chartes ajoutent souvent des limites de short-term pour les pubs ou un TP plus strict. **La charte du diffuseur prime toujours** : il faut la demander.
- **ATSC A/85 (USA)** : -24 LKFS. La loi CALM impose A/85 aux publicités. Une révision majeure a été publiée en juillet 2026 (annexe streaming, annexe « Loudness and True Peak Quick Reference ») : **ses valeurs exactes restent à vérifier dans le texte**. Le -2 dBTP couramment cité vient des cahiers des charges des diffuseurs, il n'a pas été confirmé dans A/85 lors de cette recherche.

### Streaming vidéo / SVOD
- **Netflix** : -27 LKFS mesuré sur le dialogue (BS.1770-1). La tolérance annoncée est de ±2 LU dans le guide Atmos ; la page QC parle de ±3 LU pour les mesures des partenaires QC. True peak -2 dBTP dans le guide (limiteurs à -2.3 conseillés sur les beds et les objets) ; la page QC indique -1 dB TP pour le print master et les stems M&E. Mesure Atmos sur un re-rendu 5.1. **Les specs varient d'un titre à l'autre : le document fourni pour le titre fait foi.**
- Autres SVOD (Amazon, Disney+, Apple TV+) : non recherché ici. On demande le cahier des charges.

### Plateformes de diffusion web et musique
- **Spotify** (officiel) : normalise à -14 LUFS (ITU 1770), avec les modes Loud -11 et Quiet -19 pour Premium. Il **remonte** aussi les titres faibles, mais sans dépasser leur marge de TP. Exemple Spotify : un titre à -20 LUFS avec un TP à -5 n'est remonté qu'à -16. Un limiteur intervient seulement en mode Loud. Les albums sont normalisés d'un bloc. TP conseillé < -1 dBTP, < -2 dBTP si le master est plus fort que -14.
- **YouTube** (non officiel) : environ -14 LUFS, **uniquement à la baisse**. Clic droit sur la vidéo, « Statistiques pour les geeks », ligne « content loudness » : une valeur positive indique de combien de dB la vidéo est baissée ; une valeur négative indique qu'elle n'est pas remontée. YouTube Music peut se comporter autrement.
- **Apple Music** (non officiel) : Sound Check autour de -16 LUFS.
- **Instagram, TikTok** (non confirmé) : aucune documentation officielle trouvée. Les guides tiers donnent -14, voire -10 à -12. Approche prudente : -14 LUFS / -1.5 dBTP et un mix lisible sur un haut-parleur de téléphone (voix devant, peu de graves).
- **Podcasts** : -16 LUFS est l'usage courant (Apple Podcasts le recommandait). Non revérifié aujourd'hui.

### Cinéma
- Pas de cible LUFS normative. Le mix se fait dans une salle étalonnée (référence 85 dB SPL par canal pour -20 dBFS de bruit rose, dans la pratique Dolby/SMPTE) et le niveau dépend du réglage du lecteur de la salle. Pour les bandes-annonces et les pubs cinéma, il existe des limites en Leq(m) (par exemple TASA, SAWA). **[THÉORIQUE]**, non recherché en détail : à documenter si un projet cinéma arrive.

## 3. Recettes complémentaires

### Vertical 1080x1920 [TESTÉ EN LABO]
Recadrage au centre (perte des côtés, recadrer à la main si le sujet n'est pas au centre) :
```bash
ffmpeg -i MASTER.mov -vf "crop=ih*9/16:ih,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p" \
  -c:v libx264 -preset slow -crf 19 -profile:v high -level:v 4.2 -g 50 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart OUT_9x16.mp4
```
Fond flou + image 16:9 au centre :
```bash
-filter_complex "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2[bg];[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[v]" -map "[v]" -map 0:a
```
Pour un décalage du recadrage : `crop=ih*9/16:ih:X:0`, où X est le bord gauche en pixels.

### Débit cible en 2 passes [TESTÉ EN LABO]
```bash
ffmpeg -y -i IN -vf format=yuv420p -c:v libx264 -preset medium -b:v 8M -maxrate 10M -bufsize 16M -profile:v high -pass 1 -an -f null /dev/null
ffmpeg -i IN -vf format=yuv420p -c:v libx264 -preset medium -b:v 8M -maxrate 10M -bufsize 16M -profile:v high -pass 2 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -c:a aac -b:a 256k -ar 48000 -movflags +faststart OUT.mp4
```

### Vérifier le faststart [TESTÉ EN LABO]
L'atome `moov` doit précéder `mdat`. Le script `labo/livraison/labo_livraison.sh` lit les en-têtes MP4 en Python. Alternative [THÉORIQUE] : `ffprobe -v trace IN.mp4 2>&1 | grep -m3 -E "type:'(moov|mdat)'"`.

### Mesurer un stem seul, ou seulement une plage [THÉORIQUE]
```bash
ffmpeg -ss 00:01:00 -t 30 -i IN -map 0:a:1 -af ebur128=peak=true -f null -
```

### Master TV en 5.1 [THÉORIQUE]
Mesurer le 5.1 tel quel : ebur128 applique la pondération BS.1770 (LFE exclu, surrounds à +1.5 dB). Ne pas mesurer un downmix à la place.

### Normalisation d'un dossier de fichiers [THÉORIQUE]
Le script `labo/loudness/labo_loudness.py` contient des fonctions réutilisables (`mesure_ebur128`, `deux_passes`, `gain_lineaire`) qu'on peut appeler en boucle.

## 4. Valeurs de spec vidéo courantes pour le web (usage, non normatif)

| Usage | Résolution | Cadence | Codec / profil | Débit indicatif | Audio |
|---|---|---|---|---|---|
| YouTube 1080p SDR | 1920x1080 | celle de la source | H.264 High, yuv420p | 8 Mb/s (24-30p), 12 Mb/s (48-60p) d'après les recommandations publiques de YouTube, non revérifiées ce jour | AAC-LC 48 kHz stéréo, ≥ 128 kb/s (on met 320) |
| Réseaux, vertical | 1080x1920 | 25 ou 30 | H.264 High | 6 à 10 Mb/s | AAC 48 kHz |
| Master d'archive | natif | natif | ProRes 422 HQ ou DNxHR HQX | — | PCM 24 bits 48 kHz |

## 5. Lecture du JSON loudnorm

`input_i`, `input_tp`, `input_lra` et `input_thresh` décrivent la source. `target_offset` est l'écart que loudnorm prévoit après son traitement. `normalization_type` indique `linear` ou `dynamic`. Les `output_*` sont l'estimation de loudnorm, à confirmer par une re-mesure ebur128.
