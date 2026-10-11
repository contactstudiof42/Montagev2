# banc_look.py : extrait des images S-Log3 en 16 bits (ffmpeg, rotation appliquée) et leur applique un look Python,
# pour itérer sans Resolve. extrait(rush, t, larg) -> float 0-1 ; vers_png(rgb, chemin).
import subprocess, json, numpy as np
from PIL import Image
RUSH = "/Volumes/SSD FAST/SONY copy/RUSH/20260929_{}.MP4"

def extrait(rush, t, larg=540, chemin=None):
    f = chemin or RUSH.format(rush)
    p = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height:stream_side_data=rotation","-of","json",f],capture_output=True,text=True)
    s = json.loads(p.stdout)["streams"][0]; w, h = s["width"], s["height"]
    if any(abs(int(d.get("rotation",0)))==90 for d in s.get("side_data_list",[])): w, h = h, w
    H = int(round(larg*h/w/2))*2
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",f,"-frames:v","1","-vf",f"scale={larg}:{H}:in_range=tv:out_range=pc,format=rgb48le","-f","rawvideo","-"],capture_output=True).stdout
    return np.frombuffer(raw, np.uint16).reshape(H, larg, 3).astype(np.float64) / 65535.0

def vers_png(rgb, chemin):
    Image.fromarray((np.clip(rgb,0,1)*255+0.5).astype(np.uint8)).save(chemin)
