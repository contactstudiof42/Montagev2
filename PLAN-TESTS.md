# PLAN DE TESTS — exercices techniques courts dans After Effects et Blender

_Créé le 2026-10-13 (audit 2, section 8 d'`AUDIT-2.md`, exercices approuvés par Diego). Remplace `PLAN-TESTS-MCP.md`, archivé dans `archives/phase-3/` (environ 75 tests écrits pour un serveur MCP absent de ce Mac). Résultats de la session 0 de Resolve : `labo/mcp/resolve-mcp.md`. Une session d'exercice suit le démarrage de `CLAUDE.md`, puis ce fichier ; les règles de sécurité de `PROMPT-PHASE-3.md` s'appliquent. Mis à jour le même jour après la réponse de Diego : After Effects passe par le MCP de Higgsfield, déjà installé ; références choisies : A pour E1, A pour E3._

## 1. Où en sont les skills (2026-10-13)
| Skill | Éprouvé | Seulement théorique | Ce qui le tranchera |
|---|---|---|---|
| `montage-after-effects` | expressions 01-11 : syntaxe et maths sous Node, avec un faux After Effects (2026-10-09) | tout le reste : rien n'a jamais tourné dans After Effects (courbe réelle d'`ease()`, F9, overshoot, `posterizeTime`, `seedRandom`, durées types, pilotage) | E0, E1, E2 |
| `montage-blender` | méthode et réglages en VM Linux, Blender 4.2.3, CPU (34 pièces d'atelier) | le Mac : Blender 5.2.2 LTS, GPU, API de 4.2 à 5.x, Eevee | E0, E3, E4 |
| `montage-motion-design-principes` | le titre de marque, jugé par Diego ; l'habillage vu sur 45 vidéos | les principes d'animation (paramètre qui porte le sens, asymétrie, matière, lisibilité) : maquettes | E1, E2 |
| `montage-pilotage-mcp` | Resolve par son MCP, sur deux projets | After Effects (MCP de Higgsfield, ExtendScript par `osascript`, `aerender`) et Blender (ligne de commande, MCP) : jamais | E0 |

Sur le Mac (relevé le 2026-10-13) : After Effects 26.3.0 avec `aerender`, Blender 5.2.2 LTS, Premiere 26.3.0, Resolve Studio 21.1.1. Serveurs MCP : Resolve actif ; Blender installé des deux côtés mais désactivé dans Claude ; After Effects : le plugin Higgsfield est installé, mais son connecteur n'apparaît pas encore dans mes sessions (section 6).

## 2. La liste des moyens
_Préparée après l'application de l'audit 2, dans la même session : voir la section 6._

## 3. Où travailler
Fichiers de travail (projets `.aep` et `.blend`, rendus, mesures lourdes) dans `videos/phase-3/tests-techniques/_travail/` et `rendus/` (hors Git) ; brief des exercices dans `videos/phase-3/tests-techniques/brief.md` (le directeur artistique le lit) ; textes, journal, mesures et planches légères dans `projets-phase-3/tests-techniques/`. Rien d'acheté, aucun compte créé par moi. Les exercices n'utilisent que de la matière créée pour l'occasion ; les références restent sur le Mac et n'entrent jamais dans un projet After Effects ouvert pendant que le plugin Higgsfield est connecté (règles de Diego, 6.3).

## 4. La méthode commune à chaque exercice
1. **Intention et critères écrits avant le premier geste** (`montage-pilotage-mcp`).
2. **Construit** dans After Effects par le MCP de Higgsfield (construire, modifier, voir le projet), ou par script ExtendScript quand c'est plus fiable ou plus mesurable (choix de Diego, 2026-10-13) ; dans Blender par script (bpy), le MCP servant à voir la scène ouverte et à vérifier chaque geste. **Rendu en local** en images PNG (`aerender`, Blender en ligne de commande) et **mesuré hors du logiciel**.
3. **Un témoin raté**, rendu exprès, que la mesure doit attraper : sinon le contrôle ne prouve rien (« concevoir le contrôle pour qu'il puisse échouer »).
4. Pour ce qui touche au goût : **planche côte à côte avec la référence**, puis **directeur artistique à froid** (bande d'images du rendu à côté de celle de la référence), puis **une seule question à l'œil de Diego**.
5. Après l'exercice : les marqueurs des skills montent ([TESTÉ EN CONDITIONS RÉELLES], avec la date) ou la règle est corrigée ; un échec gagne une règle, et n'empêche pas les autres exercices.

L'outil de mesure du mouvement (`labo/outils/courbe_mouvement.py`, à écrire en E0) suit le centre d'un élément image par image (moyenne pondérée par l'alpha, sur fond uni) et trace position, vitesse et accélération en PNG : ma façon de « voir » une courbe d'animation, et de la comparer à celle de la référence mesurée de la même manière.

## 5. Les exercices
Références choisies par Diego le 2026-10-13 : A pour E1 et A pour E3 (6.6). Les critères de E1 sont recalibrés sur une mesure provisoire de la référence (ci-dessous), que je confirme par la mesure fine (`courbe_mouvement.py`) avant le premier geste ; ceux de E3 restent les miens, la référence servant au jugement côte à côte.

**E0 — Préalable : piloter les deux logiciels.**
Blender : rendre une image de test en ligne de commande sur le GPU du Mac ; relever le moteur, le temps par image, les identifiants d'API qui ont changé depuis la 4.2. After Effects : un script de dix lignes lancé par `osascript` crée une composition et l'enregistre ; `aerender` la rend en PNG ; `ffprobe` la lit. Si un serveur MCP est installé : `get` de l'état de la scène, une capture, une modification lue en retour. Résultat : une table « réussi / contourné / à la main » dans ce fichier, comme la session 0 de Resolve. Écrire `labo/outils/courbe_mouvement.py` et le vérifier sur un rendu synthétique dont la courbe est connue.
After Effects par le MCP de Higgsfield, **avant tout exercice** (demande de Diego) : vérifier, puis écrire en 6.7, ce que ses outils font réellement sur ce Mac (créer une composition, des calques, des images clés, des expressions, rendre), quelles actions consomment des crédits Higgsfield et lesquelles n'en consomment pas, et ce qui transite par ses serveurs. Méthode : la liste des outils et leurs descriptions d'abord ; aucun outil de génération ; chaque type d'appel essayé seul sur une composition de test sans aucune matière de client, le solde de crédits relevé avant et après s'il est visible, les connexions réseau du plugin observées pendant l'appel ; chaque résultat comparé à ce qu'`aerender` rend en local.

**E1 — After Effects : un titre qui se pose (3 s, 1920×1080, 25 i/s).**
Référence : Swile POW, « Une seule carte, » (6.6, A). Mesure provisoire du 2026-10-13 (bord haut du texte, image 4K ramenée à l'échelle 1080p) : le texte apparaît d'un coup, opaque ; il monte d'environ 44 px en dix images (pas successifs : 13,5 ; 15 ; 4,5 ; 3 ; 2 ; 2 ; 2,5 ; 0,5 ; 0,5 ; 0,5 px) ; aucun flou de mouvement ; ensuite la mise en page grandit lentement.
L'exercice : deux mots neutres créés pour l'occasion (pas le texte du film), en Inter blanc sur noir, reproduisent ce geste par images clés (arrivée très freinée : influence d'arrivée forte, de sortie faible), puis tenue.
Témoins : clés linéaires ; Easy Ease symétrique (F9) ; ma version d'avant le choix (montée de 20 px avec fondu, flou qui se résorbe et flou de mouvement).
Critères mesurés sur le rendu (provisoires, confirmés par la mesure fine de la référence) : (a) au moins 60 % de la course dans les deux premières images, puis une vitesse qui décroît sans jamais devenir négative (pas de rebond) ; (b) moins de 0,5 px par image à partir de la huitième image, puis position stable à ±0,25 px pendant la tenue ; (c) aucun flou de mouvement : sur l'image la plus rapide, des bords aussi nets qu'au repos (à 10 % près), comme la référence ; (d) course totale à ±10 % de celle de la référence ; (e) tenue d'au moins 1,5 s ; (f) les trois témoins sont distingués par la mesure.
Goût : planche des bandes d'images à côté de celles de la référence, faite hors d'After Effects ; directeur artistique à froid (« au niveau » ou « presque » attendu). La question de Diego : le titre se pose-t-il avec poids, ou flotte-t-il ?

**E2 — After Effects : overshoot et boucle par expressions (2 × 3 s).**
(a) Un carré passe de 0 à 100 % d'échelle en 12 images, clés linéaires, puis l'overshoot inertiel (recette 05). Critères : pic de 107 % ±1 point, deux images (±1) après la dernière clé, comme sous Node ; posé à 100 % ±0,5 avant une seconde. Témoin : dernière clé en Easy Ease → aucun dépassement (le piège « vitesse d'arrivée nulle »).
(b) Une boucle de 2 s (`loopOut("cycle")`) et un `wiggle` figé par `seedRandom`. Critères : images 0 et 50 identiques (écart moyen < 0,5/255) ; deux rendus successifs identiques ; vitesse continue à la jointure ; `posterizeTime(8)` à 25 i/s donne des tenues de 3 et 4 images.
Pas de jugement de goût : cet exercice confirme ou corrige mes recettes (les onze vérifications de l'ancienne liste « À vérifier dans After Effects »).

**E3 — Blender : un packshot dans le noir (5 s, 1920×1080, 25 i/s).**
Une sphère chromée et un petit objet mat sur un sol noir brillant ; deux softbox émissives invisibles à la caméra ; travelling avant lent, accéléré puis freiné ; vue AgX. Une image de test avant le rendu complet.
Témoins : sans les softbox (chrome noir) ; caméra linéaire.
Critères mesurés sur le rendu : (a) au moins deux reflets de softbox lisibles sur la sphère, et la sphère nettement plus lumineuse que dans le témoin, qui doit échouer ; (b) au plus 0,5 % des pixels à 250 ou plus (des reflets ponctuels seulement), et le blanc maximal relevé, pour confirmer ou corriger « AgX plafonne vers 222 » ; (c) noirs du fond au 5e centile ≤ 10/255, sans bruit visible une fois amplifiés six fois ; (d) diamètre apparent de la sphère monotone, vitesse maximale vers le milieu du mouvement, aucune image dont la vitesse saute de plus de 20 % par rapport à ses voisines ; (e) même image 0 sur deux rendus ; temps par image relevé.
Goût : planche côte à côte avec la référence (Swile POW, packshot en 3D, 6.6, A : noirs, douceur des reflets, bruit, vitesse du mouvement), directeur artistique à froid. Blender ne passe pas par Higgsfield ; la référence reste sur le Mac. La question de Diego : ça fait CG, ou cheap ?

**E4 — Blender : une chute calée à l'image (3 s).**
Un objet tombe sur une table et rebondit deux fois, par clés calculées ; l'impact tombe exactement à l'image 40 ; flou de mouvement ; un son d'impact posé à l'image 40.
Témoin : un objet qui traverse le cadre en une image (il doit disparaître dans le flou, ce qui confirme « ralentir l'objet ou rapprocher la caméra »).
Critères mesurés : (a) image de contact = 40, sans pénétration de la table (à 1 px près sur toutes les images) ; (b) hauteurs des rebonds dans le rapport prévu, à ±10 % ; (c) flou présent aux images rapides, et objet lisible sur chaque image (aire au moins la moitié de l'aire au repos) ; (d) attaque du son à 1,600 s ±1 ms ; −14 LUFS ±0,5 et crête ≤ −1 dBTP sur le fichier encodé.
La question de Diego (à l'œil et à l'oreille) : la chute a-t-elle du poids, l'impact tombe-t-il juste ?

**E5 — Assemblage et livraison (8 s).**
Le rendu de E3 en fond, le titre de E1 composé dans After Effects, un étalonnage simple, livré en master du studio (H.265 Main 10) et en H.264 pour le web.
Critères : (a) pas de double conversion : un gris à 18 % rendu dans Blender sort à la valeur Rec.709 attendue, à ±2 codes près ; (b) titre lisible : contraste d'au moins 4,5:1 avec le fond sous le texte ; (c) master : hevc, Main 10, `yuv420p10le`, BT.709 ; web : High, `yuv420p`, faststart ; autant d'images que la composition, aucune perdue ni doublée ; (d) PSNR du master contre un PNG 16 bits ≥ 40 dB, noirs amplifiés six fois sans bloc.
Goût : directeur artistique à froid sur la planche finale.

## 6. La liste des moyens et les références à choisir
_Préparée le 2026-10-13, après l'application de l'audit 2. Relevé fait sur le Mac le même jour, en lecture seule (préférences de Blender et d'After Effects, extensions de Claude, polices, bibliothèques Python) : je n'ai rien installé ni réglé. macOS, Blender et Claude sont en anglais : les intitulés sont donnés en anglais (en français entre parenthèses quand ça aide). Mise à jour le même jour après la réponse de Diego : After Effects passe par le MCP de Higgsfield, déjà installé (kumoproductions n'est pas installé) ; références A et A._

### 6.1 Déjà en place (relevé le 2026-10-13)
| Élément | État |
|---|---|
| Blender 5.2.2 LTS | Cycles réglé sur **METAL** (le GPU du Mac). |
| Module « MCP » dans Blender (Blender Lab, v1.0.3) | **Installé et activé** depuis le 5 octobre (dépôt `lab.blender.org` ajouté). Il ouvre un pont sur `localhost:9876` ; **Auto Start** coché : le pont démarre seul une seconde après l'ouverture de Blender. |
| Blender : **Edit → Preferences → System → Network → Allow Online Access** | **Coché.** Le module refuse de démarrer sans lui. |
| Extension « Blender » dans Claude (Blender Lab, serveur v1.0.1) | **Installée le 5 octobre, mais désactivée** : c'est pour ça qu'aucune de mes sessions ne la voit (les extensions activées, comme Resolve Studio, y apparaissent). |
| After Effects 26.3 : **Settings → Scripting & Expressions → Allow Scripts to Write Files and Access Network** (en français : Paramètres → Scripts et expressions → Autoriser les scripts à écrire des fichiers et à accéder au réseau) | **Coché** (`Pref_SCRIPTING_FILE_NETWORK_SECURITY = 1` dans les préférences 26.3). C'est le seul réglage d'After Effects dont j'ai besoin. |
| `aerender` | Présent (`/Applications/Adobe After Effects 2026/aerender`). |
| Plugin Higgsfield dans After Effects (extension `ai.higgsfield.cep` v1.0.57, installée le 8 octobre, pour After Effects et Premiere) et outil en ligne de commande `higgsfield` 1.1.26 | **Installés.** Son pont s'est connecté à `wss://bridge.higgsfield.ai` le 11 octobre (journal du plugin). |
| Connecteur « HIGGSFIELD MCP » dans Claude (`https://bridge.higgsfield.ai/mcp`) | **Pas visible dans mes sessions** : le répertoire de Claude l'indique « non connecté » pour ce compte (relevé le 2026-10-13 dans l'après-midi). |
| Node 25.6.1, `npx`, `uv` 0.12.23 | Présents (le serveur d'After Effects demande Node 24 ou plus). |
| Python du dépôt (`.venv`) | numpy, OpenCV, Pillow, SciPy, scikit-image, imageio : de quoi tout mesurer. |
| Polices | Inter (famille complète), Helvetica Neue, Avenir Next. SF Pro absente, inutile depuis le choix de la référence A. |
| SSD | 358 Go libres (une séquence PNG 16 bits de 5 s en 1080p pèse environ 1 Go). |

### 6.2 Ce que je te demande (dans l'ordre, environ cinq minutes)
| # | Quoi | À quoi ça sert | Coût, origine | Où exactement |
|---|---|---|---|---|
| 1 | Activer l'extension Blender dans Claude | Me donner des yeux dans le Blender ouvert : captures de la vue, résumés de la scène, rendus de la vue | Gratuit ; **officiel** (Blender Lab, la fondation Blender), du répertoire d'extensions de Claude | Claude → **Settings…** (⌘,) → **Extensions** → **Blender** → **Enable** (Paramètres… → Extensions → Activer) |
| 2 | Le connecteur HIGGSFIELD MCP, connecté au compte Claude de mes sessions | Le MCP d'After Effects que tu as choisi : construire, modifier et voir le projet | Ton compte Higgsfield ; outil commercial ; crédits seulement pour la génération IA, jamais sans ton accord | Tu le dis installé ; ma session ne le voit pas (6.1). Je vérifie en tout début de E0 ; s'il manque : Claude → Settings → Connectors → HIGGSFIELD MCP → Connect, avec ton compte Higgsfield (intitulés de claude.ai, que je n'ai pas pu lire dans l'app). After Effects ouvert, le panneau Higgsfield connecté à ton compte |
| 3 | Autoriser Claude à piloter After Effects | Lancer mes scripts ExtendScript par `osascript` (le MCP de Higgsfield n'en a pas besoin : il passe par son plugin, dans After Effects) | Réglage macOS | À la première demande, la fenêtre « “Claude” wants access to control “Adobe After Effects 2026”… » → **Allow**. Le réglage apparaît ensuite dans **System Settings → Privacy & Security → Automation → Claude → Adobe After Effects 2026** (interrupteur allumé). Je déclencherai la fenêtre en tout premier en E0 : reste là les deux premières minutes |
| 4 | Si macOS le demande : l'accès au SSD | Qu'After Effects et Blender enregistrent `.aep`, `.blend` et rendus dans `videos/phase-3/tests-techniques/_travail/` | Réglage macOS | Fenêtre « “Adobe After Effects 2026” would like to access files on a removable volume » → **Allow** (réglage : **System Settings → Privacy & Security → Files & Folders → Adobe After Effects 2026 → Removable Volumes**) ; même chose pour Blender. Si le pare-feu (activé sur ton Mac) demande « Do you want the application “Blender.app” to accept incoming network connections? » → **Allow** : le pont n'écoute que ton Mac (`localhost`) |

Ce que tu fais (ta réponse du 2026-10-13) : la ligne 1, puis Allow aux fenêtres de macOS au début de E0 (lignes 3 et 4).

### 6.3 Les deux serveurs MCP
**Blender : le serveur officiel de Blender Lab** (blender.org/lab/mcp-server ; code : projects.blender.org/lab/blender_mcp ; licence GPL-3.0) [SOURCÉ ; lu dans son code le 2026-10-13].
- Pourquoi lui : fait par la fondation Blender, il suit l'API de Blender 5 (5.1 minimum, tu as 5.2.2) et embarque la documentation de l'API et le manuel, que je peux interroger (je connais surtout l'API de la 4.2) ; c'est aussi lui que Claude distribue, déjà installé chez toi.
- Ce qu'il peut faire sur ton Mac, Blender ouvert : résumer le fichier, les objets, un objet en détail (données, matériaux, modificateurs), les fichiers manquants et les bibliothèques liées ; **capturer une zone (la vue 3D) ou toute la fenêtre**, que je regarde comme une image ; rendre la vue ou une vignette dans un fichier ; aller à un onglet, cadrer un objet dans la vue ; exécuter du Python dans le Blender ouvert ; chercher dans la documentation.
- Limites : il exécute le code sans garde-fou (donc seulement sur les fichiers d'exercice de `_travail/`, jamais sur le `.blend` d'un client). L'extension de Claude est en v1.0.1, le module de Blender en v1.0.3 : compatibilité à vérifier en E0 [NON VÉRIFIÉ]. Si ça coince : mettre l'extension à jour, ou ajouter le serveur par `claude mcp add` après avoir désactivé l'extension, jamais les deux à la fois (Resolve est déjà en double : l'extension « DaVinci Resolve Studio » et le serveur « DaVinci Resolve » de `~/.claude.json`).
- Écarté : « BlenderMCP », communautaire : même port 9876 (conflit avec l'officiel), télémétrie activée par défaut, et rien de plus pour ces exercices.

**After Effects : le MCP de Higgsfield** (choix de Diego, 2026-10-13 ; déjà installé). Adobe ne publie aucun serveur MCP pour After Effects ; kumoproductions, que je recommandais, n'est pas installé.
- Comment il marche [lu dans le code du plugin, 2026-10-13 ; à vérifier en E0] : le connecteur de Claude parle à `https://bridge.higgsfield.ai/mcp` ; les serveurs de Higgsfield relaient chaque commande au plugin, dans After Effects, par `wss://bridge.higgsfield.ai/plugin/ws`. Le plugin exécute de l'ExtendScript, sait rendre l'image courante dans un fichier temporaire et envoyer images et vidéos vers les serveurs de Higgsfield ; il se connecte à ton compte par OAuth et charge des réglages à distance. Conséquence probable : **tout ce que le MCP lit ou montre du projet passe par les serveurs de Higgsfield**, images comprises.
- Ce qu'E0 établit avant tout exercice (ta demande) : ce que ses outils font réellement sur ce Mac, ce qui consomme des crédits et ce qui n'en consomme pas, ce qui transite (table 6.7).
- **Tes règles** (2026-10-13) : « Aucun crédit de génération (images ou vidéos IA) sans me demander, avec le coût estimé. » « Aucun fichier de client envoyé à Higgsfield sans mon accord. Les exercices techniques n'utilisent que de la matière créée pour l'occasion. » Les références « restent sur le Mac : ne les envoie pas à Higgsfield. »
- Ce que j'en tire pour les exercices : les projets After Effects ne contiennent que de la matière créée pour l'occasion (textes neutres en Inter, solides, formes, rendus de E3) ; aucune référence n'entre dans un projet After Effects ouvert pendant que le plugin est connecté (les planches de comparaison se font hors d'After Effects) ; les rendus qu'on mesure sortent d'`aerender`, en local.

### 6.4 Qui construit, qui regarde, qui rend
| | Construire | Voir avant de rendre | Rendre | Juger |
|---|---|---|---|---|
| After Effects | MCP de Higgsfield ; ou script ExtendScript (`.jsx`) lancé par `osascript` (`DoScriptFile`) quand c'est plus fiable ou plus mesurable ; le `.aep` enregistré dans `_travail/` | MCP de Higgsfield : relire les clés et les influences réellement posées, voir une image (elle passe par ses serveurs) | `aerender` en local, séquence PNG | Mesures hors du logiciel (`courbe_mouvement.py`), planche côte à côte, directeur artistique, ta question |
| Blender | Script Python en ligne de commande (`Blender -b -P`) : il construit et enregistre le `.blend` | J'ouvre le `.blend` dans Blender ; MCP : capture de la vue caméra, résumé de la scène, rendu de la vue | Ligne de commande, Cycles sur METAL, séquence PNG | Les mêmes |

Dans Blender, le script reste la source (rejouable, gardé dans `projets-phase-3/tests-techniques/`) et le MCP sert d'yeux ; dans After Effects, ce que le MCP construit est relu et, quand ça compte pour la mesure, rejoué par script. Si un serveur manque le jour des exercices, tout se fait quand même par script : je le note dans la table de E0.

### 6.5 Ce qui n'est pas nécessaire
- **Accessibility** (Accessibilité) pour Claude : pas au début ; si une fenêtre de dialogue d'After Effects bloque un script, je te le dis.
- **Screen & System Audio Recording** (Enregistrement de l'écran) et **Full Disk Access** (Accès complet au disque) : non. Les captures de Blender et les images d'After Effects sont faites par les logiciels eux-mêmes.
- Rien à acheter, aucun compte nouveau, aucun plugin de plus. Crédits Higgsfield : les exercices n'en prévoient aucun ; jamais sans ton accord et un coût estimé. Pas d'HDRI (deux softbox émissives suffisent). Le son d'impact de E4 viendra de ton abonnement Artlist le jour venu.

### 6.6 Les références à choisir (une pour E1, une pour E3)
Planche : `projets-phase-3/tests-techniques/references-E1-E3.png` (une image par référence ; le mouvement ne s'y voit pas).

**Choix de Diego (2026-10-13) : A pour E1, A pour E3**, comme je le recommandais. Les deux restent sur le Mac : jamais envoyées à Higgsfield, ni importées dans un projet After Effects que le plugin peut lire.

**E1 — un titre qui se pose.** Parmi tes références des réseaux, aucune ne fait monter un titre : noahlazo, dont tu aimes « les titres », les pose d'une coupe, sans animation, dans un film de 405 px de haut ; c'est une référence de style (couleur, placement, répliques), pas d'animation.

| | Référence | Ce qu'elle montre | Ce que E1 devient |
|---|---|---|---|
| A | **Swile POW** (film du studio), « Une seule carte, » vers 1:09,5 ; 4K, 25 i/s ; `videos/projets-f42/SWILE_POW_169_V5_STJAUNE.mov` | Mesuré image par image : le texte arrive d'un coup (opaque dès la première image), monte d'environ 44 px (à l'échelle 1080p) en dix images, **les deux tiers dans les deux premières**, puis se freine jusqu'à moins d'un demi-pixel par image ; **aucun flou de mouvement** (lettres nettes à l'image la plus rapide, en pleine résolution) ; ensuite toute la mise en page grandit très lentement. Police sans empattement, fine, blanche sur noir, à côté d'une carte en 3D [VU SUR IMAGES, mesuré] | Le geste de E1, à ton niveau de livraison, mesurable en pleine résolution. Ses chiffres remplacent les miens (20 px, fondu, flou) ; mon fondu flouté devient un témoin. Police : celle du projet si tu l'as, sinon Inter |
| B | **Apple, iPhone 17 « 3x More Scratch Resistant »**, 0:25,7-0:30,1 ; 1080p ; `videos/pubs/iPhone 17_ 3x More Scratch Resistant_1080p.mp4` | Le texte (SF Pro, blanc, petit) arrive avec le plan, sans animation, puis il est remplacé sur place par « Relax, it's iPhone 17 », puis par le logo. Tes mots : « quelque chose d'assez simple et épuré, à la Apple » (carnet 2) [VU SUR IMAGES] | Un exercice de typographie : corps, graisse, approche, placement et lisibilité sur l'image, au pixel près. La courbe d'animation n'est plus testée qu'en E2, ou en variante (« posé en dix images ») que je te montre. Aurait demandé SF Pro |
| C | **EGO, « Visite extraordinaire d'une Bibliothèque-Univers »**, « QUEL EST LE SENS DE LA VIE ? », 0:26-0:31 ; 1080p, 30 i/s ; dans `videos/youtube/` | Le titre se révèle mot à mot : chaque mot apparaît flou puis se met au point, sur un fond presque noir et texturé ; le texte, chaud, reste sombre (au plus 120 sur 255) ; aucun mouvement, puis une coupe au noir [VU SUR IMAGES, mesuré] | Le fondu et le flou qui se résorbe, sans la montée : critères sur la courbe du flou, l'opacité et le décalage entre les mots, mesurés sur la référence |

**E3 — un packshot dans le noir.**

| | Référence | Ce qu'elle montre | Ce que E3 devient |
|---|---|---|---|
| A | **Swile POW**, packshot en 3D, 1:08,8-1:19,5 ; 4K | Une carte noire, puis un téléphone, sur fond noir, dessinés seulement par des reflets doux sur les arêtes et les faces ; l'objet bouge lentement ; ton niveau de livraison [VU SUR IMAGES] | La plus proche de l'exercice (un objet sombre et brillant dans le noir, des reflets maîtrisés, un mouvement lent), comparable en pleine résolution : noirs, douceur des reflets, bruit, vitesse |
| B | **Apple, iPhone 17**, packshot 0:25,7-0:30,1 ; 1080p | Le téléphone orange sur une table de bois sombre, lumière basse et chaude, faible profondeur de champ, reflets qui scintillent sur les objectifs ; caméra fixe [VU SUR IMAGES] | Une référence de lumière et de matière (la seule couleur vive est le produit) ; le mouvement de caméra se juge sur mon rendu seul |
| C | **darius, Nike Air Max Muse**, fin 0:36,9-0:38,5 ; 360x640 ; `videos/reseaux/video-by-dariusbuesch-zf-3-exg.mp4` | La chaussure, sombre et brillante, flotte au centre d'un vignettage gris, sous le titre « air max muse » [VU SUR IMAGES] | Une intention seulement : en 360x640, ni les reflets ni le bruit ne se mesurent |

Si aucune ne te va pour E3 : le film officiel d'Apple « Introducing iPhone 17 Pro » (pas vu ; à toi de le déposer si tu le veux, je ne télécharge rien).

### 6.7 Le MCP de Higgsfield, vérifié en E0 (à remplir avant tout exercice)
| Action | Réellement fait sur ce Mac ? | Crédits Higgsfield ? | Ce qui transite par ses serveurs |
|---|---|---|---|
| Lire le projet (compositions, calques, images clés) | | | |
| Créer une composition | | | |
| Créer des calques (texte, solide, forme) | | | |
| Poser des images clés et leurs influences | | | |
| Écrire une expression | | | |
| Exécuter un script ExtendScript | | | |
| Rendre une image pour la voir | | | |
| Rendre une séquence ou un fichier | | | |
| Outils de génération IA (images, vidéos) | jamais appelés sans l'accord de Diego, coût estimé à l'appui | | |
