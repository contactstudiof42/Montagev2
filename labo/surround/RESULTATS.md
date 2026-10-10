# Labo downmix surround (BACKLOG 34) : Lo/Ro, Lt/Rt `pan`, Lt/Rt Hilbert

10/10/2026, ffmpeg 6.1.1, Python 3 + numpy + scipy 1.17. Aucun matériau protégé : tout est synthétique.
Reproduire depuis la racine du dépôt : `python3 labo/surround/labo_surround.py` (environ 25 s). Les wav sont écrits dans `labo/rendus/surround/`, qui est ignoré par git (`.gitignore` : `labo/rendus/`). Les chiffres bruts sont dans `labo/surround/resultats.json`.

## Matériau (5.1 synthétique, 10 s, 48 kHz, 24 bits, disposition ffmpeg `5.1` = FL FR FC LFE BL BR)

| Stem | Contenu | Canaux |
|---|---|---|
| `dia` | bruit rose filtré 300-3000 Hz, enveloppe syllabique à environ 4,5 syll./s, phrases de 2 s, environ -25 dBFS RMS pendant la parole | C |
| `mus` | accords sinus Am-F-C-G (2,5 s chacun), L/R en partie corrélés (corr. 0,61), environ -31 dBFS RMS par canal | L, R |
| `amb` | bruit rose passe-bas 8 kHz, **décorrélé** (deux tirages différents), -43 dBFS RMS, soit 12 dB sous la musique | Ls, Rs |
| `amb_corr` | la même ambiance, mais **identique** dans Ls et Rs (piège) | Ls, Rs |
| `amb_wrap` | la même ambiance identique dans L, R, Ls et Rs (room tone ou réverbe étalée) | L, R, Ls, Rs |
| `lfe` | bruit + sinus 45 Hz, < 120 Hz | LFE |
| `full` | dia + mus + amb + lfe | 5.1 |

Chaque stem est passé seul dans chaque downmix : on voit ce que devient chaque élément, pas seulement le mix.

## Les quatre downmix

```bash
# Lo/Ro ITU BS.775 (C et surround à -3 dB, LFE omis) [TESTÉ EN LABO]
ffmpeg -i in51.wav -af "pan=stereo|FL=FL+0.7071*FC+0.7071*BL|FR=FR+0.7071*FC+0.7071*BR" -c:a pcm_s24le loro.wav

# Lt/Rt « pan » simple : S = 0,5·(Ls+Rs) (= somme à -6 dB, soit -3 dB par rapport à une surround seule), -S dans L, +S dans R, sans déphasage [TESTÉ EN LABO]
ffmpeg -i in51.wav -af "pan=stereo|FL=FL+0.7071*FC-0.5*BL-0.5*BR|FR=FR+0.7071*FC+0.5*BL+0.5*BR" -c:a pcm_s24le ltrt_pan.wav

# Lt/Rt Hilbert en Python : Lt = L + 0,7071·C - H(S) ; Rt = R + 0,7071·C + H(S), H = scipy.signal.hilbert (FFT, non causal) [TESTÉ EN LABO]
#   voir downmixes() dans labo_surround.py

# Lt/Rt Hilbert en ffmpeg seul : FIR de Hilbert de 2047 points (fenêtre de Blackman) écrit en wav mono, puis afir sur S ;
# les fronts sont retardés de 1023 échantillons (adelay) pour rester alignés [TESTÉ EN LABO]
ffmpeg -i in51.wav -i hilbert_ir_2047.wav -filter_complex "\
[0:a]asplit=2[a][b];\
[a]pan=stereo|c0=FL+0.7071*FC|c1=FR+0.7071*FC,adelay=delays=1023S:all=1[fr];\
[b]pan=mono|c0=0.5*BL+0.5*BR[s];[s][1:a]afir=gtype=none:irgain=1:dry=1:wet=1[hs];\
[hs]asplit=2[h1][h2];[h1]pan=mono|c0=-1*c0[hn];\
[fr]channelsplit=channel_layout=stereo[fl][frr];\
[fl][hn]amix=inputs=2:normalize=0[lt];[frr][h2]amix=inputs=2:normalize=0[rt];\
[lt][rt]join=inputs=2:channel_layout=stereo[out]" -map "[out]" -c:a pcm_s24le ltrt_hilb_ff.wav
# La sortie a 1023 échantillons de latence (21,3 ms) : à recaler, par ex. avec atrim=start_sample=1023, avant de remettre l'audio sur l'image.
```

La réponse impulsionnelle est générée par le script : `h[n] = 2/(π·n)` pour n impair, 0 sinon, n = -1023..1023, multipliée par une fenêtre de Blackman. Le gain mesuré est de 0,0 dB à 100 Hz, 1 kHz et 15 kHz.

## Mesures

Commandes de mesure :
```bash
ffmpeg -nostats -i x.wav -af ebur128=peak=true -f null -                              # I et TP stéréo (ou 5.1)
ffmpeg -nostats -i x.wav -af "pan=mono|c0=0.5*c0+0.5*c1,ebur128=peak=true" -f null -   # repliement mono M = (L+R)/2
ffmpeg -v error -i x.wav -af "aphasemeter=video=0,ametadata=print:key=lavfi.aphasemeter.phase:file=-" -f null - \
  | awk -F= '/phase/{s+=$2;n++}END{print s/n}'                                          # phase moyenne
```
Convention mono : M = (L+R)/2 mesuré comme un canal unique. Un élément au centre y perd donc **exactement 3 LU** par rapport à la stéréo : c'est la référence « stable ». La corrélation L/R est calculée sur tout le fichier (numpy, Pearson sans centrage).

I en LUFS, TP en dBTP. « -70 » = plancher du compteur, donc silence.

| Stem | Version | I stéréo | TP stéréo | I mono | TP mono | Corr. L/R |
|---|---|---|---|---|---|---|
| full | 5.1 | -23,5 | -6,6 | | | |
| | Lo/Ro | -23,5 | -8,4 | -26,8 | -8,8 | 0,84 |
| | Lt/Rt pan | -23,5 | -8,2 | -26,8 | -8,8 | 0,83 |
| | Lt/Rt Hilbert py | -23,5 | -8,3 | -26,8 | -8,8 | 0,83 |
| | Lt/Rt Hilbert ffmpeg | -23,5 | -8,3 | -26,8 | -8,8 | 0,84 |
| dia (C) | 5.1 | -24,6 | -6,6 | | | |
| | les 4 versions | -24,6 | -9,6 | -27,6 | -9,6 | 1,00 |
| mus (L/R) | 5.1 | -28,7 | -20,0 | | | |
| | les 4 versions | -28,7 | -20,0 | -32,7 | -21,4 | 0,61 |
| **amb** (Ls/Rs décorrélés) | 5.1 | **-41,9** | -30,1 | | | |
| | Lo/Ro | -46,4 | -33,1 | **-52,4** | -35,8 | -0,07 |
| | Lt/Rt pan | -46,4 | -32,8 | **-70 (disparue)** | | -1,00 |
| | Lt/Rt Hilbert py | -46,4 | -33,8 | **-70 (disparue)** | | -1,00 |
| | Lt/Rt Hilbert ffmpeg | -46,4 | -35,7 | **-70 (disparue)** | | -1,00 |
| amb_corr (Ls = Rs) | 5.1 | -40,7 | -30,0 | | | |
| | Lo/Ro | -45,2 | -33,0 | -48,2 | -33,0 | 1,00 |
| | Lt/Rt (les 3) | -42,2 | -30,0 à -32,4 | -70 (disparue) | | -1,00 |
| amb_wrap (L=R=Ls=Rs) | 5.1 | -38,4 | -30,0 | | | |
| | Lo/Ro | -37,6 | -25,3 | -40,6 | -25,3 | 1,00 |
| | Lt/Rt pan | -39,2 | -23,9 | -45,2 | -30,0 | **Lt muet** (RMS Lt -240 dBFS, Rt -37,0) |
| | Lt/Rt Hilbert py | -39,2 | -26,8 | -45,2 | -30,0 | 0,00 (Lt et Rt à -40,0 dBFS RMS) |
| | Lt/Rt Hilbert ffmpeg | -39,2 | -27,5 | -45,2 | -30,0 | 0,26 |
| lfe | 5.1 et toutes versions | -70 (exclu de BS.1770) | | -70 | -inf | |

Phase moyenne `aphasemeter` : full Lo/Ro +0,41 ; amb Lo/Ro -0,04 ; amb Lt/Rt pan **-1,00** ; amb_wrap Hilbert +0,01. L'aphasemeter fait une moyenne par trame à poids égal (les silences entre les phrases comptent autant que la parole), d'où un 0,41 plus bas que la corrélation globale de 0,84.

Null test Hilbert Python contre ffmpeg (mix complet, après recalage de 1023 échantillons) : **-23,5 dB** sur toute la bande, mais **-81,5 dB au-dessus de 50 Hz**. Le FIR de 2047 points ne déphase pas correctement sous environ 50 Hz, et le bruit rose y met beaucoup d'énergie, ce qui explique la corrélation résiduelle de 0,26 sur amb_wrap. Pour descendre plus bas, il faut un FIR plus long (latence plus grande) ou un passe-haut sur S, ce qu'un encodeur réel fait de toute façon (S est limité à environ 100 Hz-7 kHz en Dolby Surround, [THÉORIQUE]).

## Ce qu'on en retient

1. **Dialogue stable partout** [TESTÉ EN LABO] : identique au 0,1 LU près dans les 4 downmix, -3,0 LU en mono, ce qui est la perte de référence. TP -9,6 partout.
2. **L'ambiance arrière en Lo/Ro** [TESTÉ EN LABO] : -4,5 LU en stéréo (coefficient -3 dB et perte de la pondération +1,5 dB des surrounds), puis **-10,5 LU en mono** par rapport au 5.1, soit **-7,5 LU de plus que le dialogue**. L'écart entre ambiance et dialogue passe de 17,3 LU (5.1) à 21,8 (stéréo) puis 24,8 (mono). Elle ne disparaît pas, mais elle recule nettement : décorrélée, elle perd 6 LU au repliement au lieu de 3.
3. **L'ambiance arrière en Lt/Rt mono : disparition totale (-70 LUFS)** [TESTÉ EN LABO], qu'elle soit décorrélée ou non, avec `pan` comme avec Hilbert. S est placé en ±S dans Lt/Rt, donc Lt+Rt l'annule. **Le déphasage de 90° ne sauve pas le mono** : il tourne S par rapport aux fronts, pas Lt par rapport à Rt. Corrélation L/R de l'ambiance seule = -1,00.
4. **Ce que le 90° apporte vraiment** [TESTÉ EN LABO] : quand le même signal est à l'avant et à l'arrière (`amb_wrap`), le `pan` simple **annule complètement Lt** (L - S = 0) et met tout dans Rt : l'image part à droite. Avec Hilbert, Lt et Rt sont égaux (-40,0 dBFS RMS chacun) et décorrélés. Sur des signaux indépendants (dia, mus, amb), `pan` et Hilbert donnent les mêmes LUFS au 0,1 près. Seul le TP change un peu (Hilbert -1 à -3 dB plus bas sur les ambiances).
5. **Loudness du mix entier** : -23,5 LUFS dans les 4 versions. La perte des arrières ne se voit pas sur le chiffre global, car l'ambiance ne pèse rien en LUFS. **Mesurer le mix seul ne montre pas le problème** : il faut écouter ou mesurer le stem d'ambiance.
6. **LFE** : absent de tous les downmix, et exclu de la mesure du 5.1 (-70 LUFS seul).

## Ce qui a échoué ou n'a pas été fait

- **`aiir`** : pas tenté. Un déphaseur de 90° en IIR demande deux chaînes d'all-pass (paire de Hilbert IIR, coefficients d'Olli Niemitalo par ex.) appliquées l'une aux fronts, l'autre à S, ce qui est plus long à valider. L'`afir` suffit et colle à scipy à -81 dB au-dessus de 50 Hz. Statut : [THÉORIQUE].
- **Pas de décodeur Pro Logic** pour vérifier le retour en 5.1 (ffmpeg n'en a pas, `surround` est un upmixeur générique). La séparation C/S n'est donc pas mesurée.
- Premier essai du null test sans recaler la latence de l'`afir` : +3 dB (signaux décalés). Il faut recaler de (taps-1)/2 = 1023 échantillons.
- Ce n'est pas un vrai mix : les LU sont des ordres de grandeur, le dialogue synthétique n'a pas de réverbe captée dans les arrières, etc.
