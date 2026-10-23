// OCR d'un PDF scanné avec les frameworks de macOS (PDFKit + Vision), sans rien installer.
// Compiler : swiftc -O labo/outils/ocr_pdf.swift -o /tmp/ocr_pdf
// Lancer   : /tmp/ocr_pdf livre.pdf sortie.txt PREMIERE DERNIERE [dossier_png]
// Sortie : une ligne "=== PAGE n ===" par page du PDF (page du PDF, pas du livre : recaler sur les en-têtes).
// Langues : fr-FR, en-US. ~0,7 s par page (427 pages en 5 min, 2026-10-23).
import PDFKit
import Vision
import AppKit
// usage: ocr in.pdf out.txt first last [pngdir]
let a = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: a[1]))!
let first = Int(a[3])!, last = min(Int(a[4])!, doc.pageCount)
let pngDir: String? = a.count > 5 ? a[5] : nil
var out = ""
for i in (first-1)..<last {
  let page = doc.page(at: i)!
  let box = page.bounds(for: .mediaBox)
  let scale: CGFloat = 2000.0 / max(box.width, box.height)
  let w = Int(box.width*scale), h = Int(box.height*scale)
  let cs = CGColorSpaceCreateDeviceRGB()
  let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0, space: cs, bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)!
  ctx.setFillColor(CGColor(red:1,green:1,blue:1,alpha:1)); ctx.fill(CGRect(x:0,y:0,width:w,height:h))
  ctx.scaleBy(x: scale, y: scale)
  page.draw(with: .mediaBox, to: ctx)
  let img = ctx.makeImage()!
  if let d = pngDir {
    let rep = NSBitmapImageRep(cgImage: img)
    try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: "\(d)/p\(i+1).png"))
  }
  let req = VNRecognizeTextRequest()
  req.recognitionLevel = .accurate
  req.recognitionLanguages = ["fr-FR", "en-US"]
  req.usesLanguageCorrection = true
  try! VNImageRequestHandler(cgImage: img).perform([req])
  let lines = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }
  out += "\n\n=== PAGE \(i+1) ===\n" + lines.joined(separator: "\n")
}
try! out.write(toFile: a[2], atomically: true, encoding: .utf8)
