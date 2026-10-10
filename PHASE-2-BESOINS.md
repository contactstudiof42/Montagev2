# PHASE 2 — ce dont j'ai besoin pour analyser de vraies vidéos

_Écrit le 2026-10-10, à la clôture de la phase 1. Pour vous : quoi m'envoyer, ce que je veux vérifier avec, et comment je « regarde » une vidéo._

## Comment m'envoyer les vidéos
- **Par lien de fichier** (Dropbox, Google Drive, WeTransfer) : YouTube est illisible depuis ma machine (elle est bloquée comme « robot »).
- MP4 H.264 suffit ; si vous avez le fichier d'origine (ProRes, log), envoyez-le pour les couples rushes + montage.
- **Des extraits de 1 à 3 minutes**, pas des films entiers. Nommez les fichiers par catégorie : `REF-joker-escalier.mp4`, `STUDIO-pub-xxx.mp4`, `RUSH-xxx/`, `CONTRE-xxx.mp4`.
- Les vidéos restent hors du dépôt Git (dossier ignoré) : je n'y copie que mes mesures et mes planches.
- Pour vos projets : quelques lignes de commentaire (ce qui marche, ce que vous changeriez, le brief d'origine) valent plus que la vidéo seule.

## La liste : environ 40 vidéos
| Catégorie | Quoi | Combien | Durée | Ce que je veux vérifier |
|---|---|---|---|---|
| **A. Vos références** (`GOUTS.md`) | **Interstellar** : l'amarrage (« No time for caution »), Cooper devant 23 ans de messages, le montage alterné planète d'eau / Terre | 3 | 2-3 min chacun | Mes fiches rythme : règle du temps entendue, alterné qui raccourcit (`montage-rythme`, pièce 29) |
| | **Joker** : la descente de l'escalier, la montée du début, le métro | 3 | 1-3 min | Dominante gardée, peau protégée, une couleur méritée ; posture selon l'axe et la focale (`montage-couleur-et-intention`, pièce 31) |
| | **Ziak**, « Même pas un grincement » : je l'ai déjà ; le revoir **avec le son** et mes mesures | 1 | entier | Montage calé sur l'arrangement et pas sur le beat (`culture/ziak…`) |
| | **EGO** : une ouverture, un passage de changement d'échelle, une fin | 3 | 1-2 min | Silence pendant le recul, témoin dans le cadre (pièce 22, `montage-youtube`) |
| | **Kinetic editing** : des edits que vous aimez | 4 | 30-60 s | Densité de coupes, SFX par seconde, calage au beat, transitions (`montage-kinetic-editing`) |
| **B. Projets du studio commentés** | Projets finis variés : pub, Reel / TikTok, clip, corporate, YouTube si vous en faites ; avec vos commentaires | 8-10 | 1-3 min | Votre goût réel au travail ; mes skills contre vos décisions ; formats que vous faites le plus |
| **C. Rushes + montage final** | Pour une même séquence : les rushes (10-20 min max) + le montage final + si possible l'export EDL ou XML | 5 couples | final 1-3 min | Ce qu'on garde et jette, où l'on coupe dans une prise (Murch, clignement), micro-sauts de jump cut (labo `micro-sauts`), durée des plans |
| | Idéalement : un face caméra / interview, une scène à deux personnes, un clip, un edit réseaux, un témoignage corporate | | | Jump cut et punch-in, champ-contrechamp et fond qui raccorde, calage musique, réaction tenue |
| **D. Contre-exemples** | Ce que vous trouvez raté, surcoté ou cliché : un kinetic surchargé, un corporate ennuyeux, une pub cliché de son secteur, une vidéo « qui fait IA », un clip sur-monté | 6 | 30 s - 2 min | Mes tests de cliché et de « ça bouge pour rien » (`montage-regard`, `montage-direction-artistique`) |
| **E. Scènes de vérification** (au choix, si vous les avez) | Un champ-contrechamp de fiction, un montage alterné classique (*Le Parrain*, baptême), un plan long tenu (Haneke), un gag de sitcom | 4 | 1-2 min | Principes `[ÉPROUVÉ EN MAQUETTE]` : raccord de fond, alterné, attente habitée, timing comique |

Ordre souhaité : A, puis C (le plus instructif), puis B, D, E.

## Les 10 questions sur vos goûts (réponses courtes suffisent)
1. Quels formats faites-vous le plus (pub, réseaux verticaux, corporate, clip, YouTube) ?
2. En général : plutôt **retenue** (plans longs, silence) ou **énergie** (montage serré, typo qui bouge) ? Ou selon le projet ?
3. Dans *Interstellar*, qu'est-ce qui vous tient : l'**accélération** du montage alterné, ou les **longs plans** où le temps s'arrête ?
4. Dans *Joker*, l'escalier vous plaît pour **le corps** (la danse), **la lumière**, ou le **contraste** avec la montée du début ?
5. Kinetic : **transitions tournées** (whip pans, rotations) ou **coupe sèche + bruitage d'impact** ?
6. Sous-titres animés pour les réseaux : mot qui **apparaît sec**, mot qui **« pop »**, ou ligne qui se **colore** au fil de la voix ?
7. L'image : **grain et défauts** (argentique) ou image **nette et propre** ?
8. La nuit : des visages qu'on ne voit **presque pas**, ou toujours **lire les yeux** ?
9. L'IA générative dans vos projets : **visible et assumée**, **invisible** (raccords, plans manquants), ou **à éviter** ?
10. Un film, un clip ou une pub que vous trouvez **surcoté**, et une typo ou une palette que vous **détestez** ?

Questions pratiques en plus (une ligne chacune) : cadence de vos projets (25 ou 30 i/s) ? rushes de téléphone en cadence variable ? normes de loudness pour vos livraisons TV ?

## Ma méthode pour « voir » une vidéo
Je ne regarde pas une vidéo en temps réel : je la découpe en images et en courbes, puis je lis les planches. Votre ressenti en salle reste la mesure finale ; mes mesures disent **où** regarder et **pourquoi**.
1. **Fiche technique** (ffprobe) : cadence (fixe ou variable), résolution, espace couleur, durée ; loudness intégré et true peak (ffmpeg `ebur128`).
2. **Coupes** : détection normalisée pour les images sombres (`labo/analyse-clip/analyse_clip.py`, validé sur Ziak : 87 coupes là où l'outil standard en voyait 38) et `labo/outils/coupes.py` (fusion à ±1 image, robuste au grain). Si vous fournissez l'EDL ou le XML, il sert de vérité. Les fondus : `labo/fondus/variance.py`.
3. **Images**, à trois rythmes :
   - **1 image par plan** (milieu du plan) : la planche de tout le montage d'un coup d'œil ;
   - **première et dernière image de chaque plan** : la planche des raccords ;
   - **toutes les images (25 i/s) autour des coupes clés** et **2 images/s** sur les mouvements : la bande-film (`coupes.py`).
4. **Son** : courbe de volume court terme (LUFS toutes les 100 ms), tempo et temps forts (librosa, dans `analyse_clip.py`), coupes comparées aux temps et à la présence de la basse ; spectrogramme.
5. **Mesures ciblées** selon la question : densité d'événements par minute (`labo/youtube/densite.py`), micro-sauts de jump cut (`labo/micro-sauts/micro_sauts.py`), photosensibilité (`labo/photosensibilite/flash_check.py`), où va le regard (`labo/saillance/residu_spectral.py`), direction d'un whip (`labo/kinetic/whip-flot/`), temps de lecture d'un texte (`labo/paroles/temps_lecture.py`), tempos et cadences (`labo/outils/tempos.py`), luminance et part des couleurs chaudes (`analyse_clip.py`).
6. **Synthèse** : une fiche par vidéo (ce que je vois, ce que ça confirme ou contredit dans mes skills) ; les principes confirmés passent de `[ÉPROUVÉ EN MAQUETTE]` à `[VÉRIFIÉ SUR IMAGES RÉELLES]`.

### Outils qui manquent (à construire au début de la phase 2)
- **Transcription mot à mot horodatée** (faster-whisper, CPU) : indispensable pour les interviews, le face caméra et les paroles de clip. Non installé.
- **Séparation voix / musique / effets** (demucs) : pour juger la place de la musique et des bruitages. Non installé.
- **Détection de visages et de regards** (OpenCV ou MediaPipe) : pour placer automatiquement la boîte du visage dans `micro_sauts.py` et mesurer les sauts de regard.
- **Mouvement de caméra** (flot optique global : panoramique, travelling, zoom) : seulement partiel aujourd'hui (`whip-flot`).
- **Palette par plan** (couleurs dominantes, courbe de température sur le montage) : simple à écrire.
- **Un script unique `voir.py`** qui enchaîne les étapes 1 à 5 et produit le dossier d'analyse d'une vidéo.
- Ce que je ne peux pas remplacer : **écouter** et sentir le temps réel. Pour le son et le rythme ressenti, vos commentaires sont la référence.
