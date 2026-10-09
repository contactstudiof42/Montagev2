// mock.js — harnais Node SIMPLIFIÉ des globals d'expressions After Effects.
// Objectif : vérifier la logique mathématique des expressions du labo.
// Ce n'est PAS After Effects : wiggle(), ease(), loopOut() sont des approximations.
// Toute valeur obtenue ici doit être reconfirmée dans AE (phase 2).
'use strict';
const fs = require('fs');
const vm = require('vm');
const path = require('path');

// ---------- maths vectorielles façon AE ----------
const isArr = Array.isArray;
const zip = (a, b, f) => isArr(a) ? a.map((x, i) => f(x, isArr(b) ? b[i] : b)) : (isArr(b) ? b.map(y => f(a, y)) : f(a, b));
const add = (a, b) => zip(a, b, (x, y) => x + y);
const sub = (a, b) => zip(a, b, (x, y) => x - y);
const mul = (a, k) => zip(a, k, (x, y) => x * y);
const div = (a, k) => zip(a, k, (x, y) => x / y);
const length = (a, b) => { const v = b === undefined ? a : sub(a, b); return isArr(v) ? Math.hypot(...v) : Math.abs(v); };
const clamp = (v, lo, hi) => zip(v, 0, x => Math.min(Math.max(x, Math.min(lo, hi)), Math.max(lo, hi)));

// ---------- interpolation ----------
// linear(t, tMin, tMax, v1, v2) ou linear(t, v1, v2) avec t dans [0,1]
function interp(shape) {
  return function (t, a, b, c, d) {
    let tMin = a, tMax = b, v1 = c, v2 = d;
    if (c === undefined) { tMin = 0; tMax = 1; v1 = a; v2 = b; }
    let u = tMax === tMin ? (t >= tMax ? 1 : 0) : (t - tMin) / (tMax - tMin);
    u = Math.min(Math.max(u, 0), 1);
    const s = shape(u);
    return zip(v1, v2, (x, y) => x + (y - x) * s);
  };
}
// Approximation : la courbe exacte d'ease() d'AE n'est pas documentée publiquement.
const linear = interp(u => u);
const ease = interp(u => 0.5 - 0.5 * Math.cos(Math.PI * u));
const easeIn = interp(u => 1 - Math.cos(u * Math.PI / 2));   // part lentement
const easeOut = interp(u => Math.sin(u * Math.PI / 2));      // arrive lentement

// ---------- bruit déterministe pour wiggle ----------
function hash(n) { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); }
function noise1(x, seed) { // value noise lissé, sortie dans [-1,1]
  const i = Math.floor(x), f = x - i, u = f * f * (3 - 2 * f);
  const a = hash(i + seed * 1000) * 2 - 1, b = hash(i + 1 + seed * 1000) * 2 - 1;
  return a + (b - a) * u;
}

// ---------- propriété keyframée ----------
// keys : [{t, v, interp:'linear'|'hold'|'ease'}]
function makeProperty(keys, staticValue) {
  keys = (keys || []).slice().sort((a, b) => a.t - b.t);
  function valueAtTime(t) {
    if (!keys.length) return staticValue;
    if (t <= keys[0].t) return keys[0].v;
    if (t >= keys[keys.length - 1].t) return keys[keys.length - 1].v;
    for (let i = 0; i < keys.length - 1; i++) {
      const k0 = keys[i], k1 = keys[i + 1];
      if (t >= k0.t && t < k1.t) {
        if (k0.interp === 'hold') return k0.v;
        const f = k0.interp === 'ease' ? ease : linear;
        return f(t, k0.t, k1.t, k0.v, k1.v);
      }
    }
  }
  const dt = 1e-4;
  const prop = {
    numKeys: keys.length,
    key: i => ({ time: keys[i - 1].t, value: keys[i - 1].v, index: i }),
    nearestKey: t => { let best = 0; keys.forEach((k, i) => { if (Math.abs(k.t - t) < Math.abs(keys[best].t - t)) best = i; }); return prop.key(best + 1); },
    valueAtTime,
    velocityAtTime: t => div(sub(valueAtTime(t + dt / 2), valueAtTime(t - dt / 2)), dt),
    loopOut(type = 'cycle', n = 0) { // approximation du comportement documenté
      const t = prop._time; if (keys.length < 2) return valueAtTime(t);
      const first = n > 0 ? keys[Math.max(0, keys.length - 1 - n)] : keys[0], last = keys[keys.length - 1];
      if (t <= last.t) return valueAtTime(t);
      const d = last.t - first.t, e = t - last.t, c = Math.floor(e / d), r = e - c * d;
      if (type === 'cycle') return valueAtTime(first.t + r);
      if (type === 'pingpong') return c % 2 === 0 ? valueAtTime(last.t - r) : valueAtTime(first.t + r);
      if (type === 'offset') return add(valueAtTime(first.t + r), mul(sub(last.v, first.v), c + 1));
      if (type === 'continue') return add(last.v, mul(prop.velocityAtTime(last.t - 1e-3), e));
      throw new Error('type loopOut inconnu : ' + type);
    },
  };
  return prop;
}

// ---------- contexte complet ----------
function makeContext(o = {}) {
  const fps = o.fps || 25;
  const prop = makeProperty(o.keys, o.value);
  const sliders = o.sliders || {};
  const layers = o.layers || {};
  const ctx = {
    time: o.time || 0,
    thisComp: {
      frameDuration: 1 / fps,
      duration: o.compDuration || 10,
      layer: id => {
        const L = layers[id];
        if (!L) throw new Error('calque inexistant : ' + id);
        const p = makeProperty(L.keys, L.value);
        return { transform: { position: p, rotation: p, scale: p, opacity: p }, position: p };
      },
    },
    index: o.index || 1,
    inPoint: o.inPoint || 0,
    outPoint: o.outPoint || 10,
    source: { duration: o.sourceDuration || 10 },
    timeToFrames: (t, f = fps) => Math.floor(t * f),
    framesToTime: (fr, f = fps) => fr / f,
    effect: name => {
      if (!(name in sliders)) throw new Error('effet manquant : ' + name);
      return () => sliders[name]; // effect("X")("Slider") -> valeur
    },
    add, sub, mul, div, length, clamp, linear, ease, easeIn, easeOut,
    Math, Number, String, isNaN,
  };
  Object.assign(ctx, {
    value: prop.numKeys ? undefined : o.value,
    numKeys: prop.numKeys,
    key: prop.key,
    nearestKey: prop.nearestKey,
    valueAtTime: prop.valueAtTime,
    velocityAtTime: prop.velocityAtTime,
    loopOut: (type, n) => { prop._time = ctx.time; return prop.loopOut(type, n); },
    posterizeTime: ups => { ctx.time = Math.floor(ctx.time * ups + 1e-9) / ups; return ups; },
    wiggle: (freq, amp, oct = 1, ampMult = 0.5, t) => {
      const tt = t === undefined ? ctx.time : t;
      return isArr(ctx.value)
        ? ctx.value.map((v, i) => v + amp * octaves(tt * freq, i + 1, oct, ampMult))
        : ctx.value + amp * octaves(tt * freq, 1, oct, ampMult);
    },
  });
  if (prop.numKeys) ctx.value = prop.valueAtTime(ctx.time);
  return ctx;
}
function octaves(x, seed, oct, ampMult) {
  let s = 0, a = 1, f = 1, norm = 0;
  for (let k = 0; k < oct; k++) { s += a * noise1(x * f, seed + k * 7); norm += a; a *= ampMult; f *= 2; }
  return s / norm;
}

// Évalue un fichier .js d'expression : la valeur de la dernière instruction est le résultat (comme AE).
function run(file, opts) {
  const code = fs.readFileSync(path.resolve(__dirname, file), 'utf8');
  const ctx = makeContext(opts);
  return vm.runInNewContext(code, ctx, { filename: file });
}

module.exports = { run, makeContext, linear, ease };
