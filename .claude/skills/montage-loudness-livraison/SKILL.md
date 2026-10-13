---
name: montage-loudness-livraison
description: À utiliser au mixage final et à l'export, dès qu'il faut « caler le son », « mettre aux normes », viser des LUFS/LKFS, respecter l'EBU R128 (-23), l'ATSC A/85 (-24), un true peak (dBTP), un LRA, ou livrer un master pour YouTube, Instagram, Reels, TikTok, Spotify, la TV, Netflix ou le cinéma. Couvre les specs de livraison (H.264, H.265 Main 10, yuv420p, faststart, AAC 48 kHz, vertical 9:16, tags couleur BT.709), le master par défaut du studio, la normalisation loudnorm en deux passes et la vérification avec ffmpeg/ffprobe. Mots entendus : « c'est moins fort que les autres vidéos », « la plateforme baisse mon son », « c'est aux normes PAD ? », « fais-moi le master Insta », QC, livrable.
---

# Loudness et livraison

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Pourquoi, mesures des vidéos de référence, recettes ffmpeg, images sombres, pièges en détail, livraison 5.1, cibles hors plateformes : [references.md](references.md). Preuves : `labo/loudness/RESULTATS.md`, `labo/livraison/RESULTATS.md`. Version d'avant : `archives/audit-2/skills/montage-loudness-livraison/`._

**Fait foi sur** : les cibles de loudness, les specs de livraison, la normalisation et la vérification d'un fichier exporté, pour toutes les applications. Intention sonore et liste d'écoute : `montage-son-et-emotion` ; réglages d'export dans Resolve : `montage-resolve`.

## 1. Mesurer sur le fichier encodé, toujours
- `ffmpeg -nostats -i IN -af ebur128=peak=true:framelog=quiet -f null -` : lire `I`, `LRA` et `True peak` dans le bloc `Summary` (compteur étalonné sur l'EBU 3341). [TESTÉ EN LABO]
- `labo/outils/qc_livraison.sh FICHIER [cible]` : pistes, codec et bits, intégré, LRA, crête, crêtes décodées, noirs de début et de fin. (Gagnée : six fichiers livrés du studio sur sept au-dessus de −1 dBTP ; ma V1 du film de mariage à +2,9 dBTP, vue par ce contrôle avant la livraison.)
- Un codec avec perte remonte la crête (+1,9 dB après AAC au labo) : limiteur sur-échantillonné avant l'encodage, puis nouvelle mesure.

## 2. Cibles (vérifiées le 2026-10-09)
| Destination | Intégré | Crête max | Statut de l'information |
|---|---|---|---|
| TV Europe (EBU R128, v5 nov. 2023) | -23 LUFS ±0.5 LU (±1 en direct) | -1 dBTP | **Officiel** (EBU) |
| TV USA (ATSC A/85, loi CALM) | -24 LKFS | -2 dBTP couramment appliqué | -24 officiel ; A/85 révisée en juillet 2026, valeurs à vérifier |
| Netflix (fiction/série) | -27 LKFS **dialogue-gated** (BS.1770-1), ±2 LU | -2 dBTP (Atmos) ; -1 dBTP au QC du print master et des stems | Officiel ; à revérifier sur le spec du titre |
| Spotify | Normalise à -14 LUFS (Loud -11, Quiet -19) | < -1 dBTP ; < -2 dBTP si le master est plus fort que -14 | **Officiel** |
| YouTube | ~ -14 LUFS, **baisse seulement** | ~ -1 dBTP conseillé | **Non confirmé officiellement** |
| Apple Music (Sound Check) | ~ -16 LUFS | ~ -1 dBTP | **Non confirmé officiellement** |
| Instagram / Reels / TikTok | -14 LUFS souvent cité (d'autres disent -10 à -12) | -1 à -2 dBTP | **Non confirmé** |

Hors plateformes ([references.md](references.md)) : lecteur sans normalisation, parole -18 LUFS, musique -16 ; film d'entreprise, master web -16 LUFS / LRA 6-10, version salle -18 LUFS.

Ce que je conseille (un choix, pas une norme) : **web et réseaux -14 LUFS ; crête visée -1,5 dBTP, acceptée jusqu'à -1** (le seuil du verdict « livrable » de `montage-regard`) ; **TV France / UE -23 / -1** (la charte PAD de la chaîne prime) ; **cinéma** : pas de cible LUFS, on mixe à l'étalonnage de la salle.

## 3. Le master du studio depuis Resolve (réglages de Diego, 2026-10-11) [universel : défaut du studio ; la spec du client prime]
Par défaut pour tout rendu final, **quand aucune spec ne l'interdit** (une chaîne, une plateforme ou une agence qui exige du H.264 8 bits ou du ProRes : sa spec prime) : **H.265 Main 10 sur le GPU**, **débit élevé** (≈ 40 Mb/s en 1080x1920 25p, ≈ 80 en UHD), **multipass**, « Bypass re-encode when possible » **désactivé**, « Force sizing / debayer to highest quality » **activés** ; la qualité passe avant la vitesse. (Gagnée : un rendu à 11 Mb/s qui donnait « une bouillie ».) Par script : `SetCurrentRenderFormatAndCodec("mp4", "H265")`, puis `SetRenderSettings({"EncodingProfile": "Main10", "MultiPassEncode": True, "VideoQuality": 40000, "NetworkOptimization": True, "AudioCodec": "aac", "AudioSampleRate": 48000})` ; les cases « Force… » et « Bypass… » ne sont pas dans l'API : un préréglage enregistré à la main, puis `LoadRenderPreset`.

## 4. Vérifier le livrable
`ffprobe -v error -select_streams v:0 -show_entries stream=profile,level,width,height,pix_fmt,sample_aspect_ratio,r_frame_rate,color_range,color_space,color_transfer,color_primaries,bit_rate -of default=nw=1 OUT.mp4`
Attendu : **H.264 (spec client)** : `High`, `yuv420p` ; **H.265 Main 10 (défaut du studio)** : `hevc`, `Main 10`, `yuv420p10le`. Dans les deux cas : `tv/bt709` ×3, SAR `1:1`, atome `moov` avant `mdat` pour le web ; une image du rendu contre la même image rendue en PNG 16 bits (PSNR ≥ 40 dB, noirs amplifiés ×6 sans bloc).

## 5. Les pièges qui ont mordu au labo (détail : [references.md](references.md))
- **Passer de mono à stéréo coûte 3 dB** avec `-ac 2` : dupliquer par `pan=stereo|c0=c0|c1=c0`.
- **loudnorm passe en dynamique sans prévenir** (3 essais sur 4 au labo) : lire `normalization_type`, prendre un LRA cible ≥ LRA mesuré ; préférer le gain statique (`volume=`), puis un limiteur sur-échantillonné si la crête dépasse.
- loudnorm sort en 192 kHz sans `-ar 48000` ; une crête visée à -1 sort à -0,9 : viser -1,5.

## 6. Avant d'envoyer
- Cible connue par écrit (spec du client, charte de la chaîne, plateforme) et datée.
- Mesure `ebur128` sur le fichier : `I` à ±0,5 LU de la cible, crête ≤ cible, LRA noté.
- Audio 48 kHz (24 bits au master, AAC 48 kHz pour le web), canaux conformes ; vidéo : résolution, cadence et SAR conformes, tags BT.709, faststart pour le web ; vertical : zones de sécurité vérifiées à l'œil.
- Relecture du fichier exporté, pas de la timeline : synchro, coupures, glitchs, début et fin.
- **La liste minutée de ce que Diego doit écouter** : je n'entends pas le mix (`montage-son-et-emotion`).
- Nom de fichier et fiche jointe (I, crête, LRA, codec, débit, date).
