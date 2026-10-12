# kinetic.py etape : passage kinetic du photobooth (détourage BiRefNet local, fonds qui changent toutes les 3 images, 16 temps du remix).
# etapes : images (extraction UHD + LUT), masques (BiRefNet, long), compo (ProRes 422 HQ). Plan dans SEGMENTS ; temps à 25 i/s.
import sys, os, json, subprocess, numpy as np
from PIL import Image
K = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail/kinetic"; R = "/Volumes/SSD FAST/MARIAGE JO/RUSH/DIEGO/private/M4ROOT/CLIP"
LUT = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/P3/P3_mariage_photobooth.cube"
BEAT = 60 / 126.048; FPS = 25
# (rush, début source s, nb d'images de timeline, détourer ?)
SEGMENTS = [("C4040", 12.0, 12, False), ("C4040", 14.0, 48, True), ("C4029", 6.0, 47, True), ("C4135", 1.2, 48, True), ("C4028", 3.6, 24, True), ("C4028", 4.56, 11, False)]
def images():
    n = 0
    for rush, s, nb, det in SEGMENTS:
        d = f"{K}/src/{rush}_{s:.2f}"; os.makedirs(d, exist_ok=True)
        if len(os.listdir(d)) < nb:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-i", f"{R}/20260604_{rush}.MP4", "-frames:v", str(nb * 2), "-vf",
                            f"select='not(mod(n\\,2))',setpts=N/{FPS}/TB,format=rgb48le,lut3d='{LUT}',format=rgb24", "-fps_mode", "passthrough", f"{d}/f_%04d.png"], check=True)
        n += nb
    print("images", n)
def masques():
    from rembg import new_session, remove
    ses = new_session("birefnet-general", providers=["CPUExecutionProvider"])
    for rush, s, nb, det in SEGMENTS:
        if not det: continue
        d = f"{K}/src/{rush}_{s:.2f}"; md = d + "_m"; os.makedirs(md, exist_ok=True)
        for f in sorted(os.listdir(d))[:nb]:
            if os.path.exists(f"{md}/{f}"): continue
            im = Image.open(f"{d}/{f}").convert("RGB").resize((1920, 1080), Image.LANCZOS)
            remove(im, session=ses, only_mask=True).save(f"{md}/{f}"); print(rush, f, flush=True)
PAL = [(0.42, 0.18, 0.85), (0.85, 0.16, 0.50), (0.05, 0.42, 0.55), (0.10, 0.40, 0.18), (0.55, 0.20, 0.75), (0.80, 0.25, 0.30)]
def fond(k, W=3840, H=2160):
    c = np.array(PAL[k % len(PAL)]); yy, xx = np.mgrid[0:H, 0:W]; r = np.hypot((xx - W / 2) / W, (yy - H / 2) / H) * 1.6
    g = (1.15 - 0.45 * np.clip(r, 0, 1))[..., None]; return np.clip(c * g, 0, 1)
def compo(sortie):
    W, H = 3840, 2160
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", sortie], stdin=subprocess.PIPE)
    t = 0; ordre = [0, 2, 1, 3, 5, 4]; fonds = [fond(i) for i in range(len(PAL))]
    for si, (rush, s, nb, det) in enumerate(SEGMENTS):
        d = f"{K}/src/{rush}_{s:.2f}"; fs = sorted(os.listdir(d))[:nb]
        for i, f in enumerate(fs):
            im = np.asarray(Image.open(f"{d}/{f}").convert("RGB")).astype(np.float32) / 255
            if det:
                m = np.asarray(Image.open(f"{d}_m/{f}").convert("L").resize((W, H), Image.BILINEAR)).astype(np.float32)[..., None] / 255
                k = t // 3; b = fonds[ordre[k % len(ordre)]]
                temps = (t / FPS) / BEAT; fort = abs(temps - round(temps)) < 0.5 / (FPS * BEAT) and round(temps) % 4 == 0
                sujet = im
                if int(temps) % 4 == 3:                                  # un temps sur quatre : le sujet en noir et blanc, fond = sa propre image N&B assombrie
                    y = (im @ np.array([0.2126, 0.7152, 0.0722]))[..., None]; sujet = np.repeat(y, 3, -1); b = np.repeat(y * 0.35, 3, -1)
                out = sujet * m + b * (1 - m)
            else: out = im
            p.stdin.write((np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8).tobytes()); t += 1
    p.stdin.close(); p.wait(); print(sortie, t, "images", t / FPS, "s")
if __name__ == "__main__":
    {"images": images, "masques": masques}.get(sys.argv[1], lambda: compo(sys.argv[2] if len(sys.argv) > 2 else f"{K}/kinetic_V1.mov"))()
