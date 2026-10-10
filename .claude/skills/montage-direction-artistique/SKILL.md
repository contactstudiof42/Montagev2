---
name: montage-direction-artistique
description: Passer d'un brief à une direction créative de post-production, avant de monter — « quelle direction pour ce film ? », « propose-moi des pistes », « fais-moi une note d'intention », « c'est quoi le parti pris ? », « le client veut premium et tout dire en 6 s », « on peut faire un truc moins attendu ? », « il veut un effet à la mode », moodboard, traitement d'une pub, d'un clip, d'un corporate ou d'un générique, défendre une recommandation, refuser un effet gratuit ou un brief contradictoire. Pour juger une version déjà montée : `montage-regard`.
---

# Méthode de direction artistique (brief → direction → critères)

Marqueurs : [SOURCÉ] lu dans une source citée · [TESTÉ EN LABO] fait technique mesuré · [ÉPROUVÉ EN MAQUETTE] vu seulement sur maquette Blender / Pillow / ffmpeg, hypothèse à confirmer en phase 2 · [THÉORIQUE] déduit, non vérifié. Sans marqueur ici : leçon de méthode tirée d'un examen (consultation fictive notée).

**Fait foi sur** : la méthode de consultation (inventaire, intention, trois directions, recommandation, critères, refus), les tests « cliché » et « mon propre système », « maquetter la direction qu'on écarte ». Pour juger le résultat : `montage-regard` ; principes d'auteurs : `montage-references` ; conventions par format : `montage-formats`. **Quand `GOUTS.md` s'applique, le goût du client prime sur le mien.** Détail et exemples de chaque examen : `details.md` ; carton de fin : `signature-et-cartons.md`.

## Étape 0 — Inventaire et faisabilité
- **Film tourné** : lister ce que la matière contient vraiment (cadres répétés, prises longues, cadence, marge de recadrage 9:16, son seul, plans de coupe). Une direction qui exige une matière absente est écartée ou posée en tête comme question au client.
- **Avant tournage** : repérage (sources de lumière réelles, sodium ou LED, ce qu'on peut allumer ou éteindre, autorisations) ; la direction couleur se décide après la photo de repérage de nuit.
- **Case « Ce qui doit exister pour que l'idée tienne »** (un tiers qui accepte, une archive, un lieu) : si l'idée en dépend, la direction est **conditionnelle** (le dire dans son nom) et une direction sans cette dépendance est obligatoire. (Quatre récidives : examens n°3, 5, 6, 10.)

## Étape 1 — Comprendre l'intention (rien proposer avant)
Sept lignes ; une ligne vide se déduit et s'écrit comme hypothèse :
1. **Émotion visée** (un mot + une nuance). 2. **Message** unique. 3. **Public** et son état (pressé, captif, sceptique). 4. **Diffusion** (plateforme, durée, son ou non, premier écran). 5. **Contraintes** (budget, délais, charte, rushes, droits, règles du secteur : santé, finance, alcool, enfants). 6. **Ce que le projet ne doit pas être**. 7. **Contradictions du brief**, nommées tout de suite.

**1 bis — L'idée propre au sujet** : avant `montage-references` ou `GOUTS.md`, écrire une image qui n'appartient qu'à ce sujet ; les références la traitent, ne la remplacent pas. Cas particuliers (détail : `details.md`) :
- Corporate : **l'humain par la compétence, pas par la biographie** ; aucune situation personnelle exposée sans accord (dispositifs : `montage-formats`).
- **« Sans musique »** : désigner le son récurrent qui fera le refrain, et prévoir le lieu silencieux.
- **Sponsor dans le sujet** : registre habituel du créateur, coupe franche, aucune affirmation du film ne touche le produit, placé après la première récompense.
- **Public âgé** : texte fixe, corps ≥ 5 % de la hauteur, téléphone seul 3-4 s, un carton = une information.

## Étape 2 — Trois directions contrastées
Elles diffèrent sur **l'axe principal** (retenue / spectaculaire, réel / graphique, lent / rapide, chaud / froid, sérieux / ironique) ; **au moins une change de registre** ; si deux reposent sur un dispositif, la troisième s'en passe. **Pas de direction de paille** : chacune doit pouvoir gagner.

Fiche fixe : nom + parti pris en une phrase · références (principe emprunté, 2-3) · rythme · palette · typographie · son (et place du silence) · effets (chacun justifié) · risque · faisabilité (jours, coût, enfants, animaux, météo) · version muette et 2 premières secondes.

Tests à passer sur chaque direction :
- **Cliché** : combien de films de la catégorie l'ont fait ? (`culture/cliches-de-secteur.md`)
- **Mon propre système**, appliqué aussi à la direction **recommandée** : est-ce que je refais ma dernière pièce, mon dispositif favori (le cadre qui revient avec un détail changé, « une seule chaleur méritée », le hors-champ) ou le goût du client comme une recette ? Si oui, l'écrire, donner l'argument contre, et qu'une direction le **renverse**.
- **Le rythme du sujet** : sa dramaturgie physique existe-t-elle déjà ? La cadrer avant d'inventer.
- **Révélation** : mystère (cacher) ou suspense (montrer d'abord) ; ne pas confondre avec le choc.
- **Ne pas montrer** (présence, menace, doute) : envisager le **hors-champ sonore** comme direction à part entière.
- **Ne citer que ce qu'on a analysé** ; une référence citée doit agir dans le découpage, sinon la retirer.
- **Ralenti sur rushes à cadence normale** : mains, cheveux, eau, occlusions = l'interpolation fabrique des monstres (`labo/interpolation/`) [TESTÉ EN LABO] ; proposer d'abord le ralenti **du temps**, habité par un geste. [ÉPROUVÉ EN MAQUETTE] (pièce 15)
- **Le coupable désigné** quand le brief dit « pas culpabilisant » : le retirer de l'image, le garder au son.
- **Clip** : dire comment l'artiste est filmé et quelles phrases tombent sur quels plans ; illustrer l'ancrage et le seul geste physique, laisser le reste à la musique ou au concept ; contrepoint de sens, continuité d'espace ; un regard caméra sur le vers où le « je » parle d'être vu. [ÉPROUVÉ EN MAQUETTE] (pièce 19) Geste naturel suffisant en plan taille : [À TRANCHER EN PHASE 2].
- **Générique de série** : prévoir une version courte ; il se juge au 4e visionnage.
- **Lumières qui clignotent dans le sujet** : contrôle de photosensibilité dès le traitement (`labo/photosensibilite/flash_check.py`) [TESTÉ EN LABO].

## Étape 3 — Recommander et défendre
- Choisir une direction ; argumenter **contre l'intention**, pas par goût ; dire ce qu'on perd.
- **Maquetter la direction qu'on écarte** : avant d'écarter la plus audacieuse (« trop sombre », « trop anxiogène »), 10 à 20 min de maquette. Deux fois (examens n°1 et n°13), la piste refusée sur le papier a donné en maquette la meilleure image du projet ; son vrai risque était ailleurs et se corrigeait. Dans la consultation, dire ce qui a été maquetté. [ÉPROUVÉ EN MAQUETTE] (pièces 17, 34)
- **Tic de l'hybride** (« B + un morceau de C ») : écrire la version pure et dire ce que l'emprunt ajoute ; sinon le retirer.
- **Sécurité des personnes filmées** : un concept qui prive (froid, sommeil, nourriture, hauteur) exige un protocole écrit, sinon refuser l'élément.
- **Relecture « tranché ? »** : chaque « peut-être » est tranché ou écrit comme option explicite pour le client.
- Si `GOUTS.md` contredit la recommandation : le signaler, proposer la version conforme, garder mon argument en une ligne.

## Étape 4 — Critères de réussite (avant de réaliser)
3 à 5 critères vérifiables sur planche ou mesure : « message lisible à 2 s sans son » ; « pas de plan > 3 s avant la rupture à 0:12 » ; « -14 LUFS intégré, dialogue intelligible au téléphone ».

## Étape 5 — Savoir dire non (avec une alternative)
- **L'effet gratuit** : « qu'est-ce que l'effet dit que l'image ne dit pas ? » ; si rien, le retirer.
- **La mode** qui ne sert pas le projet ; **le « plus »** (texte, plans, musique) : proposer d'enlever.
- **Le brief contradictoire** : faire choisir, avec une version de chaque si nécessaire.
- **Le texte qu'on ne peut pas lire** : un texte est une durée (14-15 car./s ATAA, 17 Netflix FR, plancher 16 images) [SOURCÉ] ; chiffrer la contradiction (« 24 noms = 18 s de lecture sur 30 s ») puis hiérarchiser (`montage-references`, liste en rangs).
- **La technique du matin** : une technique découverte au labo le jour même ne porte pas seule une recommandation sans une pièce qui la montre en mouvement.

## Double livrable (film + extraits verticaux)
Un tournage, deux montages : macro pour le film, kinetic pour les extraits. Au tournage : 4K ou open gate, zone verticale sûre, son seul des objets pour les SFX (`montage-preparation-tournage-vfx`).

## Format de rendu d'une consultation
1. Intention (7 lignes). 2. Trois directions (fiche fixe). 3. Recommandation argumentée (ce qui a été maquetté). 4. Critères. 5. Vigilance (tournage, droits, livraison). Fiction dialoguée et autres exemples : `details.md`.

## Limites connues
Éprouvée sur 13 examens fictifs (notes de 13 à 15/20 sur les n°1 à 8, détail dans `details.md`) ; tics récurrents : faisabilité tardive, dispositif favori recommandé, direction audacieuse écartée sans maquette. Jamais encore sur un vrai brief client.
