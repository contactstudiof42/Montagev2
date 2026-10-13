Annexe de `SKILL.md` : vocabulaire, nuances des cibles, pourquoi, recettes ffmpeg, mesures des vidéos de référence, images sombres, pièges en détail, livraison 5.1 et cibles hors plateformes (le SKILL.md fait foi). Les sections « Quand », « Pourquoi », « Recettes », « Pièges » et l'ancienne checklist ont été déplacées du SKILL.md à l'audit 2 (2026-10-13).

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
  - **Vu sur cinq livraisons du studio** (fiches dans `analyses/projets-f42/`) : deux pubs réseau à l'intégré juste (-14,5 et -14,7 LUFS) mais au true peak de -0,6 et 0,0 dBTP ; les trois autres de +3,1 (crêtes décodées au-dessus de 0 dBFS) à -0,8 dBTP : cinq fichiers sur cinq au-dessus de -1 dBTP. Outil : `labo/outils/qc_livraison.sh FICHIER [cible]` (pistes, codec et bits, intégré, LRA, true peak, crêtes décodées, noir de début et de fin). Le QC mesure les deux, sur le fichier encodé : `ffmpeg -i f -map 0:a -af ebur128=peak=true -f null -`. [TESTÉ EN LABO]
- **Un seul mix ne sert pas toutes les sorties.** Un master TV R128 (-23) mis en ligne tel quel n'est pas « faux » : YouTube ne le remonte pas, il paraîtra simplement plus faible que les autres vidéos. Pour les réseaux sociaux, on fait une déclinaison plus dense, mais pas écrasée.

## Ce que font les vidéos de référence
**Ce que font les vidéos de référence (phase 2, mesuré sur les fichiers téléchargés)** : YouTube de 23 à 57 min de -21,3 (EGO) à **-11,6 / -12,0 LUFS** (« Qui est l'imposteur », LRA 3,6-3,8 LU, aucun silence) ; docs de créateurs -16,6 / -16,7 (Tiger, CIA) ; pubs TV françaises -23,1 à -23,2 (deux Intermarché, Lacoste) ; clips -10,9 à -12,9. Le divertissement et le clip sont plus forts que la référence de lecture : YouTube les baisse, ils gardent un son « plein » mais perdent leur dynamique. Rien de tout cela n'est une norme ; c'est le terrain.

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

### Images sombres : éviter les bandes dans les dégradés [TESTÉ EN LABO, sur images synthétiques et rendus Blender]
Pourquoi c'est artistique : un film bas et dense (goût de l'utilisateur : Joker, Ziak) vit dans les 5 % du bas de l'échelle, là où le 8 bits n'a qu'une vingtaine de niveaux. Des bandes dans un ciel nocturne ou un fond de studio détruisent la matière du noir.
- Master et échanges en **10 bits** (ProRes 422 HQ, DNxHR HQX, ou `-pix_fmt yuv420p10le`) : indice de marches 1,6 contre 5,3 en 8 bits.
- Le tramage ±1 niveau et `-tune grain` ne survivent pas à x264 dans les noirs (mesuré : aucun gain, même à CRF 16).
- Livraison réseaux (la plateforme ré-encode en 8 bits) : **le 10 bits survit à un ré-encodage à débit correct** (rendu Blender en panoramique : 0,007 de marches visibles contre 0,037 pour un master 8 bits) ; **pas de grain par défaut** : sur une image majoritairement noire, un grain σ 2 consomme le débit et fait **pire** à débit plafonné (0,16). Grain fin (`noise=c0s=4:allf=t`) seulement pour un **dégradé long et doux** (ciel de nuit, brume, mur en rebond) et après un essai **en mouvement** ré-encodé (3,2 au lieu de 5,2 sur un dégradé plein cadre). **Ne jamais juger l'encodage d'un plan sombre sur une image fixe** : immobile, 8 et 10 bits sont identiques.
- Artistiquement : un noir dur (Willis : on décide quoi garder, le reste est noir) encaisse mieux la plateforme qu'un clair-obscur laiteux [ÉPROUVÉ EN MAQUETTE].
Détail et mesures : `labo/encodage/RESULTATS.md`, `labo/encodage/noir-protege/RESULTATS.md`.

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

## Ancienne checklist de livraison (le SKILL.md fait foi)

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

Annexe de `SKILL.md` : vocabulaire, nuances des cibles, recettes complémentaires, livraison 5.1 et cibles hors plateformes en détail (le SKILL.md fait foi). Tout ce qui est marqué [TESTÉ EN LABO] a été exécuté le 2026-10-09 avec ffmpeg 6.1.1 ; voir `labo/loudness/RESULTATS.md` et `labo/livraison/RESULTATS.md`.

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
- **Instagram, TikTok** (non confirmé) : aucune documentation officielle trouvée. En plus de la cible conseillée dans `SKILL.md`, un mix lisible sur un haut-parleur de téléphone (voix devant, peu de graves).
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

<a id="livraison-51"></a>
## Livraison 5.1 en détail (déplacé de SKILL.md ; sources : `sources/surround-hors-champ-2026-10.md`)
- **France, PAD (CST RT 040 v1.2, 2016, lue)** : -23 LUFS ±1 LU, **-3 dBTP** (plus strict que R128), pistes 1-6 = L R C LFE Ls Rs, mesure en 5.1 **et** en Lt/Rt, Lo/Ro, dual mono. France Télévisions (annexe 2023) ne prévoit **pas** de 5.1 (stéréo, pistes 3-6 en silence). **Arte : aucune spec publique trouvée**, demander au chargé de production.
- **LFE** : alignement +10 dB à la lecture, limité à 120 Hz, jamais d'info essentielle (ITU-R BS.775) ; exclu de la mesure BS.1770 ; surrounds pondérés ×1,41.
- **Downmix ITU Lo/Ro sans LFE** [TESTÉ EN LABO] (formule `pan` dans `SKILL.md` § 5 bis) : `-ac 2` est faux parce que swresample normalise les coefficients (mesuré -42,1 contre -34,5 LUFS) ; si l'on tient à `-ac 2` : `-af aresample=rematrix_maxval=10 -ac 2`.
- **Piège d'étiquettes**, détail : la disposition `5.1` de ffmpeg nomme les arrières `BL/BR`, `5.1(side)` les nomme `SL/SR` ; en `7.1`, ffmpeg met les arrières en 5-6 et les côtés en 7-8.
- **Compatibilité mono** : mesurer la phase moyenne (`aphasemeter`) ; une ambiance identique dans Ls/Rs disparaît en Lt/Rt mono.
- **Ce que deviennent les arrières** [TESTÉ EN LABO, matériau synthétique, revérifié à la main] (`labo/surround/RESULTATS.md`, `sources/surround-ltrt-labo-2026-10.md`) : une ambiance seulement dans Ls/Rs perd 4,5 LU en Lo/Ro stéréo, **10,5 LU en Lo/Ro mono** (7,5 de plus que le dialogue, stable) et **disparaît en Lt/Rt mono** (-70 LUFS), **même avec un vrai déphasage de 90°** : le Hilbert stabilise l'image stéréo, il ne sauve pas le mono.
- Le LUFS du mix reste à -23,5 dans les quatre downmix. Repli du stem d'ambiance en mono pour le mesurer : `pan=mono|c0=0.5*c0+0.5*c1,ebur128=peak=true`.
- **Piège du Lt/Rt « simple »** (`pan=stereo|FL=FL+0.7071*FC-0.5*BL-0.5*BR|FR=FR+0.7071*FC+0.5*BL+0.5*BR`) : un même signal à l'avant et à l'arrière (réverbe, room tone sur 4 canaux) donne un **Lt muet**. Lt/Rt de référence : FIR de Hilbert 2047 points dans `afir=gtype=none` + `adelay=1023S` sur les fronts (21 ms de latence), graphe dans `RESULTATS.md` ; trop court sous 50 Hz.
- **Intention**, précision : avec un pied discret et décorrélé dans L/R, la présence hors champ (la pièce d'à côté, quelqu'un derrière) survit aux deux downmix et au mono du téléphone ; ce qui n'est qu'à l'arrière est un luxe de salle.

<a id="hors-plateformes"></a>
## Hors plateformes (déplacé de SKILL.md ; recherche du 2026-10-10, détail et sources : `sources/loudness-hors-plateformes-2026-10.md`)
| Contexte | Cible | True peak | Statut |
|---|---|---|---|
| Lecture réseau sans normalisation (site, lecteur intégré) : **AES TD1008** (sept. 2021, remplace TD1004) | parole / contenu mixte **-18 LUFS** ; musique **-16 LUFS** | -1 dBTP avant codec avec perte | Valeurs LUFS confirmées ; true peak par citation secondaire (PDF AES en 403) |
| Podcast (Apple Podcasts) | -16 LKFS ±1 | ≤ -1 dBFS | Officiel (Apple) |
| Livre audio (ACX) | RMS -23 à -18 dB | crêtes ≤ -3 dB, bruit ≤ -60 dB RMS | Officiel (ACX) |
| Salle de réunion, salon, événement | aucune norme ; usage pro -16 (web) à -18 (salle) | -1 dBTP | **Pratique de métier**, pas de source primaire |
| Cinéma / DCP | pas de LUFS ; bandes-annonces ≤ 85 dB Leq(m), pubs ≈ 82 (TASA, ISDCF) | — | Plafonds, pas cibles ; aucune conversion Leq(m)→LUFS officielle |

**Film d'entreprise**, pourquoi les valeurs de `SKILL.md` § 3 (-16 n'était pas sourcé avant cette recherche) : en web, le lecteur ne normalise pas, on ne veut ni être plus faible que la vidéo voisine ni écraser la voix ; en salle, la sonorisation est inconnue, souvent forte et réverbérante : marge et dynamique serrée pour que la voix passe. Pourquoi deux versions : une salle pardonne moins les écarts de dynamique qu'un casque, et le régisseur règle son gain une fois, sur la première minute.
