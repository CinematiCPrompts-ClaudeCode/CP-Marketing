import os, csv, io, gzip, time, datetime, jwt, requests
def load_env(p=".env"):
    for line in open(p):
        line=line.strip()
        if line and not line.startswith("#") and "=" in line:
            k,v=line.split("=",1); os.environ.setdefault(k.strip(),v.strip())
load_env()
now=int(time.time())
tok=jwt.encode({"iss":os.environ["ASC_ISSUER_ID"],"iat":now,"exp":now+60*19,"aud":"appstoreconnect-v1"},
               open(os.environ["ASC_PRIVATE_KEY_PATH"]).read(),algorithm="ES256",
               headers={"kid":os.environ["ASC_KEY_ID"]})
vendor=os.environ["ASC_VENDOR_NUMBER"]
by_type={}; grand=0; days=0
yest=datetime.date.today()-datetime.timedelta(days=1)
for i in range(120):
    d=(yest-datetime.timedelta(days=i)).isoformat()
    r=requests.get("https://api.appstoreconnect.apple.com/v1/salesReports",
        headers={"Authorization":f"Bearer {tok}","Accept":"application/a-gzip"},
        params={"filter[frequency]":"DAILY","filter[reportDate]":d,"filter[reportType]":"SALES",
                "filter[reportSubType]":"SUMMARY","filter[vendorNumber]":vendor,"filter[version]":"1_1"})
    if r.status_code!=200: continue
    days+=1
    tsv=gzip.GzipFile(fileobj=io.BytesIO(r.content)).read().decode("utf-8")
    for row in csv.DictReader(io.StringIO(tsv),delimiter="\t"):
        pt=(row.get("Product Type Identifier","") or "").strip()
        u=int(row.get("Units",0) or 0)
        by_type[pt]=by_type.get(pt,0)+u; grand+=u
print(f"\nDays with a report (last 120): {days}")
print("Units by Product Type Identifier:")
for pt,u in sorted(by_type.items()): print(f"   {pt or '(blank)':<8} {u}")
print(f"\n   '1*' first-time  = {sum(u for pt,u in by_type.items() if pt[:1]=='1')}")
print(f"   '3*' redownloads = {sum(u for pt,u in by_type.items() if pt[:1]=='3')}")
print(f"   ALL units (120d) = {grand}")
