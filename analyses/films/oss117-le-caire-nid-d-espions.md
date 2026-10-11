# *OSS 117 : Le Caire, nid d'espions* (Michel Hazanavicius, 2006)

_Fiche ouverte le 2026-10-11 (phase 2, session 7, film vague 2 n°4). **État : passe globale + 2 séquences + coupes / parole sur deux scènes** ; restent l'ouverture, une scène de nuit bleue et la comparaison complète avec *Le Dîner de cons* (voir « À faire »). Source : Blu-ray 1080p HEVC 10 bits (SDR BT.709), VF d'origine AC3 5.1. Pas de sous-titres texte complets : transcription Whisper `-mc 0` (`videos/_travail/oss117/transcription.srt`, 1 241 segments). **Fantômes et boucles repérés** : « Je n'ai pas vu ça » répété toutes les secondes de 54:23 à 54:41, « Allah est-ce que vous voyez ? » ×7 à 47:15-47:34 (l'appel à la prière), 34 « Sous-titrage… » sur les passages sans voix. Planches commitées : `oss117-courbes.png`, `oss117-couleur.png`, `oss117-poulets.png` (17:50-19:50), `oss117-fin.png` (1:30:30-1:34:30). Aucune fiche de phase 1 sur Hazanavicius._

Skills relus : `montage-rythme` (timing comique), `culture/timing-comique-sitcom.md`, `culture/gags-de-montage.md`, `analyses/films/diner-de-cons.md` (l'autre comédie française de la phase 2), grille de `montage-regard`.

## Intention
Un pastiche des films d'espionnage des années 1950-60 (OSS 117, agent français sûr de lui, ignorant et raciste sans le savoir). La forme imite le cinéma de l'époque pour que le décalage vienne du personnage, pas du montage.

## Forme [mesuré]
- **1 h 39 min ; au moins 1 317 plans, ASL 4,5 s, médiane 2,9 s**, 54 plans de 15 s ou plus. **-21,8 LUFS intégrés.**
- **Densité plate, de 10 à 22 coupes/min presque tout le film**, comme *Le Dîner de cons* (10 à 20) : la comédie de dialogue a une densité plate (deux films sur deux).
- **La crête de 30 coupes/min (minute 91) est fausse** : à 1:31:42-1:31:52, dix-huit « plans » de 0,5 s exactement sont le même cadre éclairé par les explosions du bateau derrière la fenêtre pendant le baiser (leçon « fausses coupes de lumière », *Joker*, *Mad Max*). Sans eux, la fin n'est pas plus rapide que le reste.
- Couleur : un beige sablé et chaud presque partout, et quelques blocs **bleu nuit saturé** (vers 0:35-0:39, 0:51-0:53, 1:23) : la « nuit américaine » des films d'époque. À vérifier sur images.

## Séquences

### Les poulets (17:50-19:50) [VU SUR IMAGES, `oss117-poulets.png`]
- Le gag de répétition (« Et ce bruit ? — C'est aussi le poulet ») est monté en **champ-contrechamp de 0,8 à 1,7 s**, une question et une réponse par plan ; puis le gag visuel (OSS allume et éteint la lumière, les poulets se taisent et reprennent) tient dans un plan de 3,1 s. La scène suivante (le patron, 18:35-19:57) revient à des plans de 2 à 8 s, et finit sur un plan de 30 s.
- Même partage que *Le Dîner de cons* : **l'échange verbal en champ-contrechamp rapide, le gag de situation dans un plan qui le contient**.

### La fin (1:30:30-1:34:30) [VU SUR IMAGES, `oss117-fin.png`]
- Le baiser dans la chambre pendant que le bateau explose derrière la fenêtre (en un cadre), puis le bureau du chef (champ-contrechamp de 1 à 4 s), un **carton « FIN »** plein écran à 1:33:18, puis **un générique de casting à l'ancienne** : chaque acteur nommé sur un plan du film (3 à 4,5 s chacun), jusqu'à Jean Dujardin en dernier, de profil sur fond uni.
- **L'habillage vient du genre pastiché** : le carton « FIN » et le casting nominatif sont des signes des films des années 1960. Même principe que les clips (« l'habillage vient du sujet »), appliqué à un pastiche : l'habillage vient de l'époque imitée.

## Coupes et parole [mesuré, `coupes_parole.py` ; **doute sur la source**]
| Passage | Coupes | Parole (mix / voix séparée) | Coupes pendant la parole (mix / voix séparée) |
|---|---|---|---|
| 7:00-10:40 (« blanquette ») | 60 | 71 % / 76 % | **57 % / 90 %** |
| 17:50-19:50 (poulets) | 29 | 55 % / 73 % | **52 % / 86 %** |
- Sur le mixage, les coupes qui tombent dans un silence le font très tôt (0,08 à 0,40 s après la fin de la réplique, médiane 0,21 s), comme *Le Dîner de cons* (0,35 s) : presque pas d'air.
- **Les deux sources donnent des résultats très différents** (57 % contre 90 %). La leçon de session 5 dit de préférer la voix séparée quand il y a un fond musical ; ici, la part de parole bouge peu (71 % contre 76 %) mais les micro-silences du mixage disparaissent sur la voix séparée (traînées de réverbération de demucs ?). **Je ne tranche pas** : dans les deux cas, OSS 117 coupe au moins autant pendant la parole que *Le Dîner de cons* (40-44 %, mesuré sur mixage) et ne laisse presque jamais d'air. À revoir en passe de révision en marquant une vingtaine de coupes à la main.

## Ce qui confirme, contredit ou complète mes skills
- **Confirme** « une comédie de dialogue a une densité plate » (bilan de la vague 1, *Le Dîner de cons*) : deux films sur deux.
- **Confirme** « les fausses coupes de lumière » (`PROMPT-PHASE-2.md`, leçons) : sans contrôle, la crête de la fin aurait fait croire à un climax accéléré.
- **Confirme** le partage du timing comique (`montage-rythme`, *Le Dîner de cons*) : échange en champ-contrechamp rapide, gag de situation dans un plan.
- **Complète** « l'habillage vient du sujet » (bilan des clips) : dans un pastiche, il vient de l'époque imitée (carton « FIN », casting nominatif).

## Principes transférables
1. **Le pastiche est un sérieux** : la forme copie l'époque sans clin d'œil (montage, cartons, couleur) ; le comique vient du personnage. Pour une pub parodique (GOUTS.md : « même un Comic Sans MS couleur caca peut être bien utilisé dans un spot parodique »), imiter le genre jusqu'au générique.
2. **Une question, une réponse, un plan** : un gag de répétition se monte vite en champ-contrechamp ; le gag visuel garde un plan large qui le contient.

## Ce que Diego en a dit
Rien sur ce film (aucune note dans `NOTES-DIEGO.md`). Le rapprochement avec la parodie vient de GOUTS.md (réponse 10).

## À faire
- Ouverture (générique et flash-back), une scène de nuit bleue (couleur sur image extraite), la chorégraphie ou la bagarre (le gag dans le plan).
- Trancher la mesure coupes / parole (mix ou voix séparée) en marquant des coupes à la main.
