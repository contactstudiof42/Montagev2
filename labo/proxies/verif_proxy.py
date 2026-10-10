"""Vérifie qu'un proxy est rattachable à son original (critères Premiere « Attach Proxies » / Resolve « proxy media »,
d'après la doc Adobe [THÉORIQUE pour le comportement des logiciels]) : même cadence, même nombre d'images, mêmes canaux audio,
même rapport d'image, même timecode de départ. Usage : python3 verif_proxy.py original proxy [proxy...]"""
import json, subprocess, sys
from fractions import Fraction
def info(f):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-show_streams", "-show_format", "-of", "json", f],
                                  capture_output=True, text=True).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video"); a = [s for s in j["streams"] if s["codec_type"] == "audio"]
    tc = v.get("tags", {}).get("timecode") or j["format"].get("tags", {}).get("timecode") or next(
        (s.get("tags", {}).get("timecode") for s in j["streams"] if s.get("tags", {}).get("timecode")), None)
    return dict(codec=v["codec_name"], taille=f'{v["width"]}x{v["height"]}', cadence=v["r_frame_rate"], images=int(v["nb_read_packets"]),
                rapport=str(Fraction(v["width"], v["height"])), pistes_audio=len(a), canaux=[s["channels"] for s in a], timecode=tc,
                Mo=round(int(j["format"]["size"]) / 1e6, 2))
o = info(sys.argv[1]); print("ORIGINAL", json.dumps(o))
for p in sys.argv[2:]:
    i = info(p); ecarts = [k for k in ("cadence", "images", "rapport", "pistes_audio", "canaux", "timecode") if i[k] != o[k]]
    print("PROXY", p.split("/")[-1], json.dumps(i), "→", "OK" if not ecarts else "ÉCART : " + ", ".join(ecarts))
