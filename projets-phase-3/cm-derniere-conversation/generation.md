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

