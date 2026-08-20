#!/usr/bin/env python3
"""Probe every useful metric for the two most recent IG + FB posts."""
import os, json, urllib.parse, urllib.request, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.refresh import load_env, META_GRAPH, _mget

load_env()
TOKEN = os.environ.get("META_ACCESS_TOKEN")
if not TOKEN:
    print("No META_ACCESS_TOKEN"); sys.exit(1)

IG_METRICS = [
    "impressions","reach","plays","video_views","views",
    "total_interactions","saved","shares","comments","likes",
    "ig_reels_aggregated_all_plays_count","ig_reels_video_view_total_time",
]
FB_METRICS = [
    "post_video_views","post_video_views_organic","post_video_views_paid",
    "post_video_complete_views_organic","post_video_views_10s",
    "post_video_views_unique","post_impressions","post_impressions_unique",
    "post_impressions_organic","post_reactions_by_type_total",
    "video_total_views","video_views","video_avg_time_watched",
]

def probe(post_id, ptoken, metrics, label):
    print(f"\n--- {label} ({post_id}) ---")
    for m in metrics:
        try:
            url = META_GRAPH + f"/{post_id}/insights?" + urllib.parse.urlencode(
                {"metric": m, "period": "lifetime", "access_token": ptoken})
            d = _mget(url)
            vals = d.get("data", [])
            if not vals:
                print(f"  {m:55s}  (no data)")
                continue
            item = vals[0]
            v = item.get("value")
            if v is None:
                vlist = item.get("values", [])
                v = vlist[0].get("value") if vlist else None
            print(f"  {m:55s}  {v}")
        except Exception as e:
            msg = str(e)
            if hasattr(e, "read"):
                try: msg = e.read().decode()[:120]
                except: pass
            print(f"  {m:55s}  ERROR: {msg[:100]}")

    # Also try fetching the field directly on the media object
    print(f"  --- object fields ---")
    for field in ["play_count","video_views","views","like_count","comments_count"]:
        try:
            url = META_GRAPH + f"/{post_id}?" + urllib.parse.urlencode(
                {"fields": field, "access_token": ptoken})
            d = _mget(url)
            v = d.get(field, "(not present)")
            print(f"  object.{field:50s}  {v}")
        except Exception as e:
            print(f"  object.{field:50s}  ERROR")

pages = _mget(META_GRAPH + "/me/accounts?" + urllib.parse.urlencode(
    {"fields": "id,name,access_token,instagram_business_account", "access_token": TOKEN})).get("data", [])

for pg in pages:
    ptoken = pg.get("access_token", TOKEN)

    # 2 most recent FB posts
    fb = _mget(META_GRAPH + f"/{pg['id']}/posts?" + urllib.parse.urlencode(
        {"fields": "id,message,created_time", "limit": 3, "access_token": ptoken}))
    for post in fb.get("data", [])[:2]:
        probe(post["id"], ptoken, FB_METRICS,
              f"FB {post.get('created_time','')[:10]} — {(post.get('message') or '')[:40]}")

    # 2 most recent IG posts
    ig_id = pg.get("instagram_business_account", {}).get("id")
    if ig_id:
        med = _mget(META_GRAPH + f"/{ig_id}/media?" + urllib.parse.urlencode(
            {"fields": "id,caption,timestamp,media_type", "limit": 3, "access_token": TOKEN}))
        for m in med.get("data", [])[:2]:
            probe(m["id"], TOKEN, IG_METRICS,
                  f"IG {m.get('timestamp','')[:10]} {m.get('media_type','')} — {(m.get('caption') or '')[:35]}")
