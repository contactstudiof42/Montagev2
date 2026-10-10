# Loudness hors broadcast : cibles de livraison (état octobre 2026)

Recherche du 10/10/2026. Mesures en LUFS / LKFS selon ITU-R BS.1770 (1 LU = 1 dB). « à confirmer » = pas vérifié sur une source primaire.

## Tableau de synthèse

| Contexte | Cible intégrée | True peak max | LRA conseillée | Source (date) |
|---|---|---|---|---|
| AES TD1008 : parole et contenus mixtes (podcast, flux de type radio, pubs, assistants vocaux) | **-18 LUFS** (point d'ancrage = la parole) | **-1 dBTP en entrée du codec avec perte** (§4) ; jusqu'à -0,5 dBTP possible pour les codecs à haut débit (256 kb/s), en dessous de -1 dBTP pour les bas débits (§7B) | Pas de valeur chiffrée trouvée (à confirmer) | AESTD1008.1.21-9 (24/09/2021). Valeurs dB TP relevées seulement dans des citations secondaires, à confirmer sur le PDF |
| AES TD1008 : musique | **-16 LUFS** (normalisation par album ; titre le plus fort vers -14 au maximum, à confirmer) ou par titre à -16 LUFS au maximum | idem | non | Idem ; Production Advice (01/10/2021), Radio World |
| AES TD1008 : flux temps réel mêlant parole et musique | **-17 LUFS** (compromis) | idem | non | Telos Alliance (doc. en ligne), à confirmer sur le PDF |
| AES TD1004 (2015, **remplacé** par TD1008) | plage de **-16 à -20 LUFS** | -1 dBTP | non | Production Expert / Pro Tools Expert (secondaire) |
| Vidéo corporate sur site web (lecteur intégré sans normalisation) | **-16 LUFS** recommandé par les praticiens (plage de -14 à -18) | -1 dBTP | ~8 à 12 LU (à confirmer, pratique courante) | Pas de norme. Blog J. Nilo (praticien) ; cohérent avec TD1008 pour la parole et avec Apple Podcasts |
| Salle de réunion, vidéoprojecteur, salon, événement | **Pas de norme.** En pratique -16 à -18 LUFS, LRA plus réduite pour les petits haut-parleurs et les lieux bruyants (à confirmer) | -1 dBTP | ≤ 8 LU conseillé (à confirmer) | Aucune source primaire trouvée. Avis de praticiens ; le niveau réel dépend de la sono et du réglage du régisseur |
| Broadcast TV Europe (pour comparaison) | -23 LUFS ±0,5 LU (±1 LU en direct) | -1 dBTP | pas de limite (R128 s1 : max short-term pour les formats courts) | EBU R 128 v4 (2020) ; R 128 s1 v3 |
| Cinéma / DCP | **Pas de cible LUFS.** Calibration de lecture (SMPTE RP 200) : 85 dBC par canal, bruit rose à -20 dBFS. Plafond des bandes-annonces : **85 dB Leq(m)** (TASA, depuis 2001), pubs ~82 Leq(m) | ~-1 à -3 dBTP en pratique (à confirmer) | pas de valeur | ISDCF Doc 11 (15/03/2016) ; liste de diffusion et forum DCP-o-matic |
| Court métrage en DCP (règle empirique) | ~-18 à -20 LUFS intégré, parole dans le niveau habituel d'un long métrage | | | Forum DCP-o-matic (anecdotique, à confirmer) |
| Podcast Apple | **-16 LKFS ±1 dB** | **-1 dBFS true peak** | non | Apple Podcasts for Creators, « Audio requirements » (page consultée le 10/10/2026) |
| Livre audio ACX / Audible | **RMS entre -23 et -18 dB** (pas en LUFS) | **crêtes ≤ -3 dB** | bruit de fond ≤ -60 dB RMS | ACX Help « Audio Submission Requirements » (page actuelle) |
| Spotify | Normalisation à **-14 LUFS** (Quiet -19, Loud -11) | < -1 dBTP ; < -2 dBTP si le master dépasse -14 LUFS | non | Spotify for Artists, « Loudness normalization » (consultée le 10/10/2026) |
| Apple Music (Sound Check) | **~-16 LUFS** (inspiré de TD1008) | -1 dBTP conseillé | non | Meterplugs / I. Shepherd (03/2022). Pas de document Apple officiel trouvé : à confirmer |
| YouTube | **-14 LUFS** (consensus ; YouTube baisse le volume des sons forts mais ne remonte pas les sons faibles) | -1 dBTP conseillé | non | Aucune page officielle Google trouvée : à confirmer. « Stable Volume » (2023, TechCrunch) est une option de compression dynamique distincte |

## Recommandation pratique : film corporate

1. **Master principal web / lecteur intégré / réseaux** : **-16 LUFS intégré, true peak ≤ -1 dBTP**, LRA d'environ 6 à 10 LU. La voix doit rester intelligible sur haut-parleurs d'ordinateur portable. Ce niveau correspond à TD1008 pour la parole (-18) avec 2 LU de marge et à Apple Podcasts, et il reste proche de la cible -14 de YouTube et Spotify : le lecteur baissera le son de 2 dB tout au plus, sans le remonter.
2. **Version événement / salle / salon** : partir du même mix. Sur sono de lieu, livrer à **-18 LUFS, -1 dBTP** (plus de marge pour le régisseur), avec une LRA plus faible (≤ 6 à 8 LU) si le lieu est bruyant (salon). Toujours faire un test de niveau sur place. Le niveau réel dépend du réglage de la sono, pas du fichier.
3. **Diffusion TV** : livrer une version séparée à **-23 LUFS ±0,5, -1 dBTP**, conforme à la fiche technique du diffuseur (PAD).
4. **Projection cinéma (DCP)** : ne pas viser un LUFS. Mixer dans une salle calibrée à 85 dBC (ou à 79 à 82 dBC pour une petite salle), puis vérifier le **Leq(m) ≤ 85** pour un format de type bande-annonce. Pour un court métrage, un repère approximatif est -18 à -20 LUFS (à confirmer).
5. **Toujours** : limiteur true peak avant l'encodage AAC/MP3, contrôle sur haut-parleurs de portable et de téléphone, et toujours le même master pour toutes les versions web.

## Sources

- AES TD1008 (doc. officiel) : https://www.aes.org/technical/documentDownloads.cfm?docID=731 (403 lors de la consultation, non lu directement)
- Production Advice (I. Shepherd), résumé de TD1008 : https://productionadvice.co.uk/td1008/
- Telos Alliance, « Understanding Loudness for Streaming Audio » (compromis à -17) : https://docs.telosalliance.com/docs/understanding-loudness-for-streaming-audio
- Radio World sur TD1008 : https://www.radioworld.com/?p=115138
- Production Expert, de TD1004 à TD1008 : https://www.production-expert.com/production-expert-1/aes-update-loudness-recommendations-for-audio-only-streaming
- Citations de TD1008 §4 et §7B (true peak), source secondaire : https://raw.githubusercontent.com/M-Igashi/baken/main/docs/true-peak-ceiling.md
- Apple Podcasts, Audio requirements : https://podcasters.apple.com/support/audio-requirements
- ACX, Audio Submission Requirements : https://help.acx.com/s/article/acx-audio-submission-requirements
- Spotify for Artists, Loudness normalization : https://support.spotify.com/us/artists/article/loudness-normalization/
- Meterplugs, Apple passe au LUFS (-16) : https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html
- TechCrunch, YouTube Stable Volume (07/2023) : https://techcrunch.com/2023/07/17/youtube-is-testing-a-new-stable-volume-feature-across-its-mobile-apps/
- ISDCF Doc 11, mesure de la loudness des films (TASA, 85 Leq(m)) : https://files.isdcf.com/papers/ISDCF-Doc11-MovieLoudnessMeasurement20160315.pdf
- Forum DCP-o-matic (repères LUFS pour les courts, Leq(m) comme plafond) : https://dcpomatic.com/forum/viewtopic.php?p=12379
- J. Nilo, loudness des dialogues pour la vidéo (corporate -16 / -1 dBTP) : https://josephnilo.com/blog/dialogue-loudness-lufs-true-peak-video/
- EBU R 128 v4 et R 128 s1 : https://tech.ebu.ch/docs/r/r128v4_0.pdf, https://tech.ebu.ch/publications/r128s1

## Ce qui reste incertain

- **True peak et LRA de TD1008** : le PDF AES n'a pas pu être ouvert (403). Le -1 dBTP en entrée de codec et la nuance -0,5 dBTP viennent de citations secondaires.
- **YouTube -14 LUFS** et **Apple Music -16 LUFS** : valeurs admises par la profession, mais aucune page officielle de Google ou d'Apple n'a été trouvée.
- **Salle de réunion et salons** : aucune norme ni source primaire. Les chiffres donnés sont des usages de praticiens.
- **Cinéma** : pas de correspondance officielle entre Leq(m) et LUFS. Les repères LUFS des courts métrages sont anecdotiques. SMPTE RP 200 (calibration à 85 dBC) est un document payant, non consulté directement.
- **ACX** : le seuil de bruit de fond diffère selon les versions (« ≤ -60 dB » sur la page actuelle, « -60 à -50 » dans d'anciennes citations).
