# « L'Air » — préparation de la génération

_Le scénario et le découpage font foi (`script.md`, `scenario.md`) ; ce fichier ne garde que les choix de génération. Remplace le projet `cm-cyberpunk` (Diego, 2026-10-23), dont il reprend la chaîne (Blender → GPT → génération sur Oxen) et les leçons. Médias : `/Volumes/SSD FAST/CM TEST /`._

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
- **Plans avec dialogue** (2, 3, 4, 5, 7a, environ 22 s) : Seedance 2.5, en deux générations écrites comme des scènes déjà montées (2-3 puis 4-5-7a), avec une voix de référence par personnage pour garder les mêmes voix.
- **Plans sans dialogue du modèle** (1, 6, 7b, 8a, 8b, environ 20 s) : candidats pour Omni Flash en 720p, à partir d'une image de départ faite dans GPT (le cadrage, donc ce qui cache les entraves, est fixé par l'image). Moitié moins cher que Seedance en 720p.
- **Test d'abord** (environ 2 $) : le même plan sans dialogue en Seedance et en Omni, comparés côte à côte en pleine résolution avec une image de référence pro. Si Omni ne tient pas (visages, matière, cohérence avec les plans Seedance), tout reste en Seedance.

Budget estimé : test 2 $ · Seedance 480p pour régler les prompts ≈ 2,60 $ · Seedance 720p, deux prises ≈ 11,40 $ · Omni 360p pour régler ≈ 1 $ · Omni 720p, deux à trois prises ≈ 7,50 $. Total ≈ 24,50 $, sans réserve : les plans ratés deux fois passent en 480p agrandi avec Topaz.

## Question ouverte
- Adapter « L'Air » à un univers cyberpunk : piste proposée à Diego le 2026-10-23 (futur proche discret), non tranchée.
