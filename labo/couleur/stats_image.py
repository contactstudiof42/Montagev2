# stats_image.py IMG... : luma p2/p50/p98, part >= 250, chroma moyen OkLCh, teinte dominante des tons moyens
import sys, numpy as np
from PIL import Image
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/couleur"); from oklab import vers_lch
for f in sys.argv[1:]:
    im = np.asarray(Image.open(f).convert("RGB")).astype(np.float64) / 255
    y = (im @ [0.2126, 0.7152, 0.0722]) * 255; L, C, h = vers_lch(im)
    m = (L > 0.35) & (L < 0.7); a = (C[m] * np.cos(np.radians(h[m]))).mean(); b = (C[m] * np.sin(np.radians(h[m]))).mean()
    print(f"{f.split('/')[-1][:40]:40s} p2 {np.percentile(y,2):5.0f} p50 {np.percentile(y,50):5.0f} p98 {np.percentile(y,98):5.0f} brule {np.mean(y>=250)*100:4.1f}% chroma {C.mean():.3f} moyens {np.degrees(np.arctan2(b,a))%360:4.0f}° {np.hypot(a,b):.3f}")
