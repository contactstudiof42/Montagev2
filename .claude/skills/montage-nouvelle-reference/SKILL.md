---
name: montage-nouvelle-reference
description: Analyser une référence ajoutée par l'utilisateur après coup — une vidéo déposée dans videos/a-traiter/, ou un simple nom écrit dans videos/NOTES-DIEGO.md ou dans la conversation (un film, un clip, une pub, une chaîne YouTube, un monteur, un réalisateur, un studio). « Regarde ce clip », « j'ai ajouté une vidéo », « regarde le travail de tel monteur », « tu connais X ? analyse-le », « nouvelle référence », « j'adore ce passage à 1 h 52 ». Range la vidéo, produit la fiche d'analyse, l'inscrit dans REFERENCES.md et met à jour les skills. Pour se servir d'une référence déjà analysée dans un projet : `montage-references`.
---

# Analyser une nouvelle référence

Marqueurs : [VU SUR IMAGES] vérifié sur les images de la vidéo · [TESTÉ EN LABO] mesuré · [ÉPROUVÉ EN MAQUETTE] vu sur maquette · [SOURCÉ] lu dans une source citée · [THÉORIQUE] déduit · [NON VÉRIFIÉ] à confirmer.

**Fait foi sur** : l'accueil d'une référence (rangement, inscription, méthode d'analyse, mise à jour des skills). La méthode détaillée des films en deux passes est dans `PROMPT-PHASE-2.md` ; les leçons de méthode qui s'y accumulent priment sur ce skill. Juger ce qu'on voit : `montage-regard`. Énoncer le principe transférable : `montage-references`.

## 1. Identifier ce qui arrive
- **Une vidéo** (dans `videos/a-traiter/`) : relever la fiche technique (`ffprobe` : durée, définition, cadence, pistes audio et sous-titres, espace couleur, HDR). Choisir la catégorie : `films/`, `clips/`, `pubs/`, `youtube/`, `projets-f42/`.
- **Un nom seul** : œuvre, auteur, chaîne ou studio. Chercher sur le web ce qui est visible légalement (bandes-annonces, chaîne officielle, entretiens, making-of) ; aucune vidéo téléchargée sans accord, rien de payant.
- **Ce que l'utilisateur en dit** (NOTES-DIEGO.md, conversation, RETOURS-DIEGO.md) : le minutage qu'il cite est la première séquence à analyser. Sa phrase est recopiée telle quelle dans la fiche, jamais dans `GOUTS.md` (qu'il dicte lui-même).

## 2. Ranger et inscrire
- Déplacer la vidéo de `a-traiter/` vers sa catégorie, avec un nom lisible. Ne jamais la commiter (`videos/` est ignoré ; vérifier `git status`).
- Ajouter une ligne dans `REFERENCES.md` : titre, catégorie, date d'ajout, date d'analyse (vide tant qu'elle n'est pas faite), chemin de la fiche.

## 3. Analyser
**Vidéo de moins de 10 min (clip, pub, extrait)** : une passe sur toute la vidéo.
- `labo/analyse-clip/analyse_clip.py` (fiche technique, loudness, coupes, tempo, transcription) puis `labo/outils/planche.py` (une image par plan, courbe LUFS dessous ; PNG sous 500 Ko).
- **Pub** : à quelle seconde le message et la marque arrivent, et ce qui reste si on coupe à 15 ou 6 s.
- **Clip** : coupes sur le temps, la mesure ou la structure ? (concentration de phase comparée au hasard, comme sur SDM).

**Vidéo longue (film, YouTube long)** : deux passes.
1. Passe globale : `labo/outils/passe_globale.sh FILM SORTIE [piste VO] [sous-titre]` (copie 480p, sous-titres, coupes, loudness, vignettes toutes les 10 s), puis courbes de densité de coupes et de volume par minute.
2. 5 à 8 séquences clés (minutages de l'utilisateur d'abord, puis pics et creux des courbes), une image par plan, son sur la même ligne de temps. Environ 150 images regardées au plus.

**Toujours** :
- Les détecteurs ratent les coupes cachées (occlusion d'un corps, filé, fondu lent) : dans tout plan de plus de 15 s, une image toutes les 2 à 3 s. [VU SUR IMAGES] (SDM, 0:47)
- Juger la couleur sur une image extraite, pas sur la planche (palette réduite).
- Un tempo détecté peut être le double ou la moitié du tempo ressenti. [VU SUR IMAGES]
- **Un nom seul, sans vidéo** : fiche `culture/<nom>.md` en [SOURCÉ], principes en [NON VÉRIFIÉ] tant que rien n'a été vu ; noter dans `RAPPORT.md` quelle vidéo il faudrait pour vérifier (sans la réclamer pendant une routine).

## 4. Confronter
- Une fiche `culture/` existe sur l'œuvre ou l'auteur ? Écrire ce qui tient, ce qui est faux, ce qui manque, et corriger la fiche.
- Pour chaque skill concerné : ce que la vidéo **confirme** (le principe passe en [VU SUR IMAGES] avec la référence et le minutage), **contredit** (corriger le skill, pas seulement la fiche), **ajoute**.
- Une erreur de méthode découverte va dans « Leçons de méthode » de `PROMPT-PHASE-2.md` (ou dans ce skill), sinon la session suivante la répétera.

## 5. Produire
Fiche `analyses/<catégorie>/<titre>.md` :
- **intention** (une phrase : ce qu'elle veut faire ressentir ou comprendre) ;
- **forme** (durée, nombre de plans, durée moyenne et médiane, courbe de rythme, structure en blocs minutés) ;
- **choix par domaine** avec minutages : rythme, cadre, couleur, son, transitions, effets, typographie ;
- **confirme / contredit / complète** les skills ;
- **principes transférables** (3 à 5, empruntables sans copier l'image) ;
- **ce que l'utilisateur en a dit** ;
- **doutes**.
Planche éventuelle à côté (PNG < 500 Ko). Puis : date d'analyse dans `REFERENCES.md`, skills mis à jour, `git status` (aucun média), commit, push.

## Pièges
- Ne pas plaquer la grille de mes skills : chercher d'abord ce qui **surprend**, c'est là qu'on apprend.
- Ne pas déduire le goût de l'utilisateur d'une seule référence : noter l'hypothèse dans `RAPPORT.md`, le confirmer quand une deuxième référence va dans le même sens.
- Ne pas citer plus d'une courte phrase de dialogue ou de paroles par fiche ; résumer plutôt.
