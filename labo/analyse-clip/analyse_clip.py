#!/usr/bin/env python3
"""Analyse mesurée d'un clip ou d'une pub : coupes, flashs, durées de plans, tempo,
rapport coupes/beat, coupes selon la présence de la basse, lumière et accents chauds.

Usage : python3 -I analyse_clip.py <video> <dossier_sortie>
Dépendances : ffmpeg, numpy, librosa. Le média n'est jamais copié dans le dépôt.
Pensé pour les images sombres : la différence image à image est normalisée par la
luminosité (scdet de ffmpeg sous-détecte fortement dans le noir : 38 coupes au lieu de 87
sur le clip de Ziak)."""
import sys, os, json, subprocess, numpy as np

def frames_small(video, w=64, h=36):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", video, "-vf", f"scale={w}:{h}:flags=area",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float32)

def fps_of(video):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate",
                        "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip()
    a, b = r.split("/"); return float(a) / float(b)

def detect(a):
    g = a.mean(-1); n = len(g); L = g.mean(axis=(1, 2))
    d = np.zeros(n)
    for i in range(1, n):
        d[i] = np.abs(g[i] - g[i-1]).mean() / ((L[i] + L[i-1]) / 2 + 8)
    cand = [i for i in range(2, n-2) if d[i] == d[max(0, i-12):i+13].max()
            and d[i] > max(3.5 * np.median(d[max(0, i-12):i+13]), 0.18)]
    cuts, flashes = [], []
    for c in cand:  # flash = pic de luminosité qui revient au niveau de départ
        w = L[max(0, c-3):min(n, c+7)]; base = min(w[0], w[-1])
        (flashes if (w.max() > 1.8 * base and abs(w[0] - w[-1]) < 0.3 * max(w[0], w[-1])) else cuts).append(c)
    return g, L, cuts, flashes

def main(video, out):
    import librosa
    os.makedirs(out, exist_ok=True); fps = fps_of(video)
    a = frames_small(video); g, L, cuts, flashes = detect(a); n = len(a); dur = n / fps
    c = np.array(cuts) / fps; sh = np.diff(np.concatenate([[0], c, [dur]]))
    wav = os.path.join(out, "audio.wav")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "22050", wav], check=True)
    y, sr = librosa.load(wav, sr=22050)
    tempo = float(np.atleast_1d(librosa.beat.beat_track(y=y, sr=sr)[0])[0]); T = 60 / tempo
    phase = abs(np.mean(np.exp(2j * np.pi * np.mod(c / T, 1.0)))) if len(c) else 0
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512)); f = librosa.fft_frequencies(sr=sr, n_fft=2048)
    t = librosa.times_like(S[0], sr=sr, hop_length=512); lo = S[f < 120].mean(0)
    secs = int(dur); bass = np.array([lo[(t >= i) & (t < i+1)].mean() for i in range(secs)])
    bass_db = 20 * np.log10(bass + 1e-9); bass_db -= bass_db.max(); on = bass_db > -20
    idx = np.minimum(np.floor(c).astype(int), secs - 1)
    Y = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    warm = (((a[..., 0] - a[..., 2]) > 40) & (a[..., 0] > 80)).mean(axis=(1, 2)) * 100
    res = {
        "duree_s": round(dur, 2), "fps": fps, "plans": len(sh), "flashs": len(flashes),
        "ASL_s": round(float(sh.mean()), 2), "duree_mediane_s": round(float(np.median(sh)), 2),
        "durees_hist_[0-1,1-2,2-3,3-5,5-8,8+]": np.histogram(sh, [0, 1, 2, 3, 5, 8, 999])[0].tolist(),
        "tempo_bpm": round(tempo, 1),
        "concentration_phase_coupes_au_temps": round(float(phase), 2),
        "hasard_attendu": round(1 / np.sqrt(max(len(c), 1)), 2),
        "coupes_par_min_basse_presente": round(float(on[idx].sum() / max(on.sum(), 1) * 60), 1),
        "coupes_par_min_basse_absente": round(float((~on)[idx].sum() / max((~on).sum(), 1) * 60), 1),
        "luma_moyenne": round(float(Y.mean()), 1), "luma_mediane": round(float(np.median(Y)), 1),
        "pixels_sous_30_pct": round(float(np.mean(Y < 30) * 100), 1),
        "accent_chaud_pct_image": round(float(warm.mean()), 2),
        "coupes_s": [round(float(x), 2) for x in c], "flashs_s": [round(x / fps, 2) for x in flashes],
    }
    json.dump(res, open(os.path.join(out, "mesures.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in res.items() if not k.endswith("_s") or k in ("ASL_s", "duree_s")}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
