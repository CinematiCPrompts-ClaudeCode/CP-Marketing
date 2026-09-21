#!/usr/bin/env python3
"""Turn on App Store Connect Analytics Reports — the impressions / product-page-views /
conversion feed that `salesReports` (used by refresh.py) does not provide.

There is NO toggle for this in the App Store Connect web UI. Analytics Reports are
request-driven: you POST one report request per app, and Apple then generates daily
report instances from that point forward. First data lands roughly 24-48h later.

Usage:
    python scripts/enable_analytics.py                # read-only: list apps + existing requests
    python scripts/enable_analytics.py --create       # create the ONGOING request  (WRITES)
    python scripts/enable_analytics.py --create --snapshot   # also request 1y of history

Reads the same .env credentials as refresh.py. Needs the key's role to be Admin, App
Manager, or Developer; a 403 on the POST almost always means the key's role is too low,
not that the request was malformed.
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://api.appstoreconnect.apple.com/v1"


def load_env():
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def token():
    import jwt
    need = ["ASC_KEY_ID", "ASC_ISSUER_ID", "ASC_PRIVATE_KEY_PATH"]
    missing = [n for n in need if not os.environ.get(n)]
    if missing:
        sys.exit(f"Missing in .env: {', '.join(missing)}")
    key_path = os.environ["ASC_PRIVATE_KEY_PATH"]
    if not os.path.isabs(key_path):
        key_path = os.path.join(ROOT, key_path)
    now = int(time.time())
    return jwt.encode(
        {"iss": os.environ["ASC_ISSUER_ID"], "iat": now, "exp": now + 60 * 19,
         "aud": "appstoreconnect-v1"},
        open(key_path).read(),
        algorithm="ES256", headers={"kid": os.environ["ASC_KEY_ID"]})


def main():
    load_env()
    try:
        import requests
    except ImportError:
        sys.exit("pip install requests pyjwt cryptography")

    tok = token()
    h = {"Authorization": f"Bearer {tok}"}
    create = "--create" in sys.argv
    snapshot = "--snapshot" in sys.argv
    created, failed = [], []

    r = requests.get(f"{BASE}/apps", headers=h, params={"limit": 50})
    if r.status_code != 200:
        sys.exit(f"GET /apps failed {r.status_code}: {r.text[:400]}")
    apps = r.json().get("data", [])
    if not apps:
        sys.exit("No apps visible to this key.")

    print(f"{len(apps)} app(s) visible to this key:\n")
    for a in apps:
        at = a["attributes"]
        print(f"  {at.get('name')}  ({at.get('bundleId')})   id={a['id']}")

    for a in apps:
        app_id, name = a["id"], a["attributes"].get("name")
        rr = requests.get(f"{BASE}/apps/{app_id}/analyticsReportRequests", headers=h)
        if rr.status_code != 200:
            print(f"\n[{name}] cannot read report requests ({rr.status_code}): "
                  f"{rr.text[:200]}")
            continue
        existing = rr.json().get("data", [])
        print(f"\n[{name}] existing analytics report requests: {len(existing)}")
        for e in existing:
            ea = e["attributes"]
            print(f"   - {ea.get('accessType')}  stopped={ea.get('stoppedDueToInactivity')}"
                  f"  id={e['id']}")

        if not create:
            continue

        wanted = ["ONGOING"] + (["ONE_TIME_SNAPSHOT"] if snapshot else [])
        have = {e["attributes"].get("accessType") for e in existing}
        for access in wanted:
            if access in have:
                print(f"   = {access} already exists, skipping")
                continue
            # accessType is the ONLY writable attribute on this resource — sending
            # anything else (e.g. 'name') is rejected 409 ENTITY_ERROR.ATTRIBUTE.UNKNOWN.
            body = {"data": {
                "type": "analyticsReportRequests",
                "attributes": {"accessType": access},
                "relationships": {"app": {"data": {"type": "apps", "id": app_id}}}}}
            cr = requests.post(f"{BASE}/analyticsReportRequests", headers=h, json=body)
            if cr.status_code in (200, 201):
                print(f"   + created {access}: id={cr.json()['data']['id']}")
                created.append(f"{name}/{access}")
            else:
                print(f"   ! {access} failed {cr.status_code}: {cr.text[:300]}")
                failed.append(f"{name}/{access} ({cr.status_code})")

    if not create:
        print("\nRead-only. Nothing was created.")
        print("To turn it on:  python scripts/enable_analytics.py --create --snapshot")
    elif failed and not created:
        sys.exit(f"\nNOTHING WAS CREATED. Failed: {', '.join(failed)}")
    else:
        if failed:
            print(f"\nPartial: {len(created)} created, failed -> {', '.join(failed)}")
        print("\nApple generates the first daily instance in ~24-48h.")
        print("Reports that matter here:")
        print("  APP_STORE_ENGAGEMENT  -> impressions, product page views")
        print("  APP_STORE_COMMERCE    -> downloads, conversion rate")
        print("Read them via /v1/analyticsReportRequests/{id}/reports"
              " -> /instances -> /segments (gzipped CSV).")


if __name__ == "__main__":
    main()
