"""Inventaire d'un dossier de rushes (lecture seule) : ffprobe + XML caméra -> CSV.
Usage : inventaire.py DOSSIER_RUSH sortie.csv
"""
import csv, json, subprocess, sys, re
from pathlib import Path
src, out = Path(sys.argv[1]), sys.argv[2]
rows = []
for f in sorted(src.glob("*.MP4")):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(f)],
                                  capture_output=True, text=True).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    a = [s for s in j["streams"] if s["codec_type"] == "audio"]
    tc = j["format"].get("tags", {}).get("timecode") or v.get("tags", {}).get("timecode", "")
    created = j["format"].get("tags", {}).get("creation_time", "")
    x = f.with_name(f.stem + "M01.XML")
    meta = x.read_text(errors="ignore") if x.exists() else ""
    def m(p):
        r = re.search(p, meta); return r.group(1) if r else ""
    rows.append(dict(fichier=f.name, duree=round(float(j["format"]["duration"]), 2), fps=v.get("r_frame_rate"),
                     taille=f"{v['width']}x{v['height']}", codec=v["codec_name"], pix=v.get("pix_fmt"),
                     transfer=v.get("color_transfer", ""), audio=f"{len(a)}x{a[0]['channels']}ch" if a else "",
                     timecode=tc, creation=created,
                     gamma=m(r'name="CaptureGammaEquation" value="([^"]+)"'), capture_fps=m(r'captureFps="([^"]+)"'),
                     lentille=m(r'<Lens modelName="([^"]+)"'), heure=m(r'<CreationDate value="([^"]+)"')))
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), "rushes,", round(sum(r["duree"] for r in rows) / 60, 1), "min")
