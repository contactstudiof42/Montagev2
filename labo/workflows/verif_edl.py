"""Vérificateur d'EDL CMX 3600 (session 10, BACKLOG 58). Usage : python3 verif_edl.py fichier.edl cadence [tc_depart_attendu]
Contrôles : (1) cohérence durée source / durée enregistrement / vitesse M2 (source = record × vitesse) ;
(2) timecode d'enregistrement du 1er événement contre le départ attendu (défaut 01:00:00:00) ;
(3) lignes M2 sans événement correspondant (nom de bobine / clip) ; (4) trous et chevauchements en enregistrement."""
import sys, re
f, fps = sys.argv[1], int(sys.argv[2]); depart = sys.argv[3] if len(sys.argv) > 3 else "01:00:00:00"
def tc(s):
    h, m, se, fr = map(int, re.split("[:;]", s)); return ((h * 60 + m) * 60 + se) * fps + fr
ev, m2, alertes = [], {}, []
for l in open(f, encoding="utf-8", errors="replace"):
    p = l.split()
    if len(p) >= 8 and p[0].isdigit():
        tcs = [x for x in p if re.fullmatch(r"\d\d:\d\d:\d\d[:;]\d\d", x)]
        if len(tcs) == 4:
            ev.append({"n": p[0], "bobine": p[1], "trans": p[3], "si": tc(tcs[0]), "so": tc(tcs[1]), "ri": tc(tcs[2]), "ro": tc(tcs[3]), "nom": None})
    elif p and p[0] == "M2":
        m2.setdefault(p[1], []).append(float(p[2]))
    elif "FROM CLIP NAME:" in l or "TO CLIP NAME:" in l:
        if ev: ev[-1]["nom"] = l.split(":", 1)[1].strip().replace(" FF", "")
if ev and ev[0]["ri"] != tc(depart):
    alertes.append(f"départ : 1er événement enregistré à {ev[0]['ri']} images, attendu {depart} ({tc(depart)} images)")
for e in ev:
    nom = e["nom"] or e["bobine"]; rd = e["ro"] - e["ri"]; sd = e["so"] - e["si"]
    v = m2.get(nom, [None])[0]
    if rd == 0: continue
    vit = 1.0 if v is None else v / fps
    attendu = rd * abs(vit)
    if v is not None and v == 0: attendu = 1 if sd else 0  # arrêt sur image : 1 image source (ou 0)
    if abs(abs(sd) - attendu) > 1:
        alertes.append(f"év. {e['n']} {nom} : source {sd} images pour {rd} enregistrées à vitesse {vit:g} → attendu {attendu:g}")
for a, b in zip(ev, ev[1:]):
    if b["ri"] != a["ro"] and b["ro"] - b["ri"] > 0 and a["ro"] - a["ri"] > 0:
        alertes.append(f"enregistrement : {'trou' if b['ri'] > a['ro'] else 'chevauchement'} entre év. {a['n']} et {b['n']} ({b['ri'] - a['ro']} images)")
noms = {e["nom"] for e in ev} | {e["bobine"] for e in ev}
for k in m2:
    if k not in noms: alertes.append(f"M2 « {k} » sans événement correspondant")
print(f"{len(ev)} événements, {sum(len(v) for v in m2.values())} lignes M2")
print("\n".join("ALERTE " + a for a in alertes) if alertes else "aucune alerte")
