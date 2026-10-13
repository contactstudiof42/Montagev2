---
name: montage-nouvelle-reference
description: Analyser une référence ajoutée par l'utilisateur après coup — une vidéo déposée dans videos/a-traiter/, ou un simple nom écrit dans videos/NOTES-DIEGO.md ou dans la conversation (un film, un clip, une pub, une chaîne YouTube, un monteur, un réalisateur, un studio, un tutoriel). « Regarde ce clip », « j'ai ajouté une vidéo », « regarde le travail de tel monteur », « tu connais X ? analyse-le », « nouvelle référence », « j'adore ce passage à 1 h 52 ». Range la vidéo, produit la fiche d'analyse avec des mesures vérifiées, l'inscrit dans REFERENCES.md et met à jour les skills. Pour se servir d'une référence déjà analysée dans un projet : `montage-references`.
---

# Analyser une nouvelle référence

_Réécrit le 2026-10-13 (audit 2) : il reçoit les règles de vérification d'une vraie vidéo (gagnées en phase 2 : 14 conclusions sur 45 corrigées en révision) et la méthode d'analyse de `PROMPT-PHASE-2.md` (phase close). Méthode détaillée, chaîne d'outils et leçons de méthode : [methode-analyse.md](methode-analyse.md). Version d'avant : `archives/audit-2/skills/montage-nouvelle-reference/`._

Marqueurs : `CLAUDE.md`. **Fait foi sur** : l'accueil d'une référence (rangement, inscription, méthode d'analyse, vérification des mesures, mise à jour des skills). Juger une version montée : `montage-regard` ; énoncer le principe transférable et s'en servir : `montage-references`.

## 1. Identifier ce qui arrive
- **Une vidéo** (dans `videos/a-traiter/`) : fiche technique (`ffprobe` : durée, définition, cadence, pistes audio et sous-titres, espace couleur, `color_transfer` pour le HDR). Catégorie : `films/`, `clips/`, `pubs/`, `youtube/`, `projets-f42/`, `reseaux/` (vidéos courtes des réseaux : analyse **de toutes les images**, pas des coupes du détecteur), `methodes/` (tutoriels : on en tire **une méthode**, pas une analyse de montage ; ce qui est lu à l'écran [VU SUR IMAGES] séparé de ce qui est déduit [THÉORIQUE] ; fiche dans `analyses/methodes/`). Une vidéo déposée comme référence d'un projet en cours s'analyse de même et entre au carnet avec la portée que donne Diego.
- **Un nom seul** : œuvre, auteur, chaîne ou studio ; chercher ce qui est visible légalement (bandes-annonces, chaîne officielle, entretiens) ; aucune vidéo téléchargée sans accord, rien de payant. Fiche `culture/<nom>.md` en [SOURCÉ], principes en [NON VÉRIFIÉ] tant que rien n'a été vu.
- **Ce que Diego en dit** (`NOTES-DIEGO.md`, conversation, `RETOURS-DIEGO.md`) : le minutage qu'il cite est la première séquence à analyser ; sa phrase est recopiée telle quelle dans la fiche, jamais dans `GOUTS.md` (qu'il dicte lui-même).

## 2. Ranger et inscrire
Déplacer la vidéo de `a-traiter/` vers sa catégorie, avec un nom lisible ; ne jamais la commiter (`videos/` est ignoré ; `git status`). Une ligne dans `REFERENCES.md` : titre, catégorie, date d'ajout, date d'analyse, chemin de la fiche.

## 3. Analyser
- **Moins de 10 min** (clip, pub, extrait) : une passe sur toute la vidéo (`labo/analyse-clip/analyse_clip.py`, puis `labo/outils/planche.py`, PNG sous 500 Ko). Moins de 45 s : toutes les images. Pub : à quelle seconde le message et la marque arrivent, ce qui reste à 15 ou 6 s.
- **Vidéo longue** : passe globale (`labo/outils/passe_globale.sh`), puis 5 à 8 séquences clés (les minutages de Diego d'abord), environ 150 images regardées au plus. Chaîne complète : [methode-analyse.md](methode-analyse.md).

## 4. Vérifier avant d'écrire un chiffre [VU SUR IMAGES] (gagnées en révision : ce que j'avais regardé a tenu, ce que j'avais recopié d'un outil s'est trompé une fois sur trois)
1. **Regarder avant de nommer une cause** : une « rafale de stroboscopes » était un magasin de tapis, une « rafale de panique » un seul plan porté flou, une « rafale de réaction » un téléviseur dans le champ.
2. **Une vignette par plan ne juge ni un plan long ni une rafale** : plan long, différence image par image (`verif_plan.py`) et tuile à 1 image / 2 s ; rafale, 6 images consécutives autour de chaque coupe (`bandes_coupes.py`), et toutes les images si les plans semblent à 2-3 images.
3. **Un détecteur se trompe dans les deux sens, de façon prévisible** : il fusionne le sombre, l'action accélérée, le texte sur noir et tout plan de moins de 0,6 s ; il invente des coupes sur les éclairs, les écrans, les plans portés flous et l'animation par saccades. Un nombre de plans est un minimum ; une série de plans à la durée minimale est un soupçon.
4. **Un pourcentage de parole ne se cite qu'après un spectrogramme** (25 à 30 coupes) : mesurée par l'énergie, la part des coupes pendant la parole était trop haute sept fois sur sept. La durée des silences est plus robuste.
5. **Un calage sur la musique ne se cite que contre le hasard, sur la musique séparée de la voix** (`calage.py`, demucs), avec l'écart signé : sur le mixage, la voix fabrique de faux calages.
6. **Retirer logos, générique monté et cartons avant toute statistique.**
7. **Une fiche écrite sans voir est juste dans l'esprit et fausse dans les chiffres** : une référence citée de mémoire se vérifie sur l'image.
Chaque nouvelle erreur de méthode s'inscrit dans [methode-analyse.md](methode-analyse.md), sinon la session suivante la répétera.

## 5. Confronter et produire
- Une fiche `culture/` existe ? Écrire ce qui tient, ce qui est faux, ce qui manque, et corriger la fiche. Pour chaque skill concerné : ce que la vidéo confirme (le principe passe en [VU SUR IMAGES] avec la référence et le minutage), contredit (corriger le skill), ajoute.
- Fiche `analyses/<catégorie>/<titre>.md` : intention ; forme (durée, plans, médiane, courbe de rythme, blocs minutés) ; choix par domaine avec minutages ; ce qui confirme, contredit ou complète les skills ; 3 à 5 principes transférables ; ce que Diego en a dit ; doutes. Puis la date d'analyse dans `REFERENCES.md`, `git status`, commit, push.

## Pièges
- Ne pas plaquer la grille de mes skills : chercher d'abord ce qui surprend.
- Ne pas déduire le goût de Diego d'une seule référence : l'hypothèse va dans `RAPPORT.md` (niveau 4 de la hiérarchie).
- Pas plus d'une courte phrase de dialogue ou de paroles par fiche ; résumer plutôt.
