#!/usr/bin/env python3
"""Fetch App Store downloads using the App Store Connect Sales report.

Setup: see CREDENTIALS.md. Needs in .env:
  ASC_KEY_ID, ASC_ISSUER_ID, ASC_VENDOR_NUMBER, ASC_PRIVATE_KEY_PATH
Install: pip install -r requirements.txt   (PyJWT + cryptography + requests)
Run:     python scripts/fetch_appstore.py [YYYY-MM-DD]
         (defaults to yesterday; Apple data lags ~1 day)

How it works: signs a short-lived ES256 JWT, calls /v1/salesReports for a DAILY
SUMMARY, unzips the TSV, and sums the download units for the period.
"""
import os, sys, gzip, io, time, datetime, csv

def load_env(path=".env"):
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

def make_token(key_id, issuer_id, p8_path):
    import jwt  # PyJWT
    private_key = open(p8_path).read()
    now = int(time.time())
    payload = {"iss": issuer_id, "iat": now, "exp": now + 60 * 18,
               "aud": "appstoreconnect-v1"}
    return jwt.encode(payload, private_key, algorithm="ES256",
                      headers={"kid": key_id, "typ": "JWT"})

def main():
    load_env()
    import requests
    need = ["ASC_KEY_ID", "ASC_ISSUER_ID", "ASC_VENDOR_NUMBER", "ASC_PRIVATE_KEY_PATH"]
    missing = [n for n in need if not os.environ.get(n)]
    if missing:
        sys.exit("Missing in .env: " + ", ".join(missing) + " — see CREDENTIALS.md")

    report_date = sys.argv[1] if len(sys.argv) > 1 else \
        (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

    token = make_token(os.environ["ASC_KEY_ID"], os.environ["ASC_ISSUER_ID"],
                       os.environ["ASC_PRIVATE_KEY_PATH"])

    params = {
        "filter[frequency]": "DAILY",
        "filter[reportDate]": report_date,
        "filter[reportType]": "SALES",
        "filter[reportSubType]": "SUMMARY",
        "filter[vendorNumber]": os.environ["ASC_VENDOR_NUMBER"],
        "filter[version]": "1_1",
    }
    r = requests.get("https://api.appstoreconnect.apple.com/v1/salesReports",
                     headers={"Authorization": f"Bearer {token}",
                              "Accept": "application/a-gzip"},
                     params=params)
    if r.status_code == 404:
        sys.exit(f"No report for {report_date} yet (Apple lags ~1 day, and "
                 f"there must be activity that day). Try an earlier date.")
    if r.status_code != 200:
        sys.exit(f"App Store Connect error {r.status_code}: {r.text[:300]}")

    tsv = gzip.GzipFile(fileobj=io.BytesIO(r.content)).read().decode("utf-8")
    rows = list(csv.DictReader(io.StringIO(tsv), delimiter="\t"))

    # Product Type Identifier: "1*" = first downloads, "3*" = redownloads/updates
    first, redownload = 0, 0
    for row in rows:
        units = int(row.get("Units", 0) or 0)
        ptype = (row.get("Product Type Identifier", "") or "").strip()
        if ptype.startswith("1"):
            first += units
        elif ptype.startswith("3"):
            redownload += units

    print(f"\n  App Store — {report_date}\n  " + "-"*40)
    print(f"  {first:>6,}  first-time downloads")
    print(f"  {redownload:>6,}  redownloads / updates")
    print("  " + "-"*40)
    print(f"  {first:>6,}  → this is your 'downloads' number\n")
    print("  → paste into data/performance-log.csv (installs column)\n")

if __name__ == "__main__":
    main()
