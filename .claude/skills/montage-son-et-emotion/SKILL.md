---
name: montage-son-et-emotion
description: Rapport image et son au service de l'émotion — sound design, silence, ambiance, bruitage, musique contre ou avec l'image, raccord sonore, montage son, « il manque quelque chose au son », « la musique écrase tout », préparer une intention sonore pour une pub, un clip, un documentaire ou un générique.
---

# Son et émotion

Version 1 (session 1, 2026-10-09). Sources : `culture/walter-murch-blink-of-an-eye.md`, `culture/thelma-schoonmaker-raging-bull.md`, `culture/edgar-wright-montage-comique.md`, atelier `atelier/01-respiration/` (v4). Technique de niveau et de livraison : `montage-loudness-livraison`.

## Principes
1. **Le son fait la moitié de l'image, et souvent l'émotion entière.** Le spectateur pardonne une image imparfaite, jamais un son faux. Penser le son dès l'intention (`INTENTION.md`), pas à la fin.
2. **Le silence est un événement.** Retirer le son juste avant l'impact (Schoonmaker) le rend plus fort. Mais un silence numérique absolu se lit comme une panne : garder un souffle d'ambiance très bas.
3. **Le son porte le raccord** (Murch) : un son qui se transforme relie deux plans mieux qu'un fondu ; un son qui anticipe le plan suivant (pré-montage sonore, *J-cut*) tire le spectateur en avant.
4. **Un son « autre » sous un geste réel** lui donne une charge que le public ne sait pas nommer (animaux sous les coups de Raging Bull). À doser : en pub, gare à la dissonance avec le ton de marque.
5. **Musique : ne pas surligner.** Une musique qui dit la même chose que l'image est redondante ; la musique *contre* l'image (swing d'Ellington sur la dissection d'Anatomy of a Murder) crée un second sens.
6. **Le bruitage amplifié et synchrone** fait la comédie et l'énergie (montage hip-hop d'Edgar Wright) ; il doit aussi se lire visuellement pour les vues sans son.
7. **La dynamique est une émotion.** Ne pas écraser le mix pour « sonner fort » : les plateformes normalisent, l'écrasé paraît juste plat (voir `montage-loudness-livraison`).
- **L'image la plus singulière sur l'absence sonore la plus forte** : une coupure musicale (break, silence, nappe seule) est l'emplacement idéal du plan d'exception ; l'oreille s'ouvre, l'œil reçoit. Vérifié dans l'atelier 03 (le seul plan chaud posé sur la coupure devient l'événement du montage). [TESTÉ EN ATELIER]
8. **Partir d'une source réelle, puis la déformer** (Ben Burtt : le sabre laser = ronronnement de projecteurs + interférence TV) : un son enregistré et transformé paraît tangible ; un preset « whoosh » paraît générique. En kinetic, c'est ce qui sépare un montage SFX signé d'un montage de banque de sons.
9. **Une matière sonore par monde ou par personnage** (WALL-E mécanique et usé contre EVE synthétique) ; **l'intonation sans mots** suffit à donner une âme à un objet (mascotte, logo, produit qui « réagit »).
10. **Un son-signature se construit en couches à rôles distincts** (Rydstrom, T-rex : aigu = identité, grave = poids, texture = menace).
11. **Choisir un point d'audition et l'assumer** (Rydstrom, Omaha Beach : son étouffé, subjectif, puis réouverture) : un passe-bas suffit à faire entrer dans une tête ; la réouverture du mix est le retour au monde.
12. **Un son causé par l'image, seul, après le retrait du reste** (atelier 04 : le ressac s'efface, restent les gouttes qui tombent de la chaise) : le son le plus petit, s'il est le seul, porte la fin.
13. **Le son d'un strobe est inventé, et il faut le savoir** [THÉORIQUE, `sources/strobe-son-et-lecture-reperage-2026-10.md`] : un xénon fait au mieux un petit « tic » (onde de choc dans le tube) que le système son couvre ; un strobe LED est muet, à part son ventilateur. Aucune fiche ne donne de dB. Un SFX « relais / décharge » sur un coup de lumière sonorise l'**idée** de décharge, pas un son de salle. On l'emprunte au flash photo (pop, puis sifflement de recharge), à l'arc électrique ou à l'interrupteur de projecteur. Sur de la techno : un transitoire court et aigu calé sur le coup, sans queue grave, pour ne pas doubler le kick.

## Clichés à refuser (sauf parti pris)
- Le *drone* grave qui monte pour signifier la tension (je suis moi-même tombé dedans : atelier 01 v4).
- Le *whoosh* sur chaque transition, le *riser* + *impact* systématique de bande-annonce — **sauf dans le kinetic editing pour les réseaux, que l'utilisateur aime (`GOUTS.md`)** : là, la densité de SFX est le langage du style. Le cliché n'est pas la quantité, c'est **l'uniformité** : le même whoosh partout, mal calé, sans hiérarchie. Voir `montage-kinetic-editing`.
- La musique « inspirante » de banque de sons sous un corporate.
- Le son de machine à écrire sous un texte qui s'écrit.

## Méthode
1. Écrire l'intention sonore en une phrase avec l'intention visuelle.
2. Lister les **trois couches** : ambiance (le lieu), bruitages (les gestes), musique (l'émotion) ; décider laquelle mène à chaque moment, et où est le silence.
3. Caler les événements sonores sur l'image à l'image près (à 25 i/s, 1 image = 40 ms : un décalage de 2 images se sent sur un impact).
4. Mesurer : loudness intégré, LRA, true peak ; vérifier le dialogue d'abord.
5. Sans écoute possible (session cloud) : juger par forme d'onde (`showwavespic`), enveloppes et mesures, et **noter que le jugement à l'oreille reste à faire**.

## Recettes [TESTÉ EN LABO, session 1]
- Forme d'onde lisible (fond opaque, repères temporels) :
  `ffmpeg -i son.wav -filter_complex "[0]showwavespic=s=1000x160:colors=white:scale=sqrt[w];color=c=0x101820:s=1000x160[b];[b][w]overlay=format=auto" -frames:v 1 onde.png`
  (sans fond opaque, l'onde blanche sur PNG transparent est illisible.)
- Synthèse d'un souffle par bruit coloré filtré et enveloppes : `atelier/01-respiration/souffle_son.py` (numpy seul).

## À approfondir
- Fiches : faites — Ben Burtt, Gary Rydstrom (session 4, `culture/`). Reste : Murch (sound design d'*Apocalypse Now*), le silence chez Kubrick / Bresson.
- Atelier : même image, trois bandes son (avec, contre, silence) ; critique comparée.

## Présence non montrée et hors champ (session 6, sourcé : `sources/surround-hors-champ-2026-10.md`)
Quand un film doit suggérer sans trancher (un visiteur, une menace), le son hors champ est l'outil juste : il crée une présence que l'image ne confirme pas.
- **Hors champ actif ou passif** (Chion, *L'Audio-vision*) : l'actif pose une question (« qu'est-ce que c'est ? ») et fait chercher ; le passif installe un territoire et stabilise (rumeur de ville). Décider lequel on veut **avant** de placer le son. Cas extrême : *La Zone d'intérêt* (le camp n'est qu'entendu).
- **Acousmêtre** : une voix qu'on ne voit pas a des pouvoirs (tout voir, être partout) ; elle les perd quand on montre le visage. Retarder la désacousmatisation, c'est garder la menace.
- **Règles pour une présence dans les arrières** [THÉORIQUE pour le ressenti, chiffres TESTÉS EN LABO] :
  1. Préférer un son de territoire à une source ponctuelle unique (une source isolée dans une surround fait tourner la tête vers la sortie de secours).
  2. Présence active = petits indices intermittents (pas, frottement, respiration), puis ramener vers l'avant au moment choisi.
  3. **Décorréler Ls et Rs** : la même ambiance mono dans les deux arrières **s'annule entièrement** en Lt/Rt écouté en mono (-70 LUFS mesurés).
  4. **Au downmix stéréo Lo/Ro, un élément des arrières perd 4,5 LU** (-30,0 → -34,5 LUFS, revérifié en session 6) contre ~1,6 LU pour un mix complet : il recule d'environ 3 LU par rapport au reste. Écouter (ou mesurer) le Lo/Ro avant de valider.
  5. Rien d'essentiel dans le LFE : BS.1770 l'exclut de la mesure et `-ac 2` le jette.
  6. Pas de dialogue utile dans les arrières.
- Recettes ffmpeg (fabrication 5.1 de test, downmix ITU par `pan`, phase moyenne) et pièges (`-ac 2` est 7,6 dB trop bas : `aresample=rematrix_maxval=10` ou `pan`) : voir `montage-loudness-livraison` §5.1 et la source.
