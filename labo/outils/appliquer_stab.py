# appliquer_stab.py VIDEO DEBUT_S CLES.json SORTIE.mp4 : applique les clés de stabiliser.py hors de Resolve (contrôle),
# à 540 px de large, pour mesurer avec tremblement.py et juger sur une bande avant de poser les clés dans Fusion.
import sys, json, subprocess, numpy as np, cv2
v, t0, cj, out = sys.argv[1], float(sys.argv[2]), json.load(open(sys.argv[3])), sys.argv[4]
cles = cj["cles"]; n = len(cles); m0 = -cles[0]["image"] / cj["fps"]
W = 540
p = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height:stream_side_data=rotation","-of","json",v],capture_output=True,text=True)
s = json.loads(p.stdout)["streams"][0]; w, h = s["width"], s["height"]
if any(abs(int(d.get("rotation",0)))==90 for d in s.get("side_data_list",[])): w, h = h, w
H = int(round(W*h/w/2))*2
raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t0-m0),"-i",v,"-frames:v",str(n),"-vf",f"scale={W}:{H}","-pix_fmt","bgr24","-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw,np.uint8).reshape(-1,H,W,3)
enc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r",str(cj["fps"]),"-i","-","-c:v","libx264","-crf","12","-pix_fmt","yuv420p",out],stdin=subprocess.PIPE)
for k in range(min(n,len(fr))):
    c = cles[k]; S = c["Size"]; a = np.radians(c["Angle"])   # Fusion : angle anti-horaire, Y vers le haut
    cx, cy = W/2, H/2
    M = np.array([[S*np.cos(a), S*np.sin(a)], [-S*np.sin(a), S*np.cos(a)]])  # anti-horaire à l'écran (y vers le bas)
    tx = (c["X"]-0.5)*W; ty = -(c["Y"]-0.5)*H
    A = np.hstack([M, (np.array([cx,cy]) + np.array([tx,ty]) - M@np.array([cx,cy]))[:,None]])
    enc.stdin.write(cv2.warpAffine(fr[k],A,(W,H),flags=cv2.INTER_LINEAR,borderValue=(0,0,255)).tobytes())
enc.stdin.close(); enc.wait()
