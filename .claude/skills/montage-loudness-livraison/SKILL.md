---
name: montage-loudness-livraison
description: À utiliser au mixage final et à l'export, dès qu'il faut « caler le son », « mettre aux normes », viser des LUFS/LKFS, respecter l'EBU R128 (-23), l'ATSC A/85 (-24), un true peak (dBTP), un LRA, ou livrer un master pour YouTube, Instagram, Reels, TikTok, Spotify, la TV, Netflix ou le cinéma. Couvre les specs de livraison (H.264, yuv420p, faststart, AAC 48 kHz, vertical 9:16, tags couleur BT.709), la normalisation loudnorm en deux passes et la vérification avec ffmpeg/ffprobe. Mots-clés : son trop fort ou trop faible, la plateforme baisse mon son, PAD, prêt-à-diffuser, QC, export final, livrable.
---

# Loudness et livraison

Annexe détaillée : [references.md](references.md). Preuves du labo : `labo/loudness/RESULTATS.md` et `labo/livraison/RESULTATS.md`. Sources datées : `sources/loudness-livraison.md`.

## 1. Quand s'en servir

- À la **fin** du mix, quand l'équilibre dialogue/musique/effets est validé à l'oreille. La norme corrige un niveau global, elle ne remplace pas un mix.
- Avant chaque export de livrable (web, réseaux, TV, plateforme), et à chaque fois qu'un client dit « c'est moins fort que les autres vidéos ».
- Au QC d'un fichier reçu : on mesure avant de juger.

## 2. Pourquoi : ce qui compte artistiquement

- **Le loudness n'est pas le volume de la musique.** Un nombre en LUFS est la moyenne pondérée d'un programme entier. Deux films à -23 LUFS peuvent avoir un dialogue de niveau très différent si l'un a 10 minutes d'explosions.
- **Les plateformes normalisent.** YouTube, Spotify et les autres baissent ce qui est trop fort (et Spotify remonte ce qui est trop faible). Une pub écrasée par un limiteur pour sonner à -9 LUFS sera ramenée vers -14 : elle ne sera pas plus forte que le reste, mais **plus plate**. Elle aura perdu ses transitoires, son impact et son contraste, sans rien gagner en échange.
- **La dynamique sert l'émotion.** Le silence avant le coup, la musique qui monte, le chuchotement sont des écarts de niveau. Un LRA de 6 à 12 LU pour un documentaire ou une fiction web, et plus encore pour le cinéma, laisse respirer le récit. Ne compressez pas pour atteindre un chiffre.
- **Le dialogue est l'ancre.** On cale d'abord la voix à un niveau stable et intelligible, puis on place la musique et les effets autour. Netflix mesure d'ailleurs le loudness *sur le dialogue seulement* (dialogue-gated) : l'action peut monter sans que le dialogue soit écrasé.
- **Le true peak protège la diffusion.** Les codecs avec perte (AAC, Opus, Vorbis) recréent des crêtes entre les échantillons. Un fichier à -0.1 dBFS « propre » peut saturer une fois encodé. On laisse donc de la marge (-1 à -2 dBTP).
- **Un seul mix ne sert pas toutes les sorties.** Un master TV R128 (-23) mis en ligne tel quel n'est pas « faux » : YouTube ne le remonte pas, il paraîtra simplement plus faible que les autres vidéos. Pour les réseaux sociaux, on fait une déclinaison plus dense, mais pas écrasée.

## 3. Cibles (vérifiées le 2026-10-09)

| Destination | Intégré | True peak max | Statut de l'information |
|---|---|---|---|
| TV Europe (EBU R128, v5 nov. 2023) | -23 LUFS ±0.5 LU (±1 en direct) | -1 dBTP | **Officiel** (EBU) |
| TV USA (ATSC A/85, loi CALM) | -24 LKFS | -2 dBTP couramment appliqué | -24 officiel. **A/85 révisée en juillet 2026** (annexes streaming et true peak) : valeurs du nouveau texte non lues, à vérifier |
| Netflix (fiction/série) | -27 LKFS **dialogue-gated** (BS.1770-1), ±2 LU | -2 dBTP (Atmos) ; -1 dBTP au QC du print master et des stems | Officiel (pages Netflix Partner Help v1.4/1.5). Page actuelle illisible (JS), à revérifier sur le spec du titre |
| Spotify | Normalise à -14 LUFS (Loud -11, Quiet -19), remonte les titres faibles dans la limite de leur marge | < -1 dBTP ; < -2 dBTP si le master est plus fort que -14 | **Officiel** (Spotify for Artists) |
| YouTube | ~ -14 LUFS, **baisse seulement** | ~ -1 dBTP conseillé | **Non confirmé officiellement** (rétro-ingénierie, « stats for nerds ») |
| Apple Music (Sound Check) | ~ -16 LUFS | ~ -1 dBTP | **Non confirmé officiellement** |
| Instagram / Reels / TikTok | -14 LUFS souvent cité (d'autres disent -10 à -12) | -1 à -2 dBTP | **Non confirmé**, sources tierces contradictoires |

Ce que je conseille en pratique (choix, et non une norme) : **web/réseaux -14 LUFS / -1.5 dBTP** ; **TV FR/UE -23 / -1** (respecter la charte PAD de la chaîne, qui prime) ; **cinéma** : pas de cible LUFS, on mixe à l'étalonnage de la salle (85 dB SPL, Dolby). Voir references.md.

## 4. Recettes ffmpeg

### Mesurer (toujours, avant et après) [TESTÉ EN LABO]
```bash
ffmpeg -nostats -i IN -af ebur128=peak=true:framelog=quiet -f null -
```
Lire le bloc `Summary` : `I` (intégré), `LRA` et `True peak`. Le compteur a été étalonné avec le cas 1 de l'EBU 3341 : exact à 0.0 LU près.

### Normaliser par gain statique (méthode la plus juste) [TESTÉ EN LABO]
Calculer gain = cible - I mesuré, puis :
```bash
ffmpeg -i IN -af volume=-3.70dB -c:a pcm_s24le OUT.wav
```
Résultat au labo : écart de 0.0 à 0.2 LU, dynamique (LRA) intacte, 0.2 s pour 30 s d'audio. Si le TP prévu (TP mesuré + gain) dépasse la cible, ajouter un limiteur sur-échantillonné, puis re-mesurer :
```bash
-af "volume=9.9dB,aresample=192000,alimiter=limit=0.8414:attack=1:release=50:level=false,aresample=48000"
```
(0.8414 = -1.5 dBFS ; alimiter limite le pic échantillon, d'où le sur-échantillonnage et la marge. Résultat : -14.1 LUFS / -1.5 dBTP.)

### loudnorm en deux passes [TESTÉ EN LABO]
```bash
# Passe 1 : mesure
ffmpeg -nostats -i IN -af loudnorm=I=-23:TP=-1.5:LRA=20:print_format=json -f null -
# Passe 2 : réinjecter input_i, input_tp, input_lra, input_thresh, target_offset
ffmpeg -i IN -af "loudnorm=I=-23:TP=-1.5:LRA=<≥ input_lra>:measured_I=..:measured_TP=..:measured_LRA=..:measured_thresh=..:offset=..:linear=true:print_format=json" -ar 48000 -c:a pcm_s24le OUT.wav
```
**Lire `normalization_type` dans le JSON de la passe 2.** Si on obtient `dynamic` alors qu'on a demandé `linear`, loudnorm a compressé le programme. C'est arrivé dans 3 essais sur 4 du comparatif principal du labo, avec des écarts jusqu'à +1.0 LU (et jusqu'à +1.9 LU, LRA réduit de 26 à 18, dans les variantes).

### loudnorm en une passe [TESTÉ EN LABO, déconseillé pour un livrable]
Écarts mesurés de -1.0 à +2.8 LU. Acceptable seulement pour un aperçu.

### Master web H.264 [TESTÉ EN LABO]
```bash
ffmpeg -i MASTER.mov -vf "scale=1920:1080:flags=lanczos,format=yuv420p" \
  -c:v libx264 -preset slow -crf 18 -profile:v high -level:v 4.1 -g 50 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv \
  -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart OUT.mp4
```
Pour un débit cible, utiliser les 2 passes `-b:v 8M -maxrate 10M -bufsize 16M` : 7.90 Mb/s obtenus. Pour le vertical 1080x1920 (recadrage centré ou fond flou), voir references.md §3.

### Vérifier le livrable [TESTÉ EN LABO]
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=profile,level,width,height,pix_fmt,sample_aspect_ratio,r_frame_rate,color_range,color_space,color_transfer,color_primaries,bit_rate -of default=nw=1 OUT.mp4
```
Attendu : `High`, `yuv420p`, `tv/bt709` ×3, SAR `1:1` ; faststart = atome `moov` avant `mdat`.

### Mesure dialogue-gated (Netflix) [THÉORIQUE]
ffmpeg n'a pas de gating sur le dialogue. Il faut un compteur dédié (Dolby Media Meter, NUGEN VisLM, RX Loudness Control). À défaut, on peut seulement approcher en mesurant le stem dialogue seul.

## 5. Pièges (tous constatés au labo sauf mention)

1. **Passer de mono à stéréo coûte 3 dB.** `-ac 2` ou `aformat=stereo` placent le mono au centre à -3 dB par canal (mesuré : -26 au lieu de -23). Pour dupliquer, utiliser `pan=stereo|c0=c0|c1=c0`.
2. **loudnorm sort en 192 kHz** si on n'ajoute pas `-ar 48000`.
3. **`linear=true` repasse en dynamique sans prévenir** quand LRA mesuré > LRA cible, ou quand le gain ferait dépasser le TP. Prendre un LRA cible ≥ LRA mesuré.
4. **TP à -1 donne -0.9** après loudnorm (rééchantillonnage). Viser -1.5 pour sortir sous -1.
5. **loudnorm et ebur128 peuvent différer de 0.4 LU** sur un programme compressé. Le rapport de QC se fait avec ebur128 (ou le compteur du client), jamais avec le JSON de loudnorm.
6. **Un mix dynamique ne monte pas à -14 sans limiteur.** Il faut le décider au mix, et non le laisser à loudnorm.
7. **Sans tags couleur, ffprobe affiche `unknown`.** Il faut les écrire. Rendu réel sur QuickTime et sur les plateformes : non testé.
8. Le débit AAC affiché est inférieur au débit demandé sur un signal simple. Ce n'est pas un défaut.
9. [THÉORIQUE] Normaliser **après** le dernier changement de montage : un plan ajouté décale l'intégré.

## 6. Checklist de livraison

- [ ] Mix validé à l'oreille, dialogue stable et intelligible
- [ ] Cible connue **par écrit** (spec client, charte de la chaîne, plateforme) et datée
- [ ] Mesure ebur128 : I dans ±0.5 LU de la cible, TP ≤ cible, LRA noté
- [ ] `normalization_type` = linear (si loudnorm), sinon on comprend pourquoi
- [ ] Audio 48 kHz, 24 bits pour le master (AAC 48 kHz pour le web), canaux conformes (stéréo / 5.1, ordre des pistes)
- [ ] Vidéo : résolution, cadence et SAR 1:1 conformes ; yuv420p et High pour le web ; tags BT.709
- [ ] MP4 web : `+faststart` vérifié
- [ ] Vertical : zones de sécurité de l'interface (texte hors du bas et de la droite) vérifiées à l'œil
- [ ] Relecture complète du fichier exporté (et non de la timeline) : synchro, coupures, glitchs, début et fin
- [ ] Nom de fichier + fiche (I, TP, LRA, codec, débit, date) jointe au livrable
