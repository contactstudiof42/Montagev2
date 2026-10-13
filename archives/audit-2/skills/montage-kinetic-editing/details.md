Annexe de `SKILL.md` : sources, mesures de labo, leçons d'atelier, code complet des recettes et détails de photosensibilité ; les règles elles-mêmes ne sont pas répétées ici (le SKILL.md fait foi).

# montage-kinetic-editing — détail

## 1. Quand et pourquoi : sources et précisions
- Guide interne de MrBeast (fuite d'août 2024) : la 1re minute est la zone critique. Ali Abdaal : « un son à chaque fois que quelque chose apparaît à l'écran » (un son par événement visuel est la norme du genre).
- Le son rend aussi lisible un plan de 6 images.
- Respiration : un montage à 6 images constantes devient un mur ; au labo, 15 → 6 images jusqu'à l'impact, puis 15.
- Quand ce style dessert : aussi un humour qui repose sur un temps de réaction ; sinon le dire à l'utilisateur.
- Repères de durée sourcés : jump cuts toutes les 1-3 s (style Hormozi), interruptions visuelles toutes les 2-4 s (guides CapCut / retention editing, 2025-2026), chiffres d'éditeurs.

## 2. Grammaire : précisions
- **Punch-in** : la décision d'échelle (où, pourquoi) relève de `montage-youtube` § 5 ; ici seulement la mécanique (durée, courbe, flou). Un changement d'échelle ne sert pas à masquer une saute.
- **Smash cut** : aussi dans l'autre sens (fort → calme).
- **Whip** : flou de bougé = Shutter Angle. **Speed ramp** dans Premiere : Time Remapping > Speed, keyframes séparés en Bézier [THÉORIQUE].
- **Flash** : au-delà de 2 images, c'est un fondu. Le shake n'est jamais continu.
- **Masque** : ou un mouvement de caméra rapide qui sert de rideau.
- **Captions** : contour épais ; mot-clé en jaune chez Hormozi. Mesures (`labo/paroles/RESULTATS.md`, proxy OCR sur fonds synthétiques) : ré-encode à 2,5 Mb/s ; rien de lisible à 1,2 % ; sur fond clair et chargé, blanc nu et ombre portée échouent à toutes les tailles ; sinon changer de plan.
- **B-roll** : pas une seconde après le mot.
- **SFX** : impact mesuré à +2 ms de la 1re image au labo ; riser coupé 1 image avant = suck-out ; whoosh aussi pour un texte qui entre ou un glissé ; rang 5 = aussi rewind, record scratch, cash. Sources : crête du riser sur le moment clé (Epidemic Sound) ; son démarré avant la coupe, sinon il paraît en retard (Morphic). La fourchette « 3 à 6 images » n'apparaît dans aucune source écrite.
- **Hiérarchie** : un seul rang 1 sinon plus rien n'est gros ; whoosh variés aussi en hauteur et en filtre ; une coupe sèche juste avant un impact le rend plus fort ; à défaut de calage, varier la musique (drop, coupure, filtre passe-bas) comme un SFX.
- **Pro / amateur**, lignes en plus : captions qui recouvrent l'interface, 8 mots → 1-4 mots en zone sûre ; hook « Salut, aujourd'hui… » → hook visuel + sonore à l'image 1 (résultat, question, contraste) ; whoosh sur un mouvement qu'on ne voit pas → bruit (atelier 02 v1).

## 3. Leçons d'atelier et de culture
- **Pièce 02 « Étincelle »** (6 versions) : la cause = le pendule, le temps qui frotte l'allumette. La couleur réservée à la fin se mesure : ≤ 0,14 % de pixels chauds avant l'allumage, 3,7 % après (v6). Calculer les fenêtres de source depuis la cinématique dans le script : deux régressions (v2, v5) venaient de fenêtres recopiées à la main.
- **Pièce 09 « Générique de l'équipe »** (session 7) [ÉPROUVÉ EN MAQUETTE] : cartons de 3 images sur fonds de teintes différentes à luminance relative égale (~0,03, valeur HSV cherchée pour la luminance cible) : le fond ne flashe plus, mais les grands mots clairs flashent localement (6 flashs, pire seconde 3, à la limite) ; marge : cartons de 4 images ou texte moins lumineux aux passages rapides. Fonds noir / blanc alternés : 16 flashs, pire seconde 5, inlivrable. Texte à 0,72 de luminosité : toujours pire seconde 3. **Rupture de forme** : varier échelle (10 → 60 % de la hauteur), position et débord à chaque coupe ; la police ne compte qu'en grand ; le sommet change de règle, pas seulement de taille (v4 : fond commun, deux lignes géantes, même police pour les 4 acteurs, après 28 cartons où tout change).
- ***Scott Pilgrim*** (session 8, `culture/scott-pilgrim-generique-et-montage.md`) : sans règle par séquence, le kinetic devient un tic ; une transition passe par le son quand c'est possible (le bruit de A devient l'impulsion de B) ; salir = grain, accidents, sans retoucher le calage.
- **Pièce 14 « Balancier »** (session 9, `atelier/14-balancier/CRITIQUE.md`) : version kinetic = 19 plans d'une seconde et des whooshs pendant que la lampe s'arrête, le montage fabrique l'énergie que le sujet perd. Test : « le sens est-il dans la variation de vitesse du sujet ? ». Version B2 : coupes aux points morts de plus en plus espacées (1 s, 2, 4) et whooshs proportionnels à l'amplitude = la bonne version réseau ; la pulsation constante (B) est la seule fausse. Autre cas : une foule qui s'emballe.
- **Kolder et monteurs d'edits** (sessions 11 et 14, `culture/sam-kolder-travel-edit.md` de mémoire, corrigée par `culture/kinetic-edit-monteurs-reseaux-sources.md`, sources moyennes) : point commun **tourné** (Schiffer tourne dans l'ordre et note comment finit chaque plan) ou **trouvé** au banc par essais et erreurs (Brandon Li) ; la règle de mémoire « une transition kinetic se tourne » était trop absolue. Ordre de jugement : entretien Musicbed ; respirations du style = time-lapses entre les lieux. Les transitions façon Kolder sont devenues des packs (2018) : appliquées à tout, elles rendent les lieux interchangeables ; un SFX de transition correspond à un mouvement réel de l'image. **Velocity edit** : marqueurs sur les temps forts d'abord, vitesse ensuite, easing systématique ; la rampe ponctue le rythme, ne le contredit jamais. Whoosh : la répétition s'entend d'abord dans les durées identiques. L'edit de fan est une **relecture** : rapprocher deux moments séparés pour créer un sens.
- **Whip en 3D** [TESTÉ EN LABO, Blender, `labo/kinetic/whip/`] : sans animation au-delà des bords, indice de flou 0,85 contre 1,07 aux images de coupe. AE : même logique, à vérifier en phase 3.
- **Direction du filé** (session 13, `labo/kinetic/whip-flot/RESULTATS.md`) : 30° près = cos ≥ 0,87, 45° = limite ; vitesse et flou continus. Choc à réserver à l'impact voulu, sur le temps fort ; changement d'espace = fin de chapitre, jamais au milieu d'une phrase de mouvement. Rayures, grilles, stores : sens ambigu à une période près (roue de charrette). Vérifier : `python3 labo/kinetic/whip-flot/mesure_flot.py --paire A/ B/ --mvs` (DIS d'OpenCV, puis vecteurs du codec H.264 au-delà de ~15 % de largeur par image ; Farneback pleine résolution aveugle au filé). Validé sur rendus Blender (11 % de largeur/image : juste ; 40 % : s'abstient, 0 erreur) ; au-delà d'un quart de cadre par image, le sens se lit dans l'accélération de A et le ralentissement de B : y soigner la direction. L'accroche de netteté se vérifie avec l'indice de flou de `labo/kinetic/whip/mesure.py`.

## 4. Recettes : code complet
**R2** : riser de 1 s à -12 dB sous l'impact.

**R3 — Punch-in** [TESTÉ EN LABO] : whoosh court à crête sur le début du zoom.
`zoompan=z='if(lt(on,2),1,1+0.35*(1-pow(1-min((on-1)/3,1),3)))':d=1:s=540x960:fps=30:x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'`

**R4 — Shake + flash** [TESTÉ EN LABO] : `scale=W+60:H+106,crop=W:H:x='30+26*sin(n*2.9)*exp(-n/3)':y='53+26*cos(n*3.7)*exp(-n/3)',drawbox=c=white:t=fill:enable='eq(n,0)'`

**R5** : whoosh, début = coupe − k × 1600 (k = 3 à 6), crête à la coupe ; impact, attaque à la coupe, montée de 0,5 ms pour éviter le clic.

**R6** : itérer, le limiteur mange le niveau (5 passes au labo) ; `alimiter=limit=0.7079` à 192 kHz ; mesurer le MP4.

**R7** [THÉORIQUE pour Premiere / CapCut ; TESTÉ EN LABO avec drawtext] : 1 mot ou groupe par segment ; click à -20 dB sous l'impact.

**R7b — Tenir le vers** (session 15, `labo/paroles/temps_lecture-resultats.md`, `sources/sous-titres-vitesse-lecture-2026-10.md`) :
- [SOURCÉ] Netflix 17 car./s adultes (13 enfants, 20 en SME), plancher 5/6 s, plafond 7 s ; ATAA 14-15 car./s (16-17 = trop rapide), plancher 16 images, plafond 5 s ; charte CSA 2011 : 20 car. = 2 s, 36 = 3 s, 60 = 4 s. Espaces et ponctuation comptent.
- Mot à mot à ~0,3 s par mot, la voix couvre déjà l'essentiel de la lecture ; 1/2 s à 1 s = 12 à 25 images ; mots longs, vers court ou public enfant : 1 s et plus.
- La tenue laisse finir la lecture et donne au vers son poids. Un clip peut choisir d'être moins lisible (texte-texture, écho d'une voix déjà comprise, flash volontaire), mais il doit le **décider** ; un vers coupé par accident se lit comme une erreur.

**R8 — Speed ramp en transition** [THÉORIQUE] : rampes de 6-8 images ; crête du whoosh au sommet de la vitesse.

## 5. Photosensibilité : détails de labo
- 4 impacts flashés par seconde échouent ; un mot ou un logo de 6 % de l'écran qui clignote vite échoue. Principe Noé / Kan : `culture/enter-the-void-generique-noe-tom-kan.md`. Pub UK : test Harding obligatoire.
- **Inserts lumineux sur le tempo** (session 12, `labo/photosensibilite/bpm138/`) : une coupe = un allumage *ou* une extinction (2,3 flashs/s, conforme) ; allumer puis éteindre dans la même croche, ou alterner aux doubles croches = échec ; la taille ne sauve qu'en dessous de ~1 % de l'écran ; accents plus serrés : par la forme ou la teinte à luminance égale.
- **128 BPM** (atelier 20, session 15) : la fenêtre glissante de 25 images attrape 3 débuts de coups (pas « 2,13 avec de la marge ») ; marge = noires pointées, ou alterner coup de luminance et coup de teinte. Texte dans un coup blanc : noir, puis inversé (`atelier/20-la-lumiere-ecrit/CRITIQUE.md`).
- **Sommet plus long** (pièce 20 v6) : une montée, une descente ; la durée de l'état clair est un levier libre, le nombre de transitions non.
- **Rushes avec stroboscope** (session 15, rush synthétique, `labo/photosensibilite/strobe-rushes/RESULTATS.md`) : un strobe de 8 Hz donne 4 à 9 flashs/s dans le fichier selon l'obturateur. `tmix` n'efface que par coïncidence de période et fait un voile laiteux ; `deflicker` échoue sur un strobe calé ; quand ils passent, le strobe a disparu. Saccade : choisir à la main les images allumées pour que les coups tombent sur les temps (≤ 2,3 /s) ; prix : mouvement haché (esthétique à décider, cf. examen n°8).

## 6. Outils et phase 3 : précisions
- Premiere : Essential Graphics, captions sur transcription, Remix ; AE : animateurs de texte ; CapCut : styles « Hormozi », shake et zoom intégrés ; Resolve : Speed Ramp, Fairlight, Text+ ; captions automatiques : Submagic, Kapwing, Opus Clip (pages éditeurs) ; Sonniss GDC sans attribution, Mixkit License, packs Gumroad : lire la licence avant usage commercial.
- Phase 3, en plus du SKILL.md : décalage AAC à garder sous 1 image (+2 ms au labo) ; export SRT de Premiere ; Timewarp, Pixel Motion d'AE ; shake par `wiggle` × décroissance contre preset CapCut ; true peak après export AAC depuis Premiere avec limiteur à -1, -2 et -3 dBTP. Labo : `labo/kinetic/` (script, RESULTATS.md, planche, forme d'onde).
