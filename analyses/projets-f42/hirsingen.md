# « Hirsingen » — court métrage d'époque (15 min, 5.1)

_Fiche ouverte le 2026-10-11 (phase 2, session 6, projet Studio F42 n°7). **État : première passe** (vignettes toutes les 10 s, 118 plans détectés, le plus long « plan » vérifié de trois façons, loudness et QC du fichier 5.1, transcription Whisper lue). **À faire** : deux séquences en plan par plan (l'ouverture en forêt, un dialogue à la bougie), écoute impossible. Source : `HIRSINGEN 5.1 H265.mov`, HEVC 10 bits 3072×1306 (2,35:1), 25 i/s, 14 min 59, AAC 5.1. Je ne nomme pas les comédiens ; les prénoms des personnages viennent du dialogue. Pas de rushes._

**Lu avant l'analyse** : `A-LIRE.md`, `montage-regard`, `montage-grammaire` (champ / contrechamp, dialogue), `montage-rythme`, `montage-son-et-emotion`, `montage-loudness-livraison` (cinéma, 5.1), bilan de la vague 1 (plans longs réservés à ce qui compte). Goût de Diego qui s'applique (`GOUTS.md`, 7 et 8) : grain et look film ; visages sombres avec un minimum de lumière sur l'info.

## Intention [transcription, VU SUR IMAGES]
1944-1945 en Alsace (Hirsingen) : deux sœurs (Marie, Suzanne) trouvent en forêt un soldat de la Wehrmacht blessé, Franz, Autrichien enrôlé de force et déserteur. Elles le cachent ; Marie et lui se parlent à la bougie (sa femme, sa fille Sophia, la bougie qu'on allume à la fenêtre « pour que, même dans l'obscurité totale, vous retrouviez le chemin de la maison ») ; un résistant, Martin, est tué et la sœur aînée accuse Franz. Épilogue : « Lienz, Autriche — 1952 », une femme en voiture, une photo entre les mains : Marie va porter la mémoire de Franz à sa famille [DÉDUIT de l'image et du dialogue].

## Forme [mesuré]
- **118 plans détectés (un minimum : scènes sombres), ASL 7,6 s, médiane 4,6 s** ; 11 plans de plus de 15 s ; densité de 1 à 16 coupes/min. Le film le plus lent du studio, au tempo des fictions de la vague 1 les plus posées (Joker : médiane 4,5 s).
- **Structure** : ouverture en forêt presque muette (0:00-1:45 ; -45 LUFS la première minute) → capture et interrogatoire (1:45-3:10, la minute la plus coupée, 16/min) → dialogues à la bougie (3:10-11:40 ; plans tenus de 15 à 30 s, champ / contrechamp) → la rupture (12:04-13:36) → **7 s de noir** (13:36-13:43) → épilogue de 1952 (13:52, plan de 27 s) → générique.
- **Le plus long « plan » (12:04-13:36, 91,7 s) est un plan-séquence porté** [vérifié : `verif_plan.py` ne trouve aucune coupe, PySceneDetect non plus sur une copie éclaircie ; tuile à 2 images/s sur 12:06-12:30 : la caméra suit la dispute des deux sœurs à travers le linge qui sèche, d'un bout à l'autre de la pièce, et finit fixe sur Marie à genoux près du corps]. Un filé vers 12:27 pourrait cacher une coupe (leçon de *Stress* et *Whiplash*), sans changer le geste.
- **Son** (QC sur le 5.1 d'origine) : **-27,3 LUFS intégrés, LRA 20,9 LU, true peak 0,0 dBTP** ; un coup de feu à 6:50 [transcription].
- **Image** : intérieurs à la bougie et à la fenêtre, bois sombre, mur rouge, robe bleue de Marie ; forêt froide ; l'épilogue en lumière de jour.

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
3. **Vérifier l'ouverture** : Whisper écrit « Monsieur, vous m'entendez ? » à 0:30, 1:00 et 1:30, exactement au début de ses fenêtres de 30 s ; c'est soit trois appels réels espacés de 30 s, soit une phrase fantôme répétée. À l'écoute : si l'appel n'est dit qu'une fois, rien à faire ; s'il y a trois appels identiques à 30 s d'écart, c'est un rythme mécanique à varier. [NON VÉRIFIÉ]

### À regarder en plan par plan (session suivante)
- Le dialogue à la bougie (3:10-6:40) : champ / contrechamp tenu ou coupé sur la réaction ? Où tombent les coupes par rapport à la parole (`coupes_parole.py`) ?
- Les plans les plus sombres : la règle de `GOUTS.md` (« un minimum de lumière sur l'info ») tient-elle sur les visages à la bougie ?

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
