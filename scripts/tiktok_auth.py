import hashlib
import json
import os
import secrets
import time
import urllib.parse
import requests

# --- CONFIGURATION ---
# Credentials come from .env (gitignored) — NEVER hardcode them here.
# They were previously inlined in this file and reached a git commit; if you are
# reading this on a machine that ever had that version, rotate the secret in the
# TikTok developer console.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_env(path=os.path.join(ROOT, ".env")):
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    except FileNotFoundError:
        pass


_load_env()

CLIENT_KEY = os.environ.get("TIKTOK_CLIENT_KEY", "")
CLIENT_SECRET = os.environ.get("TIKTOK_CLIENT_SECRET", "")

# This must match your TikTok Developer Console EXACTLY
REDIRECT_URI = os.environ.get("TIKTOK_REDIRECT_URI", "http://127.0.0.1:8080/")

if not CLIENT_KEY or not CLIENT_SECRET:
    raise SystemExit(
        "✗ TIKTOK_CLIENT_KEY / TIKTOK_CLIENT_SECRET missing from .env\n"
        "  Add them from https://developers.tiktok.com → your app → Credentials,\n"
        "  then re-run:  ./.venv/bin/python scripts/tiktok_auth.py"
    )
# Only what refresh.py actually calls: /v2/video/list/ needs video.list and nothing else.
# Requesting user.info.basic as well used to make TikTok reject the whole authorize
# request ("Es ist etwas schiefgelaufen ... bestimmte App-Einstellungen") on apps where
# that scope isn't added — an unapproved scope fails the request before consent is shown.
# Override via TIKTOK_SCOPES in .env if a future feature needs more.
SCOPES = os.environ.get("TIKTOK_SCOPES", "video.list")
STATE = "cp"


def run_oauth_flow():
    print("====================================================")
    print("          TikTok OAuth2 Setup (Desktop, with PKCE)   ")
    print("====================================================\n")

    # App is now registered with a Desktop platform in the portal (redirect URI
    # http://127.0.0.1:8080/ added there to match). Desktop apps require full
    # PKCE: code_challenge (hex-SHA256, TikTok's documented non-standard
    # encoding) AND code_challenge_method=S256.
    code_verifier = secrets.token_urlsafe(60)
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).hexdigest()

    params = {
        "client_key": CLIENT_KEY,
        "scope": SCOPES,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": STATE,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }
    auth_url = f"https://www.tiktok.com/v2/auth/authorize/?{urllib.parse.urlencode(params)}"

    # 3. Present the URL to the user
    print("1) Open this URL in your web browser and click Authorize:\n")
    print(f"   {auth_url}\n")
    print("----------------------------------------------------")
    print("Note: After authorizing, your browser will redirect to a broken page")
    print("like '127.0.0.1 refused to connect'. THIS IS EXPECTED.")
    print("You can now copy the ENTIRE URL from your address bar and paste it.")
    print("----------------------------------------------------\n")

    # 4. Pause and wait for user input
    user_input = input("2) Paste the code or the entire redirect URL here: ").strip()

    # --- PARSE + VALIDATE ---
    # Parse properly rather than splitting on "?code=": TikTok can return the
    # authorize URL back with an ?error= on it, and the old string-split silently
    # passed that whole URL through as if it were a code. The API then replied
    # "Authorization code is expired", which sent you looking at the wrong problem.
    if not user_input:
        print("❌ You didn't paste anything.")
        return

    auth_code = user_input
    if "://" in user_input or "?" in user_input or "&" in user_input:
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(user_input).query)

        if "error" in qs:
            err = qs["error"][0]
            desc = qs.get("error_description", [""])[0]
            print(f"\n❌ TikTok refused the authorization: {err}")
            if desc:
                print(f"   {desc}")
            if err == "access_denied":
                print(
                    "\n   This is a consent-step failure — no code was ever issued.\n"
                    "   Usual causes, most likely first:\n"
                    "     1. The app is in SANDBOX mode (client key starts 'sb') and the\n"
                    "        TikTok account you logged in with is not added as a target user.\n"
                    "        Fix: developer console → your app → Sandbox → add the account.\n"
                    "     2. The scopes user.info.basic / video.list are not approved for the app.\n"
                    "     3. 'Cancel' / 'Deny' was clicked on the consent screen.\n"
                    "     4. You authorized with a different TikTok account than the one that\n"
                    "        owns the videos.\n"
                )
            return

        if "code" not in qs:
            print("\n❌ That URL has no ?code= in it, so there's nothing to exchange.")
            print("   Paste the URL you were redirected TO (it will start http://127.0.0.1:8080/),")
            print("   not the tiktok.com authorize URL you opened.")
            return

        auth_code = qs["code"][0]
        state = qs.get("state", [None])[0]
        if state and state != STATE:
            print(f"❌ state mismatch (got {state!r}, expected {STATE!r}) — aborting.")
            return

    auth_code = urllib.parse.unquote(auth_code).strip()
    if not auth_code:
        print("❌ Couldn't extract an authorization code.")
        return

    print(f"\n🔄 Cleaned auth code: {auth_code[:15]}...")
    print("🔄 Exchanging authorization code for access tokens...")

    # 5. Exchange Code for Access Token
    token_url = "https://open.tiktokapis.com/v2/oauth/token/"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
        "code_verifier": code_verifier,
    }

    try:
        response = requests.post(token_url, headers=headers, data=data)
        response_data = response.json()

        if response.status_code == 200 and "access_token" in response_data:
            print("\n✅ SUCCESS! Connected to TikTok.")
            print("====================================================")
            print(f"Access Token:  {response_data.get('access_token')[:15]}...")
            print(f"Refresh Token: {response_data.get('refresh_token')[:15]}...")
            print("====================================================")

            # Save tokens where refresh.py's TIKTOK_TOKEN_CACHE actually looks for them.
            # obtained_at lets refresh.py use the cached access_token directly while
            # still valid, instead of always going through the refresh_token grant
            # (which TikTok has been rejecting with invalid_client even for a
            # just-issued, valid refresh_token — see PROTOKOLL Aug 10).
            response_data["obtained_at"] = int(time.time())
            token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", ".tiktok_token.json")
            with open(token_path, "w") as f:
                json.dump(response_data, f, indent=4)
            print(f"\n💾 Tokens saved to '{os.path.normpath(token_path)}'")

        else:
            print("\n❌ TikTok API Error:")
            print(json.dumps(response_data, indent=2))

    except Exception as e:
        print(f"\n❌ Network error occurred: {e}")


if __name__ == "__main__":
    run_oauth_flow()