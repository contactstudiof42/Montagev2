# Pièce 25 « Au lit » — critique (session 20, 2026-10-10)

Commandes : `python3 piece.py ../rendus/25 A,B,C,D` (15 s de calcul) puis `python3 mesure.py ../rendus/25 A,B,C v1-mesures.png` (bande-film 1 image / 5 s + YAVG en jaune + LUFS court terme en bleu ; valeurs dans le `.json` voisin).

## v1 — `v1-mesures.png`
| Version | YAVG par 5 s | LUFS S par 5 s |
|---|---|---|
| A descente | 46 43 30 25 **39 41** 35 28 24 20 25 28 | -28 → -43 (dents de scie voix / silence, pente nette) |
| B plat | 36 39 37 32 26 21 **35 39 37 32 26 21** | -33 à -39, sans pente |
| C contradiction | 47 46 32 28 46 51 44 36 30 23 36 44 | -27 à -34, sans pente |

- **A ne descend pas à l'image** alors que le gradateur fait −60 % : la luminance propre de chaque plan (une lampe de chevet contre un ciel d'étoiles : ×3) écrase le gradateur. La lampe tombe à 25 s et fait **le pic de lumière de la seconde moitié** : un réveil au milieu de la descente. **L'ordre des plans est une courbe de lumière** ; un variateur appliqué sur un montage ne la corrige pas.
- **B** : la séquence de 5 plans revient **à l'identique** au bout de 30 s (même YAVG au dixième près) : la boucle se voit sur la bande-film. Plat n'est pas seulement « sans direction » : c'est **prévisible sans être attendu**. C'est là que l'ennui commence (hypothèse, non mesurable ici).
- **C** : la voix ralentit et les plans s'allongent, mais l'image et le son restent forts : sur la bande-film, C ressemble à A en plus clair, et la fin (fenêtre à 44) est plus lumineuse que le début du dernier tiers. Les canaux se contredisent à la fin, là où l'on devrait lâcher.
- **Ce qui marche le mieux n'est pas un réglage** : les fenêtres de la ville qui **s'éteignent une à une** dans le plan (le temps qui passe raconté dans l'image). La descente se lit mieux comme un **événement du monde** que comme un réglage de post (même leçon que la pièce 18 : l'œil lit l'énergie du cadre, et une extinction a une cause).

## v2 — `v2-mesures.png` (D)
D = A, mais 6 plans ordonnés par leur luminance propre (lampe, tasse, fenêtre, mer, **retour de la fenêtre presque éteinte**, étoiles), de 5 à 20 s. YAVG : 49 41 41 38 29 32 35 33 20 20 19 19 : presque monotone. Le retour de la fenêtre (le même cadre, moins de lumières) sert de **mesure du temps**, comme le cadre qui revient avec un détail changé (pièce 12).
- Reste faux : (1) le retour de la fenêtre remonte (29 → 35) au-dessus de la mer : un cadre fixe clair ne doit pas revenir après un plan plus sombre ; (2) **les 20 dernières secondes sont quasi noires** (YAVG 19, ciel à 40 % de gradateur) : sur la bande-film, ça se lit « vidéo finie » ou « écran éteint », pas « on s'endort ». **Le plancher d'une descente reste au-dessus de l'écran noir** : garder un point de lumière vivant (la lune, une seule fenêtre allumée) jusqu'à la fin.

## Leçons (versées dans `montage-rythme` et `montage-couleur-et-intention`)
1. Une descente de lumière se monte **dans l'ordre des plans** (luminance propre de chacun) avant de se régler au gradateur.
2. Une descente se lit mieux comme un **événement du monde** (des fenêtres qui s'éteignent) que comme un réglage.
3. Le plancher reste **au-dessus du noir** : un dernier point de lumière, sinon la fin se lit comme une panne.
4. Plat = boucle reconnaissable ; l'ennui vient de ce qui est prévisible sans être attendu (hypothèse).

## Limites et v3
Jugement sur bande-film et courbes, sans regarder en mouvement ni écouter ; « endort » n'est pas mesuré (phase 2 : un spectateur au lit). v3 : la mer avant le retour de la fenêtre ; une dernière fenêtre allumée qui ne s'éteint pas ; voix qui s'arrête vers 45 s et nappe seule ensuite ; version téléphone luminosité basse (YAVG perçu en mode nuit).

## v3 — `v3-mesures.png` (E)
- 1er essai (non gardé) : fenêtre en dernier, une seule lumière allumée → YAVG 20 → **32** à 40 s : un cadre fixe clair qui revient tard **réveille**, même porteur d'une jolie idée (« quelqu'un d'autre ne dort pas »).
- **E** : lampe, fenêtre, tasse, **retour de la fenêtre à moitié éteinte** (19-28 s), mer, étoiles avec **la lune non graduée** (40-60 s). YAVG : 49 43 40 39 38 33 27 26 21 21 20 20 : **monotone** pour la première fois. Sur la bande-film, les 20 dernières secondes ne se lisent plus « écran éteint » : un point blanc tient le cadre, et comme tout le reste baisse, **la lune paraît s'allumer** (elle était grise dans le plan de mer) : c'est l'œil qui s'habitue au noir. La dernière lumière n'est pas un reste : elle devient l'image.
- Verdict : E est la référence. Le retour de la fenêtre doit tomber **au milieu** (quand la luminance générale est encore au-dessus de lui), jamais à la fin.
- Reste : voix qui s'arrête vers 45 s (nappe seule ensuite) ; vérifier en mouvement que la lune « qui s'allume » ne se lit pas comme une erreur de raccord ; version téléphone en mode nuit.

## Confrontation à la fiche slow TV / ASMR (session 21)
- `culture/asmr-slow-tv-videos-pour-dormir.md` **confirme** : le changement causé par le monde (pas par un réglage) et le plancher au-dessus du noir (NRK évitait l'écran noir dans les tunnels).
- Elle **contredit** deux choses : (1) 5 à 6 coupes en 60 s, c'est encore beaucoup pour ce registre (slow TV et Bob Ross ne coupent presque pas) → v4 à tester : 2 plans seulement, la descente portée par la lumière **dans** le plan ; (2) la descente simultanée de tous les canaux n'est pas nécessaire (Bob Ross garde lumière et volume constants) : une seule direction lente suffit. Le point le plus faible reste la **voix synthétique** neutre (la voix proche et basse est le premier déclencheur cité) : en phase 2, une vraie voix enregistrée près du micro.
- Limite : une minute peut *signaler* l'endormissement, pas le provoquer (les formats réels durent 20 min à 134 h).
