// Boucle "cycle" écrite à la main avec valueAtTime : utile pour comprendre,
// ou pour boucler seulement entre deux clés choisies (ici la 1re et la dernière).
var t0 = key(1).time;
var t1 = key(numKeys).time;
var d = t1 - t0;
(numKeys > 1 && time > t1) ? valueAtTime(t0 + ((time - t1) % d)) : value;
