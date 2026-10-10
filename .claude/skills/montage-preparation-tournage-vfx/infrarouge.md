# Tournage de nuit en infrarouge proche (session 19, Y15)

Toutes les recettes sont **[THÉORIQUE]** : sourcées (`sources/infrarouge-tournage-2026-10.md`), aucune n'a été testée sur une vraie caméra. Le look a été maquetté en 3D (atelier 23).

**Quand et pourquoi** : l'IR montre ce que l'œil ne voit pas, et le spectateur le sait. Il fait ressentir trois choses, à choisir avant de louer le matériel :
- **la surveillance** (illuminateur dans l'axe, cercle de lumière, vert, bruit) : malaise, found footage, regard d'un tiers ; *Zero Dark Thirty* l'emprunte pour le raid ;
- **l'intimité volée** (source décalée et faible, grain fin, monochrome neutre) : on regarde quelqu'un qui ne se sait pas regardé (un dormeur) ; c'est tendre ou gênant selon la durée du plan ;
- **le monde animal / un autre monde** (*Planet Earth II* la nuit ; Giedi Prime dans *Dune 2*, de jour) : l'image est vraie mais n'est plus humaine, les matières changent de valeur.
Si aucune de ces trois émotions n'est voulue, une caméra très sensible en basse lumière (en couleur) est sans doute le meilleur choix.

**Caméra**
- Caméra convertie **full spectrum** (filtre IR-cut retiré) + **filtre passe-IR** devant l'objectif : 720 nm (un peu de rouge visible passe) ou 850 nm (IR seul, image franchement monochrome). Sans filtre, visible et IR se mélangent et la couleur se délave (RED 101).
- **Point en IR, à l'image** : le point se décale par rapport au visible (verre de l'objectif, pas le filtre) ; faire le point sur le moniteur, pas aux repères ; fermer un peu (mais la diffraction arrive plus tôt en IR) ; l'autofocus peut peiner. Vérifier le point chaud (hotspot) de chaque objectif avant le tournage.
- **Balance des blancs fixe**, mesurée sous l'illuminateur ; le monochrome se décide au grade (atelier 23 : le vert et le bruit coloré codent la surveillance).

**Longueur d'onde**
- **850 nm** : meilleur signal, mais une **faible lueur rouge** est visible en regardant la source (et peut gêner un dormeur ou alerter un animal).
- **940 nm** : pas de lueur, mais le capteur silicium y est souvent **2 fois moins sensible** ou pire, et les LED sont moins puissantes : plus de bruit. Pour un dormeur : 850 nm **hors de son regard** (derrière la tête, au-dessus) ou 940 nm s'il dort face à la source, à tester la première nuit.

**Illuminateur**
- **Jamais dans l'axe** pour l'intime : coaxial = cercle, lumière plate et **pupilles brillantes** (la rétine renvoie l'IR, comme les yeux rouges) ; décalé = modelé et pupilles sombres. Les yeux brillants sont un outil pour l'animal ou l'inquiétant, pas un accident.
- Faisceau étroit (25-30°) visé sur le visage depuis la direction motivée (fenêtre), faible ; la nuit reste majoritaire dans le cadre (atelier 23 v3).
- **Peau** : aspect lisse, laiteux, presque cireux, **veines superficielles sombres** ; vêtements et draps changent de valeur (un noir peut sortir blanc) : faire un essai caméra des costumes et de la literie.

**Sécurité oculaire (IEC 62471)** : le proche IR comporte un risque thermique pour la rétine, la cornée et le cristallin ; l'œil ne s'en protège pas par éblouissement, car il ne le voit pas. Une LED seule est en général « exempt », mais **un projecteur à matrice de LED se classe comme produit**. Demander au loueur ou au fabricant son **groupe de risque IEC 62471** ; garder une distance au visage, ne pas viser les yeux de près, surtout pour un sujet qui dort plusieurs heures face à la source. Ne pas inventer de seuil.

**À valider en phase 2** : essai d'une nuit (850 contre 940 nm, axe contre décalé, peau, draps) avant toute nuit gardée.
