# oxen_image.py : génère une image de « L'Air » avec GPT Image 2.5 Sunburst sur Oxen, à partir d'un prompt de prompts-gpt.md.
# .venv/bin/python -I oxen_image.py ID SORTIE.png [--ref IMAGE.png ...] [--aspect 3:2] [--res 2K] [--quality high]
# ID = titre de section de prompts-gpt.md (F1, F2…) ; les références deviennent @Image1, @Image2… dans l'ordre donné.
# La clé est lue dans launchctl (OXEN_API_KEY), jamais affichée. Chaque appel est noté dans journal-oxen.csv (budget).
import argparse, base64, csv, datetime, json, os, re, subprocess, sys, urllib.request
ICI = os.path.dirname(os.path.abspath(__file__))
PRIX = {("high", "1K"): 0.0369, ("high", "2K"): 0.0517, ("xhigh", "2K"): 0.0919, ("medium", "2K"): 0.0134}  # catalogue Oxen, 2026-10-24
p = argparse.ArgumentParser()
p.add_argument("id"); p.add_argument("sortie"); p.add_argument("--ref", action="append", default=[])
p.add_argument("--aspect", default="3:2"); p.add_argument("--res", default="2K"); p.add_argument("--quality", default="high")
a = p.parse_args()
md = open(os.path.join(ICI, "prompts-gpt.md"), encoding="utf-8").read()
bloc = re.search(rf"^### {re.escape(a.id)} .*?$(.*?)(?=^##)", md, re.S | re.M)
if not bloc: sys.exit(f"prompt {a.id} introuvable")
prompt = " ".join(l[2:].strip() for l in bloc.group(1).splitlines() if l.startswith("> "))
if "[" in prompt: sys.exit("le prompt contient encore un renvoi entre crochets")
cle = os.environ.get("OXEN_API_KEY") or subprocess.run(["launchctl", "getenv", "OXEN_API_KEY"], capture_output=True, text=True).stdout.strip()
if not cle: sys.exit("OXEN_API_KEY absente")
corps = {"model": "gpt-image-2-5-sunburst", "prompt": prompt, "aspect_ratio": a.aspect, "resolution": a.res,
         "quality": a.quality, "output_format": "png", "background": "opaque", "moderation": "low", "response_format": "b64_json"}
if a.ref:
    corps["input_image"] = ["data:image/png;base64," + base64.b64encode(open(f, "rb").read()).decode() for f in a.ref]
req = urllib.request.Request("https://hub.oxen.ai/api/ai/images/edit", data=json.dumps(corps).encode(),
                             headers={"Content-Type": "application/json", "Authorization": "Bearer " + cle})
debut = datetime.datetime.now()
try:
    rep = json.load(urllib.request.urlopen(req, timeout=900))
except urllib.error.HTTPError as e:
    sys.exit(f"erreur HTTP {e.code} : {e.read().decode()[:500]}")
img = rep["images"][0]
os.makedirs(os.path.dirname(os.path.abspath(a.sortie)), exist_ok=True)
if img.get("b64_json"): data = base64.b64decode(img["b64_json"])
else: data = urllib.request.urlopen(img["url"], timeout=300).read()
open(a.sortie, "wb").write(data)
duree = (datetime.datetime.now() - debut).seconds
json.dump({"id": a.id, "prompt": prompt, "refs": a.ref, **{k: v for k, v in corps.items() if k not in ("prompt", "input_image")}},
          open(os.path.splitext(a.sortie)[0] + ".json", "w"), ensure_ascii=False, indent=1)
j = os.path.join(ICI, "journal-oxen.csv"); neuf = not os.path.exists(j)
with open(j, "a", newline="") as f:
    w = csv.writer(f)
    if neuf: w.writerow(["date", "id", "modele", "qualite", "resolution", "prix_estime_usd", "duree_s", "fichier"])
    w.writerow([debut.isoformat(timespec="seconds"), a.id, "gpt-image-2-5-sunburst", a.quality, a.res, PRIX.get((a.quality, a.res), ""), duree, os.path.basename(a.sortie)])
print("OK", a.sortie, f"{duree} s", PRIX.get((a.quality, a.res), "?"), "$")
