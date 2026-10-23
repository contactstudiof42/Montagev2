# oxen_video.py : génère un plan de « L'Air » sur Oxen (Seedance 2.5 ou Omni Flash), à partir d'un prompt de prompts-video.md.
# .venv/bin/python -I oxen_video.py ID MODELE SORTIE.mp4 [--first IMG] [--face IMG ...] [--img IMG ...] [--video MP4 ...]
#   [--duree 6] [--res 720p] [--aspect 16:9]
# MODELE : seedance (bytedance-seedance-2-5-reference-to-video) ou omni (gemini-omni-1-1-flash).
# Seedance : --face → input_face_images (numérotées d'abord), --img → input_images, --face-video → input_face_videos (numérotées d'abord), --video → input_videos.
# Omni : --first → input_image (première image), --img → input_images (3 au plus).
# Médias envoyés en data URI. Clé et journal comme oxen_image.py.
import argparse, base64, csv, datetime, json, mimetypes, os, re, subprocess, sys, urllib.request
ICI = os.path.dirname(os.path.abspath(__file__))
MODELES = {"seedance": "bytedance-seedance-2-5-reference-to-video", "omni": "gemini-omni-1-1-flash"}
PRIX = {("seedance", "480p"): 0.117, ("seedance", "720p"): 0.263, ("seedance", "1080p"): 0.647,
        ("omni", "360p"): 0.039, ("omni", "720p"): 0.13, ("omni", "1080p"): 0.195}   # $/s, API Oxen, 2026-10-24
p = argparse.ArgumentParser()
p.add_argument("id"); p.add_argument("modele", choices=MODELES); p.add_argument("sortie")
p.add_argument("--first"); p.add_argument("--face", action="append", default=[]); p.add_argument("--img", action="append", default=[])
p.add_argument("--video", action="append", default=[]); p.add_argument("--face-video", action="append", default=[]); p.add_argument("--duree", type=int, default=6)
p.add_argument("--res", default="720p"); p.add_argument("--aspect", default="16:9")
a = p.parse_args()
md = open(os.path.join(ICI, "prompts-video.md"), encoding="utf-8").read()
bloc = re.search(rf"^### {re.escape(a.id)} .*?$(.*?)(?=^##|\Z)", md, re.S | re.M)
if not bloc: sys.exit(f"prompt {a.id} introuvable")
prompt = " ".join(l[2:].strip() for l in bloc.group(1).splitlines() if l.startswith("> "))
FICHIER_CLE = os.path.expanduser("~/.config/oxen/api_key")
cle = os.environ.get("OXEN_API_KEY") or (open(FICHIER_CLE).read().strip() if os.path.exists(FICHIER_CLE) else "")
for n in (3, 2):
    if cle and len(cle) % n == 0 and cle[:len(cle) // n] * n == cle: cle = cle[:len(cle) // n]; break
if not cle: sys.exit("clé Oxen absente")
def uri(f): return f"data:{mimetypes.guess_type(f)[0] or 'application/octet-stream'};base64," + base64.b64encode(open(f, 'rb').read()).decode()
corps = {"model": MODELES[a.modele], "prompt": prompt, "duration": a.duree, "resolution": a.res, "aspect_ratio": a.aspect, "response_format": "url"}
if a.modele == "seedance":
    if a.face: corps["input_face_images"] = [uri(f) for f in a.face]
    if a.img: corps["input_images"] = [uri(f) for f in a.img]
    if a.face_video: corps["input_face_videos"] = [uri(f) for f in a.face_video]
    if a.video: corps["input_videos"] = [uri(f) for f in a.video]
    corps["generate_audio"] = True
else:
    if a.first: corps["input_image"] = uri(a.first)
    if a.img: corps["input_images"] = [uri(f) for f in a.img[:3]]
req = urllib.request.Request("https://hub.oxen.ai/api/ai/videos/generate", data=json.dumps(corps).encode(),
                             headers={"Content-Type": "application/json", "Authorization": "Bearer " + cle})
debut = datetime.datetime.now()
try:
    rep = json.load(urllib.request.urlopen(req, timeout=1500))
except urllib.error.HTTPError as e:
    sys.exit(f"erreur HTTP {e.code} : {e.read().decode()[:800]}")
v = rep["videos"][0]
os.makedirs(os.path.dirname(os.path.abspath(a.sortie)), exist_ok=True)
data = base64.b64decode(v["b64_json"]) if v.get("b64_json") else urllib.request.urlopen(v["url"], timeout=600).read()
open(a.sortie, "wb").write(data)
duree = (datetime.datetime.now() - debut).seconds
prix = round(PRIX.get((a.modele, a.res), 0) * a.duree, 3)
json.dump({"id": a.id, "prompt": prompt, "first": a.first, "face": a.face, "img": a.img, "video": a.video, "face_video": a.face_video,
           **{k: v2 for k, v2 in corps.items() if k.startswith(("model", "duration", "resolution", "aspect", "generate"))}},
          open(os.path.splitext(a.sortie)[0] + ".json", "w"), ensure_ascii=False, indent=1)
j = os.path.join(ICI, "journal-oxen.csv")
with open(j, "a", newline="") as f:
    csv.writer(f).writerow([debut.isoformat(timespec="seconds"), a.id, MODELES[a.modele], f"{a.duree}s", a.res, prix, duree, os.path.basename(a.sortie)])
print("OK", a.sortie, f"{duree} s", prix, "$")
