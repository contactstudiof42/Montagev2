---
name: montage-rythme
description: Rythme et musicalité du montage — où et quand couper, durée des plans, tension et respiration, couper sur la musique (beat ou arrangement), tempo et cadence, dilater ou compresser le temps, ralenti, montage rapide ou plan long, timing comique. Mots entendus : « le montage est mou », « ça traîne », « c'est trop haché », « ça manque de respiration », « cale-le sur le beat », « la chute tombe à plat », « le plan dure trop / pas assez ».
---

# Rythme : tension, respiration, musicalité

**Marqueurs** : [SOURCÉ] fiche ou source écrite · [THÉORIQUE] convention du métier non vérifiée ici · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette Blender / Pillow / ffmpeg · [VU SUR IMAGES] vérifié sur de vraies vidéos (phase 2 : 13 films, 8 clips, 7 pubs, 10 vidéos YouTube, 7 projets du studio).

**Fait foi sur** : où et quand couper, durées de plans, tension / respiration, calage sur la musique et la cadence. **Ailleurs** : raccords (dont raccord mouvement), J/L-cut, définition de l'ellipse → `montage-grammaire` ; silence, sound design, musique avec ou contre l'image → `montage-son-et-emotion` ; cuts kinetic réseaux → `montage-kinetic-editing`.

Détail des mesures, des pièces et **toutes les preuves de phase 2 (minutages, chiffres, nuances par œuvre)** : [`details.md`](details.md), section « Preuves vues sur de vraies vidéos ». Ce fichier-ci donne les principes et une preuve courte.

## Ce que je crois du rythme
1. **Le rythme n'est pas la vitesse**, c'est la variation des durées. [SOURCÉ, VU SUR IMAGES] (*Interstellar* varie de 12 à 18 coupes/min, *Mad Max* de 4 à 40.)
2. **Le climax n'est pas plus rapide** : 13 films sur 13 ; ce qui marque le sommet, c'est le volume, le format, la fréquence d'alternance, **la durée de la crête** (*Mad Max* : 7 min au-dessus de 30 coupes/min, pour 34 contre 31) ou le cadre (STORM : 131 plans, puis le sommet en 5 plans de 21 à 60 s). Même le film le plus rapide (*Spider-Verse*, médiane 1,96 s) met sa crête au récapitulatif de la minute 2. La crête est souvent **juste avant** le sommet (rafale de souvenirs, silence, puis le sommet en plans larges : KAIZEN). Exception : un sommet **d'information** peut être la partie la plus rapide (« Les Jeux Tiger »). [VU SUR IMAGES]
3. **Ce qui signale, c'est l'écart à la norme que le film a installée**, dans les deux sens : *La Haine* (plan long de règle) signale par ses deux seules rafales, *Aftersun* (72 % de la durée en plans de 15 s ou plus) par ses trois raves, *Spider-Verse* en ralentissant de moitié pour la scène intime. Ce qui change d'un film à l'autre, c'est la norme et l'amplitude des écarts, pas leur logique. [VU SUR IMAGES]
4. **Le rythme suit l'état intérieur** (Schoonmaker) : dilater l'instant qui compte, compresser le reste ; un seul ralenti bien placé. [SOURCÉ]
5. **Couper à la fin d'une pensée** (Murch) pour ce qu'on retire ; le changement d'angle d'une conversation filmée, lui, ignore la parole (`montage-grammaire`). [SOURCÉ, nuancé sur images]
6. **La respiration est une décision, et plus on coupe vite, plus elle doit être franche** : *Mad Max*, le plus rapide de la vague 1, a le plus grand écart creux / crête (facteur 10) ; les creux suivent les chocs. Sans respiration, l'intensité s'aplatit (Goodfellas épuise volontairement). [VU SUR IMAGES]
7. **Arbitrer par l'émotion** : un léger faux raccord sur le temps juste vaut mieux qu'un raccord parfait à contretemps. [SOURCÉ]

## Couper sur la musique
- **Personne, dans les œuvres mesurées, ne coupe sur les temps plus qu'au hasard** : 8 clips, 5 pubs, *Whiplash*, *Spider-Verse*, Henley (*The Social Network*), contrôlés contre le hasard sur la musique séparée. Le rapport à la musique est ailleurs [VU SUR IMAGES, mesuré] :
  - **macro, la densité suit l'arrangement** : Ziak, 32 coupes/min avec la basse, 16 sans, un plan long immobile à chaque creux de basse ; Henley accélère sur la **courbe** du morceau (médiane 2,5 → 1,0 s pendant que le Grieg monte), pas sur sa grille ;
  - **sur les grands accents**, rares coupes où tout l'arrangement frappe : Gavras (Stress 38 % contre 20 % au hasard, STORM 30 % contre 19 %) ; le réel dans le plan, la musique dans la coupe ;
  - **par l'instrument qui a la phrase et le rapport de force** (*Whiplash*) ; **par la voix** (récapitulatif de *Spider-Verse* structuré par un refrain répété quatre fois).
- **Micro** (sur les temps) reste un trait du kinetic des réseaux, **jamais mesuré sur une vraie vidéo** du genre : [THÉORIQUE]. Les deux sont dans les goûts de l'utilisateur (Ziak / kinetic, pour des usages différents).
- **Hybride = défaut pub et réseaux** : intro tenue, calage là où la musique pousse, accélération avant la coupure, image d'exception sur la coupure ; **un accent ne vaut que par sa rareté** (une fois = l'événement, quatre fois = papier peint). [ÉPROUVÉ EN MAQUETTE] (pièce 03)
- **Ne jamais écrire « calé sur le beat » sans `labo/outils/calage.py`** (contrôle contre le hasard) **sur la musique séparée par demucs** : sur un tempo rapide presque toute coupe tombe près d'un temps, et la voix d'un mixage fabrique de faux calages (HOUDI : 45 % contre 27 % sur le mixage, rien sur la musique seule). [TESTÉ EN LABO]
- Un son peut porter le raccord (Murch : ventilateur → rotor) ; retirer le son juste avant l'impact (`montage-son-et-emotion`). Clip très synchronisé : verrouiller la musique **et ses droits** avant le tournage, tourner sur playback (Wright). [SOURCÉ]
- **Tempo et cadence** [TESTÉ EN LABO] : à 25 i/s, seuls 60, 75, 100, 125, 150 BPM tombent en images entières ; à 24 i/s : 60, 72, 80, 90, 96, 120, 144, 160, 180. Poser les marqueurs de temps et couper sur l'image la plus proche, en numéro d'image absolu (`round(t*fps)`), jamais en additionnant des durées arrondies (dérive mesurée : −460 ms sur 24 s).

## Le montage alterné
- **Interstellar, référence de l'utilisateur** (`GOUTS.md` prime : « l'accélération du montage alterné ») [VU SUR IMAGES] : l'accélération n'est pas une contraction régulière, elle est **en deux temps séparés par une rupture** ; c'est la **fréquence de changement de ligne** qui accélère (la densité ne monte que de 14,6 à 18 coupes/min) ; **l'alternance est suspendue pendant l'action la plus tendue** (amarrage, 8 min sur une ligne) ; chaque ligne a sa matière, ce qui rend lisibles des inserts de 2 s ; on ne coupe pas dans la preuve (l'alignement, 10 s). Poser une règle du temps puis la faire entendre ; enseigner la règle puis la rompre ; écran partagé pour expliquer, alternance pour émouvoir [ÉPROUVÉ EN MAQUETTE] (pièce 29).
- **L'autre alterné : par blocs, puis jonction** (*Avengers: Infinity War*) [VU SUR IMAGES] : avec cinq ou six lignes, des blocs de 1,5 à 7 min qui ne raccourcissent pas ; la tension monte quand **un personnage apporte sa ligne dans une autre**. Accélérer à la *Interstellar* jusqu'à trois lignes ; au-delà, des blocs (explication DÉDUITE). Forme à proposer pour un événement à plusieurs lieux.

## Où couper
- **Plan long pour ce qui compte, rafale pour l'acte** [VU SUR IMAGES] : la preuve (l'amarrage, Andrew qui joue enfin), le corps qui prend l'espace (*Joker* : escalier, toilettes, Pogo's 74 s), la sincérité (Pignon 28-33 s), la nouvelle la plus dure (Furiosa 35,5 s), la menace et le sauvetage (*Forrest Gump*, *Avengers*) se tiennent ; les coups, l'attaque, la décision se hachent. **La coupe appartient à celui qui interrompt** (les auditions de *Whiplash*). Le plan le plus long va **à la réception**, pas à l'information (`montage-grammaire`, *Spotlight*). Même décor, montage inversé pour dire l'inverse (escalier de *Joker* : un plan de dos à la montée, 16 de face à la descente).
- **La surprise arrive dans le plan** : une rafale annonce, une surprise tombe pendant qu'on regarde autre chose (l'accident de *Whiplash*, un plan de 36 s). [VU SUR IMAGES]
- **Tension par l'allongement** : dans un dialogue qui se durcit, allonger les gros plans (10 à 19 s) au lieu de couper plus vite ; tenir l'après plus longtemps que l'acte. [VU SUR IMAGES] (*Joker*)
- **Une liste dite, une image par élément ; la relation, un plan tenu** (*Forrest Gump* : cinq pluies, cinq plans, puis 69 s sur Forrest et Bubba ; règle générale en YouTube, `montage-youtube`). [VU SUR IMAGES]
- **L'après est tenu, le plus fort est suivi du plus grand vide** : silence après l'amarrage, 9 s de noir après Nux, ralentissement par paliers après le claquement d'*Avengers* (médiane 1,8 → 23,8 s), 12 s de noir puis 16 s de couloir vide à la fin d'*Aftersun*. **Finir sur le vide** : le décor 10 à 20 s après la sortie du personnage. [VU SUR IMAGES] Variante : le silence juste **avant** (*Whiplash*, *Forrest Gump*, KAIZEN). Exception : une fin de première partie coupe net (*Spider-Verse*).
- **Le sommet de panique peut se jouer dans la caméra** : « Fou-Rire » (court du studio), un seul gros plan porté de 4,8 s qui tremble et perd le point, pas une rafale. [VU SUR IMAGES]
- **Faire monter sans raccourcir les plans** : une horloge sur noir qui se resserre (*La Haine*, 13 cartons) ; un voyage au métronome de cartons « JOUR N », l'arrivée casse la cadence (KAIZEN). [VU SUR IMAGES]
- **Timing comique** [VU SUR IMAGES ET SPECTROGRAMMES] : la gaffe et le gag de situation en plan à deux ou trois (12 à 37 s, cause et effet dans le cadre), le ping-pong en champ-contrechamp de 1 à 4 s, la réaction isolée **après** la chute ; **presque pas d'air dans l'échange** (coupe au ras de la réplique : *OSS 117*, *Le Dîner de cons*, environ 0,35 s), **de l'air sur la chute** (réaction 0,4-0,5 s après, visage tenu 1,5 à 3 s en silence). Ne citer aucun pourcentage « pendant la parole » sans spectrogramme. Écart après le mot-clé ~2 images, règle de trois, réaction finie par un **bouton** [ÉPROUVÉ EN MAQUETTE] (pièce 27) ; la réplique suivante sur la fin du rire [SOURCÉ].
- **Le sujet impose souvent son rythme** : lent puis brusque pour une révélation (la laisser se poser ≥ 1 s) ; chaîne causale : couper dans les respirations entre deux contacts, jamais sur le contact quand la preuve est l'argument ; tempo propre du sujet : couper sur ses points morts ; plan de retour plus long que le plan de départ. [ÉPROUVÉ EN MAQUETTE] (pièces 04, 07, 12, 14)
- **Dilater par la durée plutôt que par la vitesse** : une attente **habitée** ; ralenti seulement sur rushes haute cadence, jamais d'interpolation sur mains, fils, occlusions. [ÉPROUVÉ EN MAQUETTE] (pièce 15)
- **Une forme qui ralentit** : une direction lente commune à tous les canaux ; une relance y est **un coup**, pas une rafale. [ÉPROUVÉ EN MAQUETTE] (pièces 25, 26)
- **Réaction tenue** : elle tient si l'enjeu est posé juste avant et si le plan change encore ; couper après le dernier geste. [SOURCÉ] **Silence vu de loin** : lui donner un support visible qui soit un acte des personnages. [ÉPROUVÉ EN MAQUETTE] (pièce 34)

## Ordres de grandeur
| Usage | Durée indicative | Remarque |
|---|---|---|
| Montage « hip-hop » d'une routine (Wright) | 6 à 12 images | 5 à 8 plans ; 1 à 2 fois par film max |
| Texte à lire | ≥ 2× le temps de lecture à voix haute | fait foi : `montage-motion-design-principes` |
| Respiration après un pic | nettement plus long que la moyenne précédente | la différence compte plus que la valeur |
| Médianes mesurées (phase 2) | de 1,96 s (*Spider-Verse*) à 8,2 s (*La Haine*) ; clips 1,2-4,2 s ; pubs longues 1,1-1,6 s | par format : `montage-formats` ; minimums pour les montages rapides |

## Pièges
- Un procédé répété (freeze frame + voix off, coupe sur chaque beat) devient un tic.
- La synchro totale enferme : si la musique change (droits, version courte), tout est à refaire.
- Sans son (réseaux), le rythme doit aussi se lire visuellement ; mixer le dialogue sous les effets est à proscrire en pub et réseaux.

## Mesurer [TESTÉ EN LABO]
`labo/analyse-clip/analyse_clip.py` (coupes, flashs, tempo, calage sur le beat, lumière) ; `scdet` pour les coupes franches (rate les fondus, sous-détecte dans le noir) ; méthode « écart au milieu » pour les fondus ; marqueurs de temps XML (`labo/marqueurs/beats_xml.py`, vérifier la phase). Commandes et chiffres : `details.md`.
Sur une vraie vidéo (chaîne et pièges : `montage-regard`, « Juger une vraie vidéo ») : **PySceneDetect par défaut ne voit aucun plan de moins de 0,6 s** (médianes et rafales = minimums ; bandes de 6 images et tuile à pleine cadence avant de citer une rafale) ; il rate les coupes du sombre et invente des coupes sur les éclairs, les écrans et le plan porté flou ; `verif_plan.py` + tuile `fps=1/2` avant de citer un plan long ; générique et logos retirés avant toute statistique.

## Reste à faire
Fiches Sally Menke, Kirk Baxter, clips (Gondry, Jonze). Mesurer un vrai kinetic de réseaux (calage micro, aucune vidéo du genre dans le corpus). Les durées fines de maquette (2 images après le mot-clé, plan de retour 4 puis 6 s) n'ont pas été vérifiées sur de vraies vidéos.
