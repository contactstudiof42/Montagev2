# Ziak — « Même pas un grincement » (Bleu Désert, 2023) — montage Antonin Brones

_Fiche ouverte le 2026-10-11 (phase 2, session 3, clip n°1). **État : terminée.** Source : 1080p, 25 i/s, 3 min 49,5, SDR (bt709). Planches commitées : une image par plan avec le volume momentané en dessous, `ziak-a.png` (0:00-1:55) et `ziak-b.png` (1:55-3:50)._

**Lu avant l'analyse** : la fiche de phase 1 `culture/ziak-meme-pas-un-grincement.md` (recherche, puis analyse mesurée sur une copie 720p le 2026-10-09), `montage-rythme` (micro ou macro), `montage-kinetic-editing`, grille de `montage-regard`. **Goût de Diego** (GOUTS.md) : « fan absolu » ; il aime ce clip et le kinetic « pour des usages différents ». Ce clip est la référence de la retenue à l'intérieur d'un morceau agressif.

## Ce que la phase 2 change à l'analyse de phase 1
La phase 1 avait déjà mesuré le clip (88 plans, coupes non calées sur le beat, 26 contre 13,4 coupes/min selon la basse). Je l'ai repris avec les leçons de la phase 2 (coupes ratées dans le sombre, recomptage avant de citer, comparaison au hasard).

| Conclusion de phase 1 | Verdict | Mesure de la phase 2 |
|---|---|---|
| 88 plans, médiane 1,67 s | **corrigée** | **environ 109 plans, médiane 1,2 s, ASL 2,1 s**. Les deux détecteurs (phase 1 en 720p, PySceneDetect en 480p) ratent les plans d'usine dans le noir. Sur une copie éclaircie (courbe qui relève les ombres), PySceneDetect en trouve 41 de plus ; vérifiés à l'œil (paire d'images avant / après) : 23 vraies, 10 éclairs de tirs, 7 étincelles ou mouvements, 1 douteuse. Le « plan de 10,4 s » de 1:01 contient en fait au moins 6 plans (bras, atelier, ouvrier casqué, étincelles). |
| Coupes non calées sur le beat | **confirmée** | Avec les 109 plans : 19 % des coupes à ±2 images d'une attaque forte (hasard 22 %, 5e-95e centile 15-29 %) ; 38 % sur un temps (hasard 35 %). Avant correction, j'avais cru qu'elles **évitaient** les attaques (12 %, sous le 5e centile) : c'était un effet des coupes manquantes. |
| Deux fois plus de coupes quand la basse est là (26 contre 13,4/min) | **confirmée, plus nette** | **32,3 coupes/min avec la basse (173 s) contre 16,1 sans (56 s)**, même méthode qu'en phase 1 (énergie sous 120 Hz par seconde, seuil à -20 dB du maximum). Toutes les coupes ajoutées tombent dans des passages avec basse. |
| Un plan long à chaque creux de basse de plus de 5 s | **confirmée** | 0:14-0:19 → 5,2 s ; 0:30-0:40 → la voiture sous la pluie, **11,8 s** (vérifié continu à 1 image/s) ; 2:13-2:37 → la femme enceinte, 6,8 + 4,0 + 3,0 + 3,8 + 6,8 s ; 3:41-3:48 → le plan d'immeuble final, 11,6 s. |
| Les éclairs des tirs battent leur propre horloge (0,60 s) | **confirmée** | La copie éclaircie compte une « coupe » toutes les 0,6 s de 0:43,5 à 0:48,9 dans le plan des motards (13 s, vérifié : un seul cadre). |
| La révélation retenue jusqu'à 3:24 | **complétée** | La créature n'est vue **en pleine lumière que pendant un éclair de 0,6 s** (3:25,4) ; avant et après, elle est dans le noir au milieu des cagoulés (2,6 s et 2,5 s), puis 4,3 s de noir. Vu à 4 images/s. |

## Intention
Un mythe froid : l'artiste masqué démonté et reconstruit « mi-ombre mi-machine » ; une menace contenue sous une drill agressive. [SOURCÉ par la phase 1 (D&AD, réalisateurs) ; DÉDUIT pour l'effet]

## Forme [mesuré, corrigé à l'œil]
- **3 min 49, environ 109 plans, ASL 2,1 s, médiane 1,2 s.** Histogramme : < 1 s : 45 · 1-2 s : 32 · 2-4 s : 16 · 4-8 s : 13 · ≥ 8 s : 3. Plus de 40 % des plans durent moins d'une seconde.
- Coupes par tranche de 15 s : 9, 6, **3, 5** (l'intro sous la pluie, les deux plans longs), puis **10, 13** (l'usine), 8, 5, **14** (la foule cagoulée, 2:00-2:15), 4, 6 (la femme enceinte), 7, 5, 11, 2 (la fin).
- **Son : -9,9 LUFS intégrés**, un mur. Le volume momentané reste presque plat de 0:30 à 3:30 ; il ne creuse que brièvement (vers 0:16, 0:58, 1:20, 1:48, 3:20) puis s'effondre pendant le noir final.
- Image très basse (médiane 8/255 en phase 1), quasi monochrome froide ; une seule couleur chaude, le feu et les étincelles.

## Choix par domaine
- **Rythme** : la vitesse de coupe suit l'**arrangement** (la basse), pas les temps. Le clip est rapide (médiane 1,2 s, plus rapide que Mad Max) et pourtant ne « tape » jamais : aucune coupe calée, aucun effet sonore surligné. C'est un montage rapide **sans kinetic**.
- **Cadre** : plongées verticales (corps au sol, cage d'escalier), objets en coupe sur fond noir, plans larges immobiles pour les plans longs (la voiture, les motards, la femme sur sa passerelle, l'immeuble).
- **Lumière et couleur** : le noir est la matière ; la lumière arrive en événements (éclairs des tirs, gerbes d'étincelles, l'éclair de la révélation).
- **Transitions et effets** : coupes franches ; aucune transition visible. Les éclairs créent des pulsations à l'intérieur des plans fixes.

## Confirme, contredit, complète
- **Confirme** `montage-rythme` (« micro ou macro, à choisir ») avec un comptage corrigé : le macro (densité selon la basse) est mesurable et net (rapport 2).
- **Confirme** la leçon de méthode des scènes sombres (Interstellar) sur un clip : **88 plans comptés deux fois par deux détecteurs différents, et c'était faux de 20 %**. Nouveau : **éclaircir la copie avant la détection** retrouve les coupes, mais ajoute les éclairs ; il faut ensuite trier à l'œil sur des paires d'images.
- **Confirme** « le plus fort suivi du vide » (Joker, Mad Max) : la révélation (0,6 s de lumière) est suivie de 4,3 s de noir et d'un plan tenu de 11,6 s.
- **Complète** `montage-kinetic-editing` : la vitesse de coupe n'est pas le kinetic. Ce clip coupe très vite (médiane 1,2 s, plus vite que Mad Max), mais sans calage, sans SFX, sans effet. Ce qui fait le kinetic, c'est **la synchronisation et le surlignage**, pas la durée des plans.
- **Complète** la règle de la révélation (Menke, phase 1) : retenir la révélation **dans le temps** (3 min 25 d'attente) **et dans la lumière** (0,6 s de visibilité). Le spectateur n'a jamais le temps de la regarder en entier : elle reste un mythe.

## Principes transférables
1. **Vite sans taper** : sur une musique agressive, couper aussi vite que la musique (moins d'une seconde) mais hors des temps ; la tension vient de la masse, pas de l'impact.
2. **La densité suit la basse** : deux fois plus de coupes quand la basse joue, un plan long et immobile à chaque creux de plus de 5 s.
3. **Montrer le personnage-clé en un éclair** : l'image la plus attendue en 0,6 s, puis le noir.
4. **Pour un clip très sombre, éclaircir la copie de travail avant de compter les coupes** (méthode, pas esthétique).

Pour Studio F42 : le principe 2 est directement applicable à un clip ou à une pub sur une musique rythmée, et il est compatible avec les deux goûts de Diego (le kinetic sur les passages avec basse, la retenue dans les creux). [DÉDUIT, à éprouver en maquette]

## Ce que Diego en a dit
GOUTS.md : « fan absolu » (2026-10-09) ; il aime ce clip, au montage qui ne colle pas au beat, et le kinetic, « pour des usages différents ». Aucun minutage ni commentaire de détail.

## Pas fait
- Le son n'est pas écouté ; la séparation de la basse par demucs n'a pas été faite (la basse est estimée par l'énergie sous 120 Hz du mixage).
- La coupe douteuse de 1:06,9 (même ouvrier casqué, plus serré : coupe dans l'axe ou mouvement de caméra ?).

## Doutes
- Le décompte de 109 plans peut encore être un minimum : un raccord entre deux plans noirs ou presque noirs reste invisible même sur la copie éclaircie.
