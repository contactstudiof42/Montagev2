# Usage : rife-reel.py <code_practical_rife> <dossier_parent_train_log> <dossier> [k=2]
# k = facteur (k-1 images inventées par paire, aux instants j/k) ; sortie 30 i/s.
# source.mkv (yuv444p 320x180, 15 i/s) -> rife.mkv (yuv444p, 30 i/s). Adapté de labo/interpolation/rife60.py.
# Différence : on reste en YUV. Les images d'origine sont recopiées telles quelles (pas d'aller-retour RGB 8 bits,
# qui coûtait ~45 dB sur un plan filmé) ; seules les images inventées passent par RGB, en flottant (BT.601 limité,
# convention par défaut de ffmpeg), avec un seul arrondi final, comme minterpolate.
import sys, subprocess, time, numpy as np, torch, torch.nn.functional as F
code, poids, R = sys.argv[1:4]; k = int(sys.argv[4]) if len(sys.argv) > 4 else 2
sys.path.insert(0, poids); sys.path.insert(0, code)
from train_log.IFNet_HDv3 import IFNet
torch.set_grad_enabled(False)
net = IFNet()
sd = torch.load(f"{poids}/train_log/flownet.pkl", map_location="cpu", weights_only=True)
sd = {k.replace("module.", ""): v for k, v in sd.items()}
r = net.load_state_dict(sd, strict=False)
print("cles manquantes :", r.missing_keys, "; inutilisees :", len(r.unexpected_keys), "(teacher/caltime, entrainement)")
net.eval()
W, H = 320, 180
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{R}/source.mkv", "-f", "rawvideo", "-pix_fmt", "yuv444p", "-"],
                     capture_output=True).stdout
src = np.frombuffer(raw, np.uint8).reshape(-1, 3, H, W)  # plans Y, U, V
n = len(src); print("source", n)
def vers_rgb(a):
    y = (a[0].astype(np.float32) - 16) / 219; u = (a[1].astype(np.float32) - 128) / 224; v = (a[2].astype(np.float32) - 128) / 224
    rgb = np.stack([y + 1.402 * v, y - 0.344136 * u - 0.714136 * v, y + 1.772 * u])
    return torch.from_numpy(rgb)[None]
def vers_yuv(t):
    r, g, b = t.numpy()
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = (b - y) / 1.772; v = (r - y) / 1.402
    out = np.stack([16 + 219 * y, 128 + 224 * u, 128 + 224 * v])
    return np.clip(out + 0.5, 0, 255).astype(np.uint8)
ph = (64 - H % 64) % 64; pw = (64 - W % 64) % 64
out = []
t0 = time.time()
for i in range(n):
    out.append(src[i])
    if i + 1 < n:
        x = torch.cat([vers_rgb(src[i]), vers_rgb(src[i + 1])], 1)
        x = F.pad(x, (0, pw, 0, ph))
        for j in range(1, k):
            _, _, merged = net(x, j / k, [16, 8, 4, 2, 1])
            out.append(vers_yuv(merged[4][0, :, :H, :W]))
    else:
        out += [src[i]] * (k - 1)  # derniere image dupliquee pour atteindre k*n
dt = time.time() - t0
print(f"inference {n-1} paires x {k-1} {dt:.1f} s ; sortie {len(out)} images")
p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "yuv444p", "-s", f"{W}x{H}", "-r", "30", "-i", "-",
                      "-c:v", "ffv1", "-pix_fmt", "yuv444p", f"{R}/rife.mkv"], stdin=subprocess.PIPE)
p.communicate(np.stack(out).tobytes())
print("temps total", f"{time.time()-t0:.1f} s")
