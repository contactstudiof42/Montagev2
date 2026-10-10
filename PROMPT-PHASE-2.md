# MISSION — PHASE 2 (LOCAL) : VOIR DE VRAIES VIDÉOS

Tu tournes en local sur le Mac de Diego, relancé par une routine. Ne pose aucune question : décide, note tes doutes dans RAPPORT.md, avance.

## Le but
En phase 1, tu as construit ton regard sur des textes et des maquettes. Ici, tu le confrontes à de vraies vidéos.
Pour chaque vidéo : qu'est-ce qui confirme tes skills, qu'est-ce qui les contredit, qu'est-ce qui est nouveau ?
Et surtout : apprendre le goût de Diego et comprendre ce que fait Studio F42, pour l'aider à faire mieux.

## Le matériel (dans videos/, inventaire dans PROGRESS.md)
- films/ : 13 films entiers.
- clips/ : 8 clips.
- pubs/ : 7 publicités choisies par Diego.
- youtube/ : 10 vidéos (dont EGO, vulgarisation au rendu cinéma, et des formats de divertissement).
- projets-f42/ : les projets du studio. Lis d'abord projets-f42/A-LIRE.md.
- NOTES-DIEGO.md (facultatif) : ce que Diego aime, minutages de scènes, contexte des projets.
- Pas de contre-exemples : Diego n'en fournira pas, ne les réclame pas. Ce qu'il n'aime pas se déduit de ses retours.

## Ordre de travail
0. Si le skill montage-nouvelle-reference n'existe pas, crée-le d'abord (méthode d'analyse d'une référence ajoutée plus tard, vidéo ou simple nom).
1. Films vague 1 : Interstellar, Joker, Whiplash, Le Dîner de cons, Mad Max: Fury Road. Puis un bilan de vague dans RAPPORT.md.
2. Clips, puis pubs.
3. YouTube.
4. Projets Studio F42.
5. Films vague 2 : Avengers: Infinity War, Forrest Gump, La Haine, OSS 117 : Le Caire, nid d'espions. Bilan de vague.
6. Films vague 3 : The Social Network, Spotlight (compare les deux), Aftersun, Spider-Man: Across the Spider-Verse. Bilan de vague.
7. Synthèse finale : révision des skills, puis « PHASE 2 TERMINÉE » dans PROGRESS.md.

## Méthode pour un film entier (deux passes)
1. Passe globale, peu coûteuse : copie légère (480p) dans videos/_travail/, détection de toutes les coupes, courbe de densité de coupes par minute, courbe de volume, transcription ou sous-titres, planches contact basse résolution de tout le film (environ une vignette toutes les 10 s). Elle donne la forme et le rythme du film entier.
2. Choix de 5 à 8 séquences clés, à partir de cette passe et des minutages de NOTES-DIEGO.md.
3. Analyse fine de ces séquences : une image par plan, son aligné sur la même ligne de temps. Pas plus d'environ 150 images regardées par film.
4. Si une fiche de phase 1 existe sur ce film ou son auteur (culture/), confronte-la au film : ce qui tient, ce qui est faux.

Clips, pubs et YouTube : la même méthode, en une passe, sur la vidéo entière. Pour une pub, regarde aussi comment le message et la marque arrivent en 15, 30 ou 60 secondes.
Projets Studio F42 : suis A-LIRE.md. Quand des rushes sont fournis, compare rushes et montage final : ce qui a été gardé, coupé, raccourci, et pourquoi.

## Ce que tu produis pour chaque vidéo
Une fiche analyses/<catégorie>/<titre>.md :
- intention : ce que la vidéo veut faire ressentir ou comprendre ;
- forme : durée, nombre de plans, courbe de rythme, structure ;
- choix par domaine : rythme, cadre, couleur, son, transitions, effets, typographie, avec des minutages précis ;
- ce qui confirme, contredit ou complète tes skills ;
- les principes transférables ;
- ce que Diego en a dit (NOTES-DIEGO.md, RETOURS-DIEGO.md).
Puis mets à jour les skills concernés. Un principe vérifié sur de vraies images passe en [VU SUR IMAGES].

## Outils (à installer en session 0, rien de payant)
ffmpeg (copies légères, extraction d'images, détection de coupes, volume EBU R128), une transcription locale adaptée au Mac (Whisper), Python avec numpy, pillow et librosa (tempo et temps forts de la musique). PySceneDetect et une séparation voix / musique si utile. Note le temps de chaque installation dans PROGRESS.md.

## Chaque session
1. Note l'heure de début (date). Tu travailles 50 minutes au maximum.
2. Fais d'abord le démarrage décrit dans CLAUDE.md (retours, boîte à références).
3. Reprends là où PROGRESS.md s'est arrêté. Un calcul long (copie légère, transcription) peut être fini dans une session et l'analyse faite à la suivante.
4. Commit et push après chaque vidéo analysée.
5. Fin : mets à jour PROGRESS.md (où reprendre) et la synthèse de RAPPORT.md (réécrite, pas empilée), commit, push, arrête-toi. Ne laisse aucun processus tourner.

## Quand la phase 2 est terminée
Les sessions suivantes ne font plus que le démarrage de CLAUDE.md (retours de Diego, boîte à références). S'il n'y a rien de neuf, dis-le en une ligne et arrête-toi.
