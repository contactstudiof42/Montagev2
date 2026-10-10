# Pièce 06 « Versions » — critiques

Grille : intention servie ? lisibilité, rythme, composition, cohérence, couleur, mouvement, originalité ou cliché, justesse.

## v1 (`v1-coupes.png`, `v1-comparaison.png`, `v1-mesures.json`)
Montage : insert (20 images) + plan large f14-65, trois fois ; arpège en boucle de 72 images (= exactement une version) ; musique coupée net à la dernière chute ; 1 s de noir. 241 images, -22,1 LUFS.
- **Critère 1, même scène : tenu.** Planche de comparaison (lignes = versions, colonnes = mêmes images) : cadre identique, la tasse occupe les mêmes pixels aux images 56 et 64 dans les trois lignes. La boucle musicale qui redémarre à chaque version dit « on recommence » sans carton.
- **Critère 2, détail lisible : raté pour la secousse.** 6 mm d'amplitude sur une table qui fait ~130 px de large pour 1,2 m : **0,6 px**. Personne ne la verra ; la version 2 est donc, pour le spectateur, une simple répétition de la 1. Erreur d'échelle : j'ai choisi l'amplitude « réaliste » en mètres sans la convertir en pixels à l'écran. Leçon : **un détail se dimensionne à l'écran, pas dans la scène.**
- **L'ombre (version 3)** est lisible (bande sombre qui traverse le mur à f38, tache au sol à f30), mais elle se lit comme **une porte qui se ferme ou un objet**, pas comme quelqu'un : un pavé n'a pas d'épaules. Et la tache rectangulaire au sol, en bas à gauche, attire l'œil pour rien.
- **Composition** : la tasse fait ~15 px de large dans le plan large ; l'élément le plus fort du cadre est la bande de lumière de la fenêtre sur le mur, qui n'a aucun rôle. Le sujet est trop petit pour qu'on cherche une différence sur lui.
- **Insert** : la tasse au bord, immobile, flou de profondeur : la question est posée. Mais il est identique trois fois, ce qui est voulu (Morris), et il n'a aucune durée propre : 0,8 s, c'est court pour une question.
- **Bug** : après l'impact (non montré) la tasse finit à moitié dans le sol ; corrigé par `repos_sol` pour la v2.
- Bilan : la structure fonctionne, mais l'exercice échoue sur son point central (on ne peut pas douter d'un détail qu'on ne voit pas).

## v2 (paramètres `v2-params.json`, montage `v2-edl.json`)
Corrections : focale 38 → 55 mm (la tasse ~45 px, la fenêtre sort du cadre), secousse 6 → 25 mm sur 11 images **et un choc sourd** au son (version 2 seulement : le détail changé passe aussi par l'oreille), silhouette avec épaules et tête, pose de repos corrigée.
