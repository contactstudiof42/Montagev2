#!/usr/bin/env python3
"""Outil général de labo : regarder et mesurer un montage autour de ses coupes (Y23, Y26, Y29).

Sources de coupes (une au choix, ou plusieurs pour les comparer) :
  --edl FICHIER.edl    CMX3600 (record in de chaque événement V ; lignes « * LOC: TC COULEUR texte » = marqueurs)
  --otio FICHIER.otio  OpenTimelineIO (1re piste vidéo ; marqueurs de la piste et des clips)
  --scdet [SEUIL]      détection ffmpeg (scdet, seuil 10 par défaut)
Sorties (préfixe --sortie P) :
  P-bande.png   une ligne par coupe : images de part et d'autre (--avant/--apres), enveloppe du son
                sous chaque image (dB RMS, -60..0), trait blanc = coupe, trait rouge = marqueur proche.
  P-courbe.png  coupes par minute (fenêtre glissante --fenetre s) + activité visuelle hors coupes.
  P.json        coupes, marqueurs, mesures ; comparaison des sources si plusieurs (tolérance ±1 image).
Activité visuelle (Y26) : différence moyenne de luminance entre images successives, mesurée sur
l'image réduite à 1/8 et floutée (le grain s'y moyenne), en excluant ±1 image autour de chaque coupe.
Usage : coupes.py VIDEO [--edl X] [--otio X] [--scdet [10]] --sortie P [--avant 6 --apres 6] [--fenetre 10] [--reduction 8]
"""
import sys, json, re, wave, subprocess, tempfile, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONDUS = []   # [début, durée] des fondus lus dans l'EDL
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)


def tc_vers_image(tc, fps):
    h, m, s, f = [int(x) for x in re.split('[:;]', tc)]
    return ((h*60 + m)*60 + s)*fps + f


def lire_edl(chemin, fps):
    coupes, marqueurs, fondus, debut = [], [], [], None
    for ligne in open(chemin, encoding='utf-8', errors='replace'):
        p = ligne.split()
        if len(p) >= 8 and p[0].isdigit() and p[2].startswith('V'):
            # « C » : 4 TC aux champs 4-7 ; « D 012 » / « W001 012 » : la durée décale les TC d'un champ
            dec = 1 if p[3][0] in 'DW' and len(p) >= 9 else 0
            rin = tc_vers_image(p[6 + dec], fps)
            debut = rin if debut is None else min(debut, rin)
            if not dec and p[6] == p[7]:
                continue                                  # ligne « de départ » d'un fondu, durée nulle
            if dec:
                fondus.append([rin, int(p[4])])
                coupes.append(rin + int(p[4]) // 2)      # un fondu compte comme une coupe en son milieu
            elif not (coupes and coupes[-1] == rin):
                coupes.append(rin)
        m = re.match(r'\*\s*LOC:\s*(\S+)\s+(\S+)\s*(.*)', ligne.strip())
        if m:
            marqueurs.append([tc_vers_image(m.group(1), fps), m.group(3) or m.group(2)])
    coupes = sorted(set(c - debut for c in coupes))[1:]   # le début du 1er plan n'est pas une coupe
    marqueurs = [[f - debut, t] for f, t in marqueurs]
    FONDUS.extend([f - debut, n] for f, n in fondus)
    return coupes, marqueurs


def lire_otio(chemin, fps):
    import opentimelineio as otio
    tl = otio.adapters.read_from_file(chemin)
    piste = next(t for t in tl.tracks if t.kind == otio.schema.TrackKind.Video)
    coupes, marqueurs, t = [], [], 0
    for m in piste.markers:
        marqueurs.append([int(round(m.marked_range.start_time.to_frames(fps))), m.name])
    for item in piste:
        d = int(round(item.duration().to_frames(fps)))
        if isinstance(item, otio.schema.Transition):
            continue
        if t > 0:
            coupes.append(t)
        for m in getattr(item, 'markers', []):
            s = item.source_range.start_time.to_frames(fps) if item.source_range else 0
            marqueurs.append([t + int(round(m.marked_range.start_time.to_frames(fps) - s)), m.name])
        t += d
    return coupes, marqueurs


def sonde(video):
    o = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                                   'stream=r_frame_rate,width,height,nb_frames', '-of', 'json', video],
                                  capture_output=True, text=True).stdout)['streams'][0]
    n, d = o['r_frame_rate'].split('/')
    return int(round(int(n)/int(d))), o['width'], o['height']


def lire_images(video, w, h):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', f'scale={w}:{h}:flags=area',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)


def enveloppe(video, fps, n):
    """dB RMS par image (-60..0) ; None si pas de son."""
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, 'a.wav')
        r = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vn', '-ac', '1', '-ar', '16000', f])
        if r.returncode or not os.path.exists(f):
            return None
        w = wave.open(f); a = np.frombuffer(w.readframes(w.getnframes()), np.int16) / 32768
    if not len(a):
        return None
    pas = 16000 / fps
    return [float(max(-60, 20*np.log10(np.sqrt(np.mean(a[int(k*pas):int((k+1)*pas)]**2) + 1e-9))))
            if int(k*pas) < len(a) else -60.0 for k in range(n)]


def scdet(video, seuil):
    err = subprocess.run(['ffmpeg', '-v', 'info', '-i', video, '-vf', f'scdet=threshold={seuil}', '-an', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    fps = sonde(video)[0]
    brut = sorted(int(round(float(t)*fps)) for t in re.findall(r'lavfi\.scd\.time:\s*([\d.]+)', err))
    # [TESTÉ EN LABO] sur image granuleuse, scdet se déclenche aussi à c+1 (et à l'image 1) : fusionner
    return [c for i, c in enumerate(brut) if c > 1 and (i == 0 or c - brut[i-1] > 1)]


def activite(petites, coupes):
    """YDIF sur image réduite + floutée, hors ±1 image des coupes. Retourne la liste par image (None aux coupes)."""
    y = petites.astype(np.float32) @ np.array([0.299, 0.587, 0.114], np.float32)
    # flou 3x3 (moyenne) sur l'image déjà réduite : le grain résiduel s'y moyenne encore
    yp = np.pad(y, ((0, 0), (1, 1), (1, 1)), mode='edge')
    yb = sum(yp[:, i:i+y.shape[1], j:j+y.shape[2]] for i in range(3) for j in range(3)) / 9
    d = [None] + [float(np.mean(np.abs(yb[k] - yb[k-1]))) for k in range(1, len(yb))]
    exclus = {c + e for c in coupes for e in (-1, 0, 1)}
    return [None if k in exclus else v for k, v in enumerate(d)]


def compare(a, b, tol=1):
    """a = référence, b = détection : vrais positifs, manqués, fausses alertes."""
    reste, vp, fa = list(a), [], []
    for c in b:
        m = next((r for r in reste if abs(r - c) <= tol), None)
        if m is None:
            fa.append(c)
        else:
            vp.append(c); reste.remove(m)
    return {'vrais': len(vp), 'manques': reste, 'fausses_alertes': fa}


def bande(images, env, coupes, marqueurs, avant, apres, fps, sortie, maxi=16):
    n, h, w = images.shape[:3]
    lignes = []
    for c in coupes[:maxi]:
        L = Image.new('RGB', (70 + (avant + apres)*w, h + 26), (24, 24, 24)); d = ImageDraw.Draw(L)
        d.text((4, 4), f'{c//fps//60}:{c//fps%60:02d}+{c%fps:02d}', fill=(230, 230, 230), font=FONT)
        for k, f in enumerate(range(c - avant, c + apres)):
            if 0 <= f < n:
                L.paste(Image.fromarray(images[f]), (70 + k*w, 0))
                if env:
                    hh = int((env[f] + 60) / 60 * 22)
                    d.rectangle([70 + k*w + 2, h + 24 - hh, 70 + (k+1)*w - 3, h + 24], fill=(110, 170, 210))
        d.line([70 + avant*w, 0, 70 + avant*w, h + 26], fill=(255, 255, 255), width=2)
        for f, t in marqueurs:
            if c - avant <= f < c + apres:
                x = 70 + (f - c + avant)*w; d.line([x, 0, x, h + 26], fill=(230, 60, 60), width=2)
                d.text((x + 3, h + 2), str(t)[:14], fill=(230, 90, 90), font=FONT)
        lignes.append(L)
    if not lignes:
        return
    P = Image.new('RGB', (max(l.width for l in lignes), sum(l.height + 3 for l in lignes)), (0, 0, 0))
    y = 0
    for l in lignes:
        P.paste(l, (0, y)); y += l.height + 3
    P.save(sortie, optimize=True)


def courbe(n, fps, coupes, act, marqueurs, fenetre, sortie):
    W, H = 900, 260
    P = Image.new('RGB', (W, H), (20, 20, 20)); d = ImageDraw.Draw(P)
    duree = n / fps
    xs = lambda t: 40 + (W - 60) * t / max(duree, 1e-6)
    dens = []
    for k in range(0, n, max(1, fps // 2)):
        t = k / fps
        nb = sum(1 for c in coupes if t - fenetre/2 <= c/fps < t + fenetre/2)
        dens.append((t, nb * 60 / fenetre))
    dmax = max([v for _, v in dens] + [1])
    for (t0, v0), (t1, v1) in zip(dens, dens[1:]):
        d.line([xs(t0), 120 - 100*v0/dmax, xs(t1), 120 - 100*v1/dmax], fill=(240, 200, 80), width=2)
    d.text((44, 4), f'coupes/min (fenêtre {fenetre} s), max {dmax:.0f}', fill=(240, 200, 80), font=FONT)
    vals = [v for v in act if v is not None]
    amax = max(vals + [1e-6])
    for k, v in enumerate(act):
        if v is not None:
            hh = 100 * v / amax; d.line([xs(k/fps), 245, xs(k/fps), 245 - hh], fill=(110, 170, 210))
    d.text((44, 134), f'activité hors coupes (YDIF réduit, max {amax:.2f})', fill=(110, 170, 210), font=FONT)
    for c in coupes:
        d.line([xs(c/fps), 125, xs(c/fps), 130], fill=(255, 255, 255))
    for f, t in marqueurs:
        d.line([xs(f/fps), 0, xs(f/fps), H], fill=(230, 60, 60)); d.text((xs(f/fps) + 2, 18), str(t)[:12], fill=(230, 90, 90), font=FONT)
    P.save(sortie, optimize=True)


def main():
    a = sys.argv[1:]
    if not a or '--sortie' not in a:
        print(__doc__); sys.exit(1)
    video = a[0]; opt = lambda k, dft: a[a.index(k)+1] if k in a else dft
    sortie = opt('--sortie', None); avant = int(opt('--avant', 6)); apres = int(opt('--apres', 6))
    fenetre = float(opt('--fenetre', 10))
    fps, W, H = sonde(video)
    sources, marqueurs = {}, []
    if '--edl' in a:
        sources['edl'], m = lire_edl(opt('--edl', None), fps); marqueurs += m
    if '--otio' in a:
        sources['otio'], m = lire_otio(opt('--otio', None), fps); marqueurs += m
    if '--scdet' in a:
        i = a.index('--scdet'); s = a[i+1] if i+1 < len(a) and not a[i+1].startswith('--') else '10'
        sources['scdet'] = scdet(video, s)
    if not sources:
        sources['scdet'] = scdet(video, '10')
    ref = next(iter(sources))
    coupes = sources[ref]
    tw = 64; th = max(2, int(round(tw * H / W / 2)) * 2)
    vignettes = lire_images(video, tw, th)
    r = int(opt('--reduction', 8))
    petites = lire_images(video, max(8, W // r), max(8, H // r))
    n = len(vignettes)
    env = enveloppe(video, fps, n)
    act = activite(petites, coupes)
    bande(vignettes, env, coupes, marqueurs, avant, apres, fps, sortie + '-bande.png')
    courbe(n, fps, coupes, act, marqueurs, fenetre, sortie + '-courbe.png')
    plans = [b - a_ for a_, b in zip([0] + coupes, coupes + [n])]
    vals = [v for v in act if v is not None]
    res = {'video': video, 'fps': fps, 'images': n, 'reference': ref, 'coupes': coupes, 'marqueurs': marqueurs,
           'duree_plan_mediane_s': float(np.median(plans)) / fps if plans else None,
           'coupes_par_min': len(coupes) * 60 * fps / max(n, 1),
           'activite_hors_coupes_moy': float(np.mean(vals)) if vals else None,
           # plancher = 5e centile (plans fixes : il ne reste que le grain) ; activité nette = moyenne - plancher
           'plancher_grain': float(np.percentile(vals, 5)) if vals else None,
           'activite_nette_moy': float(np.mean(vals) - np.percentile(vals, 5)) if vals else None,
           # soustraction quadratique image par image (signal et grain indépendants)
           'activite_nette_quad': float(np.mean(np.sqrt(np.maximum(0, np.array(vals)**2 - np.percentile(vals, 5)**2)))) if vals else None,
           'fondus': FONDUS,
           'comparaisons': {k: compare(coupes, v) for k, v in sources.items() if k != ref}}
    json.dump(res, open(sortie + '.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({k: res[k] for k in ('reference', 'coupes', 'duree_plan_mediane_s', 'coupes_par_min',
                                          'activite_hors_coupes_moy', 'plancher_grain', 'activite_nette_moy', 'activite_nette_quad', 'fondus', 'comparaisons')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
