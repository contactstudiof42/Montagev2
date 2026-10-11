# captured-by-h — collage d'archives (réseaux, 13,8 s)

_Fiche du 2026-10-11 (session 12, référence ajoutée par Diego dans `videos/reseaux/`). Source : `video-by-captured-by-h-4-mxa-5-tmrzv.mp4`, 1276x718, 30 i/s, VP9, 13,8 s. Toutes les images vues une à une (413 images, pages de 120 vignettes avec coupes détectées et barres de son), spectrogramme mix / musique / voix séparées par demucs, calage contre le hasard sur la musique séparée. Rien écouté._

## Intention
Un collage d'images d'archives et de gravures (crâne anatomique, iris, silhouettes, trou noir, schémas techniques d'appareil photo et de fusil, voilier gravé, éclipse) qui fait sentir une pensée qui s'emballe ; une seule phrase écrite, « don't believe everything you think » (4,0 s), donne la clé. [VU SUR IMAGES]

## Forme [mesuré, chaque image]
- **72 coupes en 13,8 s, médiane 0,07 s (2 images)**. Ce n'est pas un montage à cadence constante : il alterne **rafales** (2 à 4 images par plan) et **arrêts** tenus.
- Blocs : 0-1,7 s rafale (crâne, iris, crâne en négatif, 20 plans) ; 1,7-4,0 s silhouette blanche sur noir, tenue, des corps flottants **apparaissent dans le plan** (2,07 s), un lampadaire s'allume (2,47 s), l'image passe en négatif deux fois (2,50 et 2,93 s) ; 3,6-4,2 s rafale de schémas ; **4,2-6,5 s trou noir tenu 2,3 s** (dont un passage en négatif à 5,6 s) ; 6,5-7,0 s transition par glitch et collage ; 7,0-8,2 s silhouettes sur paysage gris avec une tache d'encre qui grandit ; 8,2-11,1 s rafale d'éclipses en positif / négatif alterné (1 à 3 images chacune), schémas, voilier ; 11,1-11,8 s étoile tenue ; **11,9-13,8 s fleur d'encre tenue 1,9 s jusqu'à la fin, qui s'éclaircit**.
- Les arrêts ne sont pas des plans fixes : il s'y passe toujours quelque chose (apparition, encre qui s'étend, passage en négatif). [VU SUR IMAGES]

## Choix par domaine
- **Rythme** : rafale / arrêt / rafale ; la rafale la plus dense (éclipses) tombe sous la phrase chantée, l'arrêt final sous le silence. [VU SUR IMAGES, VU SUR SPECTROGRAMME]
- **Effets** : l'**inversion positif / négatif** est l'effet-signature (au moins 15 fois) ; elle sert de flash à luminance contrastée sans ajouter d'image. Grille de papier millimétré, teintes plates (rouge, cyan, bleu) posées sur la même image : une gravure se décline en 3 à 4 variantes de 2 images.
- **Couleur** : noir et blanc dominant, une teinte plate par variante ; le trou noir et l'éclipse apportent le seul chaud (orange) de 8,8 à 10,0 s.
- **Son** (spectrogramme) : 0-4 s impacts larges et glitchs (bandes verticales sur tout le spectre) sous la première rafale ; à 4,1 s une nappe tonale démarre avec le trou noir ; 8,2-11,8 s une voix chantée (« We don't have to… », Whisper) ; **à 11,8 s tout s'arrête** : la fin se tient dans le silence. Intégré -14,0 LUFS, LRA 4,5 LU, crête -3,6 dBFS.
- **Calage** (72 coupes vues, attaques fortes de la musique séparée) : 16 % des coupes à ±1 image d'une attaque contre 20 % au hasard ; **aucun calage micro**. Les rafales et les impacts occupent les mêmes zones (0-2 s, 8-11 s), pas les mêmes images ; les deux gros impacts de 2,3 et 2,8 s tombent dans un plan tenu, 4 à 5 images avant un changement interne. [mesuré]
- **Typographie** : une seule phrase, petite, sous une image (4,0 s), sur 3 images.

## Confirme, contredit, complète
- **Confirme** « plus c'est rapide, plus il faut respirer » (`montage-kinetic-editing` § 1) et « le plus fort suivi du plus grand vide » (`montage-rythme`) : rafales de plans de 2 images entre des arrêts de 1,3 à 2,3 s, et la fin en silence.
- **Confirme** la rafale-clignotement de Yvnnis (`montage-kinetic-editing` § 3) : les plans de 2 images ne se lisent pas un par un ; ce qui se lit, ce sont les arrêts.
- **Contredit** la table des durées du skill (plan éclair 4 à 8 images) : ici la norme est 2 images, 3 au plus. Voir aussi malkimikee.
- **Complète** : un « plan tenu » de kinetic n'est pas immobile, il porte une **apparition ou une transformation** (corps qui apparaissent, encre qui s'étend, négatif).
- **Ne confirme pas** le calage micro : un kinetic très dense peut ne caler aucune coupe et rester rythmé par l'alternance rafale / arrêt.

## Principes transférables
1. **Rafale de 2 images, arrêt de 1,5 à 2,5 s** ; dans l'arrêt, une seule chose se transforme.
2. **Décliner une image en variantes** (négatif, teinte plate, grille) pour faire une rafale sans nouvelles images.
3. **Couper le son avant la dernière image** et la tenir : la fin respire.

## Ce que Diego en a dit
Retour du 2026-10-11 (`RETOURS-DIEGO.md`) sur l'ensemble du dossier : des vidéos « que j'aimais beaucoup », avec « beaucoup de kinétique, mais pas que ». Rien sur celle-ci en particulier.

## Doutes
- Auteur et contexte (art, clip, teaser) non cherchés. La phrase chantée n'a pas été vérifiée à l'oreille.
- `flash_check.py` : ÉCHEC (32 flashs, pire seconde 6) ; l'outil simplifié compte peut-être chaque coupe sombre / claire (voir le bilan dans `RAPPORT.md`).
