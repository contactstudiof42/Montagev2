# « Créer YggTorrent, puis le détruire » (enquête YouTube)

_Fiche ouverte le 2026-10-11 (phase 2, session 5, YouTube n°8). Source : 480p, 25 i/s, 1 h 11 min 20. Chaîne et présentateur : non cherchés. Les témoins sont anonymes ; je reprends seulement les pseudonymes affichés à l'écran quand c'est utile._

**Lu avant l'analyse** : `montage-youtube` (doc explicatif, 7, 8, 16 bis), `montage-motion-design-principes` (typographie animée), `montage-son-et-emotion`, fiche CIA (doc-enquête). Aucun goût de Diego sur cette vidéo.

## Intention
Raconter de l'intérieur l'histoire d'un site de partage, de sa création à sa fin, par les voix de ses fondateurs et de ses membres, qui ne peuvent pas montrer leur visage.

## Forme [mesuré]
- **1 h 11 min, au moins 651 plans, ASL 6,6 s, médiane 4,8 s** : la vidéo la plus lente des dix ; **48 plans de 15 s ou plus** ; densité de 2 à 17 coupes/min, très basse pendant les témoignages (10:00-14:00 : 2 à 5 coupes/min).
- **-22,0 LUFS, LRA 5,2 LU**, 48 silences de plus de 0,4 s (8 de plus de 1 s).
- **Trois matériaux** [VU SUR IMAGES] : le présentateur face caméra dans une chambre rose et rouge (néon, micro) ; les captures du site et du forum ; et **les témoins anonymes**.

## Séquences fines [VU SUR IMAGES]
Planches dans `videos/_travail/ygg/seq/` : 0:00-1:10, 7:30-9:10, 10:00-12:40, 1:06:30-fin, et une tuile des 3 dernières minutes (51 plans).
1. **Ouvrir par la fin** (0:00-0:58) : le message d'adieu du site (« Merci pour ces neuf années. L'histoire s'arrête ici. »), le logo, puis la fuite (« OUST! ») ; le présentateur ne parle qu'après. Même geste que le cold open de « CIA ».
2. **Un témoin anonyme = un mannequin articulé d'une couleur, une police, un sous-titre qui s'écrit mot à mot** : bleu et sérif pour l'un, orange et machine à écrire pour l'autre, vert, violet… Le mannequin, éclairé dans le noir, change de pose d'un plan à l'autre ; le mot en cours est coloré. Plans de **24 à 45 s** (10:00-12:40 : 9 plans, moyenne 18 s). **La typographie remplace le visage** : on reconnaît la voix à sa police avant de lire le pseudonyme.
3. **Le présentateur est la respiration** entre deux témoignages (1 à 11 s), à l'inverse d'un doc classique où c'est le témoin qui coupe le récit.
4. **La fin sans image** (1:08:12-1:11:20) : trois minutes de voix sur fond noir, les phrases s'écrivent dans la police de chaque témoin, puis une seule image (deux silhouettes sous un ciel étoilé). Le détecteur y voit deux « plans » de 60 et 123 s ; **la tuile en montre au moins 20 cartons** (un par phrase, quatre témoins). La dernière phrase : « En fait, la bonne fin, elle est déjà morte. »

## Confirme, contredit, complète
- **Confirme** `montage-youtube` 16 bis et la fiche CIA : le plan long d'un doc YouTube **change à l'intérieur** (ici, le texte qui s'écrit) ; ouvrir par la fin.
- **Complète** `montage-motion-design-principes` : **une police par voix** comme identité d'un témoin anonyme ; le sous-titre mot à mot n'est pas ici un effet de rétention (Hormozi) mais **un portrait**.
- **Complète** `montage-preparation-tournage-vfx` / interviews : quand on ne peut pas filmer un visage, **un objet-avatar** (mannequin) et une lumière par personne suffisent à tenir 25 à 45 s.
- **Nuance** la règle « plus de 4 min sans relance » (principe 18) : 10:00-14:00 tient à 2-5 coupes/min par la seule force des témoignages. [mesuré, effet sur la rétention non mesurable]

## Principes transférables
1. **Une voix sans visage = un avatar, une couleur, une police.** Utile pour un témoignage client anonyme, une voix d'archive, un interlocuteur au téléphone.
2. **Le texte qui s'écrit tient un plan long** (Tiger, CIA, Ygg : trois vidéos sur trois).
3. **Finir sur les voix seules** : retirer l'image à la fin pour que le spectateur écoute.

## Leçon de méthode (inscrite dans `PROMPT-PHASE-2.md`)
Sur des cartons de texte sur fond noir, PySceneDetect ne voit pas les changements (un « plan » de 123 s en contient au moins 20). Tuile à 1 image / 8 s sur tout plan long de texte avant d'en citer la durée.

## Ce que Diego en a dit
Rien sur cette vidéo.

## Pas fait, doutes
- Transcription Whisper en cours à la clôture (non lue). Sponsor (1:15-2:15, hébergeur web, présentateur et captures d'interface) non analysé en détail.
- La durée d'un témoignage (un mannequin = un plan ?) n'est pas recomptée.
