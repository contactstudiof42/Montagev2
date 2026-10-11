# The Social Network (David Fincher, 2010 ; montage Kirk Baxter et Angus Wall)

_Fiche ouverte le 2026-10-11 (phase 2, session 8, film vague 3 n°1). **État : passe globale + 3 séquences + coupes / parole de l'ouverture + calage d'Henley** ; restent les dépositions (raccords de parole) et la fin (voir « À faire »). Source : Blu-ray 1080p H.264 (SDR BT.709), **VO anglaise** (piste 3), sous-titres anglais complets (2 290). Travail dans `videos/_travail/socialnetwork/`. Planches commitées : `social-network-ouverture.png` (0:00-5:40), `social-network-facemash.png` (9:00-12:30), `social-network-henley.png` (1:24:10-1:26:20). Fiche de phase 1 confrontée : `culture/kirk-baxter-angus-wall-social-network.md`._

Skills relus : `montage-rythme` (densité, liste dite, timing), `montage-grammaire` (champ-contrechamp, J-cut, montage parallèle), `montage-son-et-emotion`, `montage-couleur-et-intention`, grille de `montage-regard`, et la fiche de phase 1 ci-dessus.

## Intention
Faire sentir une intelligence plus rapide que les autres, qui s'isole par sa vitesse ; raconter la fondation de Facebook comme un montage de témoignages contradictoires (deux dépositions et le passé).

## Forme [mesuré]
- **2 h 00 ; au moins 2 287 plans, ASL 3,2 s, médiane 2,2 s** (le plus rapide des films de la phase 2 après *Mad Max*, médiane 2,0 s), 27 plans de 15 s ou plus seulement. **-20,9 LUFS intégrés** (VO).
- **Densité haute et presque plate** : 15 à 30 coupes/min presque tout le film, sans creux de respiration (le minimum hors générique est 11-13/min). Crêtes : **la nuit de Facemash** (minutes 10-11, 32 et 44/min), une scène à la minute 67 (36/min), **Henley** (minute 85, 41/min). Ce sont des séquences de **processus ou de course**, pas le sommet dramatique.
- Volume : un long plateau parlé autour de -27 à -33 LUFS par minute, et **une seule masse forte** : la boîte de nuit avec Sean Parker puis Henley (minutes 80-85, -10 à -14 LUFS), à 70 % du film.
- **Couleur : sombre et ambrée** (luminance moyenne 41/255, à égalité avec *Whiplash* pour le film le plus sombre des 14 mesurés avec la même méthode ; chaleur 20,5 contre 6,2 pour *Spotlight* ; même famille ambre et sombre que *Whiplash*, 41 / 28,1) ; le troisième sixième (Californie, été) est le plus chaud et le plus saturé. [mesuré sur vignettes / 10 s]

## Séquences

### L'ouverture au bar (0:21-5:15) [VU SUR IMAGES, `social-network-ouverture.png`]
- **4 min 54 s de dialogue** (et non 7 min comme l'écrivait la fiche de phase 1 d'après The Ringer) : un plan à deux de 9,8 s pose les deux personnages, puis **un champ-contrechamp strict** Mark / Erica, environ 110 plans de 0,6 à 7,9 s, toujours les deux mêmes cadres, sans plan de coupe ni insert.
- **Les plans les plus longs vont aux répliques qui décident** : « Why would you ask me that? » (7,9 s), le début de la rupture d'Erica (7,7 s), « you're going to go through life… » (6,8 s). Le reste tient en 1 à 3 s.
- **Coupes et parole** [VU SUR SPECTROGRAMME, `spectro_coupes.py`, 23 coupes sur 111] : 7 clairement pendant la parole (30 %), 4 exactement à la reprise de l'autre, 12 dans un trou de 0,1 à 0,3 s. L'outil, sur la voix séparée avec `SEUIL=haut`, dit 79 % (la rumeur du bar passe dans la voix séparée). **Le chevauchement ne vient pas de coupes au milieu des répliques, mais de l'absence de trous** : sur le mixage, les rares silences entre répliques durent 0,06 à 0,23 s (quartiles). La fiche de phase 1 (« la coupe tombe souvent pendant une réplique ») est **à nuancer** : un tiers des coupes.
- **Sortie** : Mark quitte le bar, la parole cesse ; trois plans de nuit (3,7, 5,8 s) puis **un plan de 35 s** sur le campus pour le titre : la décompression après 5 min de débit (cf. principe « l'après est tenu »).

### La nuit de Facemash (9:00-12:30) [VU SUR IMAGES, `social-network-facemash.png`]
- 103 plans en 3 min 30 (ASL 2,1 s ; minute 11 à 44 coupes/min, le maximum du film). Quatre matières : le visage de Mark, **l'écran** (blog « Zuckonit », annuaires photo des maisons), les mains sur le clavier, et **en alterné la soirée du Phoenix Club** (le club où il n'entre pas : bus de filles, fête), plus les camarades de chambre.
- La voix off du blog est continue et **chaque maison citée reçoit son écran** (« First up is Kirkland », « Next is Eliot », Lowell, Adams, Quincy, Leverett) : **une liste dite, une image par élément**, troisième film où je le vois (après YouTube et *Forrest Gump*).
- **La rafale la plus dense du film est un homme qui tape** : la vitesse va à l'acte qui compte pour ce film (coder, se venger), pas à une action physique ; et l'alterné avec la fête qui l'exclut donne sa raison à la rafale.

### Henley (1:24:08-1:26:10) [VU SUR IMAGES, `social-network-henley.png`, calage mesuré]
- **Entrée par le noir** : la boîte de nuit (-9 LUFS momentanés) coupe sur **4,3 s de noir** où le son tombe à -28 ; puis un plan aérien de 6,1 s, flou de bord (effet maquette). Deux mondes forts séparés par un trou.
- **La course dure 96 s (1:24:23-1:25:59), environ 50 plans** détectés, plus le travelling. La fiche de phase 1 citait 57 plans [NON VÉRIFIÉ] : c'est plausible (50 plans + coupes ratées), pas confirmé.
- **Accélération mesurée** (médiane par fenêtre de 16 s) : 2,5 s → 8,6 s (un **vrai travelling de 13,9 s** qui longe le bateau, du large aux visages, vérifié par `verif_plan.py` et tuile : présentation de l'équipage) → 3,2 s → 1,3 s → 1,1 s → **1,0 s**. Elle **plafonne autour d'une seconde** pendant les 45 dernières secondes (plans de 0,5 à 1,8 s) : pas « plusieurs coupes par seconde » comme l'écrivait Moviegoings.
- **Calage** [mesuré, musique séparée par demucs, `calage.py`] : **aucun**, ni sur les attaques fortes (45 % contre 43 % au hasard) ni sur les temps (31 % contre 35 %), ni sur la course entière ni sur ses 45 dernières secondes. Le montage suit **la courbe du Grieg** (le volume monte de -19 à -11,5 LUFS jusqu'à 1:25:30), pas ses temps : la densité suit l'arrangement, comme dans les clips (Ziak, SDM). Le calage « sur les coups de rame » (Moviegoings) est visuel et n'est pas mesuré ici.
- **La fin** : le son retombe à l'arrivée (-17 puis -25/-30 dans le salon), un plan de paysage de 4,8 s, puis la réception en plans de 1 à 3 s et un plan de 13,9 s sur la conversation avec le prince : le vide après la course, puis l'humiliation en plan tenu.

## Ce qui confirme, contredit ou complète mes skills et fiches
- **Corrige** la fiche de phase 1 : l'ouverture dure 4 min 54 s de dialogue (pas 7 min) ; « la coupe tombe souvent pendant une réplique » ne vaut que pour un tiers des coupes, le chevauchement vient de l'absence de trous ; Henley n'atteint pas « plusieurs coupes par seconde » (plateau à 1 s) et ne coupe pas sur les temps de la musique.
- **Confirme** « le climax n'est pas plus rapide » (dixième film) : les crêtes sont Facemash et Henley, des processus et une course, pas le sommet dramatique (les dépositions, la trahison d'Eduardo).
- **Confirme** « une liste dite, une image par élément » (`montage-rythme`) : la nuit de Facemash.
- **Confirme** « la densité suit l'arrangement, pas les temps » (bilan des clips) et « l'accélération adossée à une musique qui accélère » (fiche de phase 1, principe 3), en précisant : sur la courbe, pas sur la grille.
- **Complète** « plus un film coupe vite, plus il doit respirer » (bilan vague 1) : *The Social Network* coupe vite **sans** creux ; il respire par le son (la sortie du bar, le noir avant Henley) plutôt que par le montage. Contre-exemple partiel, ou autre levier.

## Principes transférables
1. **Le débit vient de l'absence de trous, pas de coupes au milieu des phrases** : pour un dialogue « rapide », resserrer les silences entre répliques (0,1-0,2 s) avant de couper sur les réactions.
2. **Donner la rafale à l'acte qui compte pour le sujet**, même s'il est immobile (coder), et l'alterner avec ce qui l'exclut ou le motive.
3. **Accélérer sur la courbe d'une musique, pas sur sa grille** : faire passer la durée des plans de 3 s à 1 s pendant que le morceau monte, et plafonner (on ne lit plus rien sous 0,5 s).
4. **Séparer deux séquences fortes par un noir et un trou de son** (boîte de nuit → Henley).

## Ce que Diego en a dit
Rien (aucune note dans `NOTES-DIEGO.md`). Le film n'est pas dans GOUTS.md ; il est dans la liste de la mission.

## À faire
- Les dépositions : compter les raccords de parole (question en déposition, réponse dans le passé) dans le premier tiers (repère de la fiche de phase 1).
- La fin (Mark seul qui rafraîchit la page d'Erica, environ 1:53-1:56) et la trahison d'Eduardo (environ 1:43-1:45).
- Couleur par lieu (Harvard d'hiver / Californie) sur images extraites, pas sur la planche.
