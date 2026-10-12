import sys, time, numpy as np
from PIL import Image
from rembg import new_session, remove
s = new_session(sys.argv[1], providers=["CPUExecutionProvider"])
for f in sys.argv[2:]:
    im = Image.open(f).convert("RGB"); t = time.time()
    m = remove(im, session=s, only_mask=True); print(f, round(time.time() - t, 2), "s")
    m.save(f.replace(".png", f"_{sys.argv[1]}_mask.png"))
