# Spotlight (Tom McCarthy, 2015 ; montage Tom McArdle)

_Fiche ouverte le 2026-10-11 (phase 2, session 8, film vague 3 n°2). **État : passe globale + 2 séquences + 3 plans longs vérifiés + comparaison avec *The Social Network*** ; restent l'ouverture de 1976, les témoignages des victimes et l'impression (voir « À faire »). Source : 1080p H.264 (SDR BT.709), **VO anglaise** (piste 2), sous-titres anglais complets (2 321). Travail dans `videos/_travail/spotlight/`. Planches commitées : `spotlight-sipe.png` (46:30-50:00), `spotlight-colere.png` (1:36:30-1:38:30). Aucune fiche de phase 1 sur McCarthy ou McArdle._

Skills relus : `montage-rythme` (plan long, tension par l'allongement), `montage-grammaire` (dialogue, hors champ), `montage-son-et-emotion` (voix hors champ), `montage-couleur-et-intention`, grille de `montage-regard` ; et `analyses/films/the-social-network.md` pour la comparaison demandée par la mission.

## Intention
Rendre crédible une enquête de journalistes : le spectateur doit sentir le travail (lire, appeler, recouper) et recevoir l'ampleur du scandale comme eux, par les chiffres et les voix, sans spectacle.

## Forme [mesuré]
- **2 h 09 ; au moins 1 182 plans, ASL 6,6 s, médiane 4,1 s**, 76 plans de 15 s ou plus. **-20,3 LUFS intégrés.** Deux fois moins de plans que *The Social Network* pour un film plus long.
- **Densité basse et plate** : 4 à 15 coupes/min presque tout le film, sans crête véritable. **Deux fausses crêtes** : la minute 95 (21 coupes/min, médiane 0,5 s) est un plan fixe de rue où le détecteur compte des « coupes » toutes les 0,5 s (lumière qui varie : leçon *Joker*) ; et la fin (minutes 121-128, aucune coupe) est un générique de **cartons sur noir** que le détecteur ne voit pas (leçon YggTorrent).
- **Couleur : claire, désaturée, neutre** (luminance moyenne 72/255, saturation 0,26, la plus basse des films en couleur mesurés, devant *Interstellar* 0,29 ; chaleur 6,2) et **constante** d'un sixième à l'autre (chaleur 6 à 10). Bureaux à néons, bleu-gris, sans look. [mesuré sur vignettes / 10 s]

## Séquences

### Les deux appels à Richard Sipe (47:21 et 1:00:05) [VU SUR IMAGES, plans vérifiés par `verif_plan.py` et tuile]
- **47:21,5 : un plan fixe de 67,1 s**, avec une lente poussée : Rezendes seul à son bureau, la nuit, la lampe allumée, au téléphone. Sipe (l'ancien prêtre qui étudie les abus) est **une voix hors champ** qui donne pour la première fois l'idée du système. Juste avant, une conversation de couloir tenue 49 s (plus un plan de 8,5 s à travers la vitre : le détecteur avait fusionné les deux en 57,7 s) ; juste après, deux plans de 28,6 et 43,4 s (vrais) à la bibliothèque.
- **1:00:05 : un plan de 115 s** (aucune coupe pour `verif_plan.py`, tuile à 1 image / 3 s cohérente) : l'équipe autour du haut-parleur, la caméra part d'un bureau et recadre lentement jusqu'au large de la pièce ; c'est l'appel où Sipe estime le nombre de prêtres (« Ninety fucking priests? In Boston? » à 1:02:00).
- **La révélation arrive par une voix au téléphone, et l'image tient ceux qui écoutent, en un seul plan.** Les deux plus longs plans du film sont les deux moments où l'enquête change d'échelle. C'est le principe « plan long réservé à ce qui compte » de la vague 1, avec un levier nouveau : **le hors champ sonore porte l'information, le plan tenu porte la réception**.

### La colère de Mike (1:36:11-1:38:35) [VU SUR IMAGES, `spotlight-colere.png` ; spectrogramme]
- Un large de 23,9 s pose le bureau, puis la dispute Rezendes / Robby en plans de 1,8 à 9,3 s. **La tension monte par l'échelle, pas par la vitesse** : les plans moyens deviennent des gros plans serrés (« It could've been you! », 1:37:45, deux gros plans de 2,0 et 5,3 s), sans que la durée des plans baisse vraiment (médiane environ 4 s du début à la fin). Puis **l'après tenu** : « You finished? » (2,8 s), le gros plan de Mike tenu 11,3 s (« This is bullshit »), Robby 5,8 s, et le son tombe (LUFS momentané de -17 à -36/-55 dans les secondes suivantes).
- **Coupes et parole** (23 coupes de la dispute, toutes regardées sur spectrogramme) : 7 clairement pendant la parole (30 %), 7 au bord d'un mot, 9 dans un silence ; l'outil (`SEUIL=haut`, voix séparée) dit 41 %.

## Comparaison avec *The Social Network* [mesuré ; demandée par la mission]
| | *The Social Network* | *Spotlight* |
|---|---|---|
| Plans, ASL / médiane | ≥ 2 287, 3,2 / 2,2 s | ≥ 1 182, 6,6 / 4,1 s |
| Plans ≥ 15 s | 27 | 76 |
| Densité | 15-30/min, crêtes 41-44 (Facemash, Henley) | 4-15/min, aucune vraie crête |
| Image | sombre, ambrée (Y 41, chaleur 20,5) | claire, neutre, désaturée (Y 72, S 0,26, chaleur 6,2) |
| Coupes pendant la parole (spectrogramme) | 7 / 23 (30 %), ouverture | 7 / 23 (30 %), dispute |
| Silences ≥ 0,15 s entre paroles (voix séparée) | médiane 0,24 s, 12 % du temps | médiane 0,48 s, 30 % du temps |
| Plan long | la décompression (35 s après le bar), le travelling d'équipage | la révélation au téléphone (67 et 115 s) |

- **Deux films de dialogue et d'enquête, la même part de coupes pendant la parole (30 %)** : ce chiffre ne distingue pas le style. Ce qui le distingue : **la durée des plans** (du simple au double), **l'air entre les répliques** (deux fois plus long chez McCarthy, même dans la dispute la plus violente) et **l'image** (Fincher marque, McCarthy s'efface). Limite : la rumeur du bar passe dans la voix séparée de *The Social Network* et réduit ses silences mesurés ; à l'œil sur les spectrogrammes, l'écart va dans le même sens.
- **Deux façons de faire monter** : *The Social Network* monte par la vitesse (rafales sur les processus) et le son (masses fortes) ; *Spotlight* par **l'échelle des plans** et **le plan tenu** au moment où l'information change d'ordre de grandeur. Les deux réservent le plan long à autre chose que l'action.
- Pour Studio F42 : un film corporate ou une enquête de marque **gagne à la sobriété de *Spotlight*** quand le sujet doit être cru (témoignage, chiffres) ; le registre *Social Network* convient quand le sujet est la vitesse ou l'ambition (lancement, start-up). À éprouver en maquette.

## Ce qui confirme, contredit ou complète mes skills
- **Confirme** « le plan long réservé à ce qui compte » (vague 1) et **complète** : il peut tenir sur ceux qui écoutent une voix hors champ (`montage-son-et-emotion`, hors champ).
- **Confirme** « tension par l'allongement » (`montage-rythme`, *Joker*) sous une autre forme : **tension par le resserrement de l'échelle**, à durée constante.
- **Confirme** « l'après est tenu » (dispute → gros plan de 11,3 s et chute du son).
- **Confirme** deux pièges de méthode (lumière qui varie sur un plan fixe, cartons sur noir) et la fusion de plans voisins par le détecteur (57,7 s = 8,5 + 49 s).
- **Corrige ma méthode** : « coupes pendant la parole » ne caractérise pas un style de dialogue (même 30 % chez Fincher et McCarthy) ; mesurer plutôt **la durée des silences entre répliques** et la durée des plans.

## Principes transférables
1. **Une information qui change tout arrive par une voix, et l'image tient ceux qui l'entendent** (téléphone, haut-parleur, voix off), en un plan.
2. **Faire monter une dispute par l'échelle des plans**, pas par leur vitesse ; garder l'air entre les répliques.
3. **Une image qui s'efface rend un sujet crédible** : lumière de bureau, désaturation, aucune couleur de genre.

## Ce que Diego en a dit
Rien (aucune note dans `NOTES-DIEGO.md`).

## À faire
- L'ouverture (1976, commissariat, environ 0:00-3:30 : plans de 22 à 40 s) et les témoignages des victimes (Saviano à 31:28, autres témoins).
- L'impression du journal et la fin : les téléphones qui sonnent (2:00:00-2:00:30), puis les cartons sur noir (bilan chiffré, puis **quatre cartons de listes de villes** où des scandales ont été révélés) : compter les cartons et leurs durées (tuile à 1 image / 2 s).
