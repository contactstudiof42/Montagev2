// E0 : une composition de 2 s, un texte neutre en Inter blanc sur noir, file de rendu en PNG, .aep enregistré.
// Lancé par : osascript -e 'tell application "Adobe After Effects 2026" to DoScriptFile (POSIX file "<ce fichier>")'
var W = "/Volumes/SSD FAST/Montage-IA/videos/phase-3/tests-techniques/_travail/";
var LOG = W + "e0_ae_log.txt";
var out = [];
try {
  app.beginUndoGroup("E0");
  while (app.project.renderQueue.numItems) app.project.renderQueue.item(1).remove();
  for (var j = app.project.numItems; j >= 1; j--) if (app.project.item(j).name == "E0_Texte") app.project.item(j).remove();
  var comp = app.project.items.addComp("E0_Texte", 1920, 1080, 1, 2, 25);
  comp.bgColor = [0, 0, 0];
  var t = comp.layers.addText("Essai technique");
  var doc = t.property("Source Text").value;
  // « Inter-Regular » n'existe pas sur ce Mac : AE le remplace en silence par Helvetica (isSubstitute).
  // Inter y est en coupes statiques par taille optique : Inter18pt, Inter24pt, Inter28pt (display).
  doc.font = "Inter28pt-Regular"; doc.fontSize = 96;
  doc.fontCapsOption = FontCapsOption.FONT_NORMAL_CAPS; // allCaps est en lecture seule ; le panneau Caractère déteint sur les textes créés par script
  doc.fillColor = [1, 1, 1];
  doc.applyFill = true; doc.applyStroke = false; doc.justification = ParagraphJustification.CENTER_JUSTIFY;
  t.property("Source Text").setValue(doc);
  var fo = t.property("Source Text").value.fontObject;
  if (fo.isSubstitute) throw new Error("police remplacée : " + fo.postScriptName + " -> " + fo.location);
  var r = t.sourceRectAtTime(0, false);
  t.property("Transform").property("Anchor Point").setValue([r.left + r.width / 2, r.top + r.height / 2]);
  t.property("Transform").property("Position").setValue([960, 540]);
  app.endUndoGroup();
  out.push("police=" + fo.postScriptName + " (" + fo.location + ") capitales=" + t.property("Source Text").value.allCaps);

  var rq = app.project.renderQueue.items.add(comp);
  var om = rq.outputModule(1);
  var tpl = om.templates; out.push("modeles=" + tpl.join(" ; "));
  // Le format n'est pas réglable par script dans AE 26.3 (« Format » en lecture seule) : on prend un modèle
  // PNG s'il existe (à créer une fois à la main), sinon la séquence TIFF sans perte, convertie en PNG ensuite.
  var png = null, ext = "tif";
  for (var i = 0; i < tpl.length; i++) if (/PNG/i.test(tpl[i])) { png = tpl[i]; break; }
  if (png) { om.applyTemplate(png); ext = "png"; } else om.applyTemplate("TIFF Sequence with Alpha");
  out.push("modele=" + (png || "TIFF Sequence with Alpha"));
  om.file = new File(W + "e0_ae_[##]." + ext);
  app.project.save(new File(W + "e0_ae.aep"));
  out.push("enregistre=" + app.project.file.fsName);
} catch (e) { out.push("ERREUR ligne " + e.line + " : " + e.toString()); }
var f = new File(LOG); f.encoding = "UTF-8"; f.lineFeed = "Unix"; f.open("w"); f.write(out.join("\n")); f.close();
