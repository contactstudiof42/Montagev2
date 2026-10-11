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
7. Passe de révision (voir la section du même nom).
8. Synthèse finale : révision des skills, puis « PHASE 2 TERMINÉE » dans PROGRESS.md.

## Avant chaque vidéo : repartir de la phase 1
Relis le sommaire de `montage-expert`, la grille de `montage-regard`, les skills des domaines que la vidéo touche (rythme, couleur, son, formats, kinetic, youtube…) et les fiches de `culture/` liées à l'œuvre ou à son auteur. Tu analyses AVEC ce que tu sais déjà, pour le confirmer, le corriger ou le compléter : tu ne repars jamais de zéro. Chaque fiche cite les skills et fiches qu'elle confirme ou contredit.

## Méthode pour un film entier (deux passes)
1. Passe globale, peu coûteuse : copie légère (480p) dans videos/_travail/, détection de toutes les coupes, courbe de densité de coupes par minute, courbe de volume, transcription ou sous-titres, planches contact basse résolution de tout le film (environ une vignette toutes les 10 s). Elle donne la forme et le rythme du film entier.
2. Choix de 5 à 8 séquences clés, à partir de cette passe et des minutages de NOTES-DIEGO.md.
3. Analyse fine de ces séquences : une image par plan, son aligné sur la même ligne de temps. Pas plus d'environ 150 images regardées par film.
4. Si une fiche de phase 1 existe sur ce film ou son auteur (culture/), confronte-la au film : ce qui tient, ce qui est faux.

## Leçons de méthode (à appliquer à chaque vidéo, à enrichir)
- Coupes cachées (appris en session 0, SDM « #Malentouré », 0:47) : les détecteurs de coupes ratent les raccords par occlusion d'un corps ou par filé. Dans tout plan de plus de 15 s, regarde une image toutes les 2 à 3 s pour chercher une coupe cachée.
- Coupes ratées dans le sombre (appris en session 1, *Interstellar*, 37:45) : PySceneDetect adaptatif fusionne les champs-contrechamps sombres à faible contraste (un « plan » de 53 s en contenait au moins trois). Le nombre de plans d'un film est un minimum ; vérifier à l'œil tout plan long d'une scène de dialogue sombre avant de citer sa durée.
- Fausses coupes de lumière (session 1, *Joker*, métro) : un clignotement (tubes qui s'éteignent, flash, stroboscope) est compté comme une coupe. Avant de citer un pic de coupes, regarder la planche du passage ; les « plans » noirs de moins de 1 s sont suspects.
- Lignes d'un montage alterné : un classement automatique par couleur moyenne échoue (la glace chaude passe pour la Terre). Classer à l'œil sur une image toutes les 2 s (tuile ffmpeg `fps=1/2,tile=15x14`), environ 7 min par tuile.
- Plans-séquences invisibles sur une planche par plan (session 2, *Joker*, Pogo's 0:42:26) : une vignette par plan ne montre qu'une image, elle ne peut ni confirmer ni réfuter un plan long. J'avais cru faux un plan de 74 s qui est un vrai plan-séquence. Pour juger un plan long : `labo/outils/verif_plan.py` (pics de différence d'image, toutes les images) **et** une tuile à intervalle fixe (`fps=1/2`), puis 3 images/s sur le passage douteux.
- Sources HDR (session 2, *Whiplash*) : une source PQ (HDR10) lue comme du SDR donne des images grises et délavées, donc des mesures de couleur fausses. Vérifier `color_transfer` avec ffprobe ; si `smpte2084` ou `arib-std-b67`, lancer `HDR=1 passe_globale.sh` (conversion VideoToolbox, le ffmpeg Homebrew n'a ni zscale ni libplacebo).
- Calage sur la musique : `labo/outils/calage.py` compare les coupes aux attaques fortes et aux temps **contre le hasard** (mêmes coupes décalées). Ne jamais écrire « calé sur le beat » sans ce contrôle : sur un tempo rapide, presque toute coupe tombe près d'un temps.
- Parole de Diego (session 2, retour du 2026-10-11) : n'attribuer à Diego que ce qui vient de GOUTS.md, RETOURS-DIEGO.md ou d'une note de NOTES-DIEGO.md écrite par lui. Une ligne qui ressemble à un exemple de format (sous la consigne « Format : … ») n'est pas un goût. Dans le doute, l'écrire comme mon choix.
- Les deux erreurs dans le même film (session 3, *Mad Max: Fury Road*) : les éclairs de la tempête doublent le compte (146 coupes détectées, 77 réelles en 170 s), alors que l'action accélérée et sombre en cache (un « plan » de 15,7 s qui en contient au moins 8). **`verif_plan.py` échoue aussi sur l'action accélérée** : quand toutes les images changent beaucoup, aucun pic ne ressort. Avant de citer un pic ou un creux de densité : recompter le passage avec `verif_plan.py`, et regarder une tuile à 2-4 images/s sur tout « plan » long d'une scène d'action.
- Vidéo très sombre (session 3, Ziak) : deux détecteurs différents avaient compté 88 plans ; il y en a environ 109. **Éclaircir une copie de travail** (`curves=all='0/0 0.06/0.35 0.25/0.7 1/1'`) puis relancer PySceneDetect retrouve les coupes, mais compte aussi les éclairs et les étincelles : trier chaque coupe nouvelle à l'œil sur une paire d'images (0,25 s avant / après). Refaire ensuite les mesures qui dépendent des coupes (calage, densité) : avec les coupes manquantes, j'avais cru que le clip « évitait » les attaques fortes.
- Où est le sujet dans le cadre (session 3) : la saillance automatique (`centrage.py`, « spectral residual ») ne trouve pas le sujet (une fois sur trois) et donne le même chiffre pour tous les films. Ne pas l'utiliser. Compter à l'œil sur `echantillon_tiers.py` (24 images au hasard, tiers tracés) et comparer à un autre film avec la même graine.
- Règle d'auto-correction : quand tu découvres une erreur ou une limite de ta méthode, inscris la correction ICI (ou dans le skill concerné), pas seulement dans la fiche de la vidéo. Sinon les sessions suivantes ne la connaîtront pas.

## Passe de révision (étape 7, avant la synthèse)
Tes outils et tes leçons de méthode se sont améliorés en cours de route ; les premières vidéos ont été analysées sans eux. Tu ne refais pas les analyses entières : tu vérifies ce que les nouveaux instruments peuvent changer.
1. Liste les outils et les leçons de méthode apparus après chaque vidéo (dates des commits, `labo/outils/`, section « Leçons de méthode »).
2. Pour chaque vidéo analysée avant leur apparition, relance-les seulement sur les séquences concernées (parole, musique, plans longs, scènes sombres, sources HDR…). Pas de nouvelle passe globale si la sienne est encore utilisable.
3. Pars des mesures, pas de ta fiche : relis la fiche seulement après avoir mesuré, pour ne pas te confirmer toi-même.
4. Dans la fiche, ajoute une section « Révision » : chaque conclusion vérifiée marquée confirmée, corrigée ou nouvelle, avec la mesure. Si une conclusion change, corrige aussi le skill concerné et inscris la leçon dans « Leçons de méthode ».
5. Dans RAPPORT.md, donne le bilan chiffré : combien de conclusions confirmées, corrigées, nouvelles, et ce que ce taux dit de la fiabilité des analyses « à l'œil ».
Commit et push après chaque vidéo révisée. Compte deux à trois sessions, pas plus.

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
