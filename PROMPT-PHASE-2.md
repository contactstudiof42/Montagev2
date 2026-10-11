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
- Sources HDR (session 2, *Whiplash*) : une source PQ (HDR10) lue comme du SDR donne des images grises et délavées, donc des mesures de couleur fausses. Vérifier `color_transfer` avec ffprobe ; si `smpte2084` ou `arib-std-b67`, lancer `HDR=1 passe_globale.sh` (conversion VideoToolbox, le ffmpeg Homebrew n'a ni zscale ni libplacebo). Source HDR **en AV1** (session 8, *Spider-Verse*) : la puce ne décode pas l'AV1 en matériel ; `passe_globale.sh` le détecte et passe par libdav1d + `hwupload` + `scale_vt` (environ 10 fois le temps réel).
- Calage sur la musique : `labo/outils/calage.py` compare les coupes aux attaques fortes et aux temps **contre le hasard** (mêmes coupes décalées). Ne jamais écrire « calé sur le beat » sans ce contrôle : sur un tempo rapide, presque toute coupe tombe près d'un temps.
- Parole de Diego (session 2, retour du 2026-10-11) : n'attribuer à Diego que ce qui vient de GOUTS.md, RETOURS-DIEGO.md ou d'une note de NOTES-DIEGO.md écrite par lui. Une ligne qui ressemble à un exemple de format (sous la consigne « Format : … ») n'est pas un goût. Dans le doute, l'écrire comme mon choix.
- Les deux erreurs dans le même film (session 3, *Mad Max: Fury Road*) : les éclairs de la tempête doublent le compte (146 coupes détectées, 77 réelles en 170 s), alors que l'action accélérée et sombre en cache (un « plan » de 15,7 s qui en contient au moins 8). **`verif_plan.py` échoue aussi sur l'action accélérée** : quand toutes les images changent beaucoup, aucun pic ne ressort. Avant de citer un pic ou un creux de densité : recompter le passage avec `verif_plan.py`, et regarder une tuile à 2-4 images/s sur tout « plan » long d'une scène d'action.
- Vidéo très sombre (session 3, Ziak) : deux détecteurs différents avaient compté 88 plans ; il y en a environ 109. **Éclaircir une copie de travail** (`curves=all='0/0 0.06/0.35 0.25/0.7 1/1'`) puis relancer PySceneDetect retrouve les coupes, mais compte aussi les éclairs et les étincelles : trier chaque coupe nouvelle à l'œil sur une paire d'images (0,25 s avant / après). Refaire ensuite les mesures qui dépendent des coupes (calage, densité) : avec les coupes manquantes, j'avais cru que le clip « évitait » les attaques fortes.
- `verif_plan.py` supposait 23,976 i/s : faux sur un clip à 25 i/s (minutages décalés de 4 %). Corrigé en session 3 (fréquence lue dans le fichier). Vérifier la fréquence de tout outil hérité des films avant de l'appliquer à un clip ou une pub.
- Ne pas déduire le rapport à la musique d'une esthétique (session 3, *Stress*) : j'avais écrit en phase 1 « pas de coupes sur le beat » parce que le clip imite le reportage ; mesuré, ses rares coupes tombent sur les grands accents. Tester contre le hasard sur la musique séparée de la voix (demucs, 1 min pour 7 min de son).
- Calage mesuré sur le mixage = suspect (session 4, HOUDI « Belle chanson ») : sur le son complet, 45 % des coupes sur un temps contre 27 % au hasard ; sur la musique séparée de la voix, 27 % contre 24 %, donc rien. **Toujours confirmer un calage sur la musique séparée** (`AUDIO=…/no_vocals.wav calage.py …`, demucs en 10 s pour 4 min) avant de l'écrire. `calage.py` lit désormais la fréquence d'images (il supposait 23,976 i/s).
- Whisper invente (session 4) : sur une piste sans voix, il écrit « Sous-titrage Société Radio-Canada » ou « Sous-titrage ST' 501 » (Lacoste, EGO) ; sur une longue vidéo, il peut **boucler** sur une phrase (25 répétitions dans « Le jour où la CIA… », fin d'adidas). Avant de citer une transcription, chercher les lignes répétées (`sort | uniq -c`) et les phrases fantômes ; **`whisper-cli -mc 0` (sans contexte entre segments) corrige la boucle** [TESTÉ, session 5] : sur KAIZEN, la transcription normale bouclait de 30:15 à 48:18 (« T'as vu la vache ? » ×863) puis n'écrivait plus que « Sous-titrage ST' 501 » jusqu'à la fin (1 h 36 perdues) ; avec `-mc 0`, le même passage donne 152 segments sans répétition, 18 s pour 10 min. **Utiliser `-mc 0` par défaut sur toute vidéo de plus de 20 min.**
- Où est le sujet dans le cadre (session 3) : la saillance automatique (`centrage.py`, « spectral residual ») ne trouve pas le sujet (une fois sur trois) et donne le même chiffre pour tous les films. Ne pas l'utiliser. Compter à l'œil sur `echantillon_tiers.py` (24 images au hasard, tiers tracés) et comparer à un autre film avec la même graine.
- Densité de fin et plans longs sur graphique (session 5, « Tiger » et « CIA ») : un **générique monté** (noms incrustés sur une rafale de plans d'une seconde) gonfle la densité des dernières minutes ; repérer le début du générique avant de citer la vitesse d'une fin. Et PySceneDetect peut rater la coupe d'un graphique sur fond uni vers un visage (« plan » de 19,7 s qui en contenait deux) : tuile à 1 image / 2 s sur tout plan long qui commence sur un graphique.
- Parole mesurée sous un fond musical (session 5, « Qui est l'imposteur ») : `coupes_parole.py` détecte la parole par l'énergie ; sous une musique continue il trouve 34 % de parole sur le mixage contre 77 % sur la voix séparée par demucs (« coupes pendant la parole » : 19 % contre 49 %). **Séparer la voix avant de mesurer coupes et parole** dès qu'il y a une musique ou un fond sous les voix (mettre `vocals.wav` en `audio16k.wav` dans un dossier à part, décalé par `adelay` au début de l'extrait). Les mesures déjà faites sur mixage avec musique (adidas « 68 % ») sont à revoir en passe de révision.
- Cartons de texte sur fond noir (session 5, YggTorrent) : PySceneDetect n'y voit pas les changements (un « plan » de 123 s en contenait au moins 20). Tuile à 1 image / 8 s sur tout plan long de texte. Inversement, des durées de plans trop régulières (Boxho : 89 plans de 1,52 s exactement, pics à 2, 4, 6, 8 s) sont un indice, pas une erreur de détecteur : regarder deux ou trois de ces plans avant de conclure.
- Projets du studio (session 6) : **commencer par `labo/outils/qc_livraison.sh FICHIER [cible]`** (pistes son, codec et bits, intégré, LRA, true peak, crêtes décodées, noir de début et de fin) : six fichiers F42 sur sept dépassaient -1 dBTP, un saturait au-dessus de 0 dBFS, un avait deux pistes mono. Un petit logo blanc sur noir est compté comme du noir par `blackdetect` : regarder l'image.
- Whisper `-mc 0` (session 6, Hirsingen, KAIZEN) : une même phrase aux **débuts exacts des fenêtres de 30 s** (0:30, 1:00, 1:30) sur un passage presque muet est suspecte (fantôme ou phrase dupliquée) ; les « Sous-titrage… » tombent aussi toutes les 30 s et marquent les passages sans voix (utile pour repérer la musique seule).
- Tuile à 1 image / 2 s (session 6, Hirsingen) : **une grosse amorce au premier plan** (un manteau, une épaule) peut faire croire à une alternance de plans d'une vignette à l'autre ; trancher à 4 images/s avant de compter.
- Film noir et blanc de nuit (session 7, *La Haine*) : le piège des scènes sombres y est massif (un « plan » de 173 s de vol de voiture en contenait 27, un de 195 s en contenait 9) ; la médiane et le nombre de plans de PySceneDetect sont faux. **Passer `verif_plan.py` sur tout plan de plus de 60 s dans une scène de nuit** avant de citer un compte ou une durée, puis recompter. Les cartons de texte sur noir se trouvent vite avec `blackdetect=d=1:pix_th=0.12` (une petite heure blanche passe pour du noir) : en tirer la liste, puis lire chaque carton sur une image recadrée.
- Voix séparée contre mixage, dans l'autre sens (session 7, *OSS 117*) : sur deux dialogues, `coupes_parole.py` donne 57 % et 52 % de coupes pendant la parole sur le mixage, **90 % et 86 % sur la voix séparée par demucs**, alors que la part de parole bouge peu (71 % / 76 %). La voix séparée peut combler les micro-silences (réverbération, fuite). Ne citer un pourcentage qu'avec sa source, et quand les deux divergent de plus de 15 points, marquer une vingtaine de coupes à la main (paire d'images + courbe de la voix) avant de conclure.
- Coupes et parole tranchées à l'œil (session 8, *OSS 117*) : sur 20 coupes regardées sur spectrogramme (mixage et voix séparée, ±0,6 s), 4 sont clairement pendant la parole, contre 57 % (mixage) et 90 % (voix séparée) pour `coupes_parole.py`. Cause : le seuil « percentile 20 + 10 dB » ; sur une voix séparée, le percentile 20 est un quasi-silence numérique et réverbération ou fuites passent pour de la parole. **Sur une voix séparée, lancer `SEUIL=haut coupes_parole.py … 15`** (seuil sous le niveau de la parole, pas au-dessus du plancher), et tenir tout pourcentage pour une borne haute : les coupes au bord d'un mot ne se tranchent que sur spectrogramme (`labo/outils/spectro_coupes.py`). Les mesures sur voix séparée déjà citées (« Qui est l'imposteur » 49 %) sont à refaire en passe de révision.
- Rafale de « plans » de durée identique (session 9, *Aftersun*) : une série de « plans » de 0,5 s exactement sur une image qui ne change pas = **détecteur saturé** (plan fixe sombre très saturé en rouge, générique déroulant), pas des coupes. J'avais annoncé « les stroboscopes de la rave » sans regarder : c'était un magasin de tapis (environ 60 fausses coupes, 5 vraies). Avant de nommer la cause d'une rafale, regarder la planche ; et **retirer logos et générique avant toute statistique** (ici 87 s de logos et 6 min 20 de générique, médiane 4,3 s brute contre 5,5 s sur le film seul). Les vrais stroboscopes (rave) rendent le compte indécidable : les exclure et donner la statistique « hors rave » à part.
- Animation à styles mêlés (session 9, *Across the Spider-Verse*) : un personnage animé par saccades en collage (Hobie) fait déclencher PySceneDetect toutes les 0,5 s sur un plan qui ne change pas ; même signature que le magasin de tapis d'*Aftersun* (séries de « plans » à la durée minimale). Compter ces séries (≥ 3 plans de 0,5 s d'affilée) donne une borne de l'erreur : 46 plans sur 2 826 ici, 69 sur 521 dans *Aftersun*. `calage.py` plantait sur la virgule finale de `ffprobe` (corrigé).
- `SEUIL=haut` n'est pas une correction universelle (session 9, révision) : sur « Qui est l'imposteur » (conversation à plusieurs sous musique, voix séparée), il donne 63 % de coupes pendant la parole contre 30 % à l'œil (l'ancien seuil 49 %) ; sur *Le Dîner de cons*, 36 % contre 21 %. **Le pourcentage « pendant la parole » ne se cite qu'après un spectrogramme** (25 à 30 coupes suffisent) ; l'outil sert à mesurer l'air (durée des silences), plus robuste.
- Whisper `-mc 0` n'empêche pas toute répétition (session 9, révision) : KAIZEN répète « Je m'entendais pas » 19 fois en 22 s (1:55:19-1:55:41). Le contrôle `sort | uniq -c` reste obligatoire avant de citer une réplique, même avec `-mc 0`.
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
