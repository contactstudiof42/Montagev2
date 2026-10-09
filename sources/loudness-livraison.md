# Sources : loudness et livraison

Accès : **2026-10-09** pour toutes les entrées (WebSearch/WebFetch). Les mentions « lu » et « via recherche » distinguent une page ouverte directement d'une information tirée des extraits de résultats de recherche.

## Normes

| Source | URL | Ce qu'elle confirme | Mode |
|---|---|---|---|
| EBU R 128 v5.0 (PDF) | https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128v5_0.pdf (miroir indexé : https://tech-qual.ebu.ch/files/live/sites/tech/files/shared/r/r128v5_0.pdf) | -23 LUFS, ±0.5 LU (±1 LU en direct) ; TP max -1 dBTP (BS.1770 / Tech 3341, tolérance de mesure ±0.3 dB) ; v5 de novembre 2023 (références à s3, s4 et Tech 3401 ajoutées) ; Tech 3343 = production, Tech 3344 = distribution à -23 | via recherche |
| EBU R 128 s3 v2.0 | https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s3v2_0.pdf | Supplément R128 (citée, non lue) | via recherche |
| Wikipédia EBU R 128 | https://en.wikipedia.org/wiki/EBU_R_128 | Synthèse (secondaire) | via recherche |
| SVG News : révision ATSC A/85 | https://www.sportsvideo.org/2026/07/16/atsc-releases-first-major-revision-to-a-85-audio-loudness-recommended-practice-since-2013/ | Article du 16/07/2026 : première révision complète depuis 2013, nouvelles annexes streaming et « Loudness and True Peak Quick Reference ». **Ne donne aucune valeur chiffrée** | lu |
| Broadcast Bridge : révision A/85 | https://www.thebroadcastbridge.com/content/entry/22052/atsc-modernizes-industry-audio-loudness-guidance-with-revision-to-a-85-reco | Même annonce | via recherche |
| TV Technology : « LKFS & The CALM Act » | https://www.tvtechnology.com/opinions/lkfs-amp-the-calm-act | -24 LKFS comme niveau cible (A/85, version 2013) | via recherche |
| Federal Register 2014 (FCC, CALM Act) | https://www.govinfo.gov/content/pkg/FR-2014-08-27/pdf/2014-20251.pdf | La FCC impose A/85 aux pubs diffusées | via recherche |
| ATSC, mise à jour 2013 | https://www.atsc.org/news/atsc-updates-calm-acts-tv-loudness-recommended-practice/ | Historique A/85 2013 | via recherche |

**Non confirmé :** -2 dBTP pour A/85 (absent des extraits consultés) ; valeurs de l'A/85 2026.

## Plateformes

| Source | URL | Ce qu'elle confirme | Statut |
|---|---|---|---|
| Spotify for Artists : « Loudness normalization on Spotify » | https://support.spotify.com/artists/article/loudness-normalization/ | -14 LUFS (ITU 1770) ; Loud -11, Quiet -19 ; remonte les titres faibles dans la limite de leur marge (exemple -20 LUFS / -5 TP remonté à -16) ; limiteur à -1 dB en mode Loud seulement (attaque 5 ms, retour 100 ms) ; TP < -1 dBTP, < -2 dBTP si le master est > -14 ; normalisation par album | **Officiel**, lu |
| Netflix : Sound Mix Specifications & Best Practices v1.5 | https://partnerhelp.netflixstudios.com/hc/en-us/articles/360001794307 (redirige vers https://studiopartner.netflix.net/studio/branded-sound-mix-spec-and-best-practices, page JS illisible par l'outil) | -27 LKFS ±2 LU dialogue-gated (BS.1770-1) ; TP -2 dBTP ; limiteurs à -2.3 conseillés ; mesure Atmos sur re-rendu 5.1 | Officiel, **via extraits de recherche** (version courante non lue) |
| Netflix : « Loudness and True Peaks: How to Measure and When to Flag » | https://backlothelp.netflix.com/hc/en-us/articles/360050414014 | QC : -27 LKFS ±3 dialogue-gated (BS.1770-1) pour le print master ; -1 dB TP pour le print master et les stems M&E | Officiel, via recherche |
| Production Advice : « stats for nerds » (29/09/2017) | https://productionadvice.co.uk/stats-for-nerds/ | YouTube : « content loudness » = écart avec le niveau de référence ; **pas de remontée** des vidéos faibles ; l'auteur conteste l'idée de « viser -14 » | Tiers, lu |
| AI Mastering : algorithme YouTube | https://aimastering.com/blog/en/?p=426 | Rétro-ingénierie de la normalisation YouTube | Tiers, via recherche |
| Frame.io Workflow Guide : « loudness for YouTube » | https://workflow.frame.io/guide/loudness-for-youtube | YouTube autour de -14 LUFS, baisse seulement | Tiers, via recherche |
| Meterplugs : « Apple switch to LUFS » (2022) | https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html | Apple Sound Check en LUFS ; activé par défaut seulement sur les nouvelles installations (2022, peut-être périmé) | Tiers, via recherche |
| MasteringBOX : mastering for streaming | https://masteringbox.com/learn/mastering-for-streaming | Apple Music ≈ -16 LUFS | Tiers, via recherche |
| OpenClip : audio normalization | https://openclip.app/learn/audio-normalization | Instagram/TikTok ≈ -14 LUFS (affirmation non sourcée) | Tiers, via recherche |
| Opus Clip : loudness normalizers | https://opus.pro/blog/best-loudness-normalizers | Instagram/TikTok -10 à -12 LUFS (contredit le précédent) | Tiers, via recherche |

**Non confirmé officiellement au 2026-10-09 :** les cibles de YouTube (aucune page d'aide Google trouvée), d'Apple Music, d'Instagram et de TikTok.

## Outils

| Source | URL | Usage |
|---|---|---|
| Documentation des filtres ffmpeg (loudnorm, ebur128, alimiter) | https://ffmpeg.org/ffmpeg-filters.html | Paramètres. Plages vérifiées en local avec `ffmpeg -h filter=loudnorm` (ffmpeg 6.1.1 : I de -70 à -5, LRA de 1 à 50, TP de -9 à 0, linear=true par défaut) |
| EBU Tech 3341 (compteur, signaux de test) | https://tech.ebu.ch/publications/tech3341 | Cas 1 (sinus 1 kHz à -23 dBFS en stéréo = -23 LUFS) reproduit au labo, -23.0 mesuré |
