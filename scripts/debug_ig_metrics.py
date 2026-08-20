#!/usr/bin/env python3
"""Diagnostic: print every insight metric value for your recent IG posts.
Run once to find which metric name matches what Instagram shows in the app.

  python scripts/debug_ig_metrics.py
"""
import os, sys, json, urllib.parse, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_env():
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def mget(url):
    with urllib.request.urlopen(url) as r: return json.load(r)

GRAPH = "https://graph.facebook.com/v22.0"

METRICS_TO_TRY = [
    "plays",
    "ig_reels_aggregated_all_plays_count",
    "reach",
    "impressions",
    "views",
    "video_views",
    "total_interactions",
]

def probe(media_id, token):
    print(f"\n  media_id: {media_id}")
    for metric in METRICS_TO_TRY:
        for period in [None, "lifetime", "day"]:
            params = {"metric": metric, "access_token": token}
            if period: params["period"] = period
            label = f"{metric}" + (f" (period={period})" if period else "")
            try:
                d = mget(GRAPH + f"/{media_id}/insights?" + urllib.parse.urlencode(params))
                vals = d.get("data", [])
                if not vals:
                    print(f"    {label:55s} → (empty data)")
                    break
                item = vals[0]
                v = item.get("value")
                if v is None:
                    v = item.get("values", [{}])[0].get("value")
                print(f"    {label:55s} → {v}")
                break  # found a working period for this metric, move on
            except urllib.error.HTTPError as e:
                try: body = json.load(e)
                except Exception: body = {}
                err = (body.get("error") or {}).get("message", str(e))[:80]
                print(f"    {label:55s} → ERROR {e.code}: {err}")
                if period is None: break  # if no-period fails, skip period variants
            except Exception as ex:
                print(f"    {label:55s} → EXCEPTION {ex}")
                break

def main():
    load_env()
    token = os.environ.get("META_ACCESS_TOKEN")
    if not token:
        print("No META_ACCESS_TOKEN in .env"); sys.exit(1)

    pages = mget(GRAPH + "/me/accounts?" + urllib.parse.urlencode(
        {"fields": "id,name,instagram_business_account", "access_token": token})).get("data", [])
    if not pages:
        print("No Pages found for this token"); sys.exit(1)

    for pg in pages:
        ig = pg.get("instagram_business_account", {})
        if not ig.get("id"): continue
        print(f"\nIG account: {ig['id']}  (via Page: {pg.get('name')})")
        med = mget(GRAPH + f"/{ig['id']}/media?" + urllib.parse.urlencode(
            {"fields": "id,caption,timestamp,media_type", "limit": 5, "access_token": token}))
        posts = med.get("data", [])
        if not posts:
            print("  No media found"); continue
        print(f"  Probing last {len(posts)} posts:\n")
        for m in posts:
            cap = (m.get("caption") or "")[:60].replace("\n", " ")
            print(f"  [{m.get('timestamp','')[:10]}] {cap}")
            probe(m["id"], token)

if __name__ == "__main__":
    main()
