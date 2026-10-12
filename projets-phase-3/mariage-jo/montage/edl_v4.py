"""EDL du film mariage-jo, V4 (remonté à partir du dérush, 2026-10-12). Écrit montage_V4.json (maquette ffmpeg et construction Resolve).
Vidéo : piste, nom, src (s dans le rush), dur (s dans la timeline), look (V4_nb | V4_couleur), vitesse, note, [gel : arrêt sur image],
[fondu_grade : le plan suivant est la suite exacte du même rush, fondu de grade entre les deux].
Son : piste (1 voix, 2 salle et ambiances, 3 musique, 4 lit musical sous la parole), fichier, src, dur, rec, gain, fondus.
Parole : chaque extrait vient de parole_V4.json (alignement WhisperX + creux d'énergie mesuré : `labo/outils/phase3/mariage/parole.py`),
ou d'un temps fixé à la main au spectrogramme quand l'alignement échoue (applaudissements) : c'est écrit dans la note."""
import json, sys, os
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/outils/phase3/mariage")
from sync_fin import sync
MD = "/Volumes/SSD FAST/Montage-IA/projets-phase-3/mariage-jo/montage"
TW = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
M = f"{TW}/musique"; G = json.load(open(f"{M}/grilles.json"))
P = json.load(open(f"{MD}/parole_V4.json"))
HF = f"{TW}/son/REC052_traite.wav"     # HF compressé de la V3b (passe-haut 80 Hz, 3:1, limiteur) ; mêmes temps que REC052.WAV
Z1 = "/Volumes/SSD FAST/MARIAGE JO/RUSH/SON ZOOM/040626-161726.WAV"; Z2 = "/Volumes/SSD FAST/MARIAGE JO/RUSH/SON ZOOM/040626-175038.WAV"
MUS = {"igot": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/I Got a Woman (Remastered)_320k.mp3",
       "remix": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/youtube video #U2ClfSuxjhU_320k.mp3",
       "maritza": "/Volumes/SSD FAST/MARIAGE JO/MUSIQUE/la-maritza-instrumental-skdr-22.wav",
       "maritza_lit": f"{M}/sep/htdemucs/la-maritza-i/other.wav"}      # La Maritza sans batterie, basse ni voix (demucs, local)
INV = {x["nom"]: x for x in json.load(open(f"{TW}/inventaire.json"))}
def rush(nom): return "/Volumes/SSD FAST/MARIAGE JO/RUSH/" + INV[nom]["fichier"]
V, A, T, MARK, TRICHES = [], [], [], [], []
rec = 0.0
NB, CO = "V4_nb", "V4_couleur"
def v(nom, src, dur, look, piste=1, vitesse=1.0, note="", at=None, **kw):
    global rec
    r = rec if at is None else at
    e = dict(piste=piste, nom=nom, src=round(src, 3), dur=round(dur, 3), rec=round(r, 3), look=look, vitesse=vitesse, note=note); e.update(kw)
    V.append(e)
    if "TRICHE" in note: TRICHES.append((round(r, 2), nom, round(src, 2), note))
    if at is None: rec = r + dur
    return e
def a(fichier, src, dur, at, piste, gain=0.0, fin=0.0, fout=0.0, note="", role=None):
    A.append(dict(piste=piste, fichier=fichier, src=round(src, 3), dur=round(dur, 3), rec=round(at, 3), gain=gain, fin=fin, fout=fout, note=note, role=role))
def hf_rush(nom, t_hf): return t_hf - sync(nom, "HF")["decalage"]
def zoom(h): return (Z1, h + 4469.08) if h < 1122.98 else (Z2, h - 1122.98)
def texte(t, dur, txt, style, note=""): T.append(dict(rec=round(t, 3), dur=round(dur, 3), texte=txt, style=style, note=note))

def voix(cle, at, gain=0.0, note="", d=None, f=None, salle=True):
    """Pose l'extrait de parole `cle` (HF ou son caméra) à `at`. Renvoie (début, fin) dans la timeline."""
    x = P[cle]; d0 = x["d"] if d is None else d; f0 = x["f"] if f is None else f
    fich = HF if x["src"] == "HF" else x["fichier"]
    a(fich, d0, f0 - d0, at, 1, gain=gain, fin=0.04, fout=0.06, note=f"[{cle}] « {x['texte']} » {note}".strip(), role="voix")
    if x["src"] == "HF" and salle:
        zf, zs = zoom(d0); a(zf, zs, f0 - d0, at, 2, gain=-14.0, fin=0.15, fout=0.15, note="salle (Zoom) sous la voix, bornée à la voix (le Zoom entend aussi l'orateur)", role="salle_sous")
    return at, at + (f0 - d0), d0

# =============== A. L'histoire du panini (N&B) ===============
A0 = 0.0
v("FX30.5486", 2.0, 4.2, NB, note="la salle de cérémonie vide, lent travelling : cheminée fleurie, chaises, bougies (FONDU DEPUIS LE NOIR)", fondu_noir=1.2)
v("FX30.5483", 2.5, 2.8, NB, note="le miroir « Bienvenue au mariage de Jonathan & Ornella »")
v("20260604_C3651", 41.0, 2.6, NB, note="la salle se remplit, lumières de pierre (avant la cérémonie : contexte, pas une triche de parole)")
VA0 = 2.4                                                  # la voix de Jonathan commence sur le miroir (J-cut)
d_a, f_a, _ = voix("panini_a", VA0, note="voix posée sur l'installation, puis synchrone")
H = lambda rec_t: P["panini_a"]["d"] + (rec_t - VA0)      # temps HF d'un instant de la timeline (extrait continu)
v("20260604_C3689", hf_rush("20260604_C3689", H(rec)), 3.4, NB, note="Jonathan au micro, large (synchro)")
v("FX30.5635", 114.0, 3.8, NB, note="TRICHE (≈ 3 s) : Jonathan flou au premier plan, Ornella nette qui écoute ; même discours")
v("FX30.5635", 105.3, 2.2, NB, note="TRICHE : un invité sourit (même salle, même discours, 30 s avant ; temps vérifié en lecture directe)")
# C3689 : zoom rapide à 44,2-45,4 s et invité devant l'objectif à 49-50 s (vu image par image) : on n'en garde que 45,5-48,9 s
v("FX30.5635", 121.0, f_a - rec + 0.05, NB, note="TRICHE (≈ 10 s) : Jonathan flou au premier plan, Ornella écoute")
d_b, f_b, _ = voix("panini_b", f_a + (P["panini_b"]["d"] - P["panini_a"]["f"]))   # l'air naturel entre les deux phrases est gardé
r_45 = d_b + (45.5 - hf_rush("20260604_C3689", P["panini_b"]["d"]))
v("FX30.5635", 110.0, r_45 - rec, NB, note="TRICHE (≈ 20 s avant) : un invité à casquette sourit")
v("20260604_C3689", 45.5, 3.4, NB, note="Jonathan au micro, plan moyen (synchro) : « …vous allez être servis… »")
t_pan = rec
v("FX30.5635", 137.9, (d_b + 6.3 + 7.0) - rec, NB, note="TRICHE (1 s d'avance : un bras passe devant l'objectif à 137,6 s) : Ornella écoute « est-ce que tu veux mon panini ? », puis éclate de rire")
texte(d_b + 8.3, 2.6, "Un acheté, un offert.", "replique")
v("FX30.5635", 155.2, 2.4, NB, note="TRICHE : invités qui rient (≈ 10 s après, même salle)")
A_FIN = rec
a(Z2, d_a - 1122.98 - 2.0, 2.2, A0, 2, gain=-12.0, fin=1.0, fout=0.3, note="murmures de la salle avant la voix", role="salle_seule")
a(Z2, P["panini_b"]["f"] - 1122.98, A_FIN - f_b + 0.3, f_b, 2, gain=-8.0, fin=0.05, fout=0.4, note="les rires de la salle après la chute", role="salle_seule")
a(MUS["maritza"], 0.0, A_FIN + 0.3, A0, 4, gain=-22.0, fin=1.5, fout=0.5, note="La Maritza, introduction douce, sous l'histoire", role="lit")
MARK.append((A0, "A"))

# =============== B. Jonathan & Ornella (couleur, I Got a Woman sur les temps) ===============
B0 = rec; tb = G["I_Got_a_Woma"]["temps"]
def bt(k): return B0 + tb[k]
a(MUS["igot"], 0.0, 0, B0, 3, gain=-6.0, note="I Got a Woman", role="musique")
k = 0
def bk(nom, src, n, note="", vitesse=1.0, **kw):
    global k
    e = v(nom, src, bt(k + n) - rec, CO, note=note, vitesse=vitesse, **kw); k += n; return e
bk("FX30.5456", 11.0, 6, "le couple enlacé au bord du lac, large, pins parasols : TITRE")
texte(B0 + 0.6, bt(6) - B0 - 0.5, "Jonathan & Ornella", "titre")
bk("20260604_C3524", 3.0, 4, "le couple serré, bouquet, ils se regardent")
bk("20260604_C3529", 1.0, 4, "portrait du couple, sourires")
bk("20260604_C3533", 1.5, 4, "la famille : Ornella la tête sur l'épaule de Jonathan, Naël devant avec le bouquet")
bk("20260604_C3538", 10.0, 2, "Naël sourit")
e = bk("20260604_C3538", 12.0, 3, "ARRÊT SUR IMAGE : Naël", gel=True)
texte(e["rec"] + 0.15, e["dur"] - 0.2, "Naël", "nom")
bk("FX30.5467", 15.5, 4, "les trois au bord du lac, feuillage flou au premier plan")
bk("FX30.5464", 6.0, 4, "les trois au loin, cadrés par le tronc d'un arbre")
bk("FX30.5472", 0.4, 4, "ils partent en courant, main dans la main, robe dans le vent")
bk("20260604_C3540", 3.0, 4, "ils s'éloignent, de dos, au ras du sol, la robe dans le vent")
bk("20260604_C3545", 1.0, 2, "chaises « Madame » / « Monsieur », bougies")
bk("FX30.5490", 3.0, 2, "bougies")
bk("20260604_C3546", 9.5, 2, "roses sur les chaises, bascule de point")
bk("20260604_C3595", 1.0, 2, "un invité, regard caméra, sourire")
bk("20260604_C3601", 1.0, 2, "un invité rit")
bk("FX30.5577", 2.0, 4, "les invités entrent dans la salle de pierre (contre-jour)")
B_FIN = rec
A[-1]["dur"] = round(B_FIN - B0 + 0.3, 3); A[-1]["fout"] = 0.3
MARK.append((B0, "B"))

# =============== C. La cérémonie (N&B ; synchrone sur les chutes, voix posée ailleurs) ===============
C0 = rec
v("FX30.5589", 11.6, 2.8, NB, note="Ornella entre et éclate de rire (son de la salle)")
a(Z1, 135.0 + 4469.08, 3.4, C0, 2, gain=-9.0, fin=0.2, fout=0.4, note="applaudissements de l'entrée (Zoom)", role="salle_seule")
GAP = 0.45
def bloc(cle, plans, gap=GAP, **kw):
    """Voix `cle` à la position courante ; plans = [(nom, src|'sync', dur|None, note)] ; le dernier plan couvre aussi l'air qui suit."""
    global rec
    d0, f0, s0 = voix(cle, rec, **kw); t = d0
    for i, (nom, src, d, note) in enumerate(plans):
        fin_bloc = f0 + gap
        d = (fin_bloc - t) if d is None else d
        if src == "sync": src = hf_rush(nom, s0 + (t - d0)); note += " (synchro)"
        v(nom, src, d, NB, note=f"[{cle}] {note}", at=t); t += d
    rec = t
bloc("blagues", [("FX30.5593", 0.3, None, "TRICHE (≈ 3 s avant) : Jonathan plié de rire sur « il va y avoir plein de mauvaises blagues »")])
bloc("orage", [("20260604_C3657", "sync", 1.8, "l'officiant : « il y aura de l'orage tout à l'heure »"),
               ("20260604_C3658", 10.2, None, "TRICHE (≈ 20 s après) : les invités rient")])
bloc("nael", [("FX30.5603", 0.2, None, "TRICHE (1 s) : Naël, pendant « ce petit être céleste »")])
bloc("promesse", [("FX30.5616", 1.0, 2.9, "TRICHE (70 s après) : les mariés rient, serrés"),
                  ("FX30.5612", 0.3, None, "TRICHE : large de la salle")])
bloc("pere", [("20260604_C3686", 174.5, 3.6, "TRICHE (≈ 20 s après) : deux invitées l'écoutent, émues, l'une avec un éventail"),
              ("20260604_C3686", "sync", 3.6, "Ornella lit : « …mais je sais qu'il serait fier… »"),
              ("FX30.5634", "sync", None, "Jonathan qui l'écoute (Quentin)")], gap=0.7)
bloc("naze", [("FX30.5635", 177.5, 4.8, "TRICHE (≈ 1 s) : Ornella écoute « il y a onze ans… la façon la plus naze possible »"),
              ("FX30.5635", 172.0, 3.4, "TRICHE (≈ 1 s) : un invité au crâne rasé sourit (voix posée)"),
              ("FX30.5635", 98.5, 3.0, "TRICHE (≈ 1 min avant) : Ornella sourit, même discours (voix posée)"),
              ("20260604_C3690", "sync", None, "Jonathan : « …viens, on va manger un McDo » (synchro sur la chute)")], d=P["naze"]["d"], f=P["mcdo"]["f"])
texte(rec - 3.3, 2.8, "Comme pour aller manger un McDo.", "replique")
bloc("demande", [("20260604_C3695", "sync", 3.8, "« je vais te faire une vraie demande cette fois-ci » (Diego, synchro)"),
                 ("FX30.5635", "sync", 3.6, "Ornella comprend et sourit (Quentin, synchro)"),
                 ("20260604_C3695", "sync", None, "à genoux : « …ma femme pour les dix prochaines années » (synchro)")], gap=0.1)
t_et = rec
v("FX30.5635", 417.0, 4.8, NB, note="l'étreinte après la demande, fleurs derrière (Quentin, vrai moment, ≈ 4 s après la phrase)")
zf, zs = zoom(1659.3); a(zf, zs, 5.0, t_et, 2, gain=-8.0, fin=0.1, fout=0.6, note="la salle applaudit la demande (Zoom)", role="salle_seule")
bloc("collier", [("20260604_C3695", "sync", 1.8, "l'officiant : « dans dix ans, ce sera un collier »"),
                 ("20260604_C3695", 116.3, None, "TRICHE (≈ 10 s après) : Naël apporte les bracelets")], d=1693.6, f=1696.0,
     note="(fin fixée au spectrogramme : l'alignement s'étire dans les rires)")
v("20260604_C3696", 4.0, 2.6, NB, note="TRICHE (1 min après) : le bracelet au poignet, les mains (insert)")
bloc("remari", [("20260604_C3696", "sync", 3.2, "le couple écoute l'officiant (synchro ; coupé avant le panoramique de 53 s)"),
                ("FX30.5635", "sync", None, "Ornella et Jonathan, « re-mari et re-femme » (Quentin, synchro ; enchaîne sans coupure sur le baiser)")], gap=0.05, salle=True)
C_FIN = rec
MARK.append((C0, "C"))

# =============== D. Le oui rallume la couleur (dans le plan du baiser) ===============
D0 = rec
d_p, f_p, _ = voix("pelles", D0, d=1820.15, f=1822.6, note="(fin fixée au spectrogramme)")
kd = hf_rush("FX30.5635", 1820.15)
v("FX30.5635", kd, 576.6 - kd, NB, note="« vous pouvez vous rouler des grosses pelles » : Ornella rit, tête renversée (synchro, N&B)", fondu_grade=1.0)
v("FX30.5635", 576.6, 0.6, CO, note="… la couleur revient dans le même plan : Jonathan l'attire contre lui (fondu de grade, suite exacte du rush)")
e = v("FX30.5635", 577.2, 2.8, CO, note="ARRÊT SUR IMAGE en couleur : le baiser sur le front, mur de fleurs", gel=True)
texte(e["rec"] + 0.15, e["dur"] - 0.15, "Oui. Pour les dix prochaines années.", "replique")
zf, zs = zoom(1822.6); a(zf, zs, 12.0, f_p, 2, gain=-6.0, fin=0.05, fout=2.0, note="applaudissements et cris (Zoom)", role="salle_seule")
v("FX30.5635", 585.5, 2.4, CO, note="les invités applaudissent (Quentin, ≈ 6 s après le baiser)")
v("20260604_C3697", 5.0, 2.6, CO, note="Jonathan embrassé par un ami (synchro à quelques secondes)")
D_FIN = rec
tm = G["la-maritza-i"]["temps"]
km = min(range(len(tm)), key=lambda i: abs(tm[i] - 23.5)); MZ0 = tm[km]
MARK.append((D0, "D"))

# =============== E. La fête commence (La Maritza) ===============
E0 = rec
k3 = 0
def mt(i): return E0 + tm[km + i] - MZ0
def mk(nom, src, n, note=""):
    global k3
    v(nom, src, mt(k3 + n) - rec, CO, note=note); k3 += n
for nom, src, n, note in [("FX30.5702", 0.5, 2, "pieds bicolores qui battent la mesure"), ("20260604_C3820", 8.4, 4, "la dame aux cheveux blancs rit, bras levés"), ("FX30.5704", 1.0, 2, "main sur la guitare"),
                          ("FX30.5697", 1.0, 4, "le saxophoniste rit (remplace contrebasse et saxophone : panoramiques rapides)"), ("FX30.5667", 0.4, 4, "le guitariste sourit"),
                          ("FX30.5743", 9.6, 4, "la dame aux cheveux blancs danse"), ("FX30.5730", 1.2, 4, "Naël reçoit sa caricature"), ("FX30.5720", 2.0, 4, "Naël rit")]:
    mk(nom, src, n, note)
MUS_E = rec
a(MUS["maritza"], MZ0 - (E0 - D0) - 0.0, MUS_E - D0 + 0.3, D0, 3, gain=-8.0, fin=0.6, fout=0.3, note="La Maritza complète : son temps fort tombe au début de la fête ; elle se lève sous les applaudissements du baiser", role="musique")
def mot(cle, nom, note):
    global rec
    x = P[cle]; dur = x["f"] - x["d"]
    v(nom, x["d"], dur, CO, note=f"[{cle}] {note}"); a(x["fichier"], x["d"], dur, rec - dur, 1, gain=2.0, fin=0.05, fout=0.1, note=f"« {x['texte']} »", role="voix")
mot("panini2", "20260604_C3797", "Sylvain : « c'est moi qui t'emmenais avec ton panini » (le rappel)")
mot("buffet", "20260604_C3787", "« je vous aime, merci pour ce buffet gratuit »")
mot("invitee", "20260604_C3813", "Ornella déguisée en invitée : « les mariés étaient super, surtout la mariée… »")
E_FIN = rec
a(MUS["maritza"], MZ0 + (MUS_E - E0), E_FIN - MUS_E + 0.5, MUS_E, 3, gain=-24.0, fin=0.3, fout=0.5, note="La Maritza baissée sous les petits mots", role="musique_sous")
MARK.append((E0, "E"))

# =============== F. L'orage ===============
F0 = rec
v("FX30.5805", 0.5, 2.6, CO, note="la terrasse déserte sous la pluie")
a(rush("FX30.5805"), 0.5, 2.6, F0, 2, gain=0.0, fin=0.3, fout=0.2, note="pluie (son caméra)", role="salle_seule")
voix("flotte", F0 + 0.5, salle=False, note="rappel de l'officiant (17:36)")
v("20260604_C3864", 2.8, 4.0, CO, vitesse=0.25, note="la dame danse sous la pluie, bras ouverts [ralenti x4, Speed Warp]")
v("20260604_C3864", 8.8, 2.0, CO, note="puis les bras levés, temps réel")
a(rush("20260604_C3864"), 1.0, 6.0, F0 + 3.4, 2, gain=0.0, fin=0.2, fout=0.4, note="pluie, rires (son caméra, décalé)", role="salle_seule")
F_FIN = rec
MARK.append((F0, "F"))

# =============== G. La nuit et le maillot (remix) ===============
G0 = rec; tr = G["youtube_vide"]["temps"]
def rt(i): return G0 + tr[i]
k4 = 0
def rk(nom, src, n, note="", look=CO):
    global k4
    v(nom, src, rt(k4 + n) - rec, look, note=note); k4 += n
rk("FX30.5835", 0.2, 4, "le domaine à l'heure bleue, la salle éclairée (un invité au premier plan)")
rk("20260604_C3954", 17.0, 4, "la salle danse entre les plats, fenêtres bleues du crépuscule")
rk("20260604_C3952", 9.0, 4, "Jonathan et son père dansent ensemble")
rk("20260604_C3953", 0.3, 4, "le père de Jonathan danse (flashs de téléphone gardés)")
rk("20260604_C3957", 46.0, 4, "Jonathan au milieu des amis")
rk("FX30.5838", 31.0, 6, "l'accolade du père et du fils (Quentin ; temps à vérifier en lecture directe)")
G_BAL = rec
a(MUS["remix"], 0.0, G_BAL - G0, G0, 3, gain=-8.0, fin=0.0, fout=0.5, note="remix : le bal (s'éteint avant la voix du maillot)", role="musique")
x = P["ouvrir"]
v("20260604_C4007", x["d"], x["f"] - x["d"], CO, note="« alors tiens, je te laisse l'ouvrir » (synchro ; la V4 de contrôle coupait « ouvrir » : corrigé)")
a(x["fichier"], x["d"], x["f"] - x["d"], rec - (x["f"] - x["d"]), 1, gain=4.0, fin=0.05, fout=0.1, note="« Alors tiens, je te laisse l'ouvrir. »", role="voix")
t_m = rec
v("20260604_C4007", 24.8, 2.2, CO, note="le maillot se déplie")
v("FX30.5871", 6.0, 3.2, CO, note="le visage de Jonathan : il regarde le maillot, sourit (Quentin, serré)")
v("20260604_C4007", 31.0, 2.6, CO, note="Jonathan brandit le maillot devant la salle (Diego, large)")
v("20260604_C4008", 5.9, 2.6, CO, note="la salle exulte, serviette au vent")
v("FX30.5871", 11.2, 3.6, CO, note="Jonathan, bras ouverts, grand sourire, le maillot à la main (Quentin, serré ; flashs de téléphones gardés)")
G_MAIL = rec
a(rush("20260604_C4007"), 16.0, G_MAIL - t_m, t_m, 2, gain=0.0, fin=0.05, fout=0.5, note="cris de la salle (son caméra)", role="salle_seule")
a(MUS["remix"], G_BAL - G0, G_MAIL - G_BAL, G_BAL, 3, gain=-26.0, fin=0.3, fout=0.3, note="remix très bas sous le maillot", role="musique_sous")
G_FIN = rec
MARK.append((G0, "G"))

# =============== H. Dans dix ans : les mariés ===============
H0 = rec
mot("riche", "20260604_C3704", "« Dans dix ans, on se retrouve riche ! »")
mot("dixans1", "20260604_C3798", "« On se revoit dans dix ans, les mariés. »")
dj, fj = 1869.45, 1873.92
a(HF, dj, fj - dj, rec, 1, gain=0.0, fin=0.05, fout=0.3, note="Jonathan : « et je jure, je rigole pas : dans dix ans, on refait la même chose » (HF, après la cérémonie)", role="voix")
v("20260604_C3894", 88.5, 6.0, CO, note="TRICHE (voix de la fin de cérémonie sur le premier slow, 3 h après) : le couple joue contre joue, Jonathan chante")
e = v("20260604_C3894", 96.0, 4.4, CO, note="Ornella la tête sur son épaule : la fin", fondu_noir_fin=1.6)
texte(e["rec"] + 0.6, e["dur"] - 0.6, "Rendez-vous en 2036.", "fin")
a(MUS["remix"], 183.0, rec - H0, H0, 3, gain=-20.0, fin=1.0, fout=2.5, note="fin du remix, très bas, sous les voix", role="musique_sous")
MARK.append((H0, "H"))

# Ralentis x2 natifs (rush 50p lu à 50 % dans la timeline 25p)
RALENTIS = {("20260604_C3529", 1.0): "portrait (ralenti : tremblement de la main lissé)", ("20260604_C3545", 1.0): "chaises (ralenti)",
            ("FX30.5490", 3.0): "bougies (ralenti)", ("20260604_C3546", 9.5): "rose (ralenti)", ("20260604_C3595", 1.0): "regard caméra (ralenti)",
            ("20260604_C3601", 1.0): "rire (ralenti)", ("20260604_C3820", 8.4): "la dame rit (ralenti)",
            ("FX30.5704", 1.0): "guitare (ralenti)", ("FX30.5720", 2.0): "Naël rit (ralenti)",
            ("20260604_C3954", 17.0): "danse du dîner (ralenti : main lissée)", ("20260604_C3952", 9.0): "Jonathan et son père (ralenti)",
            ("20260604_C3953", 0.3): "le père danse (ralenti)", ("20260604_C3957", 46.0): "Jonathan et les amis (ralenti)", ("FX30.5838", 31.0): "l'accolade (ralenti)", ("FX30.5871", 11.2): "Jonathan bras ouverts (ralenti : joie tenue, main lissée)", ("FX30.5472", 0.4): "ils partent en courant", ("20260604_C3540", 3.0): "ils s'éloignent", ("20260604_C3894", 88.5): "le premier slow", ("20260604_C3894", 96.0): "le premier slow"}
for e in V:
    if (e["nom"], e["src"]) in RALENTIS: e["vitesse"] = 0.5; e["note"] += " [ralenti x2 natif]"

# Niveaux : gains calculés sur la loudness mesurée de chaque extrait (cibles en LUFS ; rien d'écouté)
import subprocess
CACHE_L = f"{TW}/son/loudness_cache.json"
LC = json.load(open(CACHE_L)) if os.path.exists(CACHE_L) else {}
def loud(f, s, d):
    kk = f"{f}|{s:.2f}|{d:.2f}"
    if kk not in LC:
        r = subprocess.run(["ffmpeg", "-nostats", "-ss", f"{s:.3f}", "-t", f"{max(d, 0.5):.3f}", "-i", f, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
        try: LC[kk] = float([l for l in r.split("Summary:")[1].splitlines() if "I:" in l][0].split()[1])
        except Exception: LC[kk] = -30.0
        LC[kk] = max(LC[kk], -60.0)
    return LC[kk]
CIBLE = {"voix": -17.0, "salle_seule": -22.0, "salle_sous": -32.0, "musique": -17.0, "musique_sous": -33.0, "lit": -36.0}
for x in A:
    l = loud(x["fichier"], x["src"], min(x["dur"], 60)); x["loudness"] = l; x["gain_brut"] = x["gain"]
    x["gain"] = round(max(-40.0, min(18.0, CIBLE[x["role"]] - l)), 1)
json.dump(LC, open(CACHE_L, "w"))
for x in A:
    if x["note"].startswith("[pelles]"): x["gain"] = round(x["gain"] + 4.0, 1)     # la réplique est couverte par les cris : +4 dB (à vérifier à l'oreille)

# Lit musical sous la parole de la cérémonie : La Maritza sans batterie ni basse, en continu de C0 à la fin de C
a(MUS["maritza_lit"], 30.0, C_FIN - C0 + 0.5, C0, 4, gain=0.0, fin=1.5, fout=0.8, note="La Maritza sans batterie ni basse (demucs), lit sous la cérémonie", role="lit")
x = A[-1]; x["loudness"] = loud(x["fichier"], x["src"], min(x["dur"], 60)); x["gain"] = round(max(-40.0, min(18.0, CIBLE["lit"] - x["loudness"])), 1)

# Stabilisation et exposition plan par plan (fichiers produits par les contrôles de la V4)
def lit(f, defaut):
    return json.load(open(f)) if os.path.exists(f) else defaut
STAB = lit(f"{MD}/stab_V4.json", {}); STAB.update(lit(f"{MD}/stab_V4_b.json", {})); CDL = lit(f"{MD}/cdl_V4.json", {})
for e in V:
    kk = f"{e['nom']}|{e['src']}"
    if kk in STAB and STAB[kk].get("garder"): e["stab"] = STAB[kk]
    if kk in CDL: e["cdl"] = CDL[kk]

json.dump(dict(video=V, audio=A, textes=T, blocs=MARK, duree=round(rec, 3), triches=TRICHES), open(f"{MD}/montage_V4.json", "w"), indent=1, ensure_ascii=False)
print("durée", round(rec, 2), "plans", len(V), "sons", len(A), "textes", len(T), "blocs", [(b, round(t, 1)) for t, b in MARK])
