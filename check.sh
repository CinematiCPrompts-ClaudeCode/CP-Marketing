#!/usr/bin/env bash
# Ship gate — a content package must pass this before ANY platform goes out.
# Usage:
#   ./check.sh                       # checks the newest file in packages/
#   ./check.sh packages/2026-08-12-foo.md
# Exit 0 = clear to ship. Exit 1 = fix the issues it prints first.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$HERE/scripts/preflight.py" "$@"
