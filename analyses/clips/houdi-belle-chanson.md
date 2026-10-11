# HOUDI — « Belle chanson »

_Fiche ouverte le 2026-10-11 (phase 2, session 4, clip n°6). **État : terminée (une passe, sans recherche documentaire).** Source : 1620×1080 (3:2), 25 i/s, 3 min 37, SDR. Planche commitée : `houdi-plans.png`. Le générique final (police d'arcade) crédite une équipe de tournage réelle (chef opérateur, assistants caméra, électros, machinos) **et** des postes 3D, pixel art et VFX : tournage réel mêlé d'images de synthèse. Réalisateur et monteur : non relevés avec certitude (générique trop petit sur la copie de travail)._

**Lu avant l'analyse** : `montage-rythme`, `montage-motion-design-principes` (habillage, typographie animée), `montage-couleur-et-intention`, grille de `montage-regard`. Aucune fiche de phase 1 sur ce clip. Aucun goût de Diego.

## Intention
Faire du clip **un niveau de jeu vidéo** d'horreur gothique : on traverse, en vue subjective ou en suivant un personnage, un manoir, des couloirs, une lande sous l'orage ; puis la caméra recule dans un bureau de vieux ordinateurs et entre dans un écran cathodique : c'était un jeu (« Mortal Hood »), et le clip finit sur « Level 2 ». [VU SUR IMAGES ; l'intention est DÉDUITE]

## Forme [mesuré, clip sombre : copie éclaircie et plans longs vérifiés]
- **3 min 37, 35 plans, ASL 6,2 s**. Le clip est très sombre (luminance 33 à 48 sur 255) : selon la leçon de Ziak, j'ai relancé la détection sur une **copie éclaircie** ; elle trouve 35 plans contre 34, donc le compte tient.
- **Plans longs = traversées** : 20,8 s (0:56, une façade de briques dont on longe les fenêtres, puis la lune), 16 s (1:33, un cavalier sous les éclairs), **37,6 s (2:03)** : galerie de portraits → noir → pièce carrelée et porte → un homme en gilet pare-balles qu'on suit → damier → couloir sombre → carré de lumière. `verif_plan.py` ne trouve aucune coupe et une tuile à 2 images/s montre une progression continue ; les passages d'un lieu à l'autre se font **par le noir ou par fondu**, comme les chargements d'un jeu. [VU SUR IMAGES]
- **Rafales courtes entre les traversées** : 0:28-0:45 (onze plans de 0,7 à 2,8 s : masque de ski, couloirs, intérieurs rouges), 1:29-1:33, 1:57-2:02.
- **La révélation finale** (2:40-3:08) : damier en fisheye → bureau de terminaux cathodiques → poussée dans un écran « SELECT PLAYER » (le personnage s'appelle HOUD1) → labyrinthe façon arcade → « STAGE CLEAR » → logo « Mortal Hood » → « Level 2 ». Puis 28,6 s de générique en police d'arcade.
- **Son** : plateau de -10 à -11 LUFS du début à la fin (intégré -10,9), aucun trou. [mesuré, pas écouté]
- **Couleur** : noir et sarcelle, accents rouges et orange (fenêtres, intérieurs) ; la chaleur monte quand le jeu apparaît (R-B par minute : -6,7, +6,1, +5,2, **+27,1**) : le monde de l'horreur est froid, le monde de l'écran est orange et violet. [mesuré, VU SUR IMAGES]
- **Calage** (33 coupes, 25 i/s) : **au niveau du hasard.** Sur le mixage complet, j'ai d'abord trouvé 45 % des coupes sur un temps contre 27 % au hasard (± 2 images ; 15 % contre 13 % à ± 1 image) ; **sur la musique séparée de la voix (demucs), le résultat tombe à 27 % contre 24 %** (5e-95e centile 12-39 %), et 24 % contre 19 % sur les attaques fortes. Le faux calage venait de la voix ou de l'estimateur de temps sur le mixage. [mesuré]

## Confirme, contredit, complète
- **Confirme** « le plan long d'un clip est un mouvement qui relie » (bilan des quatre clips) : ici les plans longs sont des **parcours**, la grammaire du jeu vidéo à la première ou à la troisième personne.
- **Confirme** le constat des clips : aucun des clips mesurés ne coupe sur les temps plus qu’au hasard (Ziak, Stress, Au DD, 6G, STORM, HOUDI, Gare du Nord). **Leçon de méthode** : sur le mixage, j'ai failli conclure l'inverse ; seul le contrôle sur la musique séparée tranche.
- **Complète** `montage-motion-design-principes` : **l'habillage peut être le dispositif du film** (interface de jeu, écran de sélection, « Stage clear », générique en police d'arcade). La typographie ne décore pas, elle dit « tu étais dans un jeu ».
- **Complète** `montage-couleur-et-intention` : deux mondes, deux températures (froid pour la fiction, chaud pour l'écran qui la contient), comme une matière par monde (Interstellar, vague 1).
- **Relie à** `montage-ia-generative` et `montage-blender` : un clip à petite équipe qui mélange tournage et 3D sans chercher le photoréalisme ; l'esthétique « jeu » **assume** l'image de synthèse au lieu de la cacher. (GOUTS.md : l'IA « pas assumée », « pas de slop » ; ici, c'est la 3D qui est assumée par le récit.) [DÉDUIT]

## Principes transférables
1. **Justifier une image artificielle par le récit** : si la 3D (ou l'IA) se voit, en faire le sujet (un jeu, un écran, une simulation) plutôt que de la faire passer pour du réel.
2. **Raccorder les lieux par le noir** : dans une traversée, le passage par une zone sombre cache la coupe ou le changement de décor (variante des coupes cachées par occlusion).
3. **Une révélation par recul** : finir en sortant du monde (la caméra recule jusqu'à l'écran qui le contenait), et ouvrir sur une suite (« Level 2 »).

## Ce que Diego en a dit
Rien (`GOUTS.md`, `NOTES-DIEGO.md`, `RETOURS-DIEGO.md`).

## Pas fait, doutes
- Recherche documentaire (réalisateur, part réelle de la 3D, moteur de jeu ou rendu précalculé). Je n'affirme pas qu'il s'agit d'Unreal ou d'un autre moteur.
- Les fondus de la traversée de 37,6 s peuvent cacher de vraies coupes que `verif_plan.py` ne voit pas (passages au noir). Je parle de « traversée continue à l'œil », pas de plan-séquence prouvé.
- Le calage n'a été testé qu'avec un seul estimateur de temps (librosa `beat_track`).
