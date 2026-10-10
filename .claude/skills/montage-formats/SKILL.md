---
name: montage-formats
description: Narration et montage par format — pub 6/15/30/60 s, vertical réseaux sociaux (Reels, TikTok, Shorts, LinkedIn), clip musical, film corporate / institutionnel / film de marque, documentaire, fiction courte, teaser et bande-annonce. Conventions, structure type, durées de plans, premier écran, son activé ou non, pièges et clichés de chaque format, dispositifs pour filmer l'humain en corporate. Mots d'un client ou d'un réalisateur : « on a 30 secondes », « une version 15 s et une 6 s », « il faut une déclinaison verticale », « film d'entreprise », « portrait de collaborateur », « témoignage client », « le corporate fait chiant », « teaser », « doc de 52 minutes ».
---

# Narration par format

Statut : **v1, synthèse** de mes skills, fiches `culture/` et examens n°1-3 (2026-10-10). Les ordres de grandeur de durée sont des repères de métier, pas des lois : mesurer sur des références avec `labo/analyse-clip/` avant de s'y fier. Le format décide **comment** on raconte ; l'intention (`montage-direction-artistique`) décide **quoi**.

## Principe général : le format est un contrat d'attention
Chaque format suppose un spectateur dans un état différent : captif (salle, TV), choisi (clip, YouTube), volé (fil d'actualité), professionnel (salle de réunion). On ne monte pas un spectateur volé comme un spectateur captif : le premier peut partir à chaque seconde, le second attend qu'on lui demande quelque chose.

## Pub 30 s / 15 s / 6 s (TV, préroll, cinéma)
- **Structure 30 s** : une idée, une seule. Installation (0-8 s), développement ou bascule (8-22 s), résolution + signature (22-30 s ; packshot et logo 3-5 s). Glazer (*Surfer*) : deux blocs de cadence contrastés et une seule bascule valent mieux que trois idées.
- **15 s** : n'est pas un 30 s accéléré ; c'est la bascule seule, avec le minimum d'installation. **6 s** : un plan, un signe, la marque (Saul Bass : réduire à une idée).
- **Son activé** en TV/cinéma ; **muet probable** en préroll mobile : la version doit se comprendre sans son (examen n°1).
- **Pièges** : clichés de catégorie (examen n°1 : boîte à musique, bébé au ralenti pour la santé ; examen n°3 : « avant gris / après coloré » pour la rénovation) ; trop de texte ; logo qui arrive trop tôt et tue la tension.
- Livraison : TV France -23 LUFS (EBU R128 / PAD de la chaîne), cf. `montage-loudness-livraison`.

## Vertical réseaux (Reels, TikTok, Shorts)
- **Premier écran = tout** : le sujet lisible dès la 1re image (atelier 02 : 7 plans sur 19 illisibles à leur 1re image en v1), une question ou une tension avant 2 s.
- **Muet par défaut** : sous-titres incrustés, mots-clés à l'image, SFX qui ont une cause visible (`montage-kinetic-editing`).
- **Structure hybride** (atelier 03) : accroche forte, puis densité qui suit la musique par sections, une image d'exception sur le break, une boucle ou une chute à la fin (la relecture compte).
- Zones sûres : rien d'important en bas (légende) ni à droite (boutons).
- **LinkedIn** (B2B) : même grammaire muette, énergie plus retenue, 4:5 ou 1:1 ; le hook peut être une question professionnelle en carton (examen n°3, direction C).

## Clip musical
- La musique est le scénario : couper sur l'arrangement (macro) ou sur les temps (micro), le décider consciemment (`montage-rythme`). Ziak : macro, menace contenue ; Gondry : chaque couche sonore = une famille visuelle ; Jonze : quand le corps produit le rythme, le montage se retire.
- Une idée de forme forte vaut mieux qu'un récit (concept, dispositif, plan-séquence).
- Déclinaisons verticales tirées des mêmes rushes (examen n°2 : un tournage, deux montages).

## Corporate, institutionnel, film de marque
- Le spectateur est **professionnel et sceptique** : il veut des preuves, pas des adjectifs. **La forme doit être l'argument** (examen n°3 : des paires de plans « deux vies » qui prouvent la continuité ; Honda « Cog » : quand la preuve est l'argument, ne pas couper).
- Durée : 1 min 30 à 3 min pour un film de présentation ; au-delà, chapitrer.
- **Pièges du genre** : musique « ukulélé start-up », drone d'ouverture sur le siège, sourires face caméra, mains d'artisan au ralenti en lumière dorée, interviews en succession de têtes parlantes, mots-valeurs à l'écran (« innovation », « passion »).
- Son : lu sur ordinateur portable ou en salle → dialogue au premier plan, musique basse ; loudness hors plateformes **à sourcer** (BACKLOG 0f).

### Dispositifs pour filmer l'humain (sans tomber dans l'interview en intermède)
1. **L'humain par la compétence** : un geste de métier précis, filmé assez longtemps pour qu'on comprenne qu'il est difficile.
2. **L'objet-témoin** : chaque personne raconte un objet ou un dossier précis, qu'on suit ensuite ; l'humain devient le fil du film.
3. **Le portrait muet** : 3-4 s de regard caméra, sans parole, entre deux séquences (attention : ne fonctionne que si c'est rare).
4. **La voix sur le geste** : l'interview en son seul sur la personne au travail, jamais face caméra.
5. **La question-cadre** : une situation qui structure (réunion, visite, objection) ; les témoignages en deviennent les réponses (Baxter et Wall).
6. **Éthique** : jamais de situation personnelle (insertion, santé, handicap) exposée sans accord explicite ; présenter les gens par leur fonction.

## Documentaire
- Le récit se trouve au montage : dérushage complet, transcription, puis structure (Media Intelligence et transcription : `montage-premiere`).
- **Le fil est une voix ou un regard**, pas un sujet (Varda) : un « je », un personnage, une question qu'on suit. La voix off s'écrit après le montage, par passes, pour relier, pas pour illustrer.
- Ne pas monter le choc : laisser le spectateur exposé à un plan continu quand c'est la vérité du moment (Murai).
- Ellipse et digression assumées ; rimes d'objets et de gestes comme structure invisible.

## Fiction courte
- Grammaire classique au service de l'émotion d'abord (Murch : l'émotion gagne les arbitrages) ; couper à la fin d'une pensée.
- Tenir la tension tant que le rapport de force n'a pas basculé (Menke) ; la résolution plus courte que l'attente.
- Le son peut porter les raccords (Murch, Interstellar).

## Teaser et bande-annonce
- Promettre sans raconter : poser le monde, la règle, le conflit, puis couper au sommet. Montée par sections (densité croissante), une rupture (silence), une signature. Mêmes outils que l'hybride de l'atelier 03.

## Grille rapide pour choisir
| Format | Spectateur | Son | Premier écran | Rythme dominant | Risque n°1 |
|---|---|---|---|---|---|
| Pub TV 30 s | captif | oui | moyen | une bascule | cliché de catégorie |
| Préroll / vertical | volé | non | **critique** | hybride, dense | illisible sans son |
| Clip | choisi | oui | moyen | musique (micro/macro) | illustrer les paroles |
| Corporate | professionnel | oui (faible) | faible | lent → preuve | têtes parlantes |
| Documentaire | choisi, patient | oui | faible | voix / regard | commenter au lieu de montrer |
| Fiction courte | captif | oui | faible | émotion, tension | tout expliquer |

## Lacunes
Pas encore de mesures sur des références réelles par format (durées de plans médianes) ; pas d'exercice d'atelier en documentaire ou en fiction. Voir BACKLOG.
