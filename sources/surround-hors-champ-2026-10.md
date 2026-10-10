# Son hors champ, présence suggérée et surround (5.1 / 7.1 / Atmos) en post-production

Recherche du 10/10/2026. Les faits sont reformulés et chaque fait a sa source. Statut : **lu** (document primaire ouvert et lu), **via recherche** (extrait de moteur de recherche ou source secondaire), **[TESTÉ EN LABO]** (ffmpeg 6.1.1, dossier scratchpad `surround/`), **[THÉORIQUE]**.

## 1. Disposition des canaux et rôle de chaque canal

| Fait | Source | Statut |
|---|---|---|
| 5.1 de référence : 3 enceintes avant (L/R sur un arc de 60°, donc ±30°, C au centre), 2 surrounds placées entre 100° et 120° de l'axe, pas plus près que les avants, plus un LFE optionnel | ITU-R BS.775-4 (12/2022), §2 et §3 : https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.775-4-202212-I!!PDF-E.pdf | lu |
| LFE limité à 120 Hz. Rien ne doit être diffusé au-dessus de 120 Hz sur ce canal à la télévision | BS.775-4, §4-5 et Annexe 7 (même URL) | lu |
| Alignement : le LFE est enregistré avec un décalage de -10 dB et compensé à la lecture par +10 dB de gain acoustique dans sa bande (< 120 Hz). Il faut mesurer avec un sonomètre sélectif en fréquence, sinon la lecture large bande ne donne pas +10 dB | BS.775-4, Annexe 7 | lu |
| Le LFE n'est qu'un **complément**. Il est souvent supprimé au downmix et par les installations domestiques. Les canaux principaux doivent porter tout l'essentiel. La plupart des programmes TV n'en ont pas besoin, et le LFE est alors silencieux | BS.775-4, Annexe 7 | lu |
| Les surrounds doivent garder leurs propres graves au lieu de les renvoyer vers l'avant. Le renvoi est une option du récepteur (gestion des graves) | BS.775-4, Annexe 7 | lu |
| Ordre des pistes 5.1 en France (PAD) : 1 L, 2 R, 3 C, 4 LFE, 5 Ls, 6 Rs (affectation UER R91, paires AES 1-2-3), pistes 7-8 au choix de la chaîne | CST RT 040 v1.2 (2016), §2.2.6.2 : https://cst.fr/download/33/recommandations-techniques/1017/cst-rt-040.pdf | lu |
| Cinéma (DCP) : 1 L, 2 R, 3 C, 4 LFE, 5 Ls/Lss, 6 Rs/Rss, 7 HI, 8 VI-N, 11 Lrs, 12 Rrs (pour le 7.1 DS seulement). Livrer un 7.1 DS sans CPL 5.1 associée est déconseillé | ISDCF Doc 4 (29/06/2017) : https://files.isdcf.com/papers/ISDCF-Doc4-Audio-channel-recommendations.pdf | lu |
| 7.1 = 5.1 + 2 surrounds arrière. Le dernier chiffre d'une notation Atmos (7.1.4) compte les enceintes en hauteur. Lits (beds) Atmos jusqu'à 7.1.2 ; salle de contrôle qualité Netflix en 7.1.4 | Dolby, guide 7.1.4 : https://www.dolby.com/siteassets/about/support/guide/setup-guides/7.1.4-in-wall-dolby-atmos-enabled-speaker-placement/7_1_4_in_wall_speaker_setup.pdf ; Netflix Atmos QC : https://backlothelp.netflix.com/hc/en-us/articles/360052478873 | via recherche |
| Usage courant : dialogue au centre ; ambiances, effets et musique dans les autres canaux ; dialogue intelligible même hors du point d'écoute idéal | iZotope, « 6 tips for mixing in surround » : https://www.izotope.com/en/learn/6-tips-for-mixing-in-surround | via recherche (pratique, pas une norme) |
| Écoute PAD : enceintes placées selon BS.775 ; bruit rose à -18 dBFS = 74 dB(C) par canal, LFE à 78 dB(C) ; environ 79 dB(C) par canal en mixage (hors LFE). Mixer dans un auditorium adapté à la télévision (écoute de proximité), pas dans une grande salle de cinéma | CST RT 040, §2.2.1 | lu |

**Piège ffmpeg [TESTÉ EN LABO]** : la disposition `5.1` de ffmpeg nomme les surrounds `BL/BR`, et `5.1(side)` les nomme `SL/SR`. La disposition `7.1` est FL FR FC LFE **BL BR SL SR** (arrières en 5-6, côtés en 7-8), alors que le DCP 7.1 DS met les côtés en 5-6. Il faut vérifier les étiquettes (`ffprobe`) avant tout `pan` ou `channelmap`. Commande : `ffmpeg -layouts`.

## 2. Downmix stéréo : coefficients, ce qui disparaît, pièges

| Fait | Source | Statut |
|---|---|---|
| Lo/Ro (BS.775 Tableau 2) : L' = L + 0,7071·C + 0,7071·Ls ; R' = R + 0,7071·C + 0,7071·Rs (0,7071 = -3 dB). Mono : C' = 0,7071·(L+R) + C + 0,5·(Ls+Rs). Le LFE n'apparaît dans aucune équation | BS.775-4, Annexe 4 | lu |
| PAD France, métadonnées Dolby par défaut : centre et surround à 0,707 (-3 dB) en Lo/Ro comme en Lt/Rt ; « Preferred Stereo Downmix » = Lt/Rt ; filtre passe-bas LFE actif. La compatibilité stéréo et mono doit être vérifiée en mode RF « Film Standard » | CST RT 040, §2.2.3 et tableau des métadonnées | lu |
| La version française 5.1 est souvent la composante principale : c'est elle que le téléviseur sans 5.1 downmixe en stéréo ou en mono | CST RT 040, encadré §2.2.3 | lu |
| Lt/Rt (matricé) : les surrounds sont injectés en opposition de phase dans L et R pour qu'un décodeur Pro Logic les retrouve. Lo/Ro = simple stéréo compatible mono | TV Technology : https://www.tvtechnology.com/opinions/what-is-downmixing-part-1-stereo-loro | via recherche |
| Ne pas réduire les coefficients de downmix pour éviter la saturation, afin que le 5.1 downmixé ait le même niveau qu'une stéréo native. C'est au producteur de prévoir la marge ou le DRC. Les box et téléviseurs imposent souvent Lo/Ro ou Lt/Rt sans tenir compte de la métadonnée | EBU Tech 3344 v2.1 (07/2016), §5.2 et §6.15 : https://tech.ebu.ch/docs/tech/tech3344.pdf | lu |
| Netflix (v1.5) : C → L et R à environ -3 dB ; surrounds → avant du même côté à **-3 dB au minimum** ; LFE optionnel à -8/-12 dB, filtré à 200 Hz au plus | https://backlothelp.netflix.com/hc/en-us/articles/360001794307 | via recherche (la page redirige vers un portail JS illisible) |
| Atmos : Stereo Direct ne contient aucun signal LFE. Les rendus Lo/Ro et Lt/Rt se règlent par des trims/balances de downmix 5.1/2.0, 5.1.2 et 7.1 | Steinberg, Trim and Downmix Editor : https://steinberg.help/nuendo/v11/en/cubase_nuendo/topics/surround_sound/surround_sound_adm_authoring_trim_and_downmix_editor_r.html | via recherche |

Ce que le labo a montré (fichier de test : 6 bruits roses décorrélés, LFE filtré à 120 Hz) :
- **LFE ignoré deux fois [TESTÉ EN LABO]** : un 5.1 avec le LFE seul mesure **-70 LUFS** (plancher du compteur), car BS.1770 exclut le LFE (§2, Tableau 3 : https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf). Après `-ac 2`, le LFE vaut **-inf dB**, ffmpeg le jette.
- **Surrounds pondérés à 1,41 (+1,5 dB) par BS.1770 (lu)**. Au downmix Lo/Ro, un élément placé seulement dans les arrières passe de -30,1 à **-34,6 LUFS (-4,5 LU)** : -3 dB de coefficient et perte du bonus de +1,5 dB. Le mix complet ne perd que 1,6 LU (-27,0 → -28,6). **Une présence dans les arrières baisse donc d'environ 3 LU par rapport au reste du mix en stéréo** [TESTÉ EN LABO].
- **Piège de phase Lt/Rt [TESTÉ EN LABO]** : la même ambiance mono envoyée dans Ls et Rs, encodée en Lt/Rt puis sommée en mono, tombe à **-70 LUFS**, soit une annulation totale (phase moyenne mesurée -1,0). Avec des arrières décorrélés, il reste -56,6 LUFS contre -30,1 en 5.1 : en Lt/Rt mono, le surround disparaît presque entièrement. La RT 040 exige une phase « majoritairement positive » (§2.2.5.2).
- **Normalisation cachée de ffmpeg [TESTÉ EN LABO]** : `-ac 2` est **7,7 dB** plus bas que la matrice ITU (-36,3 contre -28,6 LUFS), car swresample réduit les coefficients pour éviter tout écrêtage, ce que Tech 3344 déconseille. `aresample=rematrix_maxval=10` rend le même résultat que le `pan` ITU (-28,6).

## 3. Vérifier avec ffmpeg : commandes exactes

Toutes testées avec ffmpeg 6.1.1. Pour un fichier à disposition `5.1(side)`, remplacer `BL/BR` par `SL/SR`.

```bash
# A. Fichier 5.1 de test : 6 bruits roses décorrélés, LFE filtré à 120 Hz, 20 s [TESTÉ EN LABO -> -27,0 LUFS, TP -16,0 dBTP]
ffmpeg -f lavfi -i "anoisesrc=color=pink:seed=1:amplitude=0.1:duration=20:sample_rate=48000" \
 -f lavfi -i "anoisesrc=color=pink:seed=2:amplitude=0.1:duration=20:sample_rate=48000" \
 -f lavfi -i "anoisesrc=color=pink:seed=3:amplitude=0.1:duration=20:sample_rate=48000" \
 -f lavfi -i "anoisesrc=color=pink:seed=4:amplitude=0.3:duration=20:sample_rate=48000" \
 -f lavfi -i "anoisesrc=color=pink:seed=5:amplitude=0.1:duration=20:sample_rate=48000" \
 -f lavfi -i "anoisesrc=color=pink:seed=6:amplitude=0.1:duration=20:sample_rate=48000" \
 -filter_complex "[3]lowpass=f=120,lowpass=f=120[lfe];[0][1][2][lfe][4][5]join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-LFE|4.0-BL|5.0-BR[a]" \
 -map "[a]" -c:a pcm_s24le noise51.wav
ffprobe -v error -show_entries stream=channels,channel_layout -of default=nw=1 noise51.wav   # channels=6, 5.1

# B. Downmix Lo/Ro ITU BS.775, LFE omis [TESTÉ EN LABO -> -28,6 LUFS, TP -17,4]
ffmpeg -i noise51.wav -af "pan=stereo|FL=FL+0.7071*FC+0.7071*BL|FR=FR+0.7071*FC+0.7071*BR" -c:a pcm_s24le loro.wav

# C. Lt/Rt approché (coefficients DPLII de swresample, SANS déphasage de 90°) [TESTÉ EN LABO -> -28,3 LUFS]
ffmpeg -i noise51.wav -af "pan=stereo|FL=FL+0.7071*FC-0.6124*BL-0.5*BR|FR=FR+0.7071*FC+0.5*BL+0.6124*BR" -c:a pcm_s24le ltrt.wav
#    ou encodeur intégré (avec normalisation) : -af "aresample=matrix_encoding=dplii" -ac 2  [TESTÉ -> -37,4 LUFS]

# D. Downmix automatique sans normalisation (équivaut à B) [TESTÉ EN LABO -> -28,6]
ffmpeg -i noise51.wav -af "aresample=rematrix_maxval=10" -ac 2 -c:a pcm_s24le ac2.wav

# E. Test de compatibilité mono d'un downmix [TESTÉ EN LABO]
ffmpeg -i ltrt.wav -af "pan=mono|c0=0.5*FL+0.5*FR" -c:a pcm_s24le mono.wav

# F. Loudness + true peak (marche en 5.1 comme en stéréo, LFE exclu automatiquement) [TESTÉ EN LABO]
ffmpeg -nostats -i noise51.wav -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p'
ffmpeg -nostats -i noise51.wav -af loudnorm=I=-23:TP=-3:LRA=20:print_format=summary -f null -   # même I mesuré : -27,0

# G. Niveau par canal (vérifier qu'un canal n'est pas vide ou inversé) [TESTÉ EN LABO]
ffmpeg -i noise51.wav -af astats=measure_perchannel=RMS_level+Peak_level:measure_overall=none -f null -

# H. Phase moyenne d'une stéréo (proche de +1 = sain, proche de -1 = annulation en mono) [TESTÉ EN LABO -> -1,0 sur le cas piège]
ffmpeg -i ltrt.wav -af "aphasemeter=video=0,ametadata=print:key=lavfi.aphasemeter.phase:file=phase.txt" -f null -
```

Contrôle sur cas d'école [TESTÉ EN LABO] : 5 canaux identiques (sinus 1 kHz) mesurent -28,4 LUFS, ce qui correspond au calcul BS.1770 (3 × 1 + 2 × 1,41). Le Lo/Ro de signaux **corrélés** monte de 3 LU (-25,4) au lieu de baisser : les sommes cohérentes s'additionnent en amplitude.

## 4. Livraison télé française en 5.1

| Diffuseur / document | Loudness | True peak | Pistes 5.1 | Statut |
|---|---|---|---|---|
| CST RT 040 v1.2 (2016), référence commune des éditeurs français (PAD fichier) | -23 LUFS ±1 LU (> 2 min) ; ≤ -23 LUFS (< 2 min) ; court terme max -20 LUFS (< 2 min) ; dialogues -23 ±7 LU ; mesure en **5.1, Lt/Rt, Lo/Ro et dual mono** | **-3 dBTP** | L R C LFE Ls Rs sur 1-6 (UER R91) ; métadonnée Dialog Level = loudness intégré | lu |
| France Télévisions, annexe CDE fichiers HD (24/01/2023) : https://static.francetelevisions.fr/inline-images/Annexe%20technique%20CDE%20fichiers%20HD%20VT%20PI%2024-01-2023_FR_1.pdf | -23 LUFS ±1 LU (≥ 2 min) ; LRA ≤ 20 LU (+5) ; court terme ≤ -20 LUFS (< 2 min) ; R128 mesuré par paire | **-3 dBTP** | **Aucune 5.1 prévue** : 4, 8 ou 16 pistes mono PCM 24 bits/48 kHz ; VF stéréo 1-2, pistes 3-6 en silence, AD 7-8, VM 9-10 | lu |
| Arcom, délibération du 19/07/2011 : https://www.arcom.fr/en/find-out-more/legal-area/legal-resources/deliberation-july-19-2011-technical-characteristics-loudness-television-programs-and-commercials | -23 LUFS (BS.1770-2) ; ±1 LU depuis 2013 ; LRA ≤ 20 LU | non fixé | L'énergie du LFE ne doit pas augmenter sensiblement l'intensité perçue | lu (version EN) |
| Arte (PAD) | non trouvé | non trouvé | non trouvé | **non vérifié** |
| Repère : EBU R 128 v5.0 (11/2023) : https://tech.ebu.ch/publications/r128 | -23 LUFS ; s4 = contenus cinéma | -1 dBTP (R128) | - | lu (page de garde) |
| Netflix (v1.5) | -27 LKFS ±2 LU, filtré sur le dialogue (BS.1770-1) ; Atmos mesuré sur un re-rendu 5.1 | -2 dBTP (le QC signale à -1) | lits 2.0 à 7.1.2 ; fold-downs 5.1 demandés pour le doublage | via recherche (voir aussi `loudness-livraison.md`) |

## 5. Côté artistique : hors champ et présence suggérée

Source principale : M. Chion, *L'Audio-vision* (1990 ; trad. angl. *Audio-Vision*, Columbia UP, 1994), ch. 4-5 et glossaire. Copie consultée : https://monoskop.org/images/6/6d/Chion_Michel_Audio-Vision.pdf (lu).
- **Hors champ actif** : son acousmatique (on l'entend sans voir sa source) qui pose une question (« qu'est-ce que c'est ? ») et donne envie de regarder ailleurs. Il fait avancer le récit par la curiosité. Exemple de Chion : *Psychose* (la mère qu'on entend sans la voir).
- **Hors champ passif** : son qui installe une atmosphère, enveloppe et stabilise l'image sans donner envie de chercher sa source (sons de territoire, rumeur de ville). Il laisse le montage multiplier les gros plans sans désorienter. Exemple : *Fenêtre sur cour* (1954), avec la rumeur de la ville, la cour et les radios.
- Le **Dolby multipiste favorise le passif** : localiser réellement un son actif dans une enceinte hors écran crée un « effet de coulisses » trop réaliste. Chion évoque l'entrée de Roy Batty dans *Blade Runner*.
- **Acousmêtre** : personnage-voix ni dans l'image ni franchement hors champ, toujours sur le point d'y entrer. On lui prête quatre pouvoirs : tout voir, tout savoir, agir sur la situation, être partout. Il les perd quand on montre son visage (désacousmatisation). Exemples : *Le Testament du Dr Mabuse* (Lang), la mère de *Psychose*, le magicien d'Oz, HAL dans *2001*.
- **Superchamp** : espace créé par les ambiances multipistes autour de l'écran, presque indépendant de l'image. « Hors-champ poubelle » : chutes et fracas recueillis dans les enceintes hors écran (*Die Hard*).
- Cas récent : *La Zone d'intérêt* (Glazer, 2023). Le camp n'est jamais montré, seulement entendu derrière le mur. Le sound designer J. Burn parle de deux films, celui qu'on voit et celui qu'on entend. Sources : https://nofilmschool.com/the-zone-of-interest-sound ; https://inverse.com/entertainment/the-zone-of-interest-sound-designer-interview-johnnie-burn-oscars-nope (via recherche).

**Règles pratiques pour une présence discrète dans les arrières** (synthèse des sources ci-dessus et des tests ; ce sont des conseils, pas des normes) :
1. Préférer un son de **territoire** (passif) à une source ponctuelle. Une source identifiable dans une seule surround crée l'effet « exit sign » (porte de sortie) et fait tourner la tête (Chion ; Kerins : https://offscreen.com/pdf/kerins_diegesis.pdf, via recherche).
2. Pour une présence **active** (quelqu'un est là), la faire exister par de petits indices intermittents (pas, frottement, respiration), puis la ramener vers l'avant ou la désacousmatiser au moment voulu.
3. **Décorréler** Ls et Rs (prises ou réverbes différentes). Une source identique en opposition de phase disparaît en Lt/Rt mono (§2, test).
4. Prévoir **-3 à -4,5 LU** de perte en stéréo : vérifier que la présence s'entend encore dans le Lo/Ro (commande B) sans la monter au point de gêner en 5.1.
5. Ne rien confier d'essentiel au LFE (BS.775). Une menace sourde en grave doit aussi exister dans les canaux principaux.
6. Pas de dialogue utile dans les arrières : il doit rester intelligible pour un auditeur placé hors du point d'écoute idéal.

## Incertain / à vérifier

- **Arte (PAD)** : aucune fiche technique publique trouvée (ni loudness, ni true peak, ni ordre des pistes). À demander au chargé de production. Ne pas supposer qu'elle suit la RT 040.
- **France Télévisions 5.1** : l'annexe 2023 ne prévoit que de la stéréo, et les pistes 3-6 sont en silence (sans doute réservées, mais ce n'est pas écrit). Les specs 5.1 éventuelles (programmes UHD/cinéma) n'ont pas été trouvées.
- **RT 040** date de 2016 : vérifier qu'aucune version plus récente n'existe sur cst.fr. Elle impose -3 dBTP, plus strict que le -1 dBTP de R128.
- **Netflix** : page v1.5 lue seulement par extraits (portail JS). Coefficients de fold-down et tolérance (±2 ou ±3 LU) à confirmer sur la version en cours.
- **Dolby Atmos** : la doc officielle du Renderer (coefficients par défaut, LFE dans les rendus Lo/Ro et Lt/Rt) n'a pas été lue. Le +6 dB parfois cité pour le LFE en Atmos vient d'un forum.
- **Lt/Rt** : la commande `pan` C ne fait pas le déphasage de 90° d'un vrai encodeur Dolby Surround. Les coefficients 0,6124/0,5 viennent du code de swresample (https://github.com/FFmpeg/FFmpeg/blob/release/6.1/libswresample/rematrix.c), pas de Dolby.
- Supplément EBU R 128 s4 (cinéma) : contenu non lu.
- Tests faits sur du bruit rose et des sinus, pas sur un vrai mix : les écarts en LU sont des ordres de grandeur.
