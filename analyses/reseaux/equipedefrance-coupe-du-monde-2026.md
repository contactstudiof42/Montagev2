# Équipe de France — « Tous avec les Bleus », Coupe du monde 2026 (vertical, 43 s)

_Fiche du 2026-10-11 (session 12, référence ajoutée par Diego dans `videos/reseaux/`). Source : `video-by-equipedefrance-gjfjyv.mp4`, 720x1280, 25 i/s, 43,1 s. Toutes les images vues (1 075), passage saccadé vérifié image par image, spectrogramme, transcription (Whisper `-mc 0`), calage, écarts signés. Planche de typographie : `typo-darius-edf.png`. Rien écouté._

## Intention
Annoncer la Coupe du monde 2026 de l'équipe de France : le groupe, le voyage aux États-Unis, les trois matchs de poule, et un appel au soutien (« Tous avec les Bleus, du 11 juin au 19 juillet »), porté par le discours du sélectionneur aux joueurs. [VU SUR IMAGES, transcription]

## Forme [mesuré, chaque image]
- **56 coupes vues en 43 s, médiane 0,40 s**, mais cinq blocs très différents :
  1. **0-6,2 s : une mosaïque de portraits** se remplit case par case sur fond noir (un visage, puis deux, puis vingt), le trophée apparaît au centre (3,2 s) ; voix du sélectionneur seule, puis un **riser** qui monte jusqu'au **drop à 6,1 s** : logo FIFA 26 (6,16 s).
  2. **6,6-8,0 s : le voyage** en éclats de 0,2 à 0,4 s, enchaînés par filés (lumières de New York, drapeau américain, métro, statue de la Liberté derrière une grille, foule floue).
  3. **8,0-19,7 s : les joueurs** : portraits de 0,5 s, action, et un effet récurrent : **l'action découpée en tuiles** sur fond noir (9,6 ; 11,9 ; 13,6 ; 19,0 s), qui rappelle la mosaïque d'ouverture ; à 15,9 s la musique s'interrompt 0,3 s avant un impact.
  4. **19,7-29,2 s : les trois matchs**, trois affiches tenues **3,2, 3,2 et 2,9 s** (« FRANCE-SÉNÉGAL 16 JUIN / 21H », « FRANCE-IRAK », « NORVÈGE-FRANCE »), deux joueurs qui sautent à la tête dans la lumière, passage de l'une à l'autre par un flou de mouvement ; **la musique s'arrête** : voix seule et nappe.
  5. **29,3-39,3 s : la remontée** : visage dans l'ombre (2 s), qui se démultiplie en bandes de regards (30,3 s), puis action rapide : un dribble découpé en **sauts de temps de 5 images** (33,0-34,4 s, sept coupes dans le même plan, vérifié image par image : le joueur et les panneaux avancent d'un bond à chaque coupe), but filmé derrière le filet, célébrations, supporters (chants dans la voix séparée) ; **39,4-43 s : carton final tenu 3,7 s** sur feu d'artifice.

## Choix par domaine
- **Rythme** : vite pour l'émotion, **lent pour l'information** (trois affiches de 3 s pour qu'on lise date et heure), puis plus vite que jamais pour la fin. [VU SUR IMAGES]
- **Habillage** : la **mosaïque** est le motif du film (ouverture, tuiles d'action, bandes de regards) : un seul geste graphique décliné trois fois.
- **Couleur** : look film chaud et contrasté (orangés, bleus profonds), affiches de match en clair-obscur, carton final cyan ; le bleu du maillot partout.
- **Son** (spectrogramme) : voix seule + riser → drop sur le logo ; musique à percussions 6-19,7 s ; **silence de musique pendant les affiches** ; retour à 31,3 s ; chants de supporters. Intégré -14,1 LUFS, LRA 6,3 LU, crête -1,2 dBFS.
- **Calage** (56 coupes vues, musique séparée) : **45 % des coupes à ±1 image d'une attaque forte contre 19 % au hasard (95e centile 34 %)** ; écart signé médian **+0,3 image**. Calé à l'image. Les sauts de temps du dribble suivent la pulsation. [mesuré]
- **Typographie** : serif condensée élégante (noms de matchs, carton), date en petites capitales rouges ou blanches ; aucun sous-titre de la voix.

## Confirme, contredit, complète
- **Confirme** « la densité suit le type de phrase » (`montage-rythme`) sur un kinetic : **l'information (date, adversaire) est tenue 3 s, au calme**, l'émotion est découpée.
- **Confirme** « le plus fort précédé d'un silence » et le riser de `montage-kinetic-editing` (rang 2) : 6 s de montée vers le drop du logo ; coupure de 0,3 s avant un impact (15,9 s).
- **Contredit** « aucun calage » : calage à l'image sur la partie rythmée.
- **Contredit** R1 du skill (« image 1 = la plus forte + impact ») : le drop arrive à **6,1 s** ; les 6 premières secondes construisent (mosaïque qui se remplit, voix seule) ; ce qui accroche avant 1 s, c'est un visage connu et la voix.
- **Complète** : le **saut de temps dans un même plan** (jump cut d'action, toutes les 5 images) comme rafale sans changer de plan ; le **motif graphique décliné** (mosaïque) comme structure d'un film de 43 s.
- **Complète** `montage-formats` (vertical) : 43 s en cinq blocs, dont un d'information pure au milieu.

## Principes transférables
1. **Tenir l'information, découper l'émotion** : 3 s par carte à lire, musique coupée.
2. **Un geste graphique, trois usages** (la mosaïque à l'ouverture, dans l'action, sur les regards).
3. **Voix seule + riser jusqu'au drop**, puis l'image la plus forte (le logo) sur le drop.
4. **Saut de temps dans un même plan** sur la pulsation, pour accélérer sans couper vers ailleurs.

## Ce que Diego en a dit
Retour du 2026-10-11 : « beaucoup de kinétique, mais pas que ». Aucun commentaire sur celle-ci en particulier.

## Doutes
- Transcription Whisper approximative (« jouez et souris… ») : non citée au-delà du sens général. Agence non cherchée.
- `flash_check.py` : ÉCHEC (28 flashs, pire seconde 5).
