# RAPPORT — synthèse de la phase 2 (en cours)

_Réécrit à chaque session (dernière : 2026-10-11, session 1). La synthèse de fin de phase 1 (niveau par domaine, 10 principes, audits) est dans `archives/phase-1/RAPPORT-synthese-cloture-phase-1.md` ; le journal de la phase 1 dans `archives/phase-1/RAPPORT-journal.md`._

## Où j'en suis
- Vidéos analysées : SDM « #Malentouré » (test de méthode), **Interstellar** (passe globale et 4 séquences), **Joker** (passe globale et 3 séquences sur 6). Fiches dans `analyses/`.
- Outils de la phase 2, tous dans `labo/outils/` : `passe_globale.sh` (copie 480p, sous-titres, loudness, vignettes, coupes : 6 à 8 min pour un film de 2 à 3 h sur le M1 Max), `courbes_film.py` (coupes par minute, médiane des plans, LUFS), `couleur_film.py` (couleur, saturation, chaleur, rouge, vert par minute), `sequence.py` (une image par plan avec les sous-titres et le volume momentané).

## Ce que les vrais films m'ont appris (par ordre de solidité)
1. **Le rythme d'un film n'est pas sa densité de coupes.** Interstellar coupe de 12 à 18 fois par minute selon les actes ; son climax ne coupe pas plus vite que son premier acte. La montée vient du **volume** (un plateau fort de 30 min), du **format** (IMAX presque continu dans le dernier tiers) et de la **fréquence de changement de ligne** dans l'alterné. Joker coupe environ 9 fois par minute presque tout le film. [VU SUR IMAGES]
2. **L'accélération du montage alterné (goût de Diego) est en deux temps, séparés par une rupture** : une ligne passe de la scène à l'insert (12-44 s, puis 4-14 s), l'alternance **s'arrête** pendant l'action la plus tendue (amarrage), puis reprend à trois lignes par segments de 2-6 s (tesseract). Mon hypothèse de phase 1 (contraction régulière 8 / 4 / 2 / 1 s) était fausse. [VU SUR IMAGES]
3. **On ne coupe pas dans la preuve** : le plan le plus long de l'amarrage (10 s) est l'alignement. Principe de phase 1 confirmé sur un vrai film. [VU SUR IMAGES]
4. **La rafale de plans courts est réservée à l'acte** (violence ou euphorie, chez Joker), et l'après est tenu **plus longtemps** que l'acte (23 s après le métro, 13 s après le coup de feu). Dans un dialogue qui se durcit, la tension monte par **l'allongement** des gros plans (10-19 s). Cela nuance la règle « la résolution est plus courte que l'attente ». [VU SUR IMAGES]
5. **La couleur méritée s'annonce** : chez Joker, le rouge est presque absent pendant 95 min, mais ses rares apparitions sont toutes des **lieux de spectacle** (scène, théâtre) avant que le personnage le porte. La première chaleur (sodium) arrive juste après la première violence. [VU SUR IMAGES]
6. **Le silence ponctue la fin de l'effort** (Interstellar : perte de connaissance après l'amarrage), et pas les plans extérieurs, qui gardent la musique. [mesuré, pas écouté]
7. Le tic de Miller bat bien à 1,25 s (mesuré) ; ce n'est pas exactement « un jour ».

## Erreurs de phase 1 corrigées cette session
Contraction 8 / 4 / 2 / 1 s (Interstellar) ; « extérieurs silencieux » (Interstellar) ; « l'image de Joker s'assombrit » (elle reste stable puis s'éclaircit) ; ratios (Interstellar 2,39 ↔ 1,78 sur le Blu-ray IMAX ; Joker 1,85 confirmé).

## Limites de ma méthode découvertes (inscrites dans `PROMPT-PHASE-2.md`)
- Le détecteur de coupes **rate** les coupes des scènes sombres à faible contraste (un « plan » de 53 s qui en contient trois) et **invente** des coupes quand la lumière clignote (le métro de Joker). Les nombres de plans sont des ordres de grandeur ; aucun plan long ni aucun pic n'est cité sans vérification à l'œil.
- Classer les lignes d'un alterné par la couleur moyenne échoue ; il faut les classer à l'œil (une image toutes les 2 s).
- Le son est mesuré, **jamais écouté**. La séparation musique / effets (demucs) n'a pas encore servi.

## Doutes (à trancher plus tard, sans poser de question pendant une routine)
- `.claude/settings.json` (modèle Opus, effort high), ajouté par Diego en cours de session, **n'est pas commité** : le garde-fou de l'agent a refusé ce commit (« modification de sa propre configuration »). Diego peut le commiter lui-même s'il le souhaite.
- Le calage des coupes sur la musique (tic de Miller, entrée de la musique des escaliers de Joker) n'est pas mesuré.

## Hypothèses de goût (à confirmer par d'autres références)
- Interstellar et Joker, les deux films cités par Diego, **ne coupent pas vite**. Ce qu'il aime chez eux tient à la structure (l'alternance, la rupture) et à l'équilibre de l'image, pas à la vitesse. Cela s'oppose à son goût pour le kinetic, qu'il réserve à « d'autres usages » (GOUTS.md, précision du 2026-10-09).
