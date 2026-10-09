# Labo kinetic editing — résultats (2026-10-09)

Script : `python3 labo/kinetic/kinetic_demo.py` (≈ 10 s). Sorties lourdes dans `labo/rendus/kinetic/` (ignoré par git) ; légères ici : `planche_contact.png` (149 Ko), `forme_onde_coupes.png` (14 Ko : bleu = coupe, rouge = coupe d'impact), `mesures.json`.

## Montage produit [TESTÉ EN LABO]
- 540x960, 30 i/s, 180 images = 6,0 s, 14 plans de 6 à 15 images : `15 15 15 13 12 10 8 6 15 15 14 12 15 15`. Accélération (15 → 6 images) jusqu'au premier impact, puis on relâche (15 images) : la respiration après l'impact est voulue.
- Punch-in (plan 5) : `zoompan` 2 images larges puis ×1 → ×1,35 en 3 images, ease-out cubique.
- Impact (plans 9 et 13) : flash blanc d'**une** image (`drawbox ... enable='eq(n,0)'`) + camera shake amorti (`scale` +60 px puis `crop` à x/y = sin·exp(-n/3), amplitude 26 px, mort en ~5 images).
- Texte mot à mot (6 mots, Inter Display Bold, contour 8 px, « pop » 150 → 120 px sur la 1re image de chaque mot), chaque mot posé sur une coupe ou à mi-plan, avec un click doux.

## Son [TESTÉ EN LABO]
- SFX synthétisés en numpy (48 kHz) : whoosh = bruit dans un filtre passe-bande à variables d'état dont la fréquence balaie 250 Hz → 3-4 kHz, enveloppe en x² qui **culmine sur la coupe**, début 3 à 6 images avant (varié d'une coupe à l'autre), queue de 3 images ; impact = sinus avec chute de hauteur 98 → 38 Hz + transitoire de bruit, attaque 0,5 ms posée **sur** l'image de coupe ; click = 12 ms à 3,2 kHz ; riser = bruit à balayage 200 Hz → 6 kHz + sinus 110 → 880 Hz sur 30 images.
- Hiérarchie : impact 0 dB > riser -12 > whoosh -10 à -14 (variés) > click de coupe -20 > click de mot -22 > ambiance (bruit brun) -34. Toutes les coupes n'ont PAS de son : les 2 coupes juste avant les impacts sont sèches.
- Calage mesuré dans le MP4 final (AAC) : attaque des impacts à **+1,9 ms et +2,0 ms** de la coupe (une image = 33,3 ms). Le calage à l'image survit à l'encodage AAC.

## Ce qui a raté, et pourquoi
1. **Riser v1 trop fort** (-6 dB, crête sur la coupe) : sur la forme d'onde, il était aussi gros que l'impact et le masquait ; le pic normalisé ne dit rien du volume perçu (le riser dure 1 s, l'impact 0,1 s). Corrigé en v2 : -12 dB et coupé **1 image avant** l'impact (micro-silence = « suck-out », l'impact paraît plus gros). [TESTÉ EN LABO]
2. **Mesure d'attaque v1 fausse** (-100 ms) : le riser dépassait déjà le seuil. Corrigé par un passe-bas ~200 Hz avant la détection.
3. **Loudness d'une piste faite de transitoires** : gain statique seul = -24,6 → -14 demande +10,6 dB, mais le limiteur mange le niveau ; il a fallu **5 passes** gain + limiteur (+15,5 dB au total, ≈ 5 dB de limitation sur les impacts). Pour un vrai montage, c'est la musique et la voix qui portent l'intégré ; les SFX ne doivent pas servir à « faire le niveau ». [TESTÉ EN LABO]
4. **True peak qui remonte à l'AAC** : WAV à -1,4 dBTP → MP4 AAC 192k à **+0,5 dBTP** (+1,9 dB). Corrigé en plafonnant le limiteur à -3 dBFS (`limit=0.7079`) : WAV -2,9 dBTP → MP4 **-1,1 dBTP, -14,3 LUFS, LRA 3,4**. Conforme (-14 ±0,5 / ≤ -1). Leçon : sur un mix très transitoire, viser -2,5 à -3 dBTP avant encodage AAC et **mesurer le fichier encodé**. [TESTÉ EN LABO]
5. **Détection de coupes ffmpeg** (`select='gt(scene,0.25)'`) : 12/13 coupes trouvées + 3 faux positifs. Le flash d'une image compte double (94, 95, 96 et 150, 151) ; la coupe 109 (automate cellulaire gris → mire) a un score de 0,05 seulement et passe sous le seuil. Le flash et le shake trompent un détecteur ; le contrôle doit partir de la liste de coupes du montage (EDL), pas d'une détection.

## Limites [THÉORIQUE]
- Sources synthétiques : aucune vraie image en mouvement, donc pas de motion blur, pas de speed ramp, pas de coupe sur le mouvement testée. Le punch-in sans flou de bougé paraît plus « numérique » qu'un vrai.
- Pas de musique : la sync sur le beat n'est pas testée ici (voir `labo/rythme/`).
- Jugement esthétique fait sur planche contact et forme d'onde, pas en écoute au casque ni sur téléphone.

## Commandes clés
```bash
# flash 1 image + shake amorti
-vf "scale=600:1066,crop=540:960:x='30+26*sin(n*2.9)*exp(-n/3)':y='53+26*cos(n*3.7)*exp(-n/3)',drawbox=c=white:t=fill:enable='eq(n,0)'"
# punch-in 3 images ease-out
-vf "zoompan=z='if(lt(on,2),1,1+0.35*(1-pow(1-min((on-1)/3,1),3)))':d=1:s=540x960:fps=30:x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'"
# mesure / normalisation
ffmpeg -nostats -i IN -af ebur128=peak=true:framelog=quiet -f null -
ffmpeg -i sfx.wav -af "volume=15.50dB,aresample=192000,alimiter=limit=0.7079:attack=1:release=50:level=false,aresample=48000" out.wav
```
Placement : image de coupe `c` → échantillon `c × 1600` (48 000 / 30). Whoosh : début = `c - k×1600` avec k = 3 à 6.
