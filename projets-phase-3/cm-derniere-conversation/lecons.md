# « L'Air » — leçons du projet

_Classées par portée (`CLAUDE.md`). Une règle [universel] remonte dans son skill ; une leçon [projet] reste ici._

- **[universel] L'axe des 180° se vérifie par le calcul avant de montrer quoi que ce soit** (2026-10-24). Erreur : sur la première planche de la previz, la caméra sur lui (plans 2b, 3, 4b, 5b) était du côté +Y de la ligne d'action, et les deux personnages regardaient vers la gauche de l'écran. Diego : « rien que sur la previz que je vois, il y a un souci de règle des 180°, corrige ça dès à présent, avant quelconque livraison ». Remontée dans `montage-grammaire` § 4. Contrôle : `blender/verif_previz.py` (côté de l'axe, regards à l'écran, sol et jambes cachés avant 7b, dôme visible) ; zéro erreur avant chaque planche.
- **[projet] Mannequins Blender** : pour un personnage qui regarde +Y, une rotation positive autour de X envoie un membre pendant vers l'arrière (cuisses et bras partaient derrière). Corrigé dans `k()` de `build_previz.py` ; à vérifier sur les positions mesurées (genoux devant les hanches, mains sur la table), pas seulement à l'œil sur la planche.
