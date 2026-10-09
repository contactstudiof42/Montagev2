# Labo loudness : résultats (2026-10-09)

Environnement : ffmpeg 6.1.1-3ubuntu5 (Ubuntu), Python 3.13, conteneur Linux sans GPU.
Rendus WAV dans `labo/rendus/loudness/` (ignoré par git). Résultats bruts : `resultats.json`.

Scripts :
- `labo_loudness.py` génère le signal test, le mesure, puis compare trois méthodes (loudnorm en 1 passe, loudnorm en 2 passes `linear=true`, gain statique + limiteur) vers -23 et -14 LUFS / -1 dBTP. Durée totale : 24 s.
- `labo_variantes.py` teste des variantes de la 2e passe : avec ou sans `offset`, LRA cible élevé, TP -1.5.

Tolérance de réussite : |I mesuré - cible| ≤ 0.5 LU et TP ≤ cible (+0.05). La re-mesure se fait toujours avec le filtre `ebur128=peak=true`, qui est indépendant de loudnorm.

## 0. Étalonnage des compteurs (EBU Tech 3341, cas 1)

Sinus 1 kHz à -23 dBFS sur les deux canaux, 20 s. Valeur attendue : -23.0 LUFS.

```bash
ffmpeg -f lavfi -i "sine=f=1000:r=48000:d=20" -af "volume=-4.9382dB,pan=stereo|c0=c0|c1=c0" -c:a pcm_s24le cal_1k_m23.wav
ffmpeg -nostats -i cal_1k_m23.wav -af ebur128=peak=true:framelog=quiet -f null -
```
Résultats : ebur128 donne I = -23.0 LUFS et Peak = -23.0 dBTP. loudnorm donne input_i = -23.05. **Les deux compteurs sont justes.**

**Piège trouvé :** le premier essai passait en stéréo avec `aformat=channel_layouts=stereo` (même chose avec `-ac 2`) et mesurait **-26.0 LUFS**. Le passage mono → stéréo de libswresample place le mono au centre à -3 dB sur chaque canal. Pour dupliquer un mono sans perte, il faut `pan=stereo|c0=c0|c1=c0`.

## 1. Signal test

Le signal dure 30 s, en stéréo 48 kHz / 24 bits, avec une dynamique volontairement large :
- 0 à 10 s : bruit rose moyen (amplitude 0.25) ;
- 10 à 15 s : sinus 1 kHz ;
- 15 à 18 s : silence ;
- 18 à 24 s : bruit rose fort (amplitude 0.9) ;
- 24 à 30 s : bruit rose faible (amplitude 0.045).

Une variante « calme » passe le même signal dans `acompressor` (ratio 8, puis -6 dB). Elle imite un mix déjà maîtrisé.

| Source | I (LUFS) | LRA (LU) | TP (dBTP) |
|---|---|---|---|
| large (`signal_test.wav`) | -19.3 | 26.0 | -4.8 |
| calme (`signal_calme.wav`) | -23.9 | 11.0 | -8.3 |

## 2. Comparaison des méthodes (re-mesure ebur128)

| Source → cible | Méthode | I obtenu | Écart | TP | LRA | Mode loudnorm réel | Verdict | Temps |
|---|---|---|---|---|---|---|---|---|
| large → -23 | 1 passe | -20.2 | **+2.8** | -6.8 | 20.1 | dynamic | RATÉ | 1.6 s |
| large → -23 | 2 passes linear=true (LRA=20) | -23.0 | 0.0 | -9.6 | 20.1 | **dynamic** (repli) | OK, mais dynamique écrasée | 2.6 s |
| large → -23 | gain statique `volume=-3.70dB` | -23.0 | 0.0 | -8.5 | 26.0 | — | OK | 0.2 s |
| large → -14 | 1 passe | -12.7 | **+1.3** | -0.9 | 21.5 | dynamic | RATÉ (I et TP) | 1.5 s |
| large → -14 | 2 passes linear=true | -13.0 | **+1.0** | -0.9 | 22.3 | dynamic (repli) | RATÉ (I et TP) | 2.3 s |
| large → -14 | gain +5.3 dB + alimiter (192 kHz) | -14.2 | -0.2 | -1.4 | 26.0 | — | OK | 0.4 s |
| calme → -23 | 1 passe | -24.0 | **-1.0** | -7.4 | 10.8 | dynamic | RATÉ | 1.4 s |
| calme → -23 | 2 passes linear=true | -22.5 | +0.5 | -7.0 | 11.0 | **linear** | OK (en limite) | 1.5 s |
| calme → -23 | gain statique `volume=0.90dB` | -23.0 | 0.0 | -7.4 | 11.0 | — | OK | 0.2 s |
| calme → -14 | 1 passe | -14.9 | -0.9 | -0.9 | 9.2 | dynamic | RATÉ (I et TP) | 1.5 s |
| calme → -14 | 2 passes linear=true | -14.0 | 0.0 | -0.9 | 9.2 | dynamic (repli) | I OK, TP -0.9 > -1 | 2.5 s |
| calme → -14 | gain +9.9 dB + alimiter (192 kHz) | -14.1 | -0.1 | -1.5 | 11.1 | — | OK | 0.4 s |

Temps de calcul : pour 30 s d'audio, compter environ 0.4 s par passe en linéaire et environ 1.5 s en dynamique. Le mode dynamique sur-échantillonne en interne à 192 kHz. Le temps se rapporte à la durée, donc un programme de 60 min prendrait environ 3 min en dynamique (extrapolation non testée).

## 3. Variantes de la 2e passe (`labo_variantes.py`)

| Cas | A : avec offset | B : sans offset | C : LRA cible ≥ LRA mesuré | D : C + TP -1.5 |
|---|---|---|---|---|
| calme → -23 | linear, -22.5 | linear, -22.5 | linear, -22.5 | linear, -22.5 (TP -7.0) |
| large → -23 | dynamic, -23.0 | dynamic, **-20.2** | **linear, -22.9** (LRA 26 conservé) | linear, -22.9 |
| calme → -14 | dynamic, -14.0 | dynamic, -14.9 | dynamic, -14.9 | dynamic, -14.9, **TP -1.4** |
| large → -14 | dynamic, -13.0 | dynamic, -12.7 | dynamic, -12.1 | dynamic, -12.4, TP -1.4 |

## 4. Ce qui a marché, ce qui a raté, et pourquoi

1. **Une seule passe de loudnorm ne suffit pas** pour une livraison : on a mesuré des écarts de -1.0 à +2.8 LU. La 1re passe fonctionne en dynamique avec une fenêtre glissante, sans connaître le programme entier, et elle compresse en plus (le LRA passe de 26 à 20).
2. **`linear=true` n'est qu'une demande.** loudnorm repasse en dynamique, sans message d'erreur, dans deux cas : (a) si le LRA mesuré dépasse le LRA cible (cas « large » avec LRA=20 pour 26 mesuré) ; (b) si le gain nécessaire ferait dépasser le TP cible (tous les cas à -14 : -8.3 dBTP + 9.9 dB donne +1.6). **Il faut toujours lire `normalization_type` dans le JSON de sortie.**
3. **`offset=target_offset` n'a d'effet que si loudnorm repasse en dynamique.** En linéaire, A et B donnent la même chose. En dynamique, il est indispensable : sans lui, on obtient -20.2 au lieu de -23.0.
4. **Le TP plafonne à -0.9 dBTP pour une consigne de -1.** Le limiteur de loudnorm travaille à 192 kHz, puis le rééchantillonnage vers 48 kHz ajoute environ 0.1 dB. C'est dans la tolérance de mesure (±0.3 dB, R128), mais un QC strict le refusera. **Viser TP = -1.5** pour sortir à -1.4.
5. **loudnorm et ebur128 ne mesurent pas tout à fait la même chose sur un signal compressé.** Sur « calme », loudnorm mesure input_i = -24.33 et ebur128 -23.9, soit 0.4 LU d'écart. C'est la cause du -22.5 obtenu en linéaire. Sur le signal large, l'écart n'est que de 0.1 LU, et les deux sont exacts sur le sinus d'étalonnage. Cause probable : des différences d'implémentation (sur-échantillonnage, fenêtrage, gating). Ce point n'est **pas élucidé**.
6. **La méthode la plus juste et la plus rapide : mesurer avec ebur128 puis appliquer `volume=XdB`.** Elle donne un écart de 0.0 à 0.2 LU et conserve la dynamique d'origine. Si le TP dépasse, on ajoute un limiteur (`alimiter` à 192 kHz, plafond 0.5 dB sous la cible), puis on re-mesure. Attention : alimiter limite le pic échantillon et non le true peak, d'où le sur-échantillonnage et la marge.
7. **On ne vise pas -14 LUFS avec un mix dynamique sans limiter.** Pour passer de -24 à -14 LUFS avec un TP à -1, il faut forcément écraser les crêtes. Sinon loudnorm le fait à notre place, et mal (écarts de +1 à +1.9 LU sur la source large).

## 5. Commandes de référence

```bash
# Mesure seule (rapport final, indépendant de loudnorm)
ffmpeg -nostats -i IN -af ebur128=peak=true:framelog=quiet -f null -
# Passe 1 (mesure JSON)
ffmpeg -nostats -i IN -af loudnorm=I=-23:TP=-1.5:LRA=20:print_format=json -f null -
# Passe 2 (valeurs reprises du JSON ; prendre un LRA cible >= input_lra pour rester en linéaire)
ffmpeg -i IN -af "loudnorm=I=-23:TP=-1.5:LRA=27:measured_I=-19.40:measured_TP=-4.85:measured_LRA=26.10:measured_thresh=<input_thresh>:offset=-2.81:linear=true:print_format=json" -ar 48000 -c:a pcm_s24le OUT.wav
# Méthode gain statique (la plus juste ici)
ffmpeg -i IN -af volume=-3.70dB -c:a pcm_s24le OUT.wav
ffmpeg -i IN -af "volume=9.9dB,aresample=192000,alimiter=limit=0.8414:attack=1:release=50:level=false,aresample=48000" -c:a pcm_s24le OUT.wav
```
Note : sans `-ar 48000`, loudnorm sort en 192 kHz.
