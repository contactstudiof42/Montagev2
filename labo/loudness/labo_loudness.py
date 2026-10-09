#!/usr/bin/env python3
"""Labo loudness : génère un signal test, mesure (ebur128 + loudnorm),
normalise en 1 passe et en 2 passes (linear=true) vers -23 et -14 LUFS / -1 dBTP,
re-mesure et vérifie l'écart (tolérance ±0.5 LU).

Usage : python3 labo_loudness.py [dossier_rendus]
Sortie : tableau texte + resultats.json dans le dossier courant du script.
"""
import json, re, subprocess, sys, time
from pathlib import Path

ICI = Path(__file__).resolve().parent
RENDUS = Path(sys.argv[1]) if len(sys.argv) > 1 else ICI.parent / "rendus" / "loudness"
RENDUS.mkdir(parents=True, exist_ok=True)
FF = ["ffmpeg", "-hide_banner", "-nostdin", "-y"]
TOL = 0.5


def run(cmd):
    t = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True)
    dt = time.time() - t
    if p.returncode != 0:
        raise RuntimeError(" ".join(cmd) + "\n" + p.stderr[-2000:])
    return p.stderr, dt


def generer(src):
    """Signal test 30 s stéréo 48 kHz :
    0-10 s bruit rose 'moyen', 10-15 s sinus 1 kHz -20 dBFS, 15-18 s silence,
    18-24 s bruit rose fort (+12 dB), 24-30 s bruit rose faible (-15 dB).
    -> dynamique volontairement large (LRA élevé) pour piéger loudnorm."""
    fc = (
        "anoisesrc=color=pink:amplitude=0.25:sample_rate=48000:seed=42:duration=10[a];"
        "sine=frequency=1000:sample_rate=48000:duration=5,volume=0.1[b];"  # 0.1 ~ -20 dBFS crête
        "anullsrc=r=48000:cl=mono,atrim=duration=3[c];"
        "anoisesrc=color=pink:amplitude=0.9:sample_rate=48000:seed=7:duration=6[d];"
        "anoisesrc=color=pink:amplitude=0.045:sample_rate=48000:seed=9:duration=6[e];"
        "[a][b][c][d][e]concat=n=5:v=0:a=1,aformat=sample_fmts=s32:channel_layouts=stereo[out]"
    )
    cmd = FF + ["-filter_complex", fc, "-map", "[out]", "-c:a", "pcm_s24le", str(src)]
    _, dt = run(cmd)
    return cmd, dt


def mesure_ebur128(f):
    cmd = FF + ["-nostats", "-i", str(f), "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"]
    err, dt = run(cmd)
    summ = err[err.rfind("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+|-inf) LUFS", summ).group(1))
    LRA = float(re.search(r"LRA:\s+(-?[\d.]+) LU", summ).group(1))
    TP = re.search(r"True peak:\s+Peak:\s+(-?[\d.]+|-inf) dBFS", summ)
    return {"I": I, "LRA": LRA, "TP": float(TP.group(1)) if TP else None, "t": round(dt, 2)}, cmd


def loudnorm_json(err):
    blob = err[err.rfind("{"):err.rfind("}") + 1]
    return json.loads(blob)


def mesure_loudnorm(f, I, TP, LRA):
    cmd = FF + ["-nostats", "-i", str(f), "-af",
                f"loudnorm=I={I}:TP={TP}:LRA={LRA}:print_format=json", "-f", "null", "-"]
    err, dt = run(cmd)
    return loudnorm_json(err), dt, cmd


def une_passe(src, dst, I, TP, LRA):
    cmd = FF + ["-i", str(src), "-af", f"loudnorm=I={I}:TP={TP}:LRA={LRA}:print_format=json",
                "-ar", "48000", "-c:a", "pcm_s24le", str(dst)]
    err, dt = run(cmd)
    return loudnorm_json(err), dt, cmd


def deux_passes(src, dst, I, TP, LRA):
    m, dt1, cmd1 = mesure_loudnorm(src, I, TP, LRA)
    af = (f"loudnorm=I={I}:TP={TP}:LRA={LRA}:measured_I={m['input_i']}:measured_TP={m['input_tp']}"
          f":measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
          f":offset={m['target_offset']}:linear=true:print_format=json")
    cmd2 = FF + ["-i", str(src), "-af", af, "-ar", "48000", "-c:a", "pcm_s24le", str(dst)]
    err, dt2 = run(cmd2)
    return m, loudnorm_json(err), dt1 + dt2, [cmd1, cmd2]


def gain_lineaire(src, dst, I, TP):
    """Alternative 'manuelle' : gain statique = cible - mesure, puis limiteur
    seulement si le TP dépasse (alimiter n'est PAS true peak : marge prise)."""
    m, _ = mesure_ebur128(src)
    g = I - m["I"]
    af = f"volume={g:.2f}dB"
    if m["TP"] is not None and m["TP"] + g > TP:
        # alimiter : limit en linéaire, on vise 0.5 dB sous la cible TP, suréchantillonné x4
        lim = 10 ** ((TP - 0.5) / 20)
        af += f",aresample=192000,alimiter=limit={lim:.4f}:attack=1:release=50:level=false,aresample=48000"
    cmd = FF + ["-i", str(src), "-af", af, "-c:a", "pcm_s24le", str(dst)]
    _, dt = run(cmd)
    return af, dt, cmd


def verdict(m, I, TP):
    okI = abs(m["I"] - I) <= TOL
    okTP = m["TP"] is not None and m["TP"] <= TP + 0.05
    return ("OK" if okI else f"RATE I ({m['I'] - I:+.1f} LU)") + " / " + ("TP OK" if okTP else "TP DEPASSE")


def main():
    res = {"commandes": {}, "essais": []}
    src = RENDUS / "signal_test.wav"
    cmd, dt = generer(src)
    res["commandes"]["generation"] = " ".join(cmd)
    res["t_generation"] = round(dt, 2)
    m0, cmdm = mesure_ebur128(src)
    res["commandes"]["mesure"] = " ".join(cmdm)
    res["source"] = m0
    print(f"SOURCE  I={m0['I']} LUFS  LRA={m0['LRA']} LU  TP={m0['TP']} dBTP  ({m0['t']} s)")

    # Variante source « calme » (LRA faible) pour montrer quand linear=true tient
    calme = RENDUS / "signal_calme.wav"
    run(FF + ["-i", str(src), "-af", "acompressor=threshold=-30dB:ratio=8:attack=5:release=200:makeup=6,volume=-6dB",
              "-c:a", "pcm_s24le", str(calme)])
    mc, _ = mesure_ebur128(calme)
    res["source_calme"] = mc
    print(f"CALME   I={mc['I']} LUFS  LRA={mc['LRA']} LU  TP={mc['TP']} dBTP")

    for nom_src, s in (("large", src), ("calme", calme)):
        for I, TP, LRA in ((-23, -1, 20), (-14, -1, 11)):
            tag = f"{nom_src}_{abs(I)}"
            # 1 passe
            o1 = RENDUS / f"{tag}_1passe.wav"
            j1, dt1, c1 = une_passe(s, o1, I, TP, LRA)
            r1, _ = mesure_ebur128(o1)
            # 2 passes
            o2 = RENDUS / f"{tag}_2passes.wav"
            mm, j2, dt2, c2 = deux_passes(s, o2, I, TP, LRA)
            r2, _ = mesure_ebur128(o2)
            # gain + limiteur
            o3 = RENDUS / f"{tag}_gain.wav"
            af3, dt3, c3 = gain_lineaire(s, o3, I, TP)
            r3, _ = mesure_ebur128(o3)
            for meth, r, dt, typ, cmds in (
                ("1 passe (dynamique)", r1, dt1, j1.get("normalization_type"), [c1]),
                ("2 passes linear=true", r2, dt2, j2.get("normalization_type"), c2),
                ("gain statique (+alimiter si besoin)", r3, dt3, af3, [c3]),
            ):
                e = {"source": nom_src, "cible_I": I, "cible_TP": TP, "LRA_cible": LRA, "methode": meth,
                     "I": r["I"], "LRA": r["LRA"], "TP": r["TP"], "ecart_LU": round(r["I"] - I, 2),
                     "verdict": verdict(r, I, TP), "type_loudnorm": typ, "temps_s": round(dt, 2),
                     "cmds": [" ".join(c) for c in cmds]}
                res["essais"].append(e)
                print(f"{tag:10s} {meth:38s} I={r['I']:6.1f} LRA={r['LRA']:5.1f} TP={r['TP']:6.1f} "
                      f"ecart={e['ecart_LU']:+5.2f}  {e['verdict']:28s} type={typ}  t={dt:.2f}s")
    (ICI / "resultats.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
