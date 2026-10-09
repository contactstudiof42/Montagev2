// tests.js — lance : node tests.js  (depuis labo/ae-expressions)
'use strict';
const { execFileSync } = require('child_process');
const fs = require('fs');
const { run } = require('./mock');
const out = [];
let ok = 0, ko = 0;
function check(nom, cond, detail) { (cond ? ok++ : ko++); out.push(`| ${cond ? 'PASSE' : 'ÉCHOUE'} | ${nom} | ${detail} |`); }
const r = x => Array.isArray(x) ? '[' + x.map(v => +v.toFixed(2)).join(', ') + ']' : (typeof x === 'number' ? +x.toFixed(3) : JSON.stringify(x));

// (a) syntaxe
const files = fs.readdirSync(__dirname).filter(f => /^\d\d-.*\.js$/.test(f)).sort();
for (const f of files) {
  try { execFileSync(process.execPath, ['--check', f], { cwd: __dirname, stdio: 'pipe' }); check('node --check ' + f, true, 'syntaxe OK'); }
  catch (e) { check('node --check ' + f, false, String(e.stderr).split('\n')[0]); }
}

// (b) logique
// 01 wiggle : reste dans value ± amp, varie dans le temps, déterministe
{
  const o = t => ({ time: t, value: [960, 540], sliders: { 'Fréquence': 2, 'Amplitude': 30 } });
  let maxDev = 0; const vals = [];
  for (let t = 0; t < 10; t += 0.04) { const v = run('01-wiggle-sliders.js', o(t)); vals.push(v); maxDev = Math.max(maxDev, Math.abs(v[0] - 960), Math.abs(v[1] - 540)); }
  check('01 wiggle borné', maxDev <= 30, `écart max ${maxDev.toFixed(2)} px pour amp 30`);
  check('01 wiggle déterministe', r(run('01-wiggle-sliders.js', o(3.2))) === r(run('01-wiggle-sliders.js', o(3.2))), `t=3.2 -> ${r(run('01-wiggle-sliders.js', o(3.2)))} (deux fois)`);
}
// 02/03 loopOut (mock) : clés 0s->0, 1s->100
{
  const keys = [{ t: 0, v: 0, interp: 'linear' }, { t: 1, v: 100, interp: 'linear' }];
  const c = run('02-loopout-cycle.js', { time: 2.25, keys }), p = run('03-loopout-pingpong.js', { time: 1.25, keys });
  check('02 loopOut cycle (mock)', Math.abs(c - 25) < 1e-6, `t=2.25 -> ${r(c)} (attendu 25)`);
  check('03 loopOut pingpong (mock)', Math.abs(p - 75) < 1e-6, `t=1.25 -> ${r(p)} (attendu 75, retour)`);
}
// 04 boucle manuelle : doit égaler la logique cycle
{
  const keys = [{ t: 0.5, v: 0, interp: 'linear' }, { t: 1.5, v: 200, interp: 'linear' }];
  const a = run('04-boucle-manuelle.js', { time: 3.75, keys }), b = run('04-boucle-manuelle.js', { time: 1.0, keys });
  check('04 boucle manuelle après clés', Math.abs(a - 50) < 1e-6, `t=3.75 -> ${r(a)} (attendu 50)`);
  check('04 boucle manuelle pendant clés', Math.abs(b - 100) < 1e-6, `t=1.0 -> ${r(b)} (attendu 100)`);
}
// 05 overshoot : clés linéaires 0->100 en 0.5 s (v=200/s)
{
  const keys = [{ t: 0, v: 0, interp: 'linear' }, { t: 0.5, v: 100, interp: 'linear' }];
  let max = -Infinity, tMax = 0; const samples = [];
  for (let f = 0; f <= 100; f++) { const t = f / 25; const v = run('05-overshoot-inertiel.js', { time: t, keys }); samples.push(v); if (v > max) { max = v; tMax = t; } }
  const pendant = run('05-overshoot-inertiel.js', { time: 0.25, keys });
  const fin = run('05-overshoot-inertiel.js', { time: 3.0, keys });
  check('05 overshoot dépasse la cible', max > 100, `pic ${r(max)} à t=${tMax.toFixed(2)} s (cible 100 ; dépassement théorique max ≈ v/w·e^(-decay·t))`);
  check('05 overshoot se pose', Math.abs(fin - 100) < 0.01, `t=3 s -> ${r(fin)}`);
  check('05 inactif pendant les clés', Math.abs(pendant - 50) < 1e-6, `t=0.25 -> ${r(pendant)} (attendu 50)`);
  const v2 = run('05-overshoot-inertiel.js', { time: 0.6, keys: [{ t: 0, v: [0, 0], interp: 'linear' }, { t: 0.5, v: [100, 50], interp: 'linear' }] });
  check('05 overshoot sur tableau 2D', Array.isArray(v2) && v2[0] > 100 && v2[1] > 50, `t=0.6 -> ${r(v2)} (1er essai à t=0.7 tombait pile sur un passage à zéro : sin(0.2·2π·2.5)=0)`);
}
// 06 écho
{
  const layers = { 1: { keys: [{ t: 0, v: [0, 0] }, { t: 1, v: [100, 0] }] } };
  const v = run('06-echo-decalage.js', { time: 0.6, index: 2, layers, sliders: { 'Retard (images)': 5 } });
  check('06 écho (5 images de retard)', Math.abs(v[0] - 40) < 1e-6, `t=0.6 s -> ${r(v)} (leader à t=0.4 -> 40)`);
}
// 07 mapping
{
  const vals = [0, 20, 40, 60, 100].map(p => run('07-mapping-linear-ease.js', { sliders: { Progression: p } }));
  check('07 ease() mappe et borne', vals[0] === 0 && vals[1] === 0 && Math.abs(vals[2] - 50) < 1e-9 && vals[3] === 100 && vals[4] === 100, `p=0,20,40,60,100 -> ${vals.map(r).join(', ')}`);
}
// 08 time remap
{
  const v = run('08-time-remap-vitesse.js', { time: 3, inPoint: 1, sourceDuration: 4, sliders: { 'Vitesse %': 50 } });
  const v2 = run('08-time-remap-vitesse.js', { time: 20, inPoint: 1, sourceDuration: 4, sliders: { 'Vitesse %': 50 } });
  check('08 remap 50 %', Math.abs(v - 1) < 1e-9, `t=3 s, in=1 s -> ${r(v)} s de source (attendu 1)`);
  check('08 remap borné à la fin', Math.abs(v2 - 3.96) < 1e-9, `t=20 s -> ${r(v2)} s (dernière image source)`);
}
// 09 compteur
{
  const s = { Cible: 12500, 'Début (s)': 1, 'Durée (s)': 2 };
  const a = run('09-compteur-texte.js', { time: 0, sliders: s }), b = run('09-compteur-texte.js', { time: 3, sliders: s }), m = run('09-compteur-texte.js', { time: 2, sliders: s });
  check('09 compteur début', a === '0', `t=0 -> "${a}"`);
  check('09 compteur fin + séparateur', b === '12 500', `t=3 -> "${b.replace(' ', '⍽')}" (⍽ = espace fine insécable)`);
  check('09 compteur mi-course > moitié (easeOut)', parseInt(m.replace(' ', '')) > 6250, `t=2 -> "${m.replace(' ', '⍽')}"`);
}
// 10 posterize
{
  const o = t => ({ time: t, value: 0 });
  const a = run('10-posterize-wiggle.js', o(0.13)), b = run('10-posterize-wiggle.js', o(0.24)), c = run('10-posterize-wiggle.js', o(0.26));
  check('10 posterizeTime tient la valeur', a === b && b !== c, `t=0.13 -> ${r(a)}, t=0.24 -> ${r(b)}, t=0.26 -> ${r(c)} (palier de 1/8 s)`);
}
// 11 respiration : 30 / 10 / 45 / 15 images à 25 i/s = 4 s
{
  const s = { Inspiration: 30, 'Rétention': 10, Expiration: 45, Pause: 15, 'Amplitude %': 4 };
  const at = t => run('11-respiration.js', { time: t, value: [100, 100], sliders: s })[0];
  const pts = [0, 0.6, 1.2, 1.5, 1.6, 2.5, 3.4, 3.8, 4.6].map(t => `${t}s:${at(t).toFixed(2)}`);
  check('11 respiration plein à la rétention', Math.abs(at(1.4) - 104) < 1e-9, pts.join(' '));
  check('11 respiration vide en pause et cyclique', Math.abs(at(3.8) - 100) < 1e-9 && Math.abs(at(4.6) - at(0.6)) < 1e-9, 'pause = 100 %, t=4.6 = t=0.6');
  // asymétrie : à mi-durée de l'expiration on a déjà relâché plus de la moitié (easeOut)
  check('11 expiration asymétrique', at(1.6 + 0.9) < 102, `mi-expiration -> ${at(2.5).toFixed(2)} % (< 102 = relâche rapide puis se pose)`);
}

const md = ['| Résultat | Test | Détail |', '|---|---|---|', ...out].join('\n');
fs.writeFileSync(__dirname + '/resultats-tests.md', md + `\n\nTotal : ${ok} passent, ${ko} échouent. Node ${process.version}.\n`);
console.log(md); console.log(`\nTotal : ${ok} passent, ${ko} échouent`);
