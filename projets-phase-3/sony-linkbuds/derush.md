# Dérush — Sony LinkBuds Clip (événement KORE, 29/09/2026)

_Phase 3, session 1 (2026-10-11). Sources en lecture seule : `/Volumes/SSD FAST/SONY copy/`. Fichiers de travail (non commités) : `videos/phase-3/sony-linkbuds/_travail/` (proxies 640x360 25p convertis en 709, audio 16 kHz, planches `planches/derush_NN.jpg`, transcriptions, analyse musicale). Outils : `labo/outils/phase3/` (`inventaire.py`, `proxies.sh`, `planches_derush.py`, `analyse_musique.py`)._

## Inventaire technique [mesuré, ffprobe + XML caméra]
- **252 rushes, 40,4 min**, tous identiques : Sony **ZV-E1**, FE 24-70 mm F2.8 GM II, UHD 3840x2160, **50p** (pas de ralenti caméra : `captureFps` 50p partout), HEVC 4:2:2 10 bits, son caméra 2 canaux.
- **Tous en S-Log3 / S-Gamut3.Cine** (`CaptureGammaEquation = s-log3-cine`). Le XML cite une LUT de tournage « SLOG3 -1_7 » absente du dossier. Le flux ne porte aucun tag de transfert : **sans conversion, l'image sort grise**. Proxies et montage : conversion S-Log3 → Rec.709 (LUT Sony `SLog3SGamut3.CineToLC-709TypeA.cube` du dossier de Resolve, ou CST dans Resolve).
- Durées : 0,5 à 196 s, médiane 4,3 s. Tournage de 08:00 à 10:44 (horloge caméra, fuseau -05:00 : horloge mal réglée, ne pas s'en servir pour synchroniser).
- Son double système : **HF1** 9 fichiers (REC063-071, 48 kHz mono, de 3,6 s à 6 min 25), **HF2** 2 fichiers (REC062-063), **PERCHE** 3 fichiers (44,1 kHz stéréo : 4 s, **1 h 41** à partir de 09:39:13, 34 min à partir de 11:20:39).
- Musique : `messwave - easy.mp3`, 2 min 35.

## Musique [mesuré, librosa ; image `_travail/musique/musique.png`]
- **129,2 BPM**, mesure de 4 temps = **1,858 s** ; phrases de 8 mesures (14,9 s).
- Structure (ruptures + énergie par mesure) : 0-5,7 s intro clairsemée · 5,7-21,1 montée A · 21,1-35,7 montée B (plus dense) · **35,7 drop 1** (grosse caisse) jusqu'à 52,1 · 52,1-66 drop 1 bis (le plus fort, -9 dB) · 66-74,6 **pont calme** (-18 dB, plus d'aigus) · 74,6-88,4 reprise · **88,2-103,2 montée** (8 mesures, charleston qui revient) · 103,2-108,9 **coupure** : la mesure 52 (105,1 s) tombe à -24,7 dB, presque le silence · **108,9 drop 2** jusqu'à 133,2 · 133,2-148,2 dernier drop (-9 dB) · **148,24 arrêt net**, puis une queue faible jusqu'à 155.
- Les mesures 15, 19, 23, 31, 51, 55, 59, 67 n'ont presque plus de basses : la grosse caisse s'arrête une mesure avant chaque relance (appels).
- **Pour une minute avec une vraie fin** : le bloc **88,24 → 148,24 s dure exactement 60,0 s**, commence sur une tête de phrase, contient une montée, une respiration quasi silencieuse (à 16,9 s du montage), le drop (20,6 s du montage) et l'arrêt net de la fin du morceau. Aucun montage musical à faire, sauf pour loger le plan de fin Sony (voir `plan.md`).

## Parole (micros HF, transcription Whisper, non écoutée)
- **HF1 REC063** (4 min 37) : prises d'intro de l'animatrice face caméra. Meilleure formulation entendue (texte) : « Hello, aujourd'hui on se retrouve chez Kore à Réaumur pour faire tester les nouveaux écouteurs Sony LinkBuds Clip, avec un cours de renforcement musculaire. J'espère qu'ils sont en forme. » (prises à 2:25, 2:48, 3:29 ; à 2:05-2:23 elle bute sur « LinkBuds Clip » : à écarter).
- **HF1 REC070** (6 min 25) : **voix off produit**, plusieurs prises : « Le design ouvert des LinkBuds Clip, c'est LA solution pour vivre ton entraînement à fond. Musique, podcast, livres audio, sans jamais te déconnecter de ce qui se passe autour de toi. » (0:34, 1:09 « ça résonne », 1:48, 2:01 « une deuxième »). Écho de la pièce signalé par l'équipe : à écouter.
- **HF1 REC064-068, HF2 REC063** : témoignages de participantes après la séance (légèreté, « on les oublie », tenue pendant les mouvements « la tête en bas », entendre le coach et la musique en même temps, course à pied, open space, couleurs : beige, violet, rose). Phrases fortes : « on faisait plein de mouvements, la tête en bas… et ça n'a pas bougé » (REC064 2:02) ; « tu entends la personne à côté de toi comme s'il y avait une petite enceinte posée » (REC064 3:12) ; « on était tous coordonnés… tout le monde avec ses petits LinkBuds » (REC068 0:36-0:45).
- **Décision** : Diego veut « que du visuel » (pas de sous-titres) ; je ne monte **aucune parole porteuse de sens**. La voix off REC070 et la phrase « on était tous coordonnés » sont notées comme option pour une autre version.

## Rushes, par moment de la journée
_(Lecture des planches : 6 vignettes par rush, 12 au-delà de 20 s. « Bon » = utilisable ; timecodes en secondes depuis le début du rush.)_

**Tous les rushes sauf un sont verticaux** (métadonnée `rotation=90`, image 2160x3840 ; seul **C6729** est horizontal). Conséquence : pas de recadrage 16:9 → 9:16, et **2× de marge de zoom** pour les punch-ins dans un 1080x1920. Resolve applique la rotation à l'import [TESTÉ EN CONDITIONS RÉELLES]. Le lieu est le studio **KORE** (Paris, Réaumur), pilates sur *reformer* : un hall clair (boutique, café, vitrine sur rue) et une salle noire à néons verticaux blancs.

### 1. Hall et marque du lieu (C6478-C6497, ~1 min 30) — lumière du jour, tons beiges
- C6478, C6491-C6496 : logo KORE sur le comptoir et au sol, travellings latéraux (C6492, C6493 : lettres qui défilent, 1,4 s). C6485-C6486 : enseigne KORE en relief sur béton. C6479-C6484, C6487-C6490 : boutique (sacs, t-shirts, casquette, chaussettes, gourde) toutes marquées KORE.
- **Usage** : 1 ou 2 plans de lieu au plus (C6486 ou C6492). Tout est marqué KORE, pas Sony : en abuser fait une pub pour la salle. Mouvement latéral de C6492/C6493 = bon raccord de mouvement pour un whip.

### 2. Salle vide et produit (C6498-C6512)
- C6498-C6505 : salle noire vide, néons, reformers marqués KORE (C6500-C6502), travelling dans l'allée (C6505, 13,9 s ; bon à 6-9 s). C6503 : gros plan du tapis (numéro de machine) : texture.
- **Produit sur le reformer, salle noire** (le meilleur décor produit) : **C6506** (8,2 s, trois boîtiers rose / beige / vert d'eau, léger travelling, bon partout), **C6507** (45 s, macro qui glisse d'un boîtier à l'autre : beige net à 1,4 s, rose plein cadre 26-32 s, vert d'eau 32-35 s, **les trois en plan d'ensemble 38-45 s**), **C6508** (33 s, travelling avec néons et ressorts au premier plan, rose net 9-13 s et 21-27 s ; fin 30-32 s : néon qui passe devant = masque de transition).
- **Produit sur fond beige (hall)** : C6509 (trois boîtiers vus de dessus 0-3,5 s, puis la caméra bascule vers le sol en marbre : à jeter après 3,5 s), C6510, C6511 (boîtiers en gros plan, fixes), C6512 (vert d'eau au premier plan, léger mouvement). Plus lumineux, moins « sport » : contrepoint possible de la salle noire.

### 3. Accueil dans le hall (C6513-C6539)
- Participantes qui arrivent, discutent, rient ; un homme (staff KORE, t-shirt noir) donne des consignes (C6526, C6536, C6537 dos à la vitrine). Plans moyens, portés, sujets souvent décentrés et de dos.
- Bons : **C6514** (deux filles devant la vitrine, l'une montre son téléphone, rires 1,1-2,2 s), **C6534** (fille à lunettes et tatouages qui rit, 1,9 s, très vivant), C6515 (sourire à 0,8-1,6 s), C6517, C6535 (fille qui écoute, main à l'oreille 1-3 s : geste d'oreille), C6538 (même geste, main à l'oreille). C6519-C6523, C6527-C6533 : groupes qui écoutent, peu d'énergie.
- **Usage** : 2 ou 3 plans d'arrivée et de sourires au début (l'humain avant la séance).

### 4. Entrée dans la salle et installation (C6540-C6554)
- **C6540** (21 s) : couloir noir à néons, les participantes entrent une à une face caméra : **15,0-15,5 s une fille sourit et salue la caméra** (meilleur moment), 9,7-10 s deux filles qui rient, 17,8 s fille à lunettes. Excellent pour l'arrivée en rafale.
- C6541-C6546 : installation sur les reformers (de dos, néons). C6547-C6549 : salle qui se remplit (larges).
- **C6550** (9,1 s) : **la coach** (micro serre-tête, haut kaki) assise, parle et gesticule : 4,0-6,3 s le geste le plus fort.
- C6551 (19 s) : travelling de la salle jusqu'au dos d'une participante (fin 15,6-19 s, la coach dans le miroir). C6552 : participante qui se retourne vers la caméra (2,6-3,1 s) avec la coach au fond.
- C6553, C6554 : salle pleine, tout le monde assis, mains aux oreilles (on met les écouteurs !) : **C6553 1,4-4 s**, C6554 2,4-4,1 s.

### 5. Les écouteurs portés (C6555-C6566) — le cœur produit
- **C6555** (1,9 s, profil, dreadlocks, écouteur blanc + boucle, néons flous), **C6556** (profil, queue de cheval, écouteur net), **C6557** (de dos, chignon, écouteur, contre-jour néons), **C6558** (chouchou blanc, elle tourne la tête 3,5-4,3 s, écouteur visible).
- **C6559** (9,1 s) : **mise au point qui va du chouchou orange à l'écouteur dans l'oreille** (5,1-8,5 s : écouteur net en très gros plan) : plan produit-humain idéal.
- **C6560** (1,9 s) : très gros plan, écouteur blanc + boucle papillon sur cheveux noirs. **C6561** (3,8 s) : très gros plan d'oreille claire, écouteur et boucles dorées (net 1,2-3,1 s).
- **C6566** (4,8 s) : profil, écouteur net, **elle sourit en baissant la tête à 2,7-4,5 s**.
- C6562-C6565 : salle avant le cours (larges, participantes assises). C6564 : fille assise (chouchou orange au poignet).

### 6. Réglage des machines (C6567-C6569)
- C6567 : participantes qui règlent leur machine. **C6568** (5,8 s) : fille qui se penche sur les ressorts. **C6569** (6,2 s) : **main au chouchou orange qui accroche un ressort** (1,2-5,9 s, gros plan) : geste net, bon plan d'action « on y va ».
