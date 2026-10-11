# pages.py DOSSIER [cols=12] [rows=10] : toutes les images, cadre rouge = coupe adapt, bleu = coupe content seule,
# barre sous chaque image : onset musique (no_vocals) en jaune, énergie voix en vert.
import sys, json, subprocess, numpy as np, librosa
from PIL import Image, ImageDraw
D = sys.argv[1]; cols = int(sys.argv[2]) if len(sys.argv) > 2 else 12; rows = int(sys.argv[3]) if len(sys.argv) > 3 else 10
v = f"{D}/proxy.mp4"
n_, d_ = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height","-of","default=nw=1:nk=1",v],capture_output=True,text=True).stdout.split()
w0, h0 = int(n_), int(d_); fr_s = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=r_frame_rate","-of","default=nw=1:nk=1",v],capture_output=True,text=True).stdout.strip().split("/")
fps = float(fr_s[0]) / float(fr_s[1])
W, H = (176, int(176 * h0 / w0) // 2 * 2) if w0 > h0 else (int(150 * w0 / h0) // 2 * 2, 150)
raw = subprocess.run(["ffmpeg","-v","error","-i",v,"-vf",f"scale={W}:{H},format=rgb24","-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3); N = len(fr)
ca = json.load(open(f"{D}/coupes.json"))["coupes"]; cc = json.load(open(f"{D}/coupes_content.json"))["coupes"]
ka = {int(round(t * fps)) for t in ca}; kc = {int(round(t * fps)) for t in cc}
def env(f):
    y, sr = librosa.load(f, sr=22050, mono=True); hop = 256
    o = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop); r = librosa.feature.rms(y=y, hop_length=hop)[0]
    t = librosa.frames_to_time(np.arange(len(o)), sr=sr, hop_length=hop)
    def par_image(x):
        out = np.zeros(N)
        for k in range(N):
            m = (t >= k / fps) & (t < (k + 1) / fps)
            out[k] = x[m].max() if m.any() else 0
        return out / (np.percentile(out, 99) + 1e-9)
    return par_image(o), par_image(r)
mo, _ = env(f"{D}/sep/htdemucs/audio/no_vocals.wav"); _, vr = env(f"{D}/sep/htdemucs/audio/vocals.wav")
lab, bar = 12, 10; per = cols * rows
for p in range(0, N, per):
    im = Image.new("RGB", (cols * (W + 4), rows * (H + lab + bar + 4)), (0, 0, 0)); dr = ImageDraw.Draw(im)
    for j, k in enumerate(range(p, min(p + per, N))):
        x, y = (j % cols) * (W + 4), (j // cols) * (H + lab + bar + 4)
        dr.text((x + 1, y), f"{k/fps:.2f} #{k}", fill=(255, 255, 0) if k % int(round(fps)) == 0 else (170, 170, 170))
        im.paste(Image.fromarray(fr[k]), (x + 2, y + lab))
        col = (255, 0, 0) if k in ka else ((0, 120, 255) if k in kc else None)
        if col: dr.rectangle([x, y + lab - 2, x + W + 3, y + lab + H + 1], outline=col, width=2)
        yb = y + lab + H + 2
        dr.rectangle([x + 2, yb + bar - int(bar * min(mo[k], 1)), x + 2 + W // 2 - 1, yb + bar], fill=(230, 200, 0))
        dr.rectangle([x + 2 + W // 2, yb + bar - int(bar * min(vr[k], 1)), x + 2 + W - 1, yb + bar], fill=(0, 200, 80))
    out = f"{D}/page-{p // per + 1:02d}.jpg"; im.save(out, quality=82); print(out)
print("images", N, "fps", fps, "W", W, "H", H)
