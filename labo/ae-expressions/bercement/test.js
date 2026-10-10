// Bercement qui ralentit après un événement (marqueur) : amplitude ET période qui glissent.
// Piège testé : sin(2π t / P(t)) avec P qui varie ne donne PAS la fréquence 1/P :
// fréquence instantanée = 1/P − t·P'/P²  → le mouvement se fige puis repart (« hésitation »).
// Correct : intégrer la phase, φ(t) = 2π ∫ dt / P(t)  (forme fermée si P varie linéairement).
// Node : node test.js  (la syntaxe est celle d'une expression AE ; comportement réel dans AE : phase 2)
function P(t, t0, d, P0, P1) { const k = Math.min(1, Math.max(0, (t - t0) / d)); return P0 + (P1 - P0) * k; }
function phaseNaive(t, t0, d, P0, P1) { return 2 * Math.PI * t / P(t, t0, d, P0, P1); }
function phaseIntegree(t, t0, d, P0, P1) {
  // ∫0^t dt/P : avant t0 : t/P0 ; pendant la rampe P = P0 + a(τ) : (1/a) ln(P(t)/P0) ; après : + (t − t0 − d)/P1
  const a = (P1 - P0) / d;
  if (t <= t0) return 2 * Math.PI * t / P0;
  const tr = Math.min(t, t0 + d), rampe = Math.abs(a) < 1e-9 ? (tr - t0) / P0 : Math.log(P(tr, t0, d, P0, P1) / P0) / a;
  return 2 * Math.PI * (t0 / P0 + rampe + Math.max(0, t - t0 - d) / P1);
}
const t0 = 3.5, d = 4, P0 = 1.6, P1 = 3.2, fps = 24;
const res = { naive: [], integree: [], attendue: [] };
for (let f = 1; f < 10 * fps; f++) {
  const t = f / fps, dt = 1 / fps;
  res.naive.push((phaseNaive(t + dt, t0, d, P0, P1) - phaseNaive(t, t0, d, P0, P1)) / dt / (2 * Math.PI));
  res.integree.push((phaseIntegree(t + dt, t0, d, P0, P1) - phaseIntegree(t, t0, d, P0, P1)) / dt / (2 * Math.PI));
  res.attendue.push(1 / P(t + dt / 2, t0, d, P0, P1));
}
const err = (a) => Math.max(...a.map((v, i) => Math.abs(v - res.attendue[i])));
const min = (a) => Math.min(...a);
console.log("fréquence attendue : de", (1 / P0).toFixed(3), "à", (1 / P1).toFixed(3), "Hz");
console.log("naïve    : min", min(res.naive).toFixed(3), "Hz ; écart max", err(res.naive).toFixed(3), "Hz");
console.log("intégrée : min", min(res.integree).toFixed(3), "Hz ; écart max", err(res.integree).toFixed(4), "Hz");
// Expression AE correspondante (rotation d'un calque ; marqueur n°1 = l'événement) :
const expr = `
var amp0 = 5, amp1 = 1.2, P0 = 1.6, P1 = 3.2, d = 4;
var t0 = (marker.numKeys > 0) ? marker.key(1).time : 1e9;
var k = clamp((time - t0) / d, 0, 1), a = (P1 - P0) / d, ph;
if (time <= t0) ph = time / P0;
else ph = t0 / P0 + Math.log((P0 + a * Math.min(time - t0, d)) / P0) / a + Math.max(0, time - t0 - d) / P1;
value + ease(k, 0, 1, amp0, amp1) * Math.sin(2 * Math.PI * ph);`;
new Function("marker", "time", "value", "clamp", "ease", expr.replace(/;\s*$/, "") .replace(/\nvalue \+/, "\nreturn value +"));
console.log("syntaxe de l'expression : OK");
