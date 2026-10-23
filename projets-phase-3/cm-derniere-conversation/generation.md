# « L'Air » — préparation de la génération

_Le scénario et le découpage font foi (`script.md`, `scenario.md`) ; ce fichier ne garde que les choix de génération. Depuis le 2026-10-23 (Diego), toute la suite du projet, scénario et découpage compris, se fait dans cette session ; `script.md` est aligné sur `montage.md` V2 (commit a37cd47). Remplace le projet `cm-cyberpunk` (Diego, 2026-10-23), dont il reprend la chaîne (Blender → GPT → génération sur Oxen) et les leçons. Médias : `/Volumes/SSD FAST/CM TEST /`._

## Décisions de Diego (2026-10-23)
- Budget de génération : **25 $ sur Oxen**, stratégie économe. Compte ElevenLabs disponible (plan B des voix, bruitages).
- Son : les voix viennent du modèle si elles tiennent ; sifflements et sons de la révélation en post (`script.md`).

## Modèles sur Oxen (prix lus le 2026-10-23)
| | Seedance 2.5 Reference to Video | Gemini Omni 1.1 Flash |
|---|---|---|
| Prix | 0,12 $/s (480p) · 0,26 $/s (720p) · 0,65 $/s (1080p) | 0,04 $/s (360p) · 0,13 $/s (720p) · 0,20 $/s (1080p, agrandi) |
| Durée | 4 à 30 s | 3 à 10 s |
| Références | jusqu'à 30 images, 10 vidéos (≤ 30 s au total), 10 sons dont des voix | 3 images, 3 vidéos de 3 s au plus (mouvement ou caméra) ; **première et dernière image** |
| Son | voix, ambiance ; voix de référence possible | toujours généré, sans référence de voix |
| Usage chez les films du festival | 88 % des vidéos | absent de l'échantillon |

## Répartition proposée (à confirmer par un test)
- **Plans avec dialogue** (2, 3, 4, 5, 7a, environ 22 s) : Seedance 2.5, **un plan par génération avec 1 s de marge avant et après** (pour les J-cut et L-cut, voir `montage.md` ; remplace le regroupement en deux générations), avec une voix de référence par personnage pour garder les mêmes voix. Les répliques hors champ (plan 2, « Later. ») se prennent dans n'importe quelle prise, même en 480p, ou dans ElevenLabs.
- **Plans sans dialogue du modèle** (1, 6, 7b, 8a, 8b, environ 20 s) : candidats pour Omni Flash en 720p, à partir d'une image de départ faite dans GPT (le cadrage, donc ce qui cache les entraves, est fixé par l'image). Moitié moins cher que Seedance en 720p.
- **Test d'abord** (environ 2 $) : le même plan sans dialogue en Seedance et en Omni, comparés côte à côte en pleine résolution avec une image de référence pro. Si Omni ne tient pas (visages, matière, cohérence avec les plans Seedance), tout reste en Seedance.

Budget estimé : test 2 $ · Seedance 480p pour régler les prompts ≈ 2,60 $ · Seedance 720p, deux prises ≈ 11,40 $ · Omni 360p pour régler ≈ 1 $ · Omni 720p, deux à trois prises ≈ 7,50 $. Total ≈ 24,50 $, sans réserve : les plans ratés deux fois passent en 480p agrandi avec Topaz.

## Question ouverte
- Univers : **futur proche discret, « la dernière pièce sans micro »** (Diego, 2026-10-23). Changements proposés à la conversation d'écriture : `adaptation-futur-proche.md` ; à intégrer au scénario et à faire relire par le directeur artistique avant les prompts.

## V4 lue (commit 842184c, 2026-10-23) : points de génération
- Le dôme couvert doit être dans le cadre des plans 1, 6, 7b et 8b, en un seul exemplaire. Au plan 6 (plan à deux), le cadre doit montrer l'angle du plafond sans montrer les jambes : caméra à hauteur de table, bas du cadre au plateau. À vérifier dans Blender avant toute génération.
- La lumière rouge sous le linge (allumée du plan 6 au plan 7b, éteinte en 8b) : en post d'office, plan fixe, simple à poser ; le prompt demande le dôme éteint partout.
- Le plan 7b est le plus chargé (trois notes, la porte s'ouvre, la sortie à petits pas avec les entraves, la porte se referme, la lumière s'éteint) en 4 s : risque d'actions oubliées (leçon de studiof42-rise). Proposition : générer 6 s, n'y garder que l'ouverture et la sortie ; la porte qui se referme et la lumière qui s'éteint peuvent passer par le son et par le début du 8b.
- Le couloir : clair et froid, flou, sans personne, sans blanc brûlé.

## Découpage V2 de `montage.md` (Diego : plus de caméra sur lui, « Later. » sur lui, sa sortie sur lui) : budget recalculé
- 13 plans. Seedance (répliques à l'écran) : prise continue sur lui ≈ 20 s, sur elle ≈ 16 s, plan 7a ≈ 5 s, soit 41 s. Sans réplique du modèle (1, 6, 7b, 8a, 8b) : 27 s, candidats à Omni Flash.
- Un passage de réglage (Seedance 480p + Omni 360p) ≈ 6,00 $ ; un passage final (Seedance 720p + Omni 720p) ≈ 14,20 $ ; reste ≈ 4,80 $, dont le test comparatif ≈ 2 $.
- Si Omni ne passe pas le test, tout en Seedance : 25,80 $ pour deux passages, donc au-dessus du budget ; il faudra alors garder en 480p agrandi les plans sans visage proche (8a, 6, 1).
- Une prise continue sur lui coûte 4,70 $ en 720p : on la règle en 480p jusqu'à ce que « Later. » soit juste, avant de payer le 720p.


## Retouches prévues en post (décisions de Diego, 2026-10-24)
- **Magenta poussé à l'étalonnage**, la même correction sur toutes les plaques et tous les plans : D1 v2 garde du brun en bas des murs (mesures dans `prompts-gpt.md`).
- **Plaque D4 (plan 6)** : effacer le panneau de bois appuyé contre le bas de la porte, qu'on pourrait prendre pour une troisième chaise (plan fixe, détail immobile).
- À surveiller sur chaque plan généré : l'objectif du dôme qui dépasse sous le linge (D1 v2), la croix qui reprend un ornement ou un Christ.

## Les deux modèles vidéo sur Oxen (API lue le 2026-10-24)
- **Seedance 2.5 Reference to Video** (`bytedance-seedance-2-5-reference-to-video`) : 0,117 $/s en 480p, 0,263 $/s en 720p, 0,647 $/s en 1080p. 4 à 30 s. Jusqu'à 30 images, 10 vidéos (2 à 30 s, 30 s en tout), 10 sons. Les images de visages vont dans `input_face_images`, sinon le filtre peut bloquer ; dans le prompt, les médias avec visage sont numérotés avant les autres. Son généré par défaut. Mode brouillon 480p, puis rendu final 1080p ou 4K du même brouillon sous 7 jours. Pas de première image : l'image de départ passe en référence.
- **Gemini Omni 1.1 Flash** (`gemini-omni-1-1-flash`) : 0,039 $/s en 360p, 0,13 $/s en 720p, 0,195 $/s en 1080p (agrandi). 3 à 10 s, 24 i/s, 16:9. Première image (`input_image`) et dernière image (`tail_image_url`) ; 3 images et 3 vidéos de référence (3 s au plus chacune). Son toujours généré, décrit dans le prompt.
- Appel : `POST https://hub.oxen.ai/api/ai/videos/generate`, bloquant (1 à 10 minutes) ; file d'attente asynchrone `/ai/queue` pour les lots. Les médias passent par URL publique ou par data URI.

## Test Seedance contre Omni (proposé le 2026-10-24, à lancer avec l'accord de Diego)
- **Plan 1** (0:00 à 0:05, plan large, sans réplique du modèle, sifflement en post) : il montre les deux visages, les matières, le dôme et les jambes cachées, ce qui teste tout ce qui peut lâcher.
- **Omni Flash, 720p, 6 s** : première image S1 (`prompts-gpt.md`), références F2 et F4 (visages) et D1 v2. ≈ 0,78 $.
- **Seedance 2.5, 720p, 6 s** : S1, F1 à F4 en images de visages, D1 v2 en image, la previz du plan 1 en `@Video1` (« lis-y la caméra et les positions, pas les couleurs ni les matières »). ≈ 1,58 $.
- Total ≈ 2,36 $. Jugement : les deux côte à côte, image par image en pleine résolution, avec S1 comme référence de look ; visages fidèles aux fiches, mains, matière, jambes cachées, rien qui apparaît ou disparaît. Le mouvement et le son : liste minutée pour l'œil et l'oreille de Diego.

## Résultat du test du plan 1 (2026-10-24)
_`CM TEST /05_video/test/` : les deux plans, la vidéo côte à côte (Omni à gauche, Seedance à droite ; son d'Omni à gauche, de Seedance à droite) et les visages recadrés. Coût 2,36 $ ; total Oxen du projet : 3,34 $._
- **Commun aux deux** [mesuré sur toutes les images] : caméra fixe (aucune dérive du fond, 0 px) ; le néon ne bat pas (luminance de la fenêtre stable à 1,7 niveau près sur 255) ; jambes cachées, dôme couvert et éteint, croix nue ; les deux visages restent fidèles aux fiches d'un bout à l'autre [VU SUR IMAGES, 8 instants].
- **Omni Flash** (37 s de calcul, 0,78 $) : l'action est jouée et lisible. Il siffle, les lèvres arrondies, les yeux mi-clos ; vers 4,5 s, il s'arrête, sourit et lui fait signe ; sa tête bouge deux fois plus que dans Seedance (mesure de mouvement par seconde). Visages deux fois plus nets (variance du laplacien : 126 et 133, contre 71 et 77). Son : ambiance très basse (−42,7 LUFS), pas de voix.
- **Seedance 2.5** (194 s, 1,58 $) : plus raide. Il regarde au-dessus d'elle plutôt que vers elle ; le sifflement se voit à peine et le signe du menton manque. Son : un sifflement aigu entre 0 et 3 s (pic vers 1,8 à 2 kHz, très tonal), malgré « no whistled melody » ; il serait remplacé en post de toute façon.
- **Lecture** [VU SUR IMAGES ; un seul essai par modèle, donc fragile] : sur ce plan sans réplique, Omni fait mieux pour moitié prix. Cela va dans le sens de la répartition proposée : plans sans réplique en Omni, plans dialogués en Seedance (Omni ne prend pas de voix de référence).
- **Pour l'œil de Diego** (ce que je ne perçois pas) : Omni de 0 à 4 s, le naturel du sifflement et de la respiration ; à 4,5 s, le sourire et le signe du menton, et la bouche de la religieuse qui s'entrouvre (lue comme une parole ?) ; Seedance de 0 à 4 s, le regard qui passe au-dessus d'elle.
