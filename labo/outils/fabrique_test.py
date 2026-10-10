#!/usr/bin/env python3
"""Vidéo de test à vérité terrain pour coupes.py : N plans (durées connues), contenus en mouvement
différents, un son par plan ; écrit aussi l'EDL CMX3600 et l'OTIO exacts. Option --grain (bruit temporel fort).
Usage : fabrique_test.py DOSSIER [--grain]"""
import sys, subprocess, os
D = sys.argv[1]; grain = '--grain' in sys.argv; os.makedirs(D, exist_ok=True)
FPS = 25
durees = [50, 12, 30, 8, 75, 20, 40, 15, 60]          # images ; plans très courts (8, 12) inclus
sources = ['testsrc2', 'mandelbrot', 'testsrc', 'smptebars', 'rgbtestsrc', 'cellauto', 'life', 'testsrc2', 'mandelbrot']
filt, inputs = [], []
for i, (n, s) in enumerate(zip(durees, sources)):
    inputs += ['-f', 'lavfi', '-i', f'{s}=s=320x180:r={FPS}', '-f', 'lavfi', '-i', f'sine=f={220*(1+i%4)}:r=48000']
    vf = f'[{2*i}:v]trim=start_frame={i*7}:end_frame={i*7+n},setpts=PTS-STARTPTS,format=yuv420p,hue=h={i*40}'
    if i == 8: vf += ',vflip'                                   # même source que le plan 2 mais autre cadre
    filt.append(vf + f'[v{i}]')
    vol = 0.05 if i % 3 == 0 else 0.5                           # un plan sur trois presque silencieux
    filt.append(f'[{2*i+1}:a]atrim=end={n/FPS},asetpts=PTS-STARTPTS,volume={vol}[a{i}]')
cc = ''.join(f'[v{i}][a{i}]' for i in range(len(durees)))
g = ',noise=alls=40:allf=t' if grain else ''
filt.append(f'{cc}concat=n={len(durees)}:v=1:a=1[vc][a]'); filt.append(f'[vc]null{g}[v]')
out = os.path.join(D, 'test' + ('-grain' if grain else '') + '.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(filt), '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-crf', '18', '-c:a', 'aac', out], check=True)
tc = lambda f: f'{f//FPS//3600:02d}:{f//FPS//60%60:02d}:{f//FPS%60:02d}:{f%FPS:02d}'
t, ed = 3600*FPS, ['TITLE: test', 'FCM: NON-DROP FRAME', '']   # timeline à 01:00:00:00
for i, n in enumerate(durees):
    ed.append(f'{i+1:03d}  PLAN{i+1:02d}   V     C        {tc(0)} {tc(n)} {tc(t)} {tc(t+n)}'); t += n
ed.append(f'* LOC: {tc(3600*FPS+170)} RED relance'); ed.append(f'* LOC: {tc(3600*FPS+250)} RED chute')
open(os.path.join(D, 'test.edl'), 'w').write('\n'.join(ed) + '\n')
import opentimelineio as otio
tl = otio.schema.Timeline(name='test'); tr = otio.schema.Track(kind=otio.schema.TrackKind.Video); tl.tracks.append(tr)
for i, n in enumerate(durees):
    tr.append(otio.schema.Clip(name=f'PLAN{i+1:02d}', source_range=otio.opentime.TimeRange(
        otio.opentime.RationalTime(0, FPS), otio.opentime.RationalTime(n, FPS))))
tr.markers.append(otio.schema.Marker(name='relance', marked_range=otio.opentime.TimeRange(otio.opentime.RationalTime(170, FPS))))
otio.adapters.write_to_file(tl, os.path.join(D, 'test.otio'))
c, v = [], 0
for n in durees[:-1]: v += n; c.append(v)
print(out, 'coupes vraies :', c)
