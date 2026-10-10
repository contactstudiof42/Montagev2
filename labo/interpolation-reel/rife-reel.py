# Usage: rife-reel.py <code_practical_rife> <dossier_parent_train_log> <dossier>  (source.mkv 320x180 15 i/s -> rife.mkv 30 i/s)
# Adapté de labo/interpolation/rife60.py (entrée source.mkv, sortie à 30 i/s).
import sys, subprocess, time, numpy as np, torch, torch.nn.functional as F
code, poids, R = sys.argv[1:4]
sys.path.insert(0, poids); sys.path.insert(0, code)
from train_log.IFNet_HDv3 import IFNet
torch.set_grad_enabled(False)
net = IFNet()
sd = torch.load(f"{poids}/train_log/flownet.pkl", map_location="cpu", weights_only=True)
sd = {k.replace("module.", ""): v for k, v in sd.items() if "module." in k or True}
print(net.load_state_dict(sd, strict=False))
net.eval()
W, H = 320, 180
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{R}/source.mkv", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
src = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
n = len(src); print("source", n)
def t(a): return torch.from_numpy(a.copy()).permute(2, 0, 1)[None].float() / 255.
ph = (64 - H % 64) % 64; pw = (64 - W % 64) % 64
out = []
t0 = time.time()
for i in range(n):
    out.append(src[i])
    if i + 1 < n:
        x = torch.cat([t(src[i]), t(src[i + 1])], 1)
        x = F.pad(x, (0, pw, 0, ph))
        _, _, merged = net(x, 0.5, [16, 8, 4, 2, 1])
        m = merged[4][0, :, :H, :W].clamp(0, 1)
        out.append((m.permute(1, 2, 0).numpy() * 255 + 0.5).astype(np.uint8))
    else:
        out.append(src[i])  # derniere image dupliquee pour atteindre 2n
dt = time.time() - t0
print(f"inference {n-1} paires {dt:.1f} s ; sortie {len(out)} images")
p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30", "-i", "-",
                      "-c:v", "ffv1", "-pix_fmt", "yuv444p", f"{R}/rife.mkv"], stdin=subprocess.PIPE)
p.communicate(np.stack(out).tobytes())
print("temps total", f"{time.time()-t0:.1f} s")
