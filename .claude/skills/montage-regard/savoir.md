Annexe de `SKILL.md` : méthode de visionnage et outils (savoir, pas des règles ; le SKILL.md fait foi). Déplacée du SKILL.md à l'audit 2 (2026-10-13). Le point 5 bis (moments forts revus de près, genres d'événement) vit dans `PROMPT-PHASE-3.md`, étape 1 ; la limite « je n'écoute jamais » dans la carte des sens de `CLAUDE.md`.

# montage-regard — savoir

## Méthode de visionnage
1. Planche à intervalle régulier avec numéro d'image : lire l'**arc**. [TESTÉ EN LABO]
   `ffmpeg -i v.mp4 -vf "select='not(mod(n\,20))',scale=320:-1,tile=5x2" -frames:v 1 planche.png` (le ffmpeg du Mac n'a pas `drawtext` : numéroter avec Pillow, ou `labo/outils/planche.py`)
2. Montage rapide : planche « 1re image de chaque plan » ; plan animé : 1re, dernière et image de l'événement, pas le milieu.
3. Planche avant / après chaque coupe : un détecteur de coupe ne juge pas le raccord.
4. Mesures quand c'est possible : luminance (`signalstats`), durées de plans (`scdet`, PySceneDetect), loudness (`ebur128`). Saillance : les outils de maquette (`atelier/12-inquietude-calme/mesure.py`, `labo/saillance/`) servent sur une image construite ; sur de vraies vidéos, la saillance automatique ne trouve le sujet qu'une fois sur trois (phase 2) : compter à l'œil (`labo/outils/echantillon_tiers.py`).

## Panel de regards (leçon du cabinet validée par Diego, 2026-10-31) [TESTÉ EN CONDITIONS RÉELLES]
- **Dossier de perception** : planches avec une ligne par plan (identifiant, début, durée ; 1 image si le plan fait moins de 15 images, 2 jusqu'à 2 s, 3 au-delà), un aperçu toutes les 2 s, et une partition plan par plan (mots de la voix par whisper, bruitages traduits en mots de spectateur, état de la musique, volume en LUFS, courbe par tranches de 5 s).
- **Un agent par regard** (inconnu, cible, client), chacun limité aux fichiers que son personnage connaîtrait ; tous lancés « d'abord sans le son » (lecture muette des réseaux), puis avec la partition.
- **Vérifier avant de transmettre** : chaque fait signalé se revoit sur l'image pleine taille (confusion transcription / sous-titres, mauvais repère).
- La méthode complète (briefs des regards, autocritique, outils de perception et détecteur de doublons) vit dans le skill `panel-de-retours` du cabinet ; elle n'est pas encore remontée ici.
