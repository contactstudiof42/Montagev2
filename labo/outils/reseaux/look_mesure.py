# look_mesure.py VIDEO crop(w:h:x:y|-) [pas_s=0.5] : luma p2/p50/p98 (0-255), chroma moyen OkLCh, teinte des ombres / tons moyens / hautes lumières
import sys, subprocess, numpy as np
sys.path.insert(0, "/Volumes/SSD FAST/Montage-IA/labo/couleur")
v, crop = sys.argv[1], sys.argv[2]; pas = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
vf = (f"crop={crop}," if crop != "-" else "") + f"fps={1/pas},scale=320:-2,format=rgb24"
p = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height","-of","csv=p=0",v],capture_output=True,text=True).stdout.strip().split(",")
w, h = (int(crop.split(":")[0]), int(crop.split(":")[1])) if crop != "-" else (int(p[0]), int(p[1]))
H = int(round(320 * h / w / 2)) * 2
raw = subprocess.run(["ffmpeg","-v","error","-i",v,"-vf",vf,"-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, 320, 3).astype(np.float32) / 255
def lin(c): return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
def oklab(rgb):
    r, g, b = [lin(rgb[..., i]) for i in range(3)]
    l = 0.4122214708*r + 0.5363325363*g + 0.0514459929*b; m = 0.2119034982*r + 0.6806995451*g + 0.1073969566*b; s = 0.0883024619*r + 0.2817188376*g + 0.6299787005*b
    l, m, s = np.cbrt(l), np.cbrt(m), np.cbrt(s)
    return 0.2104542553*l + 0.7936177850*m - 0.0040720468*s, 1.9779984951*l - 2.4285922050*m + 0.4505937099*s, 0.0259040371*l + 0.7827717662*m - 0.8086757660*s
Y = (0.2126*fr[...,0] + 0.7152*fr[...,1] + 0.0722*fr[...,2]) * 255
L, A, B = oklab(fr); C = np.hypot(A, B)
print(f"images {len(fr)}  luma p2 {np.percentile(Y,2):.0f}  p50 {np.percentile(Y,50):.0f}  p98 {np.percentile(Y,98):.0f}  chroma moyen {C.mean():.3f}")
for nom, (a, b) in {"ombres": (0, 0.35), "moyens": (0.35, 0.7), "hautes": (0.7, 1.01)}.items():
    m = (L >= a) & (L < b)
    if m.sum() > 100:
        am, bm = A[m].mean(), B[m].mean(); print(f"  {nom:7s} part {m.mean():.0%}  dominante teinte {np.degrees(np.arctan2(bm, am)) % 360:.0f}°  force {np.hypot(am, bm):.3f}  chroma {C[m].mean():.3f}")
