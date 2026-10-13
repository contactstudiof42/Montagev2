# RAPPORT — synthèse

_Réécrit le 2026-10-13 (audit 2). La synthèse de fin de phase 2 et du début de la phase 3 est archivée dans `archives/phase-2/RAPPORT-synthese-phase-2-et-debut-phase-3.md` ; les bilans détaillés de la phase 2 dans `archives/phase-2/RAPPORT-bilans-detailles-phase-2.md`. Ce fichier tient : où j'en suis, ce que les projets ont montré, mes hypothèses de goût (niveau 4 de la hiérarchie : jamais la parole de Diego) et mes doutes._

## Où j'en suis
- **Phase 2** (terminée le 2026-10-11) : 45 vraies vidéos analysées, puis 13 références ajoutées par Diego (réseaux, méthode d'étalonnage, références des deux projets) ; fiches dans `analyses/`.
- **Phase 3, deux projets montés dans Resolve par son serveur MCP** : un film de marque kinetic d'une minute (V2 50 % → V5 80-85 %, quatre retours très guidés) et un film de mariage de cinq minutes à partir de 1 163 rushes (V3b 10 %, V4 25 % après l'arrivée du directeur artistique et de la relecture par re-transcription ; projet clos par Diego : « le mariage, c'est trop d'émotion pour un robot »).
- **Audit 2** (2026-10-13) : un règlement plus court (de 69 000 à environ 28 000 mots chargés d'office), une carte de ce que je perçois et ne perçois pas, la hiérarchie du goût, une seule liste de contrôle, des skills transportables.
- **Prochaine étape** : des exercices techniques courts dans After Effects et Blender (`PLAN-TESTS.md`), après les installations et réglages de Diego.

## Ce que les deux projets ont montré
- **Ce qui marche** : le dérush (tout regarder, tout transcrire, trouver les séries du cadreur, les « petits mots », l'anecdote qui ouvre le film) ; la synchro de plusieurs caméras par corrélation audio ; la recherche dans la parole ; la coupe au mot près par alignement forcé et la relecture du rendu par re-transcription (quatre défauts trouvés que mes contrôles ne voyaient pas) ; le directeur artistique à froid ; le pilotage de Resolve par script (poser à l'image près, animer, étalonner par LUT et CDL, rendre, mesurer).
- **Ce qui ne marche pas encore** : tout ce qui se juge en mouvement, à l'oreille ou dans la durée ressentie (plans qui tremblent, milieu qui ennuie, musique absente sous les discours, effets « cheap ») ; me juger moi-même (vingt coches du carnet pour un film à 10 %) ; tenir un seuil de mesure d'un projet à l'autre (68 plans sur 83 au-dessus d'un seuil hérité) ; le choix et le placement des plans non humains ; l'étalonnage au niveau de Diego (« beaucoup trop loin de ce que je suis capable de faire »).
- **Ce que j'en retiens** : une mesure vérifie, elle ne juge pas ; ce que je ne perçois pas, je le compense (planche côte à côte, directeur artistique, re-transcription, liste de ce que Diego doit regarder et écouter) ou je le signale, jamais je ne le déclare réussi.

## Hypothèses de goût (les miennes, à confirmer par Diego ou par d'autres références)
- **Films de mariage** : les trois références qu'aiment les mariés et Diego partagent un look pellicule olive aux noirs denses ou un N&B neutre, des coupes sur les temps et un humour qui vient des mariés eux-mêmes (regard caméra, répliques) ; le N&B y est toujours une séquence avec un sens, jamais un filtre. Hypothèse d'un goût « élégant et drôle » où l'effet reste rare.
- **La structure de la V4 du mariage** (une idée qui revient, deux rappels comiques tirés de la matière, un seul changement de look qui a un sens) : jugée « au niveau » par le directeur artistique, jamais validée par Diego.
- **Le kinetic de Diego** (« un mélange des deux », `GOUTS.md`) : ses références réseaux mettent souvent un look pellicule et une typo serif fine (darius, équipe de France) ; deux traits revenus au moins trois fois, pas encore dits par lui.
- **Le look film** revient dans ses références (pasalu, darius, l'équipe de France, le tutoriel du look de *Seven*) ; ce qu'il en attend d'abord est une méthode simple pour reproduire un look, pas un goût nouveau.

## Doutes
- **Rien n'a jamais été écouté** : tout jugement sonore vient de mesures, de spectrogrammes et de re-transcriptions.
- **La conversion du log qui garde les blancs** (V4 du mariage) est validée par le directeur artistique, pas par Diego.
- **After Effects et Blender n'ont jamais été pilotés sur ce Mac** : les recettes After Effects ne sont vérifiées que sous Node ; Blender ne l'a été qu'en VM Linux (4.2.3, CPU), et le Mac a la 5.2.2.
- **`flash_check.py`** échoue sur des coupes contrastées sans flash (les sept références réseaux) : à confronter à un vrai test Harding avant de juger une coupe ordinaire.
- **Les seuils de tremblement** se recalibrent sur un plan stable de chaque projet ; je ne sais pas encore les fixer pour un tournage à la main en run and gun.
- **Un modèle qui regarde et écoute vraiment le rendu** reste à discuter avec Diego (confidentialité, coût).
