"""EDL du film mariage-jo (V1). Temps en secondes. Écrit montage.json (lu par la maquette ffmpeg et par la construction Resolve).
Vidéo : piste, nom du rush, src (temps dans le rush), dur (durée dans la timeline), look (nb|couleur|nuit), vitesse (1 = temps réel ;
0.5 = ralenti x2 depuis le 50p), note. Son : piste, fichier, src, dur, rec, gain (dB), fondus (s)."""
import json, sys
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/outils/phase3/mariage")
from sync_fin import sync
M = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/musique"
G = json.load(open(f"{M}/grilles.json"))
HF = "/Volumes/SSD FAST/MARIAGE JO/RUSH/SON HF/REC052.WAV"
Z2 = "/Volumes/SSD FAST/MARIAGE JO/RUSH/SON ZOOM/040626-175038.WAV"
MUS = {"igot": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/I Got a Woman (Remastered)_320k.mp3",
       "remix": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/youtube video #U2ClfSuxjhU_320k.mp3",
       "maritza": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/la-maritza-instrumental-skdr-22.wav",
       "mambo": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/mambo-no-5-wp-0-tr-4.wav"}
V, A, T, MARK = [], [], [], []
rec = 0.0
def v(nom, src, dur, look, piste=1, vitesse=1.0, note="", at=None):
    global rec
    r = rec if at is None else at
    V.append(dict(piste=piste, nom=nom, src=round(src, 3), dur=round(dur, 3), rec=round(r, 3), look=look, vitesse=vitesse, note=note))
    if at is None: rec = r + dur
def a(fichier, src, dur, at, piste, gain=0.0, fin=0.0, fout=0.0, note=""):
    A.append(dict(piste=piste, fichier=fichier, src=round(src, 3), dur=round(dur, 3), rec=round(at, 3), gain=gain, fin=fin, fout=fout, note=note))
def hf_rush(nom, t_hf): return t_hf - sync(nom, "HF")["decalage"]          # temps du rush pour un instant du HF
def texte(t, dur, txt, style, note=""): T.append(dict(rec=round(t, 3), dur=dur, texte=txt, style=style, note=note))

# ---------------- A. Le panini (cold open), N&B ----------------
A0 = 0.0; H0 = 1358.40                                 # HF « dans notre histoire avec Lala »
def hv(nom, t_hf, dur, note=""): v(nom, hf_rush(nom, t_hf), dur, "nb", note=note)
hv("20260604_C3689", H0, 3.2, "Jonathan au micro, large, mur de pierre (synchro)")
hv("FX30.5635", H0 + 3.2, 9.2, "Jonathan flou au premier plan, Ornella nette qui écoute (synchro)")
v("FX30.5635", 105.2, 2.4, "nb", note="TRICHE : invité chauve qui sourit, 36 s avant la phrase (même salle, même lumière)")
hv("20260604_C3689", H0 + 14.8, 4.84, "Jonathan, large (synchro)")
v("FX30.5635", 129.9, 1.33, "nb", note="TRICHE : Ornella main sur la poitrine, 7 s avant (raccord)")
hv("20260604_C3689", H0 + 20.97, 7.0, "Jonathan, plan moyen : « est-ce que tu veux mon panini ? » (synchro)")
hv("FX30.5635", H0 + 27.97, 5.5, "Ornella éclate de rire (synchro, vrai moment)")
hv("20260604_C3689", H0 + 33.47, 3.5, "couple d'invités qui sourit (synchro)")
v("FX30.5635", 155.0, 3.4, "nb", note="TRICHE : homme aux lunettes sur la tête et dame blonde qui rient, 5 s après")
A_FIN = rec
a(HF, H0, A_FIN + 0.6, A0, 1, gain=0.0, fin=0.15, fout=1.2, note="voix de Jonathan, HF")
a(Z2, H0 - 1122.98, A_FIN + 0.6, A0, 2, gain=-12.0, fin=0.3, fout=1.2, note="salle (Zoom) : rires")
MARK.append((0.0, "A"))

# ---------------- B. La journée, couleur, I Got a Woman ----------------
rec = A_FIN + 0.6                                        # noir court
B0 = rec; tb = G["I_Got_a_Woma"]["temps"]
def bt(k): return B0 + tb[k]                             # temps du k-ième temps du morceau dans la timeline
a(MUS["igot"], 0.0, 0, B0, 3, gain=-6.0, note="I Got a Woman : début")   # durée fixée plus bas
v("20260604_C3576", 23.0, bt(0) - rec, "couleur", note="travelling vers les lettres J&O (le chant commence)")
k = 0
def bk(nom, src, n, look="couleur", note="", vitesse=1.0):
    global k
    v(nom, src, bt(k + n) - rec, look, note=note, vitesse=vitesse); k += n
bk("20260604_C3842", 0.5, 6, note="lettres J&O : TITRE « Jonathan & Ornella »")
texte(bt(0) + 0.2, bt(6) - bt(0) - 0.4, "Jonathan & Ornella", "titre", "sur les lettres lumineuses")
for nom, s, note in [("20260604_C3562", 16.0, "chaise « Monsieur »"), ("20260604_C3562", 21.0, "chaise « Madame »"),
                     ("20260604_C3564", 3.0, "pétales, ras du sol"), ("FX30.5490", 2.5, "bougies"), ("20260604_C3560", 10.0, "coupes"),
                     ("20260604_C3544", 1.0, "fleurs, bascule de point"), ("20260604_C3546", 7.5, "rose sur une chaise")]:
    bk(nom, s, 1, note=note)
bk("FX30.5475", 2.0, 2, note="nom du domaine")
bk("20260604_C3520", 10.0, 3, note="le couple marche vers nous, robe dans le vent")
bk("20260604_C3532", 0.5, 3, note="Ornella rit, Jonathan la regarde")
bk("20260604_C3537", 8.5, 3, note="portrait serré du couple")
bk("20260604_C3531", 0.3, 2, note="rire")
bk("20260604_C3533", 9.0, 3, note="les trois enlacés, Naël au milieu")
bk("20260604_C3538", 12.0, 5, note="Naël sourit : TITRE « Naël »")
texte(bt(k - 5) + 0.3, bt(k) - bt(k - 5) - 0.5, "Naël", "personnage")
bk("20260604_C3541", 0.5, 4, note="ils s'éloignent main dans la main, Naël derrière")
for nom, s, note in [("20260604_C3595", 1.0, "regard caméra, sourire"), ("20260604_C3609", 4.4, "rire"), ("20260604_C3597", 1.0, "accolade"),
                     ("FX30.5527", 10.3, "V face caméra"), ("20260604_C3601", 1.0, "rire"), ("20260604_C3627", 1.0, "rire"), ("FX30.5544", 2.0, "fillette en rose")]:
    bk(nom, s, 2, note=note)
bk("FX30.5577", 2.0, 4, note="silhouettes qui entrent dans la salle de pierre")
bk("20260604_C3655", 44.0, 4, note="les mariés à la porte, bouquet coloré")
B_FIN = rec
A[-1]["dur"] = round(B_FIN - B0 + 0.04, 3); A[-1]["fout"] = 0.04
MARK.append((B0, "B"))

# ---------------- C. La cérémonie, N&B (voix HF, salle du Zoom) ----------------
Z1 = "/Volumes/SSD FAST/MARIAGE JO/RUSH/SON ZOOM/040626-161726.WAV"
def zoom_de_hf(h): return (Z1, h + 4469.08) if h < 1122.98 else (Z2, h - 1122.98)
C0 = rec
def phrase(h0, h1, plans, gain_voix=0.0, salle=-13.0, note=""):
    """Pose la voix HF h0-h1 à la position courante et la couvre de plans. plans : liste de (nom, src|'sync', dur|None) ;
    'sync' = rush calé sur le HF au point où le plan commence ; dur None = jusqu'à la fin de la phrase."""
    global rec
    r0 = rec; dur = h1 - h0
    a(HF, h0, dur, r0, 1, gain=gain_voix, fin=0.06, fout=0.08, note=note)
    zf, zs = zoom_de_hf(h0 - 0.25); a(zf, zs, dur + 0.5, r0 - 0.25, 2, gain=salle, fin=0.25, fout=0.25, note="salle")
    t = r0
    for nom, src, d in plans:
        d = (r0 + dur - t) if d is None else d
        if src == "sync": src = hf_rush(nom, h0 + (t - r0))
        v(nom, src, d, "nb", note=note + (" (synchro)" if isinstance(src, float) and False else ""), at=t); t += d
    rec = r0 + dur
# entrée des mariés (salle et La Maritza en douceur)
v("FX30.5589", 11.8, 3.0, "nb", note="Ornella entre et éclate de rire (avant le HF : son de la salle)")
v("FX30.5590", 1.0, 2.2, "nb", note="les invités applaudissent, l'officiant")
a(Z1, 146.0 + 4469.08, 5.4, C0, 2, gain=-8.0, fin=0.3, fout=0.4, note="applaudissements de l'entrée (Zoom)")
a(MUS["maritza"], 0.0, 9.0, C0, 3, gain=-14.0, fin=0.5, fout=3.0, note="La Maritza, intro douce, s'éteint sous l'officiant")
phrase(181.35, 183.9, [("FX30.5591", 0.0, 1.1), ("FX30.5593", 0.2, None)], note="« Il va y avoir plein de mauvaises blagues. » TRICHE : officiant bras tendu (HF 160) ; Jonathan plié de rire (HF 178)")
phrase(218.3, 221.75, [("20260604_C3657", "sync", None)], note="« …des excuses concernant la température et le temps, la météo. » (synchro)")
phrase(223.95, 228.65, [("20260604_C3658", 10.2, None)], note="« certains détracteurs trouvaient que c'était de ma faute. Ils n'ont pas tort. » TRICHE : invités qui rient (HF 249)")
phrase(229.7, 233.0, [("20260604_C3657", "sync", None)], note="« Donc il y aura de l'orage tout à l'heure. Ne m'en voulez pas. » (synchro)")
phrase(254.55, 258.3, [("FX30.5592", 1.0, None)], note="« On n'a pas besoin de voir le ciel quand on a quelqu'un à regarder. » TRICHE : Ornella et Jonathan (HF 176)")
phrase(259.55, 264.6, [("20260604_C3658", "sync", 1.55), ("20260604_C3659", 0.0, None)], note="« Nous, les célibataires, on va se faire foutre. » + rires (synchro)")
phrase(351.8, 354.65, [("FX30.5602", "sync", 1.5), ("FX30.5599", 0.3, None)], note="« …et surtout, ils ont eu Naël. » ; Naël TRICHE (HF 320)")
phrase(358.1, 360.6, [("FX30.5603", 0.0, None)], note="« Ce petit être céleste » ; Naël (synchro à 1 s près)")
phrase(372.15, 378.0, [("FX30.5603", 2.55, 3.47), ("20260604_C3664", 0.0, None)], note="« Naël, je pense que tout le monde ici sera d'accord pour dire que c'est un enfant génial ? » TRICHE : Naël 13 s avant")
phrase(501.3, 508.15, [("FX30.5612", 0.3, 3.4), ("20260604_C3661", 2.0, None)], note="« La première fois, on se marie sur une promesse, et la deuxième fois, sur des preuves. » TRICHE : larges (HF 513 et 307)")
phrase(508.15, 512.3, [("FX30.5616", 1.0, None)], note="« On dit que l'amour rend aveugle. C'est pour les célibataires. » TRICHE : les mariés rient (HF 575)")
# vœux d'Ornella
phrase(1004.9, 1009.7, [("20260604_C3686", 5.2, None)], note="Ornella : « Mon mari, » TRICHE 4 s (même plan)")
phrase(1014.05, 1018.85, [("20260604_C3686", "sync", 2.85), ("FX30.5633", 0.05, None)], note="« nous nous sommes rencontrés il y a 13 ans et depuis ce jour, on ne s'est plus lâchés. » (synchro)")
phrase(1095.6, 1099.6, [("FX30.5634", "sync", 2.0), ("FX30.5634", 16.0, None)], note="« Et puis il y a Naël. Notre plus belle aventure. » ; Naël TRICHE (6 s après)")
phrase(1185.3, 1191.5, [("20260604_C3686", "sync", 3.0), ("FX30.5634", "sync", None)], note="« Alors je redis oui. Un oui encore plus fort… qu'il y a dix ans. » (synchro)")
# vœux de Jonathan, la demande
phrase(1597.85, 1602.75, [("20260604_C3695", "sync", 2.15), ("FX30.5635", 358.6, None)], note="« la femme parfaite n'existe pas, mais toi, tu es la femme parfaite pour moi. » ; Ornella TRICHE (5 s après)")
phrase(1646.85, 1658.6, [("20260604_C3695", "sync", 3.75), ("FX30.5635", "sync", 2.4), ("20260604_C3695", "sync", None)], note="« je vais te faire une vraie demande cette fois-ci… à genoux… ma femme pour les dix prochaines années » (synchro)")
phrase(1658.6, 1663.4, [("FX30.5635", 416.9, None)], gain_voix=-6.0, salle=-6.0, note="ils s'enlacent, la salle applaudit (Quentin, synchro)")
# bracelets, le oui
phrase(1693.15, 1695.3, [("20260604_C3695", "sync", None)], note="« Dans dix ans, ce sera un collier. » (synchro)")
phrase(1700.8, 1708.9, [("20260604_C3695", "sync", None)], note="« à cette enfant céleste, Naël, de venir leur donner leur bracelet… On applaudit Naël » (synchro)")
phrase(1797.15, 1804.15, [("20260604_C3696", "sync", None)], note="« acceptes-tu de reprendre pour épouse Ornella » (synchro)")
phrase(1806.6, 1811.0, [("FX30.5635", "sync", None)], note="« Oui, pour les dix prochaines années. » Ornella rit (synchro)")
phrase(1813.3, 1818.35, [("20260604_C3696", "sync", None)], note="« je crois que j'ai l'honneur de vous déclarer re-mari et re-femme. » (synchro)")
C_FIN = rec
MARK.append((C0, "C"))

# ---------------- D. Le oui rallume la couleur : le baiser, La Maritza éclate ----------------
D0 = rec; tm = G["la-maritza-i"]["temps"]
km = min(range(len(tm)), key=lambda i: abs(tm[i] - 23.5)); MZ0 = tm[km]          # le temps fort où le morceau démarre
def mt(i): return D0 + tm[km + i] - MZ0
v("FX30.5635", hf_rush("FX30.5635", 1822.5), mt(4) - rec, "couleur", note="LE BAISER (front) : la couleur revient (synchro)")
a(HF, 1822.5, 3.5, D0, 1, gain=-4.0, fin=0.05, fout=1.0, note="« Bravo ! »")
zf, zs = zoom_de_hf(1822.5); a(zf, zs, 9.0, D0, 2, gain=-7.0, fin=0.1, fout=2.5, note="applaudissements (Zoom)")
km2 = 4
for nom, src, n, note in [("FX30.5635", 585.6, 4, "invités qui applaudissent"), ("FX30.5638", 2.0, 4, "Jonathan embrassé, sourire"),
                          ("20260604_C3704", 0.0, 4, "cœur avec les mains face caméra"), ("FX30.5639", 16.0, 4, "Jonathan, grand sourire")]:
    v(nom, src, mt(km2 + n) - rec, "couleur", note=note); km2 += n
D_FIN = rec
MARK.append((D0, "D"))

# ---------------- E. Le cocktail : La Maritza continue ; les musiciens ; les petits mots ----------------
E0 = rec
def rush(nom): return "/Volumes/SSD FAST/MARIAGE JO/RUSH/" + next(x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json")) if x["nom"] == nom)["fichier"]
k3 = km2
def mk(nom, src, n, note="", look="couleur"):
    global k3
    v(nom, src, mt(k3 + n) - rec, look, note=note); k3 += n
for nom, src, n, note in [("FX30.5702", 0.5, 2, "pieds bicolores qui battent la mesure"), ("FX30.5698", 12.0, 2, "caisse claire"),
                          ("FX30.5704", 1.0, 2, "main sur la guitare"), ("FX30.5698", 49.0, 2, "contrebasse"), ("FX30.5698", 31.3, 2, "saxophone"),
                          ("FX30.5667", 0.4, 4, "le guitariste sourit"), ("FX30.5697", 1.0, 4, "le saxophoniste rit"),
                          ("FX30.5743", 9.6, 4, "la dame aux cheveux blancs danse"), ("20260604_C3820", 8.4, 4, "elle rit, bras levés"),
                          ("FX30.5730", 1.2, 4, "Naël reçoit sa caricature"), ("FX30.5720", 2.0, 4, "Naël rit")]:
    mk(nom, src, n, note)
MUS_FIN = rec
a(MUS["maritza"], MZ0, MUS_FIN - D0 + 14.0, D0, 3, gain=-9.0, fin=0.0, fout=2.0, note="La Maritza depuis le temps fort (23,5 s), sous le baiser, les applaudissements et le cocktail ; baissée sous les petits mots (gain réglé au mixage)")
# petits mots (la musique continue, baissée : piste 3 coupée en deux plus bas)
def mot(nom, t0, t1, note):
    global rec
    v(nom, t0, t1 - t0, "couleur", note=note); a(rush(nom), t0, t1 - t0, rec - (t1 - t0), 1, gain=2.0, fin=0.05, fout=0.12, note="petit mot (son caméra)")
mot("20260604_C3789", 8.6, 14.95, "« Le traiteur est hyper bon, vous avez dû payer ça très cher. Perso, j'aurais jamais pu faire ça, moi. »")
mot("20260604_C3787", 4.45, 7.7, "« Je vous aime. Merci pour ce buffet gratuit. »")
mot("20260604_C3797", 10.5, 13.4, "Sylvain : « C'est grâce à qui un petit peu ? C'est moi qui t'emmenais avec ton panini. »")
mot("20260604_C3813", 16.85, 18.3, "Ornella : « Ah, il faut que je sois une invitée ? »")
mot("20260604_C3813", 24.45, 33.0, "Ornella en invitée : « Les mariés étaient super, surtout la mariée… jolie robe, joli make-up, belle coiffure. Le marié était aussi très beau. »")
E_FIN = rec
# la musique : pleine jusqu'aux petits mots, puis baissée
A[-6]["dur"] = round(MUS_FIN - D0 + 0.3, 3); A[-6]["fout"] = 0.3
a(MUS["maritza"], MZ0 + (MUS_FIN - D0), E_FIN - MUS_FIN + 0.5, MUS_FIN, 3, gain=-24.0, fin=0.3, fout=0.5, note="La Maritza baissée sous les petits mots")
MARK.append((E0, "E"))

# ---------------- F. L'orage : silence de musique, la pluie, le rappel de l'officiant ----------------
F0 = rec
v("FX30.5805", 0.5, 3.6, "couleur", note="la terrasse déserte sous la pluie")
a(rush("FX30.5805"), 0.5, 3.6, F0, 2, gain=0.0, fin=0.3, fout=0.2, note="pluie (son caméra)")
a(HF, 243.0, 5.8, F0 + 0.6, 1, gain=0.0, fin=0.05, fout=0.3, note="rappel : « Mariage sous la flotte, culotte qui gigote. » (officiant, 17:36)")
v("20260604_C3864", 1.0, 9.0, "couleur", note="la dame danse sous la pluie, bras ouverts, puis bras levés")
a(rush("20260604_C3864"), 1.0, 9.0, F0 + 3.6, 2, gain=0.0, fin=0.2, fout=0.4, note="pluie, rires (son caméra)")
F_FIN = rec
MARK.append((F0, "F"))

# ---------------- G. La soirée : la reprise remixée de I Got a Woman ----------------
G0 = rec; tr = G["youtube_vide"]["temps"]
def rt(i): return G0 + tr[i]
k4 = 0
def rk(nom, src, n, note="", look="couleur"):
    global k4
    v(nom, src, rt(k4 + n) - rec, look, note=note); k4 += n
rk("20260604_C3894", 27.0, 6, "ouverture du bal : le couple, face à face")
rk("20260604_C3894", 88.0, 4, "il l'embrasse sur la tempe")
rk("20260604_C3922", 0.5, 4, "la piste explose, bras en l'air")
rk("20260604_C3899", 6.0, 4, "un invité porté")
rk("20260604_C3911", 13.6, 6, "Jonathan rit, lunettes noires")
rk("FX30.5838", 28.3, 6, "le père de Jonathan danse, bras levés, accolade")
G_BAL = rec
a(MUS["remix"], 0.0, G_BAL - G0 + 0.4, G0, 3, gain=-8.0, fin=0.0, fout=0.4, note="remix : le bal")
# le maillot (son direct, remix très bas)
v("20260604_C4007", 11.9, 1.8, "couleur", note="« alors tiens, je te laisse l'ouvrir » (synchro)")
a(rush("20260604_C4007"), 11.9, 1.8, rec - 1.8, 1, gain=4.0, fin=0.05, fout=0.1, note="son direct")
v("20260604_C4007", 26.2, 2.8, "couleur", note="le maillot se déplie")
a(rush("20260604_C4007"), 17.4, 4.2, rec - 2.8 - 0.6, 1, gain=4.0, fin=0.05, fout=0.2, note="« mais il a été signé par Marquinhos » (son décalé sur l'image : triche son)")
v("FX30.5871", 6.0, 1.8, "couleur", note="Jonathan tient le maillot (Quentin, serré)")
v("20260604_C4007", 43.2, 1.6, "couleur", note="le maillot en gros plan")
v("20260604_C4007", 47.6, 5.9, "couleur", note="« si jamais il gagne, frérot, c'est encore plus stylé… et donc vraisemblablement il gagne samedi soir » (synchro)")
a(rush("20260604_C4007"), 47.6, 5.9, rec - 5.9, 1, gain=4.0, fin=0.05, fout=0.15, note="son direct")
v("20260604_C4008", 8.0, 2.4, "couleur", note="la salle exulte, serviette au vent")
a(rush("20260604_C4008"), 8.0, 2.4, rec - 2.4, 2, gain=0.0, fin=0.05, fout=0.2, note="cris")
v("20260604_C4008", 31.0, 2.4, "couleur", note="Jonathan brandit le maillot")
v("20260604_C4009", 0.3, 2.4, "couleur", note="Jonathan se penche vers Naël, le maillot sur la table")
G_MAIL = rec
a(MUS["remix"], G_BAL - G0, G_MAIL - G_BAL, G_BAL, 3, gain=-26.0, fin=0.3, fout=0.3, note="remix très bas sous le maillot")
# la pièce montée, la salle passe au violet, rafale néon, le père et le fils
gi = min(range(len(tr)), key=lambda i: abs(G0 + tr[i] - G_MAIL - 1.7)); k4 = gi
v("20260604_C4012", 3.0, rt(k4) - rec, "couleur", note="la pièce montée"); 
rk("20260604_C4016", 47.0, 4, "la salle debout, bras levés, lumière violette", "nuit")
rk("20260604_C4017", 13.0, 4, "les mariés et la pièce montée", "nuit")
K0 = rec
rk("20260604_C4029", 3.5, 16, "PASSAGE KINETIC (à construire) : photobooth, détourage, fonds qui changent", "nuit")
for nom, src in [("20260604_C4077", 1.2), ("20260604_C4096", 2.6), ("20260604_C4106", 3.6), ("20260604_C4113", 13.6), ("20260604_C4126", 1.0), ("20260604_C4085", 2.3)]:
    rk(nom, src, 1, "rafale néon (un temps)", "nuit")
rk("FX30.5900", 8.0, 8, "Jonathan et Naël à la fontaine à chocolat", "nuit")
G_FIN = rec
a(MUS["remix"], G_MAIL - G0 + 0.0, G_FIN - G_MAIL + 0.5, G_MAIL, 3, gain=-8.0, fin=0.4, fout=0.5, note="remix : la fête")
MARK.append((G0, "G"))

# ---------------- H. Dans dix ans ----------------
H0b = rec
mot("20260604_C3798", 6.1, 7.95, "« …on se revoit dans dix ans »")
mot("20260604_C3787", 14.25, 15.5, "« à vos dix ans dans dix ans »")
mot("20260604_C3704", 7.1, 9.2, "« Dans dix ans, on se retrouve riche ! »")
v("20260604_C3696", hf_rush("20260604_C3696", 1869.0), 4.3, "couleur", note="Jonathan : « Je jure, je rigole pas : dans dix ans, on refait la même chose ! » (synchro)")
a(HF, 1869.0, 4.3, rec - 4.3, 1, gain=0.0, fin=0.05, fout=0.4, note="Jonathan")
zf, zs = zoom_de_hf(1869.0); a(zf, zs, 6.5, rec - 4.3, 2, gain=-10.0, fin=0.1, fout=1.5, note="salle")
v("20260604_C4169", 0.0, 1.85, "nuit", note="rires sur la terrasse de nuit")
v("20260604_C4166", 4.5, 3.5, "nuit", note="rires sur la terrasse de nuit")
a(rush("20260604_C4166"), 4.5, 3.5, rec - 3.5, 2, gain=-4.0, fin=0.2, fout=1.5, note="rires")
texte(rec + 0.5, 3.5, "Rendez-vous en 2036.", "fin")
rec += 4.5
a(MUS["remix"], 183.5, rec - H0b, H0b, 3, gain=-18.0, fin=1.0, fout=2.5, note="fin du remix, très bas, sous les voix")
MARK.append((H0b, "H"))

json.dump(dict(video=V, audio=A, textes=T, blocs=MARK, duree=round(rec, 3)), open(__file__.replace("edl.py", "montage.json"), "w"), indent=1, ensure_ascii=False)
print("durée", round(rec, 2), "plans", len(V), "sons", len(A))
