# doublons_timeline.py — à coller tel quel dans l'outil MCP `run_script` de Resolve (bac à sable, sans accès disque).
# Règle de Diego (2026-10-11) : dans un after movie, un événementiel, un run and gun ou un montage dynamique, on ne
# montre JAMAIS deux fois le même moment d'un même rush (un rush peut donner plusieurs plans, à des moments différents).
# Exception seulement si un ressort de récit le justifie (flashback, rappel voulu…) : à écrire dans plan.md.
# Liste chaque plan vidéo (rush, entrée et sortie en secondes du rush) et signale tout chevauchement entre deux plans
# du même rush. À lancer AVANT CHAQUE RENDU. Variables à régler : TIMELINE (None = timeline courante), PISTES, TOL.
TIMELINE = None          # nom de la timeline, ou None
PISTES = None            # liste de pistes vidéo à contrôler, ou None = toutes
TOL = 0.04               # tolérance en secondes (2 images à 50 i/s) : un contact bord à bord n'est pas un doublon
IGNORER = ("blanc", "grain", "noir", "sony_white", "Fusion", "Text", "collage")   # flashs, grain, titres, plan de fin, éléments calculés
# Fichiers rendus par Gyroflow sur une PLAGE (trim) : ils gardent le timecode de début du rush, il faut ajouter le début de la plage (s)
DECALAGES = {"C6723_stabilized_s13": 12.5, "C6723_stabilized_s29": 27.5, "C6723_stabilized_sync": 12.0,
             "C6507_stabilized_sync": 24.0, "C6507_stabilized": 24.0,
             # V5 (gyro_rendu.py) : début de plage lu dans *_preuve.json
             "C6507_gf_s24": 24.0, "C6507_gf_s38": 38.5, "C6723_gf_s12": 12.5, "C6723_gf_s27": 27.5, "C6725_gf_s0": 0.0}
# Plans calculés hors de Resolve (pic, collages) : leurs sources, en secondes depuis le DÉBUT DU FICHIER rush
# (coller le contenu de *_sources.json). Convertis avec le timecode de départ du rush lu dans le pool de médias.
# Un gel du dernier instant du plan précédent (collages) n'est pas un doublon : ne pas le lister.
EXTRA = []               # ex. [{"rush": "C6632", "debut": 2.0, "fin": 2.72, "plan": [831, 849]}, ...]

pr = resolve.GetProjectManager().GetCurrentProject()
tl = pr.GetCurrentTimeline()
if TIMELINE:
    for i in range(1, pr.GetTimelineCount() + 1):
        if pr.GetTimelineByIndex(i).GetName() == TIMELINE:
            tl = pr.GetTimelineByIndex(i)
t0 = tl.GetStartFrame()
plans = []
for tr in (PISTES or range(1, tl.GetTrackCount("video") + 1)):
    for it in tl.GetItemListInTrack("video", tr) or []:
        n = it.GetName()
        if any(k.lower() in n.lower() for k in IGNORER) or it.GetMediaPoolItem() is None:
            continue
        s, e = it.GetSourceStartTime(), it.GetSourceEndTime()
        dec = next((v for k, v in DECALAGES.items() if k in n), 0.0); s, e = s + dec, e + dec
        plans.append(dict(piste=tr, debut=it.GetStart() - t0, fin=it.GetEnd() - t0, rush=n,
                          src_in=round(s, 3), src_out=round(e, 3), arret=(e - s) < 0.05))
def tc_secondes(tc, fps):
    h, m, sec, f = [int(x) for x in tc.replace(";", ":").split(":")]
    return h * 3600 + m * 60 + sec + f / fps


tc0 = {}
def depart(rid):
    """timecode de départ (s) du rush `rid` (ex. C6632), cherché dans le pool de médias."""
    if rid in tc0: return tc0[rid]
    pile = [pr.GetMediaPool().GetRootFolder()]
    while pile:
        d = pile.pop()
        pile += d.GetSubFolderList() or []
        for c in d.GetClipList() or []:
            n = c.GetName()
            if rid in n and "stab" not in n and "_gf" not in n:
                tc0[rid] = tc_secondes(c.GetClipProperty("Start TC"), float(c.GetClipProperty("FPS")))
                return tc0[rid]
    tc0[rid] = None
    return None


for x in EXTRA:
    d0 = depart(x["rush"])
    if d0 is None:
        continue
    plans.append(dict(piste="calc", debut=x.get("plan", [None])[0], fin=x.get("plan", [None, None])[1],
                      rush="20260929_" + x["rush"] + ".calc", src_in=round(d0 + x["debut"], 3),
                      src_out=round(d0 + x["fin"], 3), arret=(x["fin"] - x["debut"]) < 0.05))
par_rush = {}
for p in plans:
    # clé = identifiant du rush (C6723) : les rendus Gyroflow, stabilisés et calculés se comparent au rush d'origine
    n = p["rush"]; i = n.find("_C6")
    par_rush.setdefault(n[i + 1:i + 6] if i >= 0 else n.split(".")[0], []).append(p)
doublons = []
for r, L in par_rush.items():
    L.sort(key=lambda p: p["src_in"])
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            a, b = L[i], L[j]
            # un arrêt sur image a une durée source presque nulle : on l'élargit à ±1 image pour le comparer
            ai, ao = (a["src_in"] - .02, a["src_out"] + .02) if a["arret"] else (a["src_in"], a["src_out"])
            bi, bo = (b["src_in"] - .02, b["src_out"] + .02) if b["arret"] else (b["src_in"], b["src_out"])
            ch = min(ao, bo) - max(ai, bi)
            if ch > TOL:
                doublons.append(dict(rush=r, plan_a=[a["debut"], a["fin"]], plan_b=[b["debut"], b["fin"]],
                                     source_a=[a["src_in"], a["src_out"]], source_b=[b["src_in"], b["src_out"]],
                                     chevauchement_s=round(ch, 3), arret_sur_image=a["arret"] or b["arret"]))
result = dict(timeline=tl.GetName(), plans=len(plans), rushes=len(par_rush), doublons=len(doublons),
              liste=sorted(doublons, key=lambda d: d["plan_b"][0] or 0))
