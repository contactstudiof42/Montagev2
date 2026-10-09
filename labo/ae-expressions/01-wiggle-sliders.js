// Wiggle piloté par deux Sliders sur le calque (Effet > Paramètres pour expressions > Paramètre glissière).
// Renommer les sliders exactement "Fréquence" et "Amplitude".
// Fréquence en oscillations/seconde, Amplitude en unités de la propriété (px, degrés…).
var freq = effect("Fréquence")("Slider");
var amp = effect("Amplitude")("Slider");
wiggle(freq, amp);
