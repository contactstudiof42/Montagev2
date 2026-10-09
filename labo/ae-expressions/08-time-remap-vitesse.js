// Remappage temporel (Time Remap) piloté par un slider "Vitesse %" (100 = normal, 50 = ralenti x2).
// Vitesse CONSTANTE uniquement : si le slider est animé, ce calcul ne l'intègre pas (voir RESULTATS).
var v = effect("Vitesse %")("Slider") / 100;
clamp((time - inPoint) * v, 0, source.duration - thisComp.frameDuration);
