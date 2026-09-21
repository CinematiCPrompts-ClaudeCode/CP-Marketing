// OCR helper for check_video.sh — reads on-screen text out of extracted video frames.
// Language correction is OFF on purpose: it would "fix" garbled AI label text
// (SPARALING -> SPARKLING) and hide exactly the defect we are looking for.
import Foundation
import Vision
import AppKit

for path in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: path),
          let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    let lines = (req.results ?? []).compactMap { ($0 as? VNRecognizedTextObservation)?.topCandidates(1).first?.string }
    for l in lines { print("\((path as NSString).lastPathComponent)\t\(l)") }
}
