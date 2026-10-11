---
name: montage-son-et-emotion
description: Le son au service de l'émotion — intention sonore, sound design, silence, ambiance, bruitage, musique avec ou contre l'image, raccord sonore, hors champ, voix off écrite après le montage. Mots entendus : « il manque quelque chose au son », « la musique écrase tout », « c'est trop illustratif », « on met quel son là-dessus ? », « on coupe la musique avant le logo ? », « ça sonne banque de sons », « on entend quelque chose qu'on ne voit pas ». Niveaux et normes : voir montage-loudness-livraison.
---

# Son et émotion

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow / ffmpeg (son jugé sur enveloppe ou voix de synthèse, pas écouté), hypothèse à confirmer en phase 2.

**Fait foi sur** : silence, sound design, musique avec ou contre l'image, hors champ, voix off. **Ailleurs** : où couper sur la musique, tempo et cadence → `montage-rythme` ; J/L-cut comme raccord de dialogue → `montage-grammaire` ; LUFS, true peak, downmix → `montage-loudness-livraison` ; SFX kinetic → `montage-kinetic-editing`.

Sources : `culture/walter-murch-blink-of-an-eye.md`, `culture/thelma-schoonmaker-raging-bull.md`, `culture/edgar-wright-montage-comique.md`, fiches Burtt et Rydstrom (`culture/`).

## Principes
1. **Le son fait la moitié de l'image, et souvent l'émotion entière.** On pardonne une image imparfaite, jamais un son faux. Penser le son dès l'intention, pas à la fin. [THÉORIQUE]
2. **Le silence est un événement.** Retirer le son juste avant l'impact (Schoonmaker) le rend plus fort ; mais un silence numérique absolu se lit comme une panne : garder un souffle d'ambiance très bas. [SOURCÉ] Vu sur *Interstellar* : pendant l'amarrage, les plans extérieurs ne sont **pas** silencieux (musique continue, -14 LUFS contre -12 à l'intérieur) ; le silence (-35 à -58 LUFS, environ 20 s) arrive **après l'effort**, quand Cooper perd connaissance. Le silence ponctue la fin de la tension. [VU SUR IMAGES, mesuré, pas écouté] Même structure sur *Joker* : le capot (1:51:29, -10,5 LUFS momentané en médiane) est suivi de 10 s de noir puis de l'hôpital presque muet (-41 LUFS) ; **le plus fort est suivi du plus grand vide** (deux films sur deux, `analyses/films/joker.md`). *Avengers: Infinity War* le fait aussi : après le claquement de doigts, la médiane de plan passe de 1,8 à 2,3, 4,6 puis 23,8 s et le son tombe de -25 à -37/-42 LUFS momentanés ; le film finit sur trois plans de 36, 13 et 35 s sans musique de victoire (`analyses/films/avengers-infinity-war.md`). *Whiplash* montre l'autre place du silence, celle de Schoonmaker : **10 s de silence juste avant le dernier coup** (1:41:31-1:41:41, -64 à -70 LUFS) sur un échange de regards, puis le coup à pleine puissance et la coupe au noir sur ce coup. Le silence avant l'impact pour le faire frapper ; le silence après l'effort pour le faire peser. [VU SUR IMAGES, mesuré, pas écouté] (`analyses/films/whiplash.md`)
3. **Le silence n'a de sens que s'il remplace un son déjà appris** : installer le son (deux fois, à une place exacte), puis le retirer ; le son ponctue la chute, il ne l'annonce pas. [SOURCÉ] (`culture/gags-de-montage.md`) Éprouvé : un « ting » sur la 1re image du plan, deux fois, retiré la 3e ; le seul son qui revient est celui de la réaction. [ÉPROUVÉ EN MAQUETTE] (pièce 27)
   Vu sur *La Haine* : les 13 cartons-horloge sur noir sont 13 trous de son (-36 à -58 LUFS momentanés contre -17 à -36 juste avant) ; le dernier est le seul où le silence commence **avant** le noir (juste après la mort de Vinz). Puis la fin est **un crescendo continu de 30 LU en 25 s** (de -48 à -17 LUFS) qui finit sur une détonation **hors champ, sur le noir** : on ne voit ni qui tire ni qui tombe. [VU SUR IMAGES, mesuré, pas écouté] (`analyses/films/la-haine.md`)
4. **Le son porte le raccord** (Murch) : un son qui se transforme relie deux plans mieux qu'un fondu ; un son qui anticipe le plan suivant tire en avant. [SOURCÉ]
5. **L'image la plus singulière sur l'absence sonore la plus forte** : une coupure musicale (break, silence, nappe seule) est la place du plan d'exception. [ÉPROUVÉ EN MAQUETTE] (pièce 03) Vu sur des clips en plateau à -10 LUFS : les rares creux sont des ponctuations de montage. *Stress* : 0,6 s de silence juste avant la bagarre du métro, puis la musique coupée net (4 s de silence total) sur le noir final ; *Au DD* : quasi-silence sur le carton-titre et un creux juste avant le travelling arrière qui révèle la foule ; *Mad Max* : 9 s de noir pendant que le son retombe de -11 à -36 LUFS après le sacrifice de Nux. [VU SUR IMAGES, mesuré, pas écouté] (`analyses/clips/justice-stress.md`, `analyses/clips/pnl-au-dd.md`, `analyses/films/mad-max-fury-road.md`) Le silence **ouvre** le sommet plus souvent qu'il ne le clôt : GENER8ION « STORM », 2 à 4 s quand Yung Lean se retourne vers la foule ; Lacoste, 2,4 s sur le plan large du court avant le geste final ; Intermarché « Conte de Noël », une demi-seconde avant l'acceptation du loup, puis **la musique retirée au retour au réel** (récit enchâssé). [VU SUR IMAGES, mesuré, pas écouté] (`analyses/clips/gener8ion-storm.md`, `analyses/pubs/`)
6. **Un son « autre » sous un geste réel** lui donne une charge qu'on ne sait pas nommer (animaux sous les coups de *Raging Bull*). En pub, gare à la dissonance avec le ton de marque. [SOURCÉ]
7. **Musique : ne pas surligner.** Celle qui dit la même chose que l'image est redondante ; contre l'image (Ellington sur *Anatomy of a Murder*), elle crée un second sens. [SOURCÉ]
8. **Bruitage amplifié et synchrone** = comédie et énergie (Wright) ; il doit aussi se lire visuellement pour les vues sans son. [SOURCÉ]
9. **La dynamique est une émotion** : ne pas écraser le mix ; les plateformes normalisent, l'écrasé paraît plat. [TESTÉ EN LABO] (voir `montage-loudness-livraison`)
10. **Partir d'une source réelle, puis la déformer** (Burtt : sabre laser = projecteurs + interférence TV) : tangible, alors qu'un preset paraît générique. [SOURCÉ]
11. **Une matière sonore par monde ou par personnage** (WALL-E contre EVE) ; l'intonation sans mots suffit à donner une âme à un objet (mascotte, logo). [SOURCÉ]
12. **Un son-signature en couches à rôles distincts** (Rydstrom, T-rex : aigu = identité, grave = poids, texture = menace). [SOURCÉ]
13. **Choisir un point d'audition et l'assumer** (Rydstrom, Omaha Beach) : un passe-bas fait entrer dans une tête ; la réouverture est le retour au monde. [SOURCÉ]
14. **Un son causé par l'image, seul, après le retrait du reste** (le ressac s'efface, restent les gouttes de la chaise) porte la fin. [ÉPROUVÉ EN MAQUETTE] (pièce 04)
15. **Le son d'un strobe est inventé** : un xénon fait au mieux un petit « tic », une LED est muette. Un SFX de décharge sonorise l'**idée** ; sur de la techno, un transitoire court et aigu sans queue grave, pour ne pas doubler le kick. [SOURCÉ] (`sources/strobe-son-et-lecture-reperage-2026-10.md`)

## Hors champ et présence non montrée [SOURCÉ] (`sources/surround-hors-champ-2026-10.md`)
- **Hors champ actif ou passif** (Chion) : l'actif pose une question et fait chercher ; le passif installe un territoire. Décider lequel **avant** de placer le son (*La Zone d'intérêt* : le camp n'est qu'entendu).
- **Acousmêtre** : une voix qu'on ne voit pas a des pouvoirs, perdus quand on montre le visage. Retarder la désacousmatisation, c'est garder la menace.
- **Présence dans les arrières** (ressenti [THÉORIQUE], chiffres [TESTÉ EN LABO]) : un son de territoire plutôt qu'une source ponctuelle ; petits indices intermittents ; **décorréler Ls et Rs** (la même ambiance mono s'annule en Lt/Rt écouté en mono : −70 LUFS) ; au downmix Lo/Ro un élément des arrières perd ~4,5 LU contre ~1,6 pour le mix (il recule de ~3 LU) ; rien d'essentiel dans le LFE ; pas de dialogue utile dans les arrières. Recettes ffmpeg : `montage-loudness-livraison` §5.1.

## Voix off écrite après le montage (principe Varda) [ÉPROUVÉ EN MAQUETTE] (pièce 33, voix de synthèse non écoutée)
- La voix dit **ce que l'image ne peut pas dire** (qui parle, le lien entre deux lieux, l'avant / après), jamais ce qu'elle montre.
- Couper au milieu d'une phrase fait porter le raccord par la syntaxe.
- Laisser 25-45 % de silence par plan ; retirer la phrase qui explique la dernière image.

## Clichés à refuser (sauf parti pris)
- Le *drone* grave qui monte pour signifier la tension.
- Le *whoosh* sur chaque transition, le *riser* + *impact* systématique — **sauf en kinetic editing réseaux, que l'utilisateur aime (`GOUTS.md`)** : le cliché n'est pas la quantité, c'est **l'uniformité** (même whoosh partout, mal calé, sans hiérarchie). Voir `montage-kinetic-editing`.
- La musique « inspirante » de banque sous un corporate ; la machine à écrire sous un texte qui s'écrit.

## Méthode
1. Écrire l'intention sonore en une phrase, avec l'intention visuelle.
2. Trois couches : ambiance (le lieu), bruitages (les gestes), musique (l'émotion) ; décider laquelle mène à chaque moment, et où est le silence.
3. Caler les événements à l'image près (à 25 i/s, 2 images de décalage se sentent sur un impact). [THÉORIQUE]
4. Mesurer loudness intégré, LRA, true peak ; vérifier le dialogue d'abord.
5. Sans écoute possible : juger par forme d'onde, enveloppes et mesures, et **noter que l'écoute reste à faire**.

## Recettes [TESTÉ EN LABO]
- Forme d'onde lisible (fond opaque) : `ffmpeg -i son.wav -filter_complex "[0]showwavespic=s=1000x160:colors=white:scale=sqrt[w];color=c=0x101820:s=1000x160[b];[b][w]overlay=format=auto" -frames:v 1 onde.png`
- Souffle synthétique par bruit coloré filtré : `atelier/01-respiration/souffle_son.py`.

## Reste à faire
Fiches Murch (*Apocalypse Now*), silence chez Kubrick / Bresson ; atelier « même image, trois bandes son (avec, contre, silence) » ; tout réécouter en phase 2.
