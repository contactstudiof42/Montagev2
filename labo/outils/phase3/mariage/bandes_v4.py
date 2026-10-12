# bandes_v4.py montage_V4.json SORTIE_DIR : pour chaque plan au tremblement signalé (moyenne > 2 px ou pic > 6 px avant stabilisation),
# une bande de 12 images consécutives (centre 40 %) + superposition de 5 images, sur le fichier RETENU (stabilisé si gardé, sinon brut),
# au milieu du passage utilisé ; mosaïque de toutes les bandes, étiquetées (temps du film, rush, mesure avant/après, fichier lu).
import sys, json, os, subprocess
from PIL import Image, ImageDraw, ImageFont
J = json.load(open(sys.argv[1])); O = sys.argv[2]; os.makedirs(O, exist_ok=True); MD = os.path.dirname(os.path.abspath(sys.argv[1]))
S = json.load(open(f"{MD}/stab_V4.json")); S.update(json.load(open(f"{MD}/stab_V4_b.json")) if os.path.exists(f"{MD}/stab_V4_b.json") else {})
INV = {x["nom"]: x for x in json.load(open("/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/inventaire.json"))}
PY = "/Volumes/SSD FAST/Montage-IA/.venv/bin/python"; L = "/Volumes/SSD FAST/Montage-IA/labo/outils/tremblement.py"
font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18); lignes = []
for e in sorted([e for e in J["video"] if e["piste"] == 1 and not e.get("gel")], key=lambda e: e["rec"]):
    r = S.get(f"{e['nom']}|{e['src']}")
    if not r: continue
    av = r["avant"]; m, p = av.get("moyenne", 0), av.get("pic", 0)
    if m <= 2 and p <= 6: continue
    d = e["dur"] * e["vitesse"]
    if r.get("garder"): f, t0 = r["fichier"], e["src"] - r["debut_plage"]; quoi = "GYROFLOW"
    else: f, t0 = f"/Volumes/SSD FAST/MARIAGE JO/RUSH/{INV[e['nom']]['fichier']}", e["src"]; quoi = "brut"
    png = f"{O}/b_{e['rec']:07.2f}.png"
    subprocess.run([PY, "-I", L, f, f"{t0:.2f}", f"{t0 + d:.2f}", "--bande", png], capture_output=True)
    ap = r.get("apres", {})
    lab = f"{int(e['rec'] // 60)}:{e['rec'] % 60:04.1f}  {e['nom'][-10:]}  avant {m:.1f}/{p:.1f}" + (f"  après {ap.get('moyenne', 0):.1f}/{ap.get('pic', 0):.1f}" if ap else "") + f"  → {quoi}" + (f"  ralenti x{1/e['vitesse']:.0f}" if e["vitesse"] != 1 else "")
    if os.path.exists(png): lignes.append((png, lab))
H = 90 + 26
for k in range(0, len(lignes), 12):
    page = lignes[k:k + 12]; im = Image.new("RGB", (2080, len(page) * H), (20, 20, 20)); dr = ImageDraw.Draw(im)
    for j, (png, lab) in enumerate(page):
        b = Image.open(png).convert("RGB"); im.paste(b, (0, j * H + 24)); dr.text((4, j * H + 2), lab, fill=(255, 220, 80), font=font)
    im.save(f"{O}/bandes_{k // 12 + 1}.jpg", quality=85); print(f"{O}/bandes_{k // 12 + 1}.jpg", len(page))
