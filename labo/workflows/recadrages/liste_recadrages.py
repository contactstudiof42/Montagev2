"""Parade (session 11) : extrait d'un XML FCP7 (Premiere / Resolve / FCP7) la liste des recadrages, nests et niveaux audio
en CSV, à joindre à l'envoi avec la vidéo de référence. Usage : python3 liste_recadrages.py fichier.xml > recadrages.csv"""
import sys, csv, xml.etree.ElementTree as ET
racine = ET.parse(sys.argv[1]).getroot(); seq = racine.find(".//sequence")
fichiers = {f.get("id"): f.findtext("name") for f in racine.iter("file") if f.findtext("name")}
tb = int(seq.findtext("rate/timebase")); tc0 = int(seq.findtext("timecode/frame") or 0)
def tc(n):
    n += tc0; return f"{n // (3600 * tb):02d}:{n // (60 * tb) % 60:02d}:{n // tb % 60:02d}:{n % tb:02d}"
w = csv.writer(sys.stdout); w.writerow(["piste", "tc_entree", "tc_sortie", "plan", "fichier", "canal_source", "nest", "effet", "parametre", "valeur"])
for k in ("video", "audio"):
    for i, tr in enumerate(seq.findall(f"media/{k}/track"), 1):
        for ci in tr.findall("clipitem"):
            base = [f"{k[0].upper()}{i}", tc(max(int(ci.findtext("start")), 0)), tc(int(ci.findtext("end"))), ci.findtext("name"),
                    fichiers.get(ci.find("file").get("id"), "") if ci.find("file") is not None else "", ci.findtext("sourcetrack/trackindex") or "",
                    "oui" if ci.find("sequence") is not None else ""]
            fx = [(fe, pa) for fe in ci.findall("filter/effect") for pa in fe.findall("parameter")]
            if not fx: w.writerow(base + ["", "", ""])
            for fe, pa in fx:
                v = pa.find("value"); kf = pa.findall("keyframe")
                val = " ".join(f"i{x.findtext('when')}={x.findtext('value')}" for x in kf) if kf else (
                      f"{v.findtext('horiz')},{v.findtext('vert')}" if v is not None and len(v) else (v.text if v is not None else ""))
                w.writerow(base + [fe.findtext("name"), pa.findtext("parameterid"), val])
