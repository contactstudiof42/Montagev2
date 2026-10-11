# planche_look4.py SORTIE.jpg '{"param": valeur}' : les 8 images témoins avec le look V4 (réglages modifiés en JSON),
# rangée du dessus = look V3 (D2) pour comparer ; + mesures OkLCh des points témoins de C6577.
import sys, json, numpy as np
sys.path.insert(0, "labo/couleur")
from look_sony import look
from look_sony_v4 import look4, PARAMS
from oklab import vers_lch
from PIL import Image
W = "videos/phase-3/sony-linkbuds/_travail/look4/"
R = ["C6577","C6561","C6628","C6576","C6608","C6657","C6725","C6495"]
p = dict(PARAMS); p.update(json.loads(sys.argv[2]) if len(sys.argv) > 2 else {})
rows = []
for fn in (lambda x: look(x, expo=0.25, force=1.0, sat=1.3, pied=0.08, ombres=0.8), lambda x: look4(x, p)):
    tiles = [Image.fromarray((fn(np.load(W+f"s_{r}.npy").astype(float))*255+.5).astype(np.uint8)).resize((270,480)) for r in R]
    row = Image.new("RGB",(270*len(R),480)); [row.paste(t,(i*270,0)) for i,t in enumerate(tiles)]; rows.append(row)
im = Image.new("RGB",(270*len(R),960)); im.paste(rows[0],(0,0)); im.paste(rows[1],(0,480)); im.save(sys.argv[1], quality=92)
y = look4(np.load(W+"s_C6577.npy").astype(float), p); L,C,h = vers_lch(y)
for nom,(x,yy) in {"joue":(205,440),"chouchou":(25,445),"flou":(330,480),"ecouteur":(118,410)}.items():
    s_=(slice(yy-5,yy+5),slice(x-5,x+5)); print(f"{nom:9s} L={L[s_].mean():.2f} C={C[s_].mean():.3f} h={np.median(h[s_]):.0f}")
