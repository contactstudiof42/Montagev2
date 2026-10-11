# RAPPORT — synthèse de la phase 2 (en cours)

_Réécrit à chaque session (dernière : 2026-10-11, session 2). La synthèse de fin de phase 1 (niveau par domaine, 10 principes, audits) est dans `archives/phase-1/RAPPORT-synthese-cloture-phase-1.md` ; le journal de la phase 1 dans `archives/phase-1/RAPPORT-journal.md`._

## Où j'en suis
- Vidéos analysées : SDM « #Malentouré » (test de méthode), **Interstellar** (passe globale + 4 séquences), **Joker** (passe globale + 7 séquences), **Whiplash** (passe globale + 6 séquences). Fiches dans `analyses/films/`. **Le Dîner de cons** en cours (passe globale + 4 séquences). Vague 1 : il reste à finir le Dîner de cons (timing comique) et Mad Max: Fury Road, puis le bilan de vague.
- Outils de la phase 2 (`labo/outils/`) : `passe_globale.sh` (copie 480p, avec `HDR=1` pour les sources PQ), `courbes_film.py`, `couleur_film.py`, `sequence.py`, et cette session `verif_plan.py` (vérifier un plan long) et `calage.py` (coupes contre musique, avec le hasard).

## Ce que les vrais films m'ont appris (par ordre de solidité)
1. **Le climax ne coupe pas plus vite que le reste** (trois films sur trois). Interstellar : 12 à 18 coupes/min selon les actes ; Joker : environ 9 presque tout le film ; Whiplash : le maximum (36/min) est la première répétition, pas le final. La montée passe par le volume, le format, la fréquence de changement de ligne d'un alterné, les filés en caméra. [VU SUR IMAGES]
2. **Les plans longs disent quelque chose de précis.** On ne coupe pas dans la preuve (l'alignement de l'amarrage ; Andrew qui joue vraiment, 9 à 14 s). Chez Joker, les plus longs plans sont les moments où le corps d'Arthur prend un espace (danse des toilettes 40 s, entrée à Pogo's 74 s, capot 43,7 s). Dans Le Dîner de cons, la tirade sincère de Pignon tient 28 à 33 s quand le film coupe toutes les 3 s, et les gags de situation se jouent en plans à deux ou à trois tenus (12 à 37 s). [VU SUR IMAGES]
3. **La rafale va à l'acte voulu, la surprise arrive dans le plan.** Joker : rafales sur les coups de feu ; Whiplash : sur la chaise et la décision de revenir. Mais l'accident de voiture de Whiplash, la violence la plus brutale, est **un plan de 36 s sans coupe**. L'après est tenu plus longtemps que l'acte (Joker, Whiplash). [VU SUR IMAGES]
4. **L'accélération du montage alterné (goût de Diego) est en deux temps, séparés par une rupture** (Interstellar) : la ligne passe de la scène à l'insert, l'alternance s'arrête pendant l'action la plus tendue, puis reprend à trois lignes par segments de 2-6 s. [VU SUR IMAGES]
5. **Le silence a deux places** : après l'effort, pour le faire peser (Interstellar après l'amarrage, Joker après le capot : le plus fort suivi du plus grand vide) ; juste avant le dernier coup, pour le faire frapper (Whiplash, 10 s de silence puis coupe au noir sur le coup). [mesuré, pas écouté]
6. **La couleur méritée** : Joker annonce le rouge par les lieux de spectacle puis le donne au corps, et le vert passe au décor au lieu de disparaître ; Whiplash code deux mondes (ambre de la musique, vert de la vie) et supprime le vert au final. [VU SUR IMAGES]
7. **Même un film de musique n'est pas forcément monté « au beat »** : dans Whiplash, les coupes ne tombent pas sur les attaques fortes plus qu'au hasard ; au plus une légère tendance aux temps. Le calage est macro (instrument, rapport de force). [mesuré ; détection d'attaques sur le mixage complet]
8. **Séparer par la coupe, réunir par le filé** (Whiplash) : le champ-contrechamp maître / élève devient, au final, des filés aller-retour dans un même plan. [VU SUR IMAGES]

## Erreurs corrigées
- Phase 1 : contraction 8 / 4 / 2 / 1 s (Interstellar) ; « extérieurs silencieux » (Interstellar) ; « l'image de Joker s'assombrit » ; « le rouge remplace le vert » à la fin de Joker ; « la danse des toilettes en un seul plan » (la danse oui, la scène en trois).
- Session 1 : j'avais cru faux le plan de 74 s de Pogo's (c'est un plan-séquence) ; j'avais attribué à Diego une note sur l'amarrage d'Interstellar qui n'était qu'un exemple de format (retour de Diego du 2026-10-11, intégré).

## Limites de ma méthode (inscrites dans `PROMPT-PHASE-2.md`)
- Les détecteurs **ratent** les coupes des scènes sombres et celles cachées dans un filé ; ils **inventent** des coupes quand la lumière clignote. Une vignette par plan ne peut ni confirmer ni réfuter un plan long : il faut `verif_plan.py` et une tuile à intervalle fixe.
- Une source HDR lue comme du SDR fausse toutes les mesures de couleur (vérifier `color_transfer`).
- Le son est mesuré, **jamais écouté** ; la séparation (demucs) n'a pas encore servi. Le calage se mesure sur le mixage complet.

## Doutes (à trancher plus tard, sans poser de question pendant une routine)
- `.claude/settings.json` (modèle Opus, effort high), ajouté par Diego, **n'est pas commité** : le garde-fou de l'agent refuse ce commit. Diego peut le commiter lui-même.
- Whiplash : combien de coupes cachent les filés des plans de 21 et 24 s ? L'hypothèse « on coupe sur l'instrument qui a la phrase » n'est pas mesurée.
- Le plan du bus « en miroir » de Joker n'a pas été cherché.

## Hypothèses de goût (à confirmer par d'autres références)
- Interstellar et Joker, les deux films cités par Diego, **ne coupent pas vite**. Ce qu'il aime chez eux tient à la structure (l'alternance, la rupture) et à l'équilibre de l'image, pas à la vitesse. Cela s'oppose à son goût pour le kinetic, qu'il réserve à « d'autres usages » (GOUTS.md, précision du 2026-10-09).
- « L'équilibre de l'ensemble » de Joker (réponse 4 de Diego) se lit sur les images comme **une même règle appliquée par tous les leviers** : quand Arthur existe, la caméra tient et la couleur change de place ; quand il agit, le montage coupe. Hypothèse à tester sur les autres films : un film « équilibré » est un film où image, couleur, son et montage obéissent à la même logique.
