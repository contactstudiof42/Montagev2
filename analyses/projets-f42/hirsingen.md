# « Hirsingen » — court métrage d'époque (15 min, 5.1)

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°7). **État : complète (première passe + deux séquences fines)** (vignettes toutes les 10 s, 118 plans détectés, le plus long « plan » vérifié de trois façons, loudness et QC du fichier 5.1, transcription Whisper lue ; dialogue à la bougie 3:10-6:45 en plan par plan, 31 plans ; coupes / parole sur 7 min). Ouverture 0:00-2:52 en plan par plan (35 plans) faite en fin de session 6. Source : `HIRSINGEN 5.1 H265.mov`, HEVC 10 bits 3072×1306 (2,35:1), 25 i/s, 14 min 59, AAC 5.1. Je ne nomme pas les comédiens ; les prénoms des personnages viennent du dialogue. Pas de rushes._

**Lu avant l'analyse** : `A-LIRE.md`, `montage-regard`, `montage-grammaire` (champ / contrechamp, dialogue), `montage-rythme`, `montage-son-et-emotion`, `montage-loudness-livraison` (cinéma, 5.1), bilan de la vague 1 (plans longs réservés à ce qui compte). Goût de Diego qui s'applique (`GOUTS.md`, 7 et 8) : grain et look film ; visages sombres avec un minimum de lumière sur l'info.

## Intention [transcription, VU SUR IMAGES]
1944-1945 en Alsace (Hirsingen) : deux sœurs (Marie, Suzanne) trouvent en forêt un soldat de la Wehrmacht blessé, Franz, Autrichien enrôlé de force et déserteur. Elles le cachent ; Marie et lui se parlent à la bougie (sa femme, sa fille Sophia, la bougie qu'on allume à la fenêtre « pour que, même dans l'obscurité totale, vous retrouviez le chemin de la maison ») ; un résistant, Martin, est tué et la sœur aînée accuse Franz. Épilogue : « Lienz, Autriche — 1952 », une femme en voiture, une photo entre les mains : Marie va porter la mémoire de Franz à sa famille [DÉDUIT de l'image et du dialogue].

## Forme [mesuré]
- **118 plans détectés (un minimum : scènes sombres), ASL 7,6 s, médiane 4,6 s** ; 11 plans de plus de 15 s ; densité de 1 à 16 coupes/min. Le film le plus lent du studio, au tempo des fictions de la vague 1 les plus posées (Joker : médiane 4,5 s).
- **Structure** : ouverture en forêt presque muette (0:00-1:45 ; -45 LUFS la première minute) → capture et interrogatoire (1:45-3:10, la minute la plus coupée, 16/min) → dialogues à la bougie (3:10-11:40 ; plans tenus de 15 à 30 s, champ / contrechamp) → la rupture (12:04-13:36) → **7 s de noir** (13:36-13:43) → épilogue de 1952 (13:52, plan de 27 s) → générique.
- **Le plus long « plan » (12:04-13:36, 91,7 s) est un plan-séquence porté** [vérifié : `verif_plan.py` ne trouve aucune coupe, PySceneDetect non plus sur une copie éclaircie ; tuile à 2 images/s sur 12:06-12:30 : la caméra suit la dispute des deux sœurs à travers le linge qui sèche, d'un bout à l'autre de la pièce, et finit fixe sur Marie à genoux près du corps]. Un filé vers 12:27 pourrait cacher une coupe (leçon de *Stress* et *Whiplash*), sans changer le geste.
- **Son** (QC sur le 5.1 d'origine) : **-27,3 LUFS intégrés, LRA 20,9 LU, true peak 0,0 dBTP** ; un coup de feu à 6:50 [transcription].
- **Image** : intérieurs à la bougie et à la fenêtre, bois sombre, mur rouge, robe bleue de Marie ; forêt froide ; l'épilogue en lumière de jour.

## L'ouverture, plan par plan (0:00-2:52) [VU SUR IMAGES, mesuré]
Planche : `videos/_travail/f42-hirsingen/seq/s2.png` (35 plans, moyenne 4,9 s).
- **Le lieu et la date d'abord, en petit** (carton en bas à gauche sur le premier plan, une tasse, la cuisine), puis la ferme à la bougie en plans tenus de 10 à 15 s, sans un mot (0:00-0:34). Le même système ferme le film (« Lienz, Autriche — 1952 ») : **deux cartons de lieu et de date encadrent le récit**.
- **La découverte en forêt** (0:34-1:30) : Marie s'approche d'un homme couché, l'appelle plusieurs fois (« Monsieur ? », « Vous m'entendez ? ») ; plans de 2 à 20 s, le plus long sur la forêt où elle s'avance (19,9 s). Les appels de Whisper aux débuts des fenêtres de 30 s sont donc **plausiblement réels** (elle l'appelle à plusieurs reprises à l'image) ; à confirmer à l'écoute.
- **L'interrogatoire** (1:43-2:52) : champ / contrechamp avec **le fusil en amorce**, plans de 1 à 4 s (la minute la plus coupée du film, 16 coupes/min), et **un seul plan tenu, 13,5 s, sur Franz qui se présente** (« Je m'appelle Franz, je suis autrichien… Laissez-moi partir », 2:16) : la peur hache, la supplique se tient. Même règle que les films de référence et que « Fou-Rire ».

## Le dialogue à la bougie, plan par plan (2:52-6:51) [VU SUR IMAGES, mesuré]
Planche : `videos/_travail/f42-hirsingen/seq/s1.png` (31 plans, moyenne 7,7 s).
- **La distance dans le cadre suit la confiance** : d'abord deux plans larges fixes qui alternent (Marie à la table près de la bougie, Franz assis par terre contre le mur, 3:56-4:45, sept retours aux mêmes cadres de 3 à 13 s) ; puis Marie s'assoit plus près, cadrée de face en plan moyen (6:16) ; puis **le premier gros plan de Franz, tenu 14,3 s**, quand il parle de sa fille (« J'imagine qu'elle a bien grandi maintenant », 6:36). On se rapproche quand ils se rapprochent. [VU SUR IMAGES]
- **La coupe attend la fin de la réplique** : 27 % des coupes pendant la parole (3:10-6:45) et 42 % (7:20-10:45), pour 36 % du temps parlé ; les autres tombent dans le silence, environ 0,5-0,65 s après la réplique, la reprise 0,6 s plus tard. C'est l'inverse de la conversation filmée (« POPCORN » : 76-88 %) et proche de la scène sincère du *Dîner de cons* (21 %) : **le dialogue grave laisse l'air autour des mots**. [mesuré, énergie du mixage ; fond musical non vérifié par séparation]
- **Entre les répliques, le son tombe au plancher** (courbe momentanée à -50 LUFS dans chaque trou) : comme dans la loge de « Fou-Rire », aucune ambiance continue ne tient la pièce. Une ferme isolée en hiver a un son (vent, bois qui craque, feu, horloge) ; à confirmer à l'écoute. [mesuré, pas écouté]
- **Lumière** : Marie est lisible (fenêtre, bougie) ; Franz par terre en plan large (4:10, 4:18) est très sombre, son visage à peine dessiné : la règle de `GOUTS.md` (« un minimum de lumière sur l'info ») est tenue sur les gros plans, limite sur les larges. [VU SUR IMAGES]

## Ce qui marche (avec la preuve)
1. **Le plan long est réservé à ce qui compte**, comme dans les cinq films de la vague 1 : les confidences de Franz sont tenues 15 à 30 s (sa femme, sa fille, la bougie, 4:59-6:36, 9:28-10:40), et **la rupture est un plan-séquence porté de 91,7 s** où la caméra cesse d'être posée : la forme change quand la confiance se brise. [VU SUR IMAGES, mesuré]
2. **Le motif de la bougie** : dite par Franz (10:23-10:40), montrée à la fenêtre et sur la table (vignettes 4:00-4:40 ; la bougie près de la photo, 11:00), elle porte le titre moral du film ; l'épilogue en fait la promesse tenue (Marie retrouve « le chemin de la maison » de Franz). [VU SUR IMAGES, transcription]
3. **7 s de noir avant l'épilogue** : le plus grand vide suit le plus fort (la mort de Martin, l'accusation), comme Mad Max (9 s de noir après Nux). [mesuré]
4. **L'ouverture est presque muette** (1 min 45 sans dialogue, sauf l'appel « Monsieur, vous m'entendez ? ») : la forêt, la découverte, le corps ; on comprend avant d'entendre. [mesuré]
5. **Une couleur par personnage et par lieu** : robe bleue de Marie sur bois sombre et mur rouge ; la forêt froide ; l'épilogue clair. [VU SUR IMAGES, vignettes]

## Ce qui pourrait être meilleur, et comment
### Finition (corrigeable sans retourner)
1. **Le mixage n'est pas diffusable tel quel** : LRA 20,9 LU (le double d'un long métrage d'action, KAIZEN 12,3), -27,3 LUFS intégrés et **true peak à 0,0 dBTP**. Sur une télévision ou un ordinateur, les confidences à la bougie (minutes 7:00-8:00 et 11:00-12:00 à -50,6 et -53,3 LUFS de moyenne) seront inaudibles et le coup de feu saturera. Pour un festival : caler les dialogues (cible d'usage -27 LKFS mesurés sur le dialogue, ou -23/-24 LUFS en intégré selon le règlement), limiter à -1 dBTP (ou -2 en 5.1), et faire un **downmix stéréo** vérifié. Les six fichiers du studio sur sept dépassent -1 dBTP.
2. **Fichier de diffusion** : HEVC 10 bits + AAC 5.1 dans un .mov est un bon fichier de visionnage, pas un fichier de festival (DCP, ou ProRes + PCM selon le règlement). À livrer en plus.
3. (Vérifié sur images : les appels de l'ouverture sont plausiblement réels, voir plan par plan.)

4. **Une ambiance continue sous les dialogues** (voir plan par plan ci-dessus), même très basse : elle évite les trous de son entre les répliques et rendrait le mixage moins dynamique sans rien perdre.


## Grille (`montage-regard`, provisoire, sur la première passe)
| Critère | Note | Preuve |
|---|---|---|
| Intention | 3 | la bougie, la confiance, la promesse tenue en 1952 |
| Lisibilité | 2 | son trop dynamique pour une diffusion hors salle |
| Liaison | 3 | motif de la bougie, plan-séquence de rupture, noir avant l'épilogue |
| Rythme | 3 | plans longs réservés aux confidences ; capture plus coupée |
| Justesse | 2 | mixage : 20,9 LU de dynamique, 0 dBTP |
(Composition, couleur, mouvement, cohérence, originalité : à noter après le plan par plan.)

## Confirme, contredit, complète
- **Confirme** sur un film du studio « les plans longs sont réservés à ce qui compte » et « le plus fort est suivi du plus grand vide » (vague 1).
- **Complète** : **changer de grammaire de caméra au moment de la rupture** (plans posés pendant la confiance, plan-séquence porté quand elle se brise).
- **Leçon de méthode confirmée** : la vignette toutes les 10 s et le compte de PySceneDetect font croire à un « plan » ; ici les deux outils disent vrai (plan-séquence), mais seule la tuile à 2 images/s permet de le dire.

## Principes transférables (pour le studio)
1. **Un objet-motif dit, montré, puis accompli** (la bougie → la photo apportée en 1952).
2. **La caméra change de régime quand le récit change de régime.**
3. **Deux mixages** : salle (dynamique) et écran domestique (dialogues remontés, LRA ≤ 15 LU), toujours ≤ -1 dBTP.

## Ce que Diego en a dit
Rien sur ce projet (titre seulement dans `NOTES-DIEGO.md`).

## Révision (passe de révision, session 9, 2026-10-11)
Outils apparus après l'analyse (session 6) : `SEUIL=haut`, `spectro_coupes.py` (session 8) ; voix séparée par demucs sur 3:10-10:45 (la fiche notait « fond musical non vérifié par séparation »). Planche `hirsingen-revision-spectro.png` (32 coupes, une sur 2).
- Outil : 27 % et 42 % sur le mixage ; 23 % et 26 % sur la voix séparée (`SEUIL=haut`). **À l'œil : 2 coupes sur 32 au milieu d'une phrase (6 %), 12 au ras d'un mot (38 %, surtout juste après la fin d'une réplique), 18 dans un silence (56 %).**
- **Corrigée** : les pourcentages (27 et 42 %) ; le second venait surtout de bruits et de fins de mots comptés comme parole.
- **Confirmée et renforcée** : **la coupe attend la fin de la réplique**. C'est le film le plus « aéré » du corpus tranché à l'œil (POPCORN 60 %, adidas 48 %, Boxho 47 %, Imposteur 30 %, *Le Dîner de cons* 20 %, Hirsingen 6 %).
