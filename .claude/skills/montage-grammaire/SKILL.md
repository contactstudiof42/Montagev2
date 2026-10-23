---
name: montage-grammaire
description: Grammaire du montage — raccords (regard, mouvement, direction, axe, forme, son), règle des 180°, champ / contrechamp, jump cut, insert, plan de coupe, ellipse, J-cut et L-cut, montage parallèle, faux raccord, monter une interview ou un dialogue, couper dans la parole, tricher un plan sur une parole, ne pas montrer deux fois le même moment. Mots entendus : « ça saute », « on est perdu dans l'espace », « ils ne se regardent pas », « le dialogue ne coule pas », « c'est haché, on comprend rien », « comment je cache cette coupe dans l'interview ? », « on a franchi l'axe », « personne ne verra le faux raccord ? ».
---

# Grammaire du montage : les règles gagnées

_Réécrit le 2026-10-13 (audit 2) : chaque règle cite l'erreur qui l'a gagnée ou le mot de Diego qu'elle porte. Savoir (180°, dialogue et interview, cécité au changement, temps, montage son) : [savoir.md](savoir.md). Version d'avant : `archives/audit-2/skills/montage-grammaire/`._

**Fait foi sur** : couper dans la parole, tricher un plan d'un autre moment sur une parole, ne pas montrer deux fois le même moment ; le savoir des raccords, de l'axe, du dialogue et du temps (annexe). Où et combien de temps tenir un plan : `montage-rythme` ; silence et sound design : `montage-son-et-emotion` ; niveaux : `montage-loudness-livraison`.

## 1. Couper dans la parole : au mot près, et relire ce qu'on entend [universel]
1. **Alignement forcé** dès qu'on coupe dans la parole : WhisperX (local, gratuit, `.venv-whisperx`) recale chaque mot sur le son. On ne coupe **que dans un silence entre deux mots**, jamais dans un mot ; un extrait commence **au début d'une phrase** et finit **à la fin d'une phrase** ; quelques images d'air avant et après. Plus la parole porte le film et plus on coupe dedans, plus le mot à mot s'étend (jusqu'à toute la parole pour un face caméra, une interview, un podcast).
2. **Relire ce que le spectateur entend** : après chaque rendu, re-transcrire le son du film rendu et lire le texte comme un spectateur. Chaque passage parlé forme des phrases complètes et compréhensibles ; un passage qui se lit haché est à reprendre (`labo/outils/phase3/mariage/relecture.py`).
(Gagnée : V3b du film de mariage, phrases qui commençaient au mauvais moment et s'arrêtaient au milieu d'un mot, « complètement haché, on comprend rien » ; solution validée par Diego le 2026-10-12. Sur la V4, la relecture a trouvé quatre défauts que mes contrôles ne voyaient pas.)

## 2. Tricher : un plan d'un autre moment sur une parole [genre : mariage et événement]
« Dans ce genre de montage, n'hésite pas à tricher. » (Diego, 2026-10-12 ; portée classée par lui le 2026-10-13.) Quand une parole nomme quelqu'un et que personne ne le filmait à cet instant, on pose un plan de lui pris avant ou après. Conditions : **raccord** (lumière, tenue, position, ce qu'il tient, ambiance autour : même lieu, même heure de lumière) pour qu'on ne voie pas que c'est un autre moment ; parfois visible, si l'intention du montage l'assume (une parole qui convoque un souvenir). Ce n'est pas un doublon : la triche prend un moment **différent**, jamais deux fois le même. Contrôle : chaque triche notée dans la note de livraison (quel plan, d'où il vient : rush, heure). **Contre-indication** : reportage où la fidélité au moment compte (documentaire compris).

## 3. Ne jamais montrer deux fois le même moment [genre : after movie, événement, run and gun]
Fichier maître de cette règle ; portée fixée par Diego : l'after movie au sens large, tout ce qui y ressemble ; « il existe beaucoup d'exceptions ailleurs : flashback, humour, podcast… ».
- Dans un after movie, un événementiel, un run and gun, un montage dynamique : **jamais deux fois le même passage d'un même rush**, rafales comprises ; un rush peut donner plusieurs plans, à des moments différents. Répéter un moment, c'est amateur (Diego) : le spectateur le reconnaît, même dans une rafale de 3 images.
- **Exception dans le genre** : un ressort de récit qui le justifie (flashback, rappel volontaire), écrit dans `plan.md`. Hors du genre (fiction, documentaire, interview, podcast, humour), la répétition d'un moment est un outil ordinaire.
- **Contrôle avant chaque rendu** : `labo/outils/doublons_timeline.py` (dans `run_script` de Resolve) liste chaque plan (rush, entrée, sortie) et signale tout chevauchement entre deux plans d'un même rush. Zéro doublon avant de rendre. **Une rafale se puise dans des passages que le film ne montre pas.** (Gagnée : onze doublons dans la V3 du film de marque kinetic, presque tous des rafales qui reprenaient le début d'un plan monté ailleurs.)

## 4. L'axe des 180° se vérifie par le calcul, avant de montrer quoi que ce soit [universel]
- Avant de montrer une previz, un découpage, des images de référence ou un montage où deux personnages se font face : pour **chaque plan**, au début, au milieu et à la fin, vérifier que la caméra est **du même côté de la ligne d'action** (la ligne entre les deux têtes, vue de dessus) que le plan d'ensemble, et que les **regards à l'écran sont opposés** (celui qui est à gauche dans le plan large regarde vers la droite, l'autre vers la gauche). Zéro erreur avant de montrer.
- Dans Blender : signe du produit vectoriel (tête B - tête A) × (caméra - tête A), et direction tête → nez projetée dans le cadre (`labo/grammaire/axe180.py`, et le contrôle de previz qui en dérive). Hors de Blender (images générées, rushes) : relever sur chaque plan de quel côté de l'écran regarde chaque personnage.
- Un axe franchi volontairement (changement de point de vue assumé, plan neutre dans l'axe) s'écrit dans le découpage, avec sa raison.
(Gagnée : previz d'un court métrage de fiction IA, 2026-10-24 : la caméra du champ sur l'homme avait été posée de l'autre côté de l'axe, et les deux personnages regardaient vers la gauche de l'écran ; Diego l'a vu sur la première planche : « corrige ça dès à présent, avant quelconque livraison ».)
