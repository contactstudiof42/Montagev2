# Note de livraison — mariage-jo, V4

_2026-10-12. Timeline **`MARIAGE_JO_V4`** du projet Resolve `P3-mariage-jo-agent` (V1, V2, V3, V3b intactes). Rendu : `videos/phase-3/mariage-jo/rendus/mariage_jo_V4.mp4` (fiche technique en bas). Fabrication : `montage/edl_v4.py` → `montage_V4.json` → `labo/outils/phase3/mariage/resolve_build_v4.py`._

## Ce que j'ai fait
La V3b n'a pas été reprise : le film est remonté à partir du dérush (passe serrée sur les moments forts, `derush-v4.md` ; toute la parole alignée mot à mot). Seule idée gardée, à ta demande : l'ouverture sur l'anecdote du panini. Plan et raisons de chaque bloc : `plan.md`. Directeur artistique appelé cinq fois (V3b, plan, look ×2, film entier) ; mes réponses : `da-retours.md`. Ce qui reste faible : `autocritique.md`.

## Tes priorités, une par une
1. **La parole** : chaque extrait commence au début d'une phrase et finit à sa fin, coupé dans un silence mesuré (WhisperX, local). Le son rendu a été re-transcrit et lu cinq fois : il se lit en phrases complètes ; cette relecture a trouvé quatre défauts, corrigés : « ouvrir » coupé avant la fin du mot, la fin de « confiance » entendue « Hein ? » devant « Mon père », un « Bonjour » parasite après le collier, et des bouts de phrases de l'ami dans l'ambiance du maillot (ambiance remplacée par des cris sans parole). Musique sous toute la cérémonie : La Maritza sans batterie ni basse (séparée en local), environ 19 dB sous la voix.
2. **L'étalonnage** : conversion du S-Log3 refaite (ni LUT de carte ni tirage), robe, costume et ciel gardent leur matière ; exposition et balance plan par plan ; fenêtres douces sur les visages ; N&B à noirs pleins. 6 images contre 6 comparables : `_travail/da_appels/4_look/` puis `5_look/`.
3. **Les plans qui tremblent** : tremblement mesuré sur les 80 plans en mouvement. Gyroflow gardé seulement quand il améliore le plan (22 plans : FX30.5483 (0:04.2), C3651 (0:07.0), C3689 (0:09.6), FX30.5635 (0:16.8), FX30.5635 (0:36.9), FX30.5456 (0:39.3), C3524 (0:46.2), C3533 (0:51.1), C3538 (0:53.5), FX30.5467 (0:56.7), FX30.5464 (0:59.1), C3540 (1:04.0), C3657 (1:20.9), C3686 (1:33.3), C3695 (1:57.8), C3695 (2:05.2), C3695 (2:13.7), C3697 (2:33.0), FX30.5743 (2:42.6), C3953 (3:18.8), FX30.5838 (3:22.6), C4007 (3:25.5), C4007 (3:32.2)) ; dans la timeline, ces plans lisent bien le fichier `_stabilized_agent`. Ralentis : C3529 (0:48.6, ×2), FX30.5472 (1:01.5, ×2), C3540 (1:04.0, ×2), C3545 (1:06.4, ×2), FX30.5490 (1:07.6, ×2), C3546 (1:08.9, ×2), C3595 (1:10.1, ×2), C3601 (1:11.3, ×2), C3820 (2:36.6, ×2), FX30.5704 (2:38.3, ×2), FX30.5720 (2:46.0, ×2), C3864 (3:07.2, ×4), C3954 (3:15.0, ×2), C3952 (3:16.9, ×2), C3953 (3:18.8, ×2), C3957 (3:20.7, ×2), FX30.5838 (3:22.6, ×2), FX30.5871 (3:37.4, ×2), C3894 (3:50.5, ×2), C3894 (3:56.5, ×2). Coupés ou remplacés après lecture image par image : Jonathan au micro (zoom pendant la phrase), « re-mari et re-femme » (panoramique vers l'officiant), saxophone et contrebasse (panoramiques rapides → le saxophoniste qui rit), Ornella (un bras passe devant l'objectif).
4. **Le storytelling** : fondu sur la salle vide, le miroir « Bienvenue », la salle qui se remplit, puis la voix ; titre sur le couple au bord du lac (pas sur du noir) ; fil « la demande naze d'il y a onze ans → la vraie demande à genoux » ; cérémonie de 1 min 10 ; le maillot avec le visage de Jonathan ; la fin sur les mariés, joue contre joue, « Rendez-vous en 2036. ».
5. **Le kinetic** : **retiré**. La matière n'a pas de corps en mouvement continu (Jonathan brandit le maillot, mais il pose) ; je ne l'atteins pas au niveau de pivetedomato. Si tu le veux quand même, le seul candidat est Jonathan bras ouverts avec le maillot (FX30.5871, 11-14 s), détouré au BiRefNet en local (test propre au bord) : à décider ensemble.
6. **Les flashs** : revenus : le premier slow (C3894), la danse du père (C3953), Jonathan qui brandit le maillot (C4007, FX30.5871). Aucun effet de flash ajouté, donc pas de contrôle de photosensibilité.

## À écouter en priorité
- 3:25.5 « Alors tiens, je te laisse l'ouvrir » : micro de caméra lointain ; la re-transcription du mix ne l'entend pas (elle l'entend sur le rush brut). À couper si elle ne passe pas.
- 2:24.8 « Vous pouvez vous rouler des grosses pelles » : couverte par les cris malgré +4 dB.
- L'isolation de voix (35 %), la musique sous la cérémonie, les fondus entre les morceaux, le limiteur du master. Rien n'a été écouté.

## Désaccords avec le directeur artistique (tu tranches)
- Titre vers 0:39 et non 0:10 : l'anecdote doit être finie avant le titre.
- Textes en crème, pas en jaune comme noahlazo : `da.md` exclut le jaune pour un couple élégant.
- Le maillot dure 17 s, pas 25 : la scène n'a pas plus de bons plans.
- La soirée reste en couleur (le N&B est réservé à la cérémonie).

## Plans remplacés hors de tes retours
Tout le film est remonté : aucun plan de la V3b n'est « gardé » au sens strict. Remplacements notables par rapport à la V3b : le titre (noir → couple au lac) ; la fin (rires d'invités → le couple au premier slow) ; la terrasse de nuit et la rafale néon retirées ; la pièce montée retirée (la nuit se resserre sur le maillot).

## Triches (un plan d'un autre moment sur une parole)
| Temps | Rush | Ce que c'est |
|---|---|---|
| 0:13.0 | FX30.5635 à 114.0 s | (≈ 3 s) : Jonathan flou au premier plan, Ornella nette qui écoute ; même discours |
| 0:16.8 | FX30.5635 à 105.3 s | un invité sourit (même salle, même discours, 30 s avant ; temps vérifié en lecture directe) |
| 0:19.0 | FX30.5635 à 121.0 s | (≈ 10 s) : Jonathan flou au premier plan, Ornella écoute |
| 0:22.7 | FX30.5635 à 110.0 s | (≈ 20 s avant) : un invité à casquette sourit |
| 0:28.4 | FX30.5635 à 137.9 s | (1 s d'avance : un bras passe devant l'objectif à 137,6 s) : Ornella écoute « est-ce que tu veux mon panini ? », puis éclate de rire |
| 0:36.9 | FX30.5635 à 155.2 s | invités qui rient (≈ 10 s après, même salle) |
| 1:17.8 | FX30.5593 à 0.3 s | [blagues]  (≈ 3 s avant) : Jonathan plié de rire sur « il va y avoir plein de mauvaises blagues » |
| 1:22.7 | C3658 à 10.2 s | [orage]  (≈ 20 s après) : les invités rient |
| 1:24.5 | FX30.5603 à 0.2 s | [nael]  (1 s) : Naël, pendant « ce petit être céleste » |
| 1:27.3 | FX30.5616 à 1.0 s | [promesse]  (70 s après) : les mariés rient, serrés |
| 1:30.2 | FX30.5612 à 0.3 s | [promesse]  : large de la salle |
| 1:33.2 | C3686 à 174.5 s | [pere]  (≈ 20 s après) : deux invitées l'écoutent, émues, l'une avec un éventail |
| 1:43.7 | FX30.5635 à 177.5 s | [naze]  (≈ 1 s) : Ornella écoute « il y a onze ans… la façon la plus naze possible » |
| 1:48.5 | FX30.5635 à 172.0 s | [naze]  (≈ 1 s) : un invité au crâne rasé sourit (voix posée) |
| 1:51.9 | FX30.5635 à 98.5 s | [naze]  (≈ 1 min avant) : Ornella sourit, même discours (voix posée) |
| 2:15.5 | C3695 à 116.3 s | [collier]  (≈ 10 s après) : Naël apporte les bracelets |
| 2:16.6 | C3696 à 4.0 s | (1 min après) : le bracelet au poignet, les mains (insert) |
| 3:50.5 | C3894 à 88.5 s | (voix de la fin de cérémonie sur le premier slow, 3 h après) : le couple joue contre joue, Jonathan chante |

## Ce que je n'ai pas su faire dans Resolve
- Fenêtres d'étalonnage qui suivent le visage : remplacées par une image en multiplication par plan (piste 2).
- Arrêt sur image : `SetSpeed(0)` ne tenait pas la bonne image ; remplacé par un plan fixe fabriqué depuis l'image exacte du rush (16 bits).
- Halo des hautes lumières (demandé par le DA) : non fait, pas d'effet posable proprement par script.

## Interpolation (ralentis au-delà de ×2)
Un seul ×4 (la dame sous la pluie), Speed Warp de Resolve. Topaz Video AI est installé sans ses modèles d'interpolation : rien téléchargé, comme demandé.

## Fiche technique
`videos/phase-3/mariage-jo/rendus/mariage_jo_V4.mp4` : 4 min 01 (240,9 s), 3840x2160, 25 i/s, HEVC Main 10 ≈ 80 Mb/s, BT.709 ; AAC 320 kb/s 48 kHz stéréo ; **−14,3 LUFS**, LRA 7,5 LU, true peak **−1,6 dBTP** (`qc_livraison.sh`). Son : mix de Resolve (isolation de voix 35 % sur la piste VOIX), puis gain +2,3 dB et limiteur suréchantillonné ×4 hors de Resolve (Resolve a refusé de lancer un rendu son seul par script : son extrait d'un rendu 1080p en PCM 24 bits). Contrôles : 0 doublon de moment ; 18 triches listées ; visages image par image (`visages.py` : alertes = paroles, rires, clignements ; regardé en mosaïque, aucune grimace) ; pas d'effet de flash ajouté.
