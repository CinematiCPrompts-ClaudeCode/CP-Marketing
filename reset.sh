#!/usr/bin/env bash
# Fresh start: archive the accumulated MEMORY (lessons/log/packages/grades) and
# drop in clean, empty ledgers. Keeps ALL plumbing, the dashboard, connections,
# brand/registry.json (the code-enforced rules), CLAUDE.md, and the template.
# Nothing is deleted — old files move to archive/<date>/ and can be removed later.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"
DATE="$(date +%Y-%m-%d)"
ARCH="archive/$DATE"

if [ -d "$ARCH" ]; then
  echo "✗ $ARCH already exists — already reset today? Move/rename it first." >&2; exit 1
fi
mkdir -p "$ARCH/packages"

echo "→ Archiving accumulated memory to $ARCH/ ..."
for f in LESSONS.md PROTOKOLL.md data/performance-log.md; do
  [ -f "$f" ] && { mkdir -p "$ARCH/$(dirname "$f")"; git mv "$f" "$ARCH/$f" 2>/dev/null || mv "$f" "$ARCH/$f"; echo "   archived $f"; }
done
# content-package history, but KEEP the format example and (templates/ is untouched)
if compgen -G "packages/*.md" > /dev/null; then
  for f in packages/*.md; do
    case "$(basename "$f")" in
      _EXAMPLE-grounded-package.md) : ;;  # keep the format reference
      *) mv "$f" "$ARCH/packages/"; echo "   archived $f" ;;
    esac
  done
fi

echo "→ Writing clean ledgers ..."
cat > LESSONS.md <<LESS
# LESSONS — what we already know (fresh start $DATE)

Clean slate. The prior ledger was useful but had tangled into corrections-on-corrections,
which was itself causing repeated mistakes. It's archived under \`archive/$DATE/\`. This file
is rebuilt from the raw numbers, not inherited.

**Read before producing anything.** Fill the three sections below from your own analysis of
\`dashboard/data.js\`. One line per entry — narrative belongs in \`PROTOKOLL.md\`; fixed rules and
verified hashtags live in \`brand/registry.json\` (the gate reads that).

---

## ★ What wins — rebuild this from data.js (only patterns you can attach a real number to)
_Empty on purpose. First run: rank every post per platform, name the top performers and the
hook shape each used, and record them here with their real view counts._

## ★ Pre-flight checklist — the gate enforces the fixed rules (\`./check.sh\` → \`brand/registry.json\`)
_Add only judgment-level reminders here as you learn them; the deterministic checks already run in code._

## ★ Verified hashtags — source of truth is \`brand/registry.json\`
_Verify any new tag on-platform, add it there, then note it here if useful._

---
*Fresh start $DATE. Rebuilt from data, not inherited. Keep it lean — a tangled ledger is what stops the system learning.*
LESS

cat > PROTOKOLL.md <<PROT
# Marketing System Protokoll

Running log of changes, fixes, and decisions. Newest first.

---

## $DATE — Fresh start (memory wiped, machine kept)
- Archived the accumulated lessons / log / packages / grades to \`archive/$DATE/\`. Kept all plumbing, the dashboard, the API connections, \`brand/registry.json\` (the code-enforced gate rules), CLAUDE.md, and the package template.
- Reason: the system was built by incremental learn-and-tweak, and the memory had accumulated corrections-on-corrections that were themselves causing the repeated mistakes. Early runs performed well from a clean base — resetting to one.
- Next: re-analyse \`dashboard/data.js\` from scratch and rebuild \`LESSONS.md\` → *What wins* from the real numbers. See \`first-run.md\`.
PROT

echo ""
echo "✓ Reset done."
echo "  Kept:     plumbing, dashboard, connections, brand/registry.json, CLAUDE.md, templates/, packages/_EXAMPLE-grounded-package.md"
echo "  Archived: $ARCH/  (delete with 'rm -rf archive' once you're sure)"
echo ""
echo "Next: paste first-run.md to the agent so it re-analyses the data and rebuilds LESSONS from scratch."
