---
name: montage-son-et-emotion
description: Le son au service de l'émotion — intention sonore, sound design, silence, ambiance, bruitage, musique avec ou contre l'image, musique sous les discours, raccord sonore, hors champ, voix off écrite après le montage, et ce que je mesure à la place de l'oreille. Mots entendus : « il manque quelque chose au son », « la musique écrase tout », « il faut une musique sous les discours », « c'est trop illustratif », « on met quel son là-dessus ? », « on coupe la musique avant le logo ? », « ça sonne banque de sons », « on entend quelque chose qu'on ne voit pas ». Niveaux et normes : voir montage-loudness-livraison.
---

# Son et émotion : ce que je mesure à la place de l'oreille

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Savoir (constats mesurés sur 45 vraies vidéos, principes vus sur les films, hors champ, voix off, clichés, recettes) : [savoir.md](savoir.md). Version d'avant : `archives/audit-2/skills/montage-son-et-emotion/`._

**Fait foi sur** : l'intention sonore, le silence, la musique avec ou contre l'image, le hors champ, la voix off, et la compensation de l'écoute. Où couper sur la musique : `montage-rythme` ; couper dans la parole : `montage-grammaire` ; LUFS, crête, downmix : `montage-loudness-livraison` ; SFX kinetic : `montage-kinetic-editing` ; écrire le texte d'une voix off : `montage-ecriture-scenario`.

## 1. Je n'entends rien : ce que je mesure, ce que Diego écoute [universel]
- **Je mesure** : la re-transcription du son rendu, lue comme un spectateur (phrases complètes, aucun mot coupé) ; l'alignement mot à mot avant toute coupe dans la parole ; l'écart entre la voix et la musique en dB (voix et musique séparées par demucs) ; les trous et les crêtes (spectrogramme, `ebur128`) ; l'attaque ou la crête de chaque son posé contre l'image de son événement.
- **Je ne perçois pas** : le timbre, l'émotion, la justesse d'une musique ou d'un bruit, une voix nettoyée qui sonne robotique, un SFX qui sonne « banque de sons ».
- **Donc** chaque note de livraison porte une liste minutée de ce que Diego doit écouter, du plus risqué au moins risqué (une réplique au micro lointain, une voix sous des cris, l'isolation de voix, la musique sous la parole, les fondus, le limiteur). Rien de sonore ne se déclare réussi sans cette écoute.

(Gagnée : V3b du film de mariage, paroles hachées que mes mesures ne voyaient pas ; « rien n'a été écouté » sur les deux projets.)

## 2. Trois couches, et laquelle mène
Ambiance (le lieu), bruitages (les gestes), musique (l'émotion) : décider à chaque moment laquelle mène, et où est le silence ; une ambiance continue sous toute la parole, jamais de son qui tombe au plancher entre deux répliques.

## 3. Une musique de fond sous les discours [genre : mariage et événement]
Les discours, vœux et lettres d'un film d'événement se posent sur une musique de fond, assez bas pour que chaque mot passe (au mariage, une version sans batterie ni basse, séparée en local, environ 19 dB sous la voix ; à faire écouter à Diego). (Diego, V3b du film de mariage : « il faut une musique de fond quand il y a les discours » ; portée classée par lui le 2026-10-13.)

## 4. Sans oreille, je ne coupe pas dans le son [universel]
Monté par script, je ne coupe jamais moi-même dans une phrase d'archive ou dans une musique (une phrase coupée en plein mot, une musique étirée en recollant des mesures : le résultat sonne faux). Je pose les extraits parlés en phrases entières, avec de la marge, la musique d'origine telle quelle, et je marque où le monteur devra couper. Le calage fin d'une accélération de coupes sur le tempo est aussi son travail. (Gagnée : projet du cabinet, 2026-10-29 ; leçon validée par Diego.)

## 5. Ce que les projets du cabinet ont appris (2026-10) [TESTÉ EN CONDITIONS RÉELLES]
Leçons validées par Diego (`/Users/diego/Post-prod clients/LECONS-A-REMONTER.md`), intégrées le 2026-10-29.
- **Voix témoin avant l'enregistrement** [universel] : sur la maquette, une voix de synthèse locale (celle du système, phrase par phrase, sur une piste à part) mesure la vraie place de chaque phrase. Les sous-titres seuls trompent : avec la voix témoin, on voit tout de suite les phrases qui débordent sur le plan suivant ou sur une archive.
- **SFX d'un mouvement animé** [universel] : caler le point le plus fort du son (pas son début) sur le pic de vitesse du mouvement, lu image par image dans les clés ou la table d'expression du travelling ; le pic du son se mesure à l'enveloppe. Pour un défilé très rapide d'années ou d'images, un effeuillage de papier (cartes, pages) sous un souffle raconte le temps qui file. Trier les whooshs sans écouter : [savoir.md](savoir.md), recettes.
- **Une série de coupes rapides** [genre : sound design, coupes rapides] : un son par coupe marche, mais des swishs font « transition ». Pour que ça fasse « cut » : des déclics secs (obturateurs d'appareil photo, clic métallique) en rotation entre 4 ou 5 sons, attaque entre 0 et 30 ms après la coupe. Contre-indication : un bloc où les coupes doivent glisser (transitions voulues, kinetic à whooshs, `montage-kinetic-editing`).
- **Où trouver les sons** : Artlist (téléchargement par Chrome) et Soundly (le monteur glisse les sons) : `montage-pilotage-mcp` § 4 ; les poser et les ranger dans Resolve : `montage-resolve`, recettes.
