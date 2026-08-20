#!/bin/zsh
set -e
cd "$(dirname "$0")"
PY="$(command -v python3 || true)"
if [ -z "$PY" ]; then echo "python3 not found — run: brew install python"; exit 1; fi
if [ ! -d ".venv" ]; then
  echo "First run — creating .venv and installing deps…"
  "$PY" -m venv .venv
  ./.venv/bin/pip install -q --upgrade pip
  ./.venv/bin/pip install -q -r requirements.txt
fi
./.venv/bin/python scripts/refresh.py
