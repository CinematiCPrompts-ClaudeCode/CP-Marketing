#!/bin/bash
# check_video.sh <video> — the pixel half of the ship gate.
#
# ./check.sh reads a package's .md and CANNOT see a rendered cut. That gap has now
# shipped the SAME banned claim twice: the 14.08 otter reel and the 08.09 marketing
# reel both carried "NO WASTED CREDITS" burned into the end card. A prose rule that
# says "remember to look at the pixels" has failed twice, so this looks for us.
#
# Extracts a frame per second, OCRs each one (Vision, via scripts/ocr_frames.swift),
# and matches the text against the banned list in brand/claims.md.
set -uo pipefail
V="${1:?usage: ./scripts/check_video.sh <video>}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$(mktemp -d)"; trap 'rm -rf "$OUT"' EXIT

echo "▸ extracting frames from $(basename "$V")"
ffmpeg -v error -y -i "$V" -vf fps=1 "$OUT/f_%03d.png" || { echo "ffmpeg failed"; exit 2; }
N=$(ls "$OUT"/f_*.png 2>/dev/null | wc -l | tr -d ' ')
echo "▸ $N frames, running OCR"
swift "$ROOT/scripts/ocr_frames.swift" "$OUT"/f_*.png 2>/dev/null | sort -u > "$OUT/text.tsv"

# Banned strings, case-insensitive. Sourced from brand/claims.md.
BANNED=(
  "no wasted credits" "zero waste" "without wasting"
  "first try" "lands first" "guaranteed"
  # "every time" alone is NOT banned — the approved promotional text reads "Pick the lighting and
  # the camera angle every time", which is true (those two dials are universal). Only the
  # outcome-guarantee constructions are:
  "perfect every time" "works every time" "shot every time"
  "harsh noon" "overcast"
  "storyboard"
  "sora"
  "gemini" "runway" "kling" "seedance" "nano banana"
)
FAIL=0
echo
for b in "${BANNED[@]}"; do
  if hit=$(grep -i -- "$b" "$OUT/text.tsv"); then
    echo "✗ BANNED: \"$b\""
    echo "$hit" | sed 's/^/    /'
    FAIL=1
  fi
done

# "golden hour" must be capitalised as Golden Hour
if grep -- "golden hour" "$OUT/text.tsv" | grep -qv "Golden Hour"; then
  echo "✗ lowercase \"golden hour\" — the live display name is Golden Hour"
  FAIL=1
fi

echo
echo "▸ ALL on-screen text — read this for garbled AI label copy, which no rule can catch:"
cut -f2 "$OUT/text.tsv" | sort -u | sed 's/^/    /'
echo
if [ "$FAIL" -eq 0 ]; then
  echo "CLEAR — no banned string found. Still read the dump above before shipping."
else
  echo "BLOCKED — fix the frames above and re-render."; exit 1
fi
