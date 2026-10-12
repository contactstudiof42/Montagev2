"""Transcription + alignement forcé mot à mot (WhisperX, local) d'un fichier son ou d'une fenêtre.

Usage (venv .venv-whisperx) :
  aligne.py SON SORTIE.json [debut_s fin_s]
Sortie : {"source", "debut", "segments": [{"s","e","texte","mots":[{"m","s","e","score"}]}]}
Temps absolus dans le fichier source (le début de la fenêtre est ajouté).
"""
import json, sys, subprocess, numpy as np
import whisperx

SR = 16000

def charge(son, debut=None, fin=None):
    cmd = ["ffmpeg", "-v", "error"]
    if debut is not None:
        cmd += ["-ss", str(debut), "-to", str(fin)]
    cmd += ["-i", son, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).copy()

_modeles = {}
def modeles():
    if not _modeles:
        _modeles["asr"] = whisperx.load_model("large-v3-turbo", "cpu", compute_type="int8", language="fr")
        _modeles["al"] = whisperx.load_align_model(language_code="fr", device="cpu")
    return _modeles["asr"], _modeles["al"]

def aligne(son, debut=None, fin=None):
    audio = charge(son, debut, fin)
    asr, (am, meta) = modeles()
    r = asr.transcribe(audio, batch_size=8, language="fr")
    a = whisperx.align(r["segments"], am, meta, audio, "cpu", return_char_alignments=False)
    d = debut or 0.0
    segs = []
    for s in a["segments"]:
        mots = [{"m": w["word"], "s": round(w["start"] + d, 3), "e": round(w["end"] + d, 3), "score": round(w.get("score", 0), 3)}
                for w in s.get("words", []) if "start" in w]
        segs.append({"s": round(s["start"] + d, 3), "e": round(s["end"] + d, 3), "texte": s["text"].strip(), "mots": mots})
    return {"source": son, "debut": d, "segments": segs}

if __name__ == "__main__":
    son, sortie = sys.argv[1], sys.argv[2]
    deb = float(sys.argv[3]) if len(sys.argv) > 3 else None
    fin = float(sys.argv[4]) if len(sys.argv) > 4 else None
    res = aligne(son, deb, fin)
    json.dump(res, open(sortie, "w"), ensure_ascii=False, indent=1)
    print(sortie, len(res["segments"]), "segments")
