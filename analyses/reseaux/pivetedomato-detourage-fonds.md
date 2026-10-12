# pivetedomato (« Made by Pölen on DaVinci Resolve ») — détourage et fonds qui changent, 7,5 s, 16:9

_Référence du projet mariage-jo, déposée par Diego le 2026-10-12 (`videos/reseaux/video-by-pivetedomato-4-u-4-ryr.mov`) : « Pas un mariage : c'est l'effet qui m'intéresse. Détourage et fonds qui changent très vite, proche du kinetic. Pour un passage de 5 à 10 secondes dans le mariage. » Fiche technique : 1276x718, 30 i/s, 224 images, H.264, AAC ; -14,1 LUFS. Toutes les images regardées (`page-01.jpg`, `page-02.jpg`), changements de fond relevés à l'œil, contre attaques et temps. Son : rien écouté._

## Intention
Montrer ce qu'on peut tirer d'un seul plan d'un corps en mouvement : la personne garde son geste continu pendant que le monde autour d'elle change à chaque double croche.

## Forme [VU SUR IMAGES]
| Temps | Ce qui se passe |
|---|---|
| 0-1,0 s | le plan brut : une personne en capuche court de profil dans une rue (caméra qui suit) |
| 1,0-1,6 s | l'image rétrécit dans le cadre noir (la course continue) |
| 1,6-2,1 s | le mot rouge « WE GON' » s'écrit **derrière** la personne (elle passe devant le texte) |
| 2,1-6,7 s | **détourage, fond qui change tous les 3 à 4 images** (0,10-0,13 s) : dégradés radiaux vert sapin, rouge-violet, bleu-rouge, rose ; le sujet change aussi d'état (contour lumineux, traits de lumière dessinés sur le corps, trame de points façon écran LED, aplat noir, solarisé) ; 31 changements en 4,6 s |
| 6,7-7,2 s | carton bleu « Made by Pölen on DaVinci Resolve » |
| 7,2-7,5 s | retour au plan brut |

## Choix par domaine
- **Rythme** [mesuré] : changements réguliers de 4 images = **une double croche à 115 BPM** (0,13 s) ; pas calés sur les attaques à ±1 image (24 %, hasard 29 %), mais 76 % à ±2 images. C'est une grille régulière plus qu'un calage sur chaque coup.
- **Ce qui rend l'effet propre** : un seul geste continu (course de profil, silhouette lisible, vêtements contrastés) ; un détourage net (bords simples : capuche, pantalon large) ; des fonds qui sont des **aplats et dégradés pleins**, jamais une autre image ; une palette limitée (vert, rouge, bleu, rose) qui revient.
- **Le sujet change plus que le fond** : sur la moitié des états, le traitement du corps (trame, contour, lumière) compte plus que la couleur du fond.

## Pour le mariage (application, [projet : mariage-jo])
- Choisir **un geste humain continu et lisible**, de profil ou de face, sur fond simple, d'au moins 3 s (une danse, une course, un lancer, une entrée), filmé à 50 i/s, net et pas trop tremblé.
- Fonds tirés de **la palette du film** (`da.md`), pas les couleurs saturées de la référence ; le N&B du film peut être un des états.
- Contrôles : détourage au bord à 200 % (`montage-regard`, « Le goût de chaque plan » 13), photosensibilité (changements de luminance rapides), durée 5 à 10 s.

## Principes transférables
1. Un geste continu + un monde qui change = vitesse sans perte de lecture.
2. Une grille rythmique régulière (double croche) suffit ; les grands changements tombent sur les temps forts.
3. Changer l'état du sujet autant que le fond.
4. Annoncer l'effet (l'image qui rétrécit, le texte derrière le sujet) puis revenir au réel.

## Doutes
- Outils exacts (Magic Mask, Fusion, effets de trame) non visibles ; la légende dit seulement « DaVinci Resolve ».
- Musique non écoutée ; la voix est un rap en boucle.
