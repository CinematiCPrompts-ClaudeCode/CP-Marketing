#!/usr/bin/env python3
"""
meta_token.py — mint a fresh long-lived Meta token after the old one dies.

Meta invalidates access tokens whenever you change your Facebook password (or when
Facebook decides to reset the session). The symptom in ./run.sh is:

    Meta API error 400: ... "The session has been invalidated because the user
    changed their password" ... code 190, error_subcode 460

Recovery is a two-step token exchange that is annoying to do by hand, so this does it.

USAGE
  1. Open the Graph API Explorer:  https://developers.facebook.com/tools/explorer
  2. Pick your app, then "Generate Access Token", granting at least:
         pages_show_list, pages_read_engagement, read_insights,
         instagram_basic, instagram_manage_insights, business_management
  3. Copy the (short-lived) token it gives you and run:

         ./.venv/bin/python scripts/meta_token.py <SHORT_LIVED_TOKEN>

  4. Paste the printed long-lived token into .env as META_ACCESS_TOKEN, then ./run.sh

Prints tokens to stdout on purpose — it never writes .env for you, so it cannot
clobber your other credentials. Nothing is logged to disk.
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH = "https://graph.facebook.com/v22.0"


def load_env(path=os.path.join(ROOT, ".env")):
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
    except FileNotFoundError:
        pass


def get(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def main():
    load_env()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    short = sys.argv[1].strip()
    app_id = os.environ.get("META_APP_ID")
    secret = os.environ.get("META_APP_SECRET")
    if not app_id or not secret:
        print("✗ META_APP_ID / META_APP_SECRET missing from .env — can't exchange.")
        sys.exit(1)

    # 1) short-lived user token -> long-lived user token (~60 days)
    url = f"{GRAPH}/oauth/access_token?" + urllib.parse.urlencode({
        "grant_type": "fb_exchange_token",
        "client_id": app_id,
        "client_secret": secret,
        "fb_exchange_token": short,
    })
    try:
        data = get(url)
    except urllib.error.HTTPError as e:
        print(f"✗ exchange failed ({e.code}): {e.read().decode()[:300]}")
        sys.exit(1)

    long_tok = data.get("access_token")
    if not long_tok:
        print("✗ no access_token in response:", data)
        sys.exit(1)

    days = int(data.get("expires_in", 0)) // 86400
    print(f"\n✓ long-lived USER token (expires in ~{days} days):\n\n{long_tok}\n")

    # 2) page token — derived from a long-lived user token, these do not expire
    try:
        pages = get(f"{GRAPH}/me/accounts?" + urllib.parse.urlencode({"access_token": long_tok}))
        for p in pages.get("data", []):
            print(f"✓ PAGE token for {p.get('name')!r} (does not expire):\n\n{p.get('access_token')}\n")
    except urllib.error.HTTPError as e:
        print(f"  (couldn't list pages: {e.code} — the user token above still works)")

    print("Next: put ONE of these in .env as META_ACCESS_TOKEN, then run ./run.sh")
    print("Prefer the PAGE token — it doesn't expire, so this won't recur every 60 days.\n")


if __name__ == "__main__":
    main()
