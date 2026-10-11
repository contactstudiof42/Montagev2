# *OSS 117 : Le Caire, nid d'espions* (Michel Hazanavicius, 2006)

_Fiche ouverte le 2026-10-11 (phase 2, session 7, film vague 2 n°4). **État : terminée en session 8** (passe globale, 4 séquences, nuits, coupes / parole tranchées à l'œil) ; reste en option la comparaison complète avec *Le Dîner de cons* (voir « À faire »). Source : Blu-ray 1080p HEVC 10 bits (SDR BT.709), VF d'origine AC3 5.1. Pas de sous-titres texte complets : transcription Whisper `-mc 0` (`videos/_travail/oss117/transcription.srt`, 1 241 segments). **Fantômes et boucles repérés** : « Je n'ai pas vu ça » répété toutes les secondes de 54:23 à 54:41, « Allah est-ce que vous voyez ? » ×7 à 47:15-47:34 (l'appel à la prière), 34 « Sous-titrage… » sur les passages sans voix. Planches commitées : `oss117-courbes.png`, `oss117-couleur.png`, `oss117-ouverture.png` (0:00-4:00), `oss117-poulets.png` (17:50-19:50), `oss117-fin.png` (1:30:30-1:34:30), `oss117-nuits.png` (quatre images de nuit : 36:00, 37:00, 51:30, 1:23:00), `oss117-bagarre.png` (42:25-43:35). Aucune fiche de phase 1 sur Hazanavicius._

Skills relus : `montage-rythme` (timing comique), `culture/timing-comique-sitcom.md`, `culture/gags-de-montage.md`, `analyses/films/diner-de-cons.md` (l'autre comédie française de la phase 2), grille de `montage-regard`.

## Intention
Un pastiche des films d'espionnage des années 1950-60 (OSS 117, agent français sûr de lui, ignorant et raciste sans le savoir). La forme imite le cinéma de l'époque pour que le décalage vienne du personnage, pas du montage.

## Forme [mesuré]
- **1 h 39 min ; au moins 1 317 plans, ASL 4,5 s, médiane 2,9 s**, 54 plans de 15 s ou plus. **-21,8 LUFS intégrés.**
- **Densité plate, de 10 à 22 coupes/min presque tout le film**, comme *Le Dîner de cons* (10 à 20) : la comédie de dialogue a une densité plate (deux films sur deux).
- **La crête de 30 coupes/min (minute 91) est fausse** : à 1:31:42-1:31:52, dix-huit « plans » de 0,5 s exactement sont le même cadre éclairé par les explosions du bateau derrière la fenêtre pendant le baiser (leçon « fausses coupes de lumière », *Joker*, *Mad Max*). Sans eux, la fin n'est pas plus rapide que le reste.
- Couleur : un beige sablé et chaud presque partout, et quelques blocs **bleu nuit saturé** (vers 0:35-0:39, 0:51-0:53, 1:23) : la **nuit américaine** des films d'époque, vérifiée sur quatre images extraites (`oss117-nuits.png`) : arcades, barque sur l'eau, bureau aux fenêtres bleues, tout en bleu dense ; seuls les visages et une chambre restent chauds. [VU SUR IMAGES]

## Séquences

### L'ouverture (0:00-3:22) [VU SUR IMAGES, `oss117-ouverture.png`]
- Le **logo Gaumont d'époque**, puis un prologue **en noir et blanc** (1945, un avion, un officier allemand) monté en champ-contrechamp de 1 à 3 s ; OSS 117 se présente à 2:16,8 (plan de 6,5 s, le plus long de l'échange). Puis un plan de lune de 16,8 s et **le générique en couleur**, sur un motif de tissu à pois des années 1960.
- **Un format et une couleur par époque** : N&B pour 1945, couleur saturée pour 1955. Même principe qu'adidas (4:3 chaud / large froid) et KAIZEN (archives N&B, webcam 4:3) : changer de matière pour changer d'époque.

### Les poulets (17:50-19:50) [VU SUR IMAGES, `oss117-poulets.png`]
- Le gag de répétition (« Et ce bruit ? — C'est aussi le poulet ») est monté en **champ-contrechamp de 0,8 à 1,7 s**, une question et une réponse par plan ; puis le gag visuel (OSS allume et éteint la lumière, les poulets se taisent et reprennent) tient dans un plan de 3,1 s. La scène suivante (le patron, 18:35-19:57) revient à des plans de 2 à 8 s, et finit sur un plan de 30 s.
- Même partage que *Le Dîner de cons* : **l'échange verbal en champ-contrechamp rapide, le gag de situation dans un plan qui le contient**.

### La bagarre du poulailler (42:21-43:42) [VU SUR IMAGES, `oss117-bagarre.png` + tuiles à 2 et 6 images/s non commitées]
- **L'attente (42:21-43:00)** : OSS appelle « Slymane ? » dans un hangar de cages à poulets, la nuit. Plans de 3 à 9 s, son presque muet entre les appels (LUFS momentané au plancher, deux pics de voix). Le « plan » de 13,2 s à 42:43,9 en contient deux (**coupe cachée dans le noir** à 42:49,7, ratée par PySceneDetect et par `verif_plan.py`) : un large fixe où OSS est minuscule au fond de l'allée (5,8 s), puis un **travelling latéral derrière les barreaux** (7,3 s) qui finit par le découvrir, regard d'un guetteur invisible. C'est la grammaire du suspense des films d'espionnage, jouée sans clin d'œil.
- **La bagarre (43:00-43:42)** : au moins 19 plans en 42 s (environ 28 coupes/min, contre 10 à 22 dans le reste du film ; le détecteur en rate au moins un, à 43:35). Les coups et les jets sont en plans de 0,5 à 2 s, cadres moyens, sans caméra portée ; mais **les deux temps comiques sont tenus** : la main qui ramasse un poulet dans la paille (4,1 s) puis **OSS debout, sérieux, un poulet tenu comme une arme** (5,6 s), et plus loin le gros plan de l'agresseur qui reçoit un poulet en plein visage. Le son monte par paliers aux premiers jets (43:13 puis 43:31).
- **Le gag est dans l'objet, pas dans le montage** : la bagarre est découpée comme une vraie bagarre de film d'époque (plus vite que le film, sans rafale), et c'est l'arme absurde, montrée dans un plan qui dure, qui fait rire. Même partage qu'aux poulets (17:50) : échange rapide, gag tenu.

### La fin (1:30:30-1:34:30) [VU SUR IMAGES, `oss117-fin.png`]
- Le baiser dans la chambre pendant que le bateau explose derrière la fenêtre (en un cadre), puis le bureau du chef (champ-contrechamp de 1 à 4 s), un **carton « FIN »** plein écran à 1:33:18, puis **un générique de casting à l'ancienne** : chaque acteur nommé sur un plan du film (3 à 4,5 s chacun), jusqu'à Jean Dujardin en dernier, de profil sur fond uni.
- **L'habillage vient du genre pastiché** : le carton « FIN » et le casting nominatif sont des signes des films des années 1960. Même principe que les clips (« l'habillage vient du sujet »), appliqué à un pastiche : l'habillage vient de l'époque imitée.

## Coupes et parole [mesuré, `coupes_parole.py`, puis tranché à l'œil sur spectrogramme en session 8]
| Passage | Coupes | Parole (mix / voix séparée) | Coupes pendant la parole (mix / voix séparée) |
|---|---|---|---|
| 7:00-10:40 (« blanquette ») | 60 | 71 % / 76 % | **57 % / 90 %** |
| 17:50-19:50 (poulets) | 29 | 55 % / 73 % | **52 % / 86 %** |
- Sur le mixage, les coupes qui tombent dans un silence le font très tôt (0,08 à 0,40 s après la fin de la réplique, médiane 0,21 s), comme *Le Dîner de cons* (0,35 s) : presque pas d'air.
- Les deux sources donnaient des résultats très différents (57 % contre 90 %). **Tranché en session 8 à l'œil** [VU SUR SPECTROGRAMME] : 20 coupes de la « blanquette » (une sur trois) regardées sur spectrogramme du mixage et de la voix séparée, ±0,6 s autour de la coupe (`videos/_travail/oss117/`, planche non commitée) :
  - **4 sur 20 clairement pendant la parole** (harmoniques continus à travers la coupe) ;
  - 2 dans un trou de moins de 0,2 s entre deux mots, 1 exactement sur la fin d'un mot ;
  - 5 dans le silence, **moins de 0,1 s après la fin de la réplique** (ou juste avant la reprise) ;
  - 8 dans un vrai silence ou sous la seule musique.
  - Donc **environ 20 à 35 % des coupes pendant la parole**, et la plupart **au ras de la réplique** : la coupe tombe sur la dernière syllabe ou dans le dixième de seconde qui suit. C'est la forme la plus serrée du timing comique sans public (*Le Dîner de cons* : environ 0,35 s d'air).
- **Pourquoi l'outil se trompait** : `coupes_parole.py` fixait le seuil de parole à « percentile 20 + 10 dB ». Sur le mixage, la musique et l'ambiance passent ce seuil (57 %). Sur la voix séparée, le percentile 20 est un quasi-silence numérique (10 dB, contre 33 dB sur le mixage) : réverbération et fuites passent le seuil (90 %). Nouveau réglage `SEUIL=haut` (percentile 90 - marge) : 43 à 48 % sur la voix séparée avec une marge de 15 à 20 dB, plus proche de l'œil, encore trop haut (les trous de moins de 150 ms entre mots sont bouchés). **Seul l'œil sur spectrogramme tranche une coupe au bord d'un mot.**

## Ce qui confirme, contredit ou complète mes skills
- **Confirme** « une comédie de dialogue a une densité plate » (bilan de la vague 1, *Le Dîner de cons*) : deux films sur deux.
- **Confirme** « les fausses coupes de lumière » (`PROMPT-PHASE-2.md`, leçons) : sans contrôle, la crête de la fin aurait fait croire à un climax accéléré.
- **Confirme** le partage du timing comique (`montage-rythme`, *Le Dîner de cons*) : échange en champ-contrechamp rapide, gag de situation dans un plan.
- **Confirme** « la rafale pour l'acte, le gag tenu » (`montage-rythme`, timing comique) : la bagarre coupe plus vite, mais ses deux temps comiques sont des plans de 4 à 6 s.
- **Confirme** la leçon des scènes sombres (`PROMPT-PHASE-2.md`) : une coupe cachée dans le noir, même dans un film en couleur bien exposé.
- **Complète** « l'habillage vient du sujet » (bilan des clips) : dans un pastiche, il vient de l'époque imitée (carton « FIN », casting nominatif).

## Principes transférables
1. **Le pastiche est un sérieux** : la forme copie l'époque sans clin d'œil (montage, cartons, couleur) ; le comique vient du personnage. Pour une pub parodique (GOUTS.md : « même un Comic Sans MS couleur caca peut être bien utilisé dans un spot parodique »), imiter le genre jusqu'au générique.
2. **Dans une parodie d'action, découper l'action au sérieux et tenir le plan de l'objet absurde** (le poulet comme arme) : le rire vient de la durée du plan sur l'objet, pas d'un effet de montage.
3. **Une question, une réponse, un plan** : un gag de répétition se monte vite en champ-contrechamp ; le gag visuel garde un plan large qui le contient.

## Ce que Diego en a dit
Rien sur ce film (aucune note dans `NOTES-DIEGO.md`). Le rapprochement avec la parodie vient de GOUTS.md (réponse 10).

## À faire
- (Option, passe de révision) Comparer la mesure coupes / parole avec *Le Dîner de cons* sur spectrogramme (`labo/outils/spectro_coupes.py`) : les deux chiffres sur énergie ne sont pas comparables.
