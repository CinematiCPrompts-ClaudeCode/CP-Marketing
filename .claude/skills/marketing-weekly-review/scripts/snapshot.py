#!/usr/bin/env python3
"""
Print a clean snapshot of the current numbers from the marketing dashboard,
for the weekly review. Run from the marketing project root:

    python .claude/skills/marketing-weekly-review/scripts/snapshot.py

(or wherever the skill lives — it looks for dashboard/data.js under the current
working directory).
"""
import json, re, os, sys, datetime

ROOT = os.getcwd()
path = os.path.join(ROOT, "dashboard", "data.js")
if not os.path.exists(path):
    print("Couldn't find dashboard/data.js under", ROOT)
    print("Run this from your marketing project root (the folder with dashboard/).")
    sys.exit(1)

txt = open(path).read()
m = re.search(r"window\.DASH\s*=\s*(\{.*\})\s*;", txt, re.S)
if not m:
    print("Found data.js but couldn't parse window.DASH from it."); sys.exit(1)
D = json.loads(m.group(1))

def parse(d):
    try: return datetime.date.fromisoformat((d or "")[:10])
    except Exception: return None

def stats(lst):
    vs = [(p.get("views") or 0) for p in lst]
    n = len(lst); tot = sum(vs); avg = (tot / n) if n else 0
    dated = [p for p in lst if parse(p.get("date"))]
    newest = max(dated, key=lambda p: p["date"]) if dated else None
    return n, tot, avg, newest

print("SNAPSHOT —", datetime.date.today().isoformat())
print("-" * 72)
for key in ("tiktok", "facebook", "youtube", "instagram"):
    lst = D.get(key, []) or []
    n, tot, avg, newest = stats(lst)
    if newest:
        nv = f'{newest.get("date","")}  "{(newest.get("name") or "(untitled)")[:30]}"  {newest.get("views")}'
    else:
        nv = "—"
    print(f"{key:10} {n:3} posts | {tot:8,} views | avg {avg:6.0f}/post | newest: {nv}")

print("-" * 72)
daily = D.get("daily", []) or []
today = datetime.date.today()
def within(d, days):
    pd = parse(d)
    return pd is not None and 0 <= (today - pd).days <= days
last7 = sum(p.get("n", 0) for p in daily if within(p.get("d"), 7))
last30 = sum(p.get("n", 0) for p in daily if within(p.get("d"), 30))
print(f"downloads  {D.get('downloads',0):,} all-time | {last30} last 30d | {last7} last 7d")
print("data updated:", D.get("updated", "?"))
