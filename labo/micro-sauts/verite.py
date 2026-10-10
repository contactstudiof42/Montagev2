"""Vérité terrain synthétique : une image source, des « après » fabriqués (punch-in s, décalage dx % largeur, bruit), et un plan différent."""
import sys, numpy as np
from PIL import Image
sys.path.insert(0, '.'); from micro_sauts import mesurer
src = Image.open(sys.argv[1]).convert('RGB'); autre = Image.open(sys.argv[2]).convert('RGB'); W, H = src.size; rng = np.random.default_rng(1)
S0 = 1.15                                                  # marge : « avant » est déjà un recadrage centré à 1,15
def fabrique(s, dx):
    s = s * S0; cw, ch = W / s, H / s; x0 = (W - cw) / 2 - dx / 100 * W / s; y0 = (H - ch) / 2
    im = src.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch)); a = np.asarray(im, np.float64) + rng.normal(0, 4, (H, W, 3))
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
avant = fabrique(1.0, 0.0); print('vrai(s, dx%) -> mesuré')
for s, dx in [(1.0, 0.0), (1.0, 0.5), (1.0, 1.5), (1.0, 3.0), (1.1, 0.0), (1.2, 1.0), (1.35, -2.0), (1.0, -0.3), (2.4, 0.0), (2.9, 1.0)]:
    print((s, dx), mesurer(avant, fabrique(s, dx)))
print('plan différent ->', mesurer(avant, autre))
