import hashlib
import json
import os
import secrets
import time
import urllib.parse
import requests

# --- CONFIGURATION ---
# Your Client Key from the previous steps
CLIENT_KEY = "sbaw38iz0q3h0sm8ga"

# Pre-filled with your actual Client Secret to avoid find-and-replace bugs
CLIENT_SECRET = "Kqw6snEaJRNV3PjmnixZ1yYkwdX8Shmk"

# This must match your TikTok Developer Console EXACTLY
REDIRECT_URI = "http://127.0.0.1:8080/"
SCOPES = "user.info.basic,video.list"
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

    # --- AUTO-CLEAN LOGIC ---
    # Extracts the code cleanly even if you paste the entire broken URL
    auth_code = user_input
    if "?code=" in auth_code:
        auth_code = auth_code.split("?code=")[1]
    if "&" in auth_code:
        auth_code = auth_code.split("&")[0]
    # ------------------------

    if not auth_code:
        print("❌ Error: You didn't paste anything.")
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