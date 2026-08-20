#!/usr/bin/env bash
# Uploads dashboard/data.js to your IONOS webspace /performance/ via SFTP (password auth).
# Prefers lftp; falls back to expect+sftp. Settings + password live in .deploy.env (never zip it).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$HERE/.deploy.env"
FILE="$HERE/data.js"

[ -f "$FILE" ]     || { echo "✗ data.js not found — run ./run.sh first." >&2; exit 1; }
[ -f "$ENV_FILE" ] || { echo "✗ Missing $ENV_FILE" >&2; exit 1; }

# shellcheck disable=SC1090
source "$ENV_FILE"
: "${DEPLOY_HOST:?set DEPLOY_HOST in .deploy.env}"
: "${DEPLOY_USER:?set DEPLOY_USER in .deploy.env}"
: "${DEPLOY_PASS:?set DEPLOY_PASS in .deploy.env}"
DEPLOY_PORT="${DEPLOY_PORT:-22}"
DEPLOY_REMOTE_DIR="${DEPLOY_REMOTE_DIR:-/performance}"
REMOTE="${DEPLOY_REMOTE_DIR%/}/data.js"

echo "→ Uploading data.js to sftp://$DEPLOY_HOST:$DEPLOY_PORT$REMOTE"

if command -v lftp >/dev/null 2>&1; then
  lftp -u "$DEPLOY_USER,$DEPLOY_PASS" "sftp://$DEPLOY_HOST:$DEPLOY_PORT" \
       -e "set sftp:auto-confirm yes; put -O \"$DEPLOY_REMOTE_DIR\" \"$FILE\"; bye"
  echo "✓ Uploaded (lftp). Hard-refresh the page (Cmd+Shift+R)."

elif command -v expect >/dev/null 2>&1; then
  export DEPLOY_HOST DEPLOY_PORT DEPLOY_USER DEPLOY_PASS FILE REMOTE
  out="$(expect <<'EXP' 2>&1 || true
set timeout 45
spawn sftp -oStrictHostKeyChecking=accept-new -P $env(DEPLOY_PORT) $env(DEPLOY_USER)@$env(DEPLOY_HOST)
expect {
  -re {(?i)password:} { send "$env(DEPLOY_PASS)\r" }
  timeout { puts "ERR_NO_PROMPT"; exit }
}
expect {
  "sftp>" {}
  -re {(?i)permission denied} { puts "ERR_AUTH"; exit }
  timeout { puts "ERR_AFTER_PW"; exit }
}
send "put \"$env(FILE)\" \"$env(REMOTE)\"\r"
expect { -re {100%|Uploading} {} timeout { puts "ERR_PUT"; exit } }
expect "sftp>"
send "bye\r"
expect eof
EXP
)"
  echo "$out" | sed 's/^/   /'
  if echo "$out" | grep -qE "100%|Uploading"; then
    echo "✓ Uploaded (expect+sftp). Hard-refresh the page (Cmd+Shift+R)."
  else
    echo "✗ Upload didn't confirm. See messages above." >&2; exit 1
  fi

else
  echo "✗ Neither lftp nor expect is available."
  echo "  Easiest fix — install lftp once:  brew install lftp"
  echo "  (If you don't have Homebrew, tell me and I'll give you another way.)"
  exit 1
fi
