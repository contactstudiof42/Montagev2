# maquette.py montage.json SORTIE.mp4 [largeur=960] [debut fin] : maquette rapide (ffmpeg) : plans avec LUT de look, sons mixés, textes en PNG
import sys, json, subprocess, os, hashlib
from PIL import Image, ImageDraw, ImageFont
J = json.load(open(sys.argv[1])); OUT = sys.argv[2]; W = int(sys.argv[3]) if len(sys.argv) > 3 else 960; H = W * 9 // 16
D0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0; D1 = float(sys.argv[5]) if len(sys.argv) > 5 else J["duree"]
R = "/Volumes/SSD FAST/MARIAGE JO/RUSH"; TW = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/mariage-jo/_travail"
INV = {x["nom"]: x for x in json.load(open(f"{TW}/inventaire.json"))}
LUT = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/P3/P3_mariage_{}.cube"
C = f"{TW}/maquette_cache"; os.makedirs(C, exist_ok=True)
FONTS = {"titre": ("/System/Library/Fonts/Supplemental/Didot.ttc", 0.075), "personnage": ("/System/Library/Fonts/Supplemental/Didot.ttc", 0.045),
         "replique": ("/System/Library/Fonts/Supplemental/Didot.ttc", 0.05), "fin": ("/System/Library/Fonts/Supplemental/Didot.ttc", 0.06)}
def seg(e):
    k = hashlib.md5(json.dumps([e["nom"], e["src"], e["dur"], e["look"], e["vitesse"], W, e.get("cadre"), 2]).encode()).hexdigest()[:12]
    f = f"{C}/{k}.mp4"
    if os.path.exists(f): return f
    x = INV[e["nom"]]; srcdur = e["dur"] * e["vitesse"]
    crop = e.get("cadre")  # [zoom, cx, cy] recadrage optionnel
    vf = f"setpts=(PTS-STARTPTS)/{e['vitesse']},fps=25,tpad=stop_mode=clone:stop_duration=3,"
    if crop: z, cx, cy = crop; vf += f"crop=iw/{z}:ih/{z}:(iw-iw/{z})*{cx}:(ih-ih/{z})*{cy},"
    vf += f"scale={W}:{H},format=rgb48le,lut3d='{LUT.format(e['look'])}',format=yuv420p"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(max(0, e["src"])), "-t", str(srcdur + 0.1), "-i", f"{R}/{x['fichier']}", "-an", "-vf", vf,
                    "-frames:v", str(round(e["dur"] * 25)), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", f], check=True)
    return f
def png_texte(t):
    k = hashlib.md5(json.dumps([t, W]).encode()).hexdigest()[:12]; f = f"{C}/t_{k}.png"
    if os.path.exists(f): return f
    fp, s = FONTS[t["style"]]; font = ImageFont.truetype(fp, int(H * s)); im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    bb = d.textbbox((0, 0), t["texte"], font=font); tw, th = bb[2] - bb[0], bb[3] - bb[1]
    pos = {"titre": (int(W * 0.06), int(H * 0.80) - th), "personnage": (int(W * 0.06), int(H * 0.86) - th), "replique": ((W - tw) // 2, int(H * 0.88) - th), "fin": ((W - tw) // 2, (H - th) // 2)}[t["style"]]
    d.text(pos, t["texte"], font=font, fill=(238, 230, 211, 255)); im.save(f); return f
# vidéo : piste 1 seulement pour la maquette (plans posés bout à bout), noir dans les trous
evs = sorted([e for e in J["video"] if e["piste"] == 1 and e["rec"] + e["dur"] > D0 and e["rec"] < D1], key=lambda e: e["rec"])
liste = f"{C}/liste.txt"; t = D0; L = []
noir = f"{C}/noir_{W}.mp4"
if not os.path.exists(noir): subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=black:s={W}x{H}:r=25", "-t", "10", "-c:v", "libx264", "-pix_fmt", "yuv420p", noir])
for e in evs:
    if e["rec"] > t + 0.02: L.append(f"file '{noir}'\noutpoint {e['rec'] - t:.3f}")
    s = seg(e); ip = max(0, D0 - e["rec"]); op = min(e["dur"], D1 - e["rec"])
    L.append(f"file '{s}'" + (f"\ninpoint {ip:.3f}" if ip > 0 else "") + (f"\noutpoint {op:.3f}" if op < e["dur"] else "")); t = e["rec"] + op
if t < D1 - 0.02: L.append(f"file '{noir}'\noutpoint {D1 - t:.3f}")
open(liste, "w").write("\n".join(L) + "\n")
vid = f"{C}/video.mp4"; subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", liste, "-c", "copy", vid], check=True)
# textes en surimpression
txt = [x for x in J.get("textes", []) if x["rec"] + x["dur"] > D0 and x["rec"] < D1]
if txt:
    args = ["ffmpeg", "-v", "error", "-y", "-i", vid]; fc = ""; last = "0:v"
    for i, x in enumerate(txt):
        args += ["-loop", "1", "-t", str(D1 - D0), "-i", png_texte(x)]; a0, a1 = x["rec"] - D0, x["rec"] - D0 + x["dur"]
        fc += f"[{i+1}:v]format=rgba,fade=in:st={a0:.2f}:d=0.3:alpha=1,fade=out:st={a1-0.3:.2f}:d=0.3:alpha=1[t{i}];[{last}][t{i}]overlay=0:0:enable='between(t,{a0:.2f},{a1:.2f})'[o{i}];"; last = f"o{i}"
    vid2 = f"{C}/video_t.mp4"; subprocess.run(args + ["-filter_complex", fc.rstrip(";"), "-map", f"[{last}]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", vid2], check=True); vid = vid2
# son
aud = [x for x in J["audio"] if x["rec"] + x["dur"] > D0 and x["rec"] < D1]
args = ["ffmpeg", "-v", "error", "-y"]; fc = ""
for i, x in enumerate(aud):
    ip = max(0, D0 - x["rec"]); args += ["-ss", str(x["src"] + ip), "-t", str(x["dur"] - ip), "-i", x["fichier"]]
    d = max(0, x["rec"] - D0); du = x["dur"] - ip
    f = f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={x['gain']}dB"
    if x["fin"] > 0 and ip == 0: f += f",afade=in:d={x['fin']}"
    if x["fout"] > 0: f += f",afade=out:st={max(0, du - x['fout']):.3f}:d={x['fout']}"
    f += f",adelay={int(d*1000)}|{int(d*1000)},apad=whole_dur={D1-D0:.3f}[a{i}];"; fc += f
fc += "".join(f"[a{i}]" for i in range(len(aud))) + f"amix=inputs={len(aud)}:normalize=0:duration=longest,atrim=0:{D1-D0:.3f}[m]"
au = f"{C}/audio.wav"; subprocess.run(args + ["-filter_complex", fc, "-map", "[m]", au], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-i", au, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", OUT], check=True); print(OUT)
