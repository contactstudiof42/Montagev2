# Inserts lumineux à 138 BPM (BACKLOG 71, session 12, 2026-10-10) — [TESTÉ EN LABO, synthétique]

Question de l'examen n°7 (extraits kinetic d'« Heure creuse » : des sources de lumière qui s'éteignent sur la batterie) : à partir de quelle densité et de quelle taille un montage d'inserts lumineux échoue-t-il au contrôle de photosensibilité ?
Script : `gen_test.py <dossier>` (18 montages de 4 s, 25 i/s, une tache claire sur fond nocturne ; ~25 s) puis `../flash_check.py` (WCAG 2.3.1, fenêtre 1/3 × 1/3).

| Motif \ taille de la source | 1 % de l'écran | 5 % | 25 % |
|---|---|---|---|
| **alt** noires (2,3 évén./s : chaque coupe allume ou éteint) | OK (0) | OK (2) | OK (2) |
| **alt** croches (4,6 évén./s) | OK (0) | **limite** (3) | **limite** (3) |
| **alt** doubles croches (9,2/s) | OK (0) | ÉCHEC (5) | ÉCHEC (5) |
| **pulse** noires (s'allume puis s'éteint à chaque noire) | OK (0) | limite (3) | limite (3) |
| **pulse** croches | OK (0) | ÉCHEC (5) | ÉCHEC (5) |
| **pulse** doubles croches | OK (0) | ÉCHEC (10) | ÉCHEC (10) |
(entre parenthèses : flashs dans la pire seconde ; échec au-delà de 3)

## Ce que ça apprend
1. **Ma phrase d'examen était fausse dans sa forme** (« croches à 4,6 Hz = plus de 3 flashs/s ») : un flash est une **paire** de transitions. Si chaque coupe sur une croche fait **une seule** transition (on alterne allumé / éteint), on n'a que 2,3 flashs/s : à la limite, ça passe. Ce qui échoue, c'est **la pulsation** (allumer puis éteindre dans la même croche : 4,6 flashs/s) et l'alternance aux **doubles croches**.
2. **La taille ne sauve qu'en dessous de ~1 % de l'écran** (une source lointaine, un point) ; à 5 % comme à 25 %, le résultat est le même, car le critère porte sur la pire fenêtre de 1/3 × 1/3 (25 % de cette fenêtre ≈ 2,8 % de l'écran). Cohérent avec le cas E de la session 7.
3. **Règle de montage** pour un kinetic de sources lumineuses à ~140 BPM : une transition de luminance par croche au plus (une coupe = un allumage **ou** une extinction, jamais les deux) ; les accents plus serrés passent par la **forme ou la teinte** à luminance égale (cas C, session 7), ou par des sources minuscules. Et le **pont sans batterie** reste le seul vrai noir.
- Limites : signal synthétique (tache nette sur fond noir, pire cas réaliste) ; le contrôle reste un outil de montage, pas un Harding FPA ; fenêtre fixe (sur un téléphone tenu près, le champ de 10° couvre plus d'écran : prudence).
