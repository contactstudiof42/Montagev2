# higgsfield_projets.py DOSSIER_SORTIE NOM=ID_DOSSIER [NOM=ID_DOSSIER ...] : télécharge les générations publiques
# d'un projet Higgsfield (snapshot_folder_id lu sur la page du projet ou dans la liste d'un concours), en ne gardant
# que le modèle, le type de sortie, les réglages et le prompt ; puis imprime les modèles et les réglages de Seedance 2.5.
# Passe par curl (le Python système n'a pas les certificats). Plafond : 12 pages de 50 générations par projet.
import sys, json, os, subprocess, time, collections, statistics
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
API = "https://fnf-api-gw.higgsfield.ai/fnf/folders/{}/items/v2?ordering=asc&include_subfolders=true&size=50"
for arg in sys.argv[2:]:
    nom, fid = arg.split("=", 1); items = []; cur = None
    for page in range(12):
        url = API.format(fid) + (f"&cursor={cur}" if cur else "")
        r = subprocess.run(["curl", "-s", "-A", "Mozilla/5.0", url], capture_output=True, timeout=90)
        try: j = json.loads(r.stdout)
        except ValueError: print(nom, "réponse illisible"); break
        for it in j.get("items", []):
            jb = it.get("job") or {}
            items.append({"type": jb.get("job_set_type"), "kind": ((jb.get("results") or {}).get("raw") or {}).get("type"),
                          "params": jb.get("params"), "created": jb.get("created_at")})
        cur = j.get("cursor")
        if not cur or not j.get("items"): break
        time.sleep(0.3)
    json.dump(items, open(os.path.join(out, nom + ".json"), "w"))
    vid = [x for x in items if x["type"] == "seedance_2_5" and x["params"]]
    lon = [len(x["params"].get("prompt") or "") for x in vid]
    print(f"{nom}: {len(items)} générations, {len(vid)} Seedance 2.5, prompt médian {int(statistics.median(lon)) if lon else 0} car.",
          "|", ", ".join(f"{k}:{v}" for k, v in collections.Counter(x['type'] for x in items).most_common(4)))
    for cle in ("duration", "resolution", "aspect_ratio"):
        print("   ", cle, collections.Counter(str(x["params"].get(cle)) for x in vid).most_common(5))
