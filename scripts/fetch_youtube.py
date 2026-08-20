#!/usr/bin/env python3
"""Fetch view/like/comment counts for your posted YouTube videos.

Setup: see CREDENTIALS.md. Needs YT_API_KEY and YT_VIDEO_IDS in .env
Run:   python scripts/fetch_youtube.py
"""
import os, sys, urllib.parse, urllib.request, json

def load_env(path=".env"):
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

def main():
    load_env()
    key = os.environ.get("YT_API_KEY")
    ids = [i.strip() for i in os.environ.get("YT_VIDEO_IDS", "").split(",") if i.strip()]
    if not key or not ids:
        sys.exit("Missing YT_API_KEY or YT_VIDEO_IDS in .env — see CREDENTIALS.md")

    # API allows up to 50 ids per call
    url = "https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({
        "part": "statistics,snippet",
        "id": ",".join(ids[:50]),
        "key": key,
    })
    with urllib.request.urlopen(url) as r:
        data = json.load(r)

    total = 0
    print(f"\n  YouTube — {len(data.get('items', []))} videos\n  " + "-"*52)
    for it in data.get("items", []):
        s = it["statistics"]
        v = int(s.get("viewCount", 0))
        total += v
        title = it["snippet"]["title"][:40]
        print(f"  {v:>7,} views  ·  {int(s.get('likeCount',0)):>4} likes  ·  {title}")
    print("  " + "-"*52)
    print(f"  {total:>7,} total YouTube views\n")
    print("  → paste per-video numbers into data/performance-log.csv\n")

if __name__ == "__main__":
    main()
