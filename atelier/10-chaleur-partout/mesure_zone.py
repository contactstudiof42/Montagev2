"""v4 : mesure dans la zone de l'événement (pixels changés par l'écran, par différence avec la version éteinte)
+ simulation d'une clé secondaire (pousser le bleu dans la zone seulement). Usage : python3 mesure_zone.py"""
import json
import numpy as np
from PIL import Image, ImageDraw
R = "/home/user/Montagev2/atelier/rendus/10"
lit = lambda v: np.asarray(Image.open(f"{R}/{v}/0001.png").convert("RGB")) / 255
paires = {"C6": "B4", "C7": "B4", "C9": "B4", "C8": "B8", "C10": "B10", "C11": "B11", "C12": "B4", "C13": "B13", "C14": "B4", "C15": "B4", "C16": "B4"}
m, ims = {}, []
for c, b in paires.items():
    A, B = lit(c), lit(b); Y = lambda x: x @ [.2126, .7152, .0722]
    z = (Y(A) - Y(B)) > 0.03  # la zone que l'événement éclaire
    zc = A[z].mean(0) if z.any() else np.zeros(3)
    m[c] = dict(zone_px=round(float(z.mean()), 4), zone_RGB=[round(float(x), 3) for x in zc],
                zone_B_moins_R=round(float(zc[2] - zc[0]), 3), zone_Y=round(float(Y(zc)), 3),
                saillance=round(float(Y(zc) / Y(A).mean()), 2), froids=round(float((A[..., 2] > A[..., 0] + .08).mean()), 4),
                chauds=round(float((A[..., 0] > A[..., 2] + .08).mean()), 3))
    ims.append((c, A))
# clé secondaire sur C6 : dans la zone (adoucie), gain bleu +, rouge - (comme une roue de couleur sur un qualifier)
A, B = lit("C6"), lit("B4"); d = np.clip(((A - B) @ [.2126, .7152, .0722]) / 0.08, 0, 1)[..., None]
G = np.clip(A * (1 + d * np.array([-0.18, -0.03, 0.15])), 0, 1)
zc = G[(d[..., 0] > 0.37)].mean(0)
m["C6+cle"] = dict(zone_RGB=[round(float(x), 3) for x in zc], zone_B_moins_R=round(float(zc[2] - zc[0]), 3),
                   froids=round(float((G[..., 2] > G[..., 0] + .08).mean()), 4))
ims.append(("C6+cle", G)); Image.fromarray((G * 255).astype(np.uint8)).save(f"{R}/C6cle.png")
out = Image.new("RGB", (480 * 4, 290 * 3))
for i, (n, a) in enumerate([("B4", lit("B4"))] + ims):
    x, y = 480 * (i % 4), 290 * (i // 4); out.paste(Image.fromarray((a * 255).astype(np.uint8)), (x, y))
    ImageDraw.Draw(out).text((x + 6, y + 274), f"{n} {m.get(n, {}).get('zone_RGB', 'eteint')}", fill=(255, 255, 255))
out.quantize(256).save("planche-v4-toutes.png", optimize=True); json.dump(m, open("mesures-v4.json", "w"), indent=1); print(json.dumps(m, indent=1))
