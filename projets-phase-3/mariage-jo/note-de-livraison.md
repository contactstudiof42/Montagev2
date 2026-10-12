# Note de livraison — mariage-jo (V3b)

_2026-10-12. Rendu : `videos/phase-3/mariage-jo/rendus/mariage_jo_V3b.mp4` (5 min 27, 3840x2160, 25 i/s, H.265 Main 10 ≈ 79 Mb/s, AAC 320 kb/s). Timeline **`MARIAGE_JO_V3b`** du projet `P3-mariage-jo-agent` (les timelines V1, V2, V3 sont gardées). Documents : `plan.md` (genre, intention, blocs), `derush.md`, `da.md`, `look.md`, `autocritique.md`, `journal.md`, `montage/edl.py` (le montage en Python : chaque plan, sa raison, ses réglages), `montage/triches.md`._

## Ce que j'ai fait
- **Le récit** (5:27, huit blocs, `plan.md`) : 0:00 le panini (Jonathan raconte leur rencontre, Ornella éclate de rire, N&B, sans musique) → 0:41 titre sur noir, puis la journée sur *I Got a Woman* (détails en rafale sur les temps, séance photo à trois, **Naël** présenté, arrivée des invités) → 1:21 la cérémonie en **N&B** (l'officiant et ses blagues, l'orage annoncé, Naël, « promesse / preuves », les vœux d'Ornella, la demande à genoux de Jonathan, les bracelets apportés par Naël, le oui « pour les dix prochaines années ») → 3:19 **le baiser rallume la couleur** et *La Maritza* éclate → 3:28 le cocktail (les musiciens par morceaux, la dame aux cheveux blancs, la caricature de Naël, les « petits mots » : le traiteur, le buffet gratuit, **Sylvain et le panini**, **Ornella déguisée en invitée**) → 4:05 **l'orage** (silence de musique, rappel de l'officiant « mariage sous la flotte », la dame qui danse sous la pluie en ralenti ×4) → 4:14 la soirée sur **la reprise remixée de *I Got a Woman*** (le bal en sommets courts, le père, **le maillot du PSG**, la pièce montée, le **passage kinetic**, la rafale néon, Jonathan et Naël à la fontaine) → 5:07 **« dans dix ans »** (trois invités, puis Jonathan : « je jure, je rigole pas : dans dix ans, on refait la même chose ! ») → « Rendez-vous en 2036. »
- **La même chanson dix ans après** : l'original de *I Got a Woman* pour la journée, sa reprise remixée (le mp3 « youtube video ») pour la fête.
- **Look** : trois LUT maison (couleur pellicule olive aux noirs denses, N&B neutre aux blancs doux, nuit), exposition plan par plan d'après les visages, contraste remonté sur 15 plans laiteux du jour blanc, grain fin.
- **Mouvement** : Gyroflow sur les plans dont la saccade dépassait le seuil, gardé seulement quand il améliore (34 plans) ; fouettés coupés.
- **Son** : HF de la cérémonie compressé, isolation de voix de Resolve à 35 % sur toutes les voix, ambiance du Zoom sous chaque phrase, niveaux calculés sur la loudness mesurée de chaque extrait, master limité : −14,4 LUFS, −2,9 dBTP (`qc_livraison.sh` OK).
- **Photosensibilité** : les photographes et les téléphones flashent pendant tout le bal et le maillot ; les passages pris dans les salves ont été remplacés ou raccourcis (voir l'autocritique pour ce qui reste).

## Les triches
21 triches, toutes listées avec le rush et l'heure réelle dans `montage/triches.md` (même salle, même lumière, même tenue ; écarts de 4 s à 4 min). La plus visible : à 1:54, « un enfant génial » est posé sur Naël filmé 13 s plus tôt.

## Ce que tu dois vérifier à l'oreille (rien n'a été écouté)
1. **Les vœux d'Ornella (2:11-2:27)** : le HF la capte mal (−37 LUFS brut, +14 à +18 dB de gain) ; le Zoom n'est pas meilleur. Isolation de voix à 35 % : est-ce humain ou robotique ?
2. **Le limiteur du master** : 2,4 dB de gain et un limiteur à −3 dBFS pour tenir −1 dBTP ; les voix de la cérémonie ont des crêtes fortes. Si ça pompe, c'est là.
3. **Les petits mots du cocktail** (3:42-4:04) : micro de la caméra, vent et brouhaha.
4. **Le maillot** (4:28-4:37) : la phrase « il a été signé par … » est déplacée de 6 s (triche son) ; Whisper entend « Martinho » : je n'ai pas mis de nom à l'écran.
5. **Les enchaînements de musique** : La Maritza qui entre en douceur sous l'officiant puis éclate au baiser ; le silence de musique sur l'orage ; l'entrée du remix au bal.

## Ce que je n'ai pas su faire, ou pas fait
- **Ralentis au-delà de ×4** : Topaz Video AI est installé mais ses modèles d'interpolation ne sont pas sur le Mac (il faudrait les télécharger, sans doute avec ton compte) : non fait sans ton accord. Speed Warp de Resolve testé à ×4 sur la dame sous la pluie (images à 200 % dans `ralenti/ralenti_x4_200pc.jpg`) : propre, léger étirement au bout des doigts. À juger image par image.
- **Gyroflow sur le père qui danse** (FX30.5838) : deux essais, aucun rendu (sortie `.tmp`) ; le plan a été remplacé par un autre moment du père (C3953), stabilisé.
- Le passage kinetic est calculé hors de Resolve (détourage BiRefNet local, `labo/outils/phase3/mariage/kinetic.py`), posé en ProRes : pour le retoucher, relancer le script.
- Les cases « Force sizing » et « Bypass re-encode » du rendu ne sont pas dans l'API ; timeline et rushes étant en UHD, le redimensionnement ne joue pas.

## Plans remplacés hors de tes retours
Aucun retour de toi sur ce projet encore ; tous les choix sont les miens.
