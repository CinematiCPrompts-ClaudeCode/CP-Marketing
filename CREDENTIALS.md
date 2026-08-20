# Credentials — get the two API keys

You need two sets of credentials. Both are free. Put the values in a `.env` file
(copy `.env.example`). Never commit `.env` or the `.p8` file to git.

---

## 1) YouTube Data API v3  (≈ 5 minutes)

Gives you views, likes, and comments for your posted videos.

1. Go to the **Google Cloud Console** → https://console.cloud.google.com
2. Top bar → **create a new project** (e.g. "cinematic-prompts") or pick one.
3. Left menu → **APIs & Services → Library**.
4. Search **YouTube Data API v3** → open it → **Enable**.
5. Left menu → **APIs & Services → Credentials**.
6. **+ Create Credentials → API key**. Copy the key.
7. (Recommended) Click **Restrict key** → under *API restrictions* limit it to
   *YouTube Data API v3* only. Keeps it safe if it ever leaks.

Put it in `.env`:
```
YT_API_KEY=AIza...your_key
YT_VIDEO_IDS=dQw4w9WgXcQ,abc123XYZ   # the IDs of videos you posted
```
A video ID is the part after `watch?v=` in the URL.

**Quota:** 10,000 units/day, free. A stats lookup costs ~1 unit. You won't get
close.

---

## 2) App Store Connect API  (≈ 10 minutes)

Gives you actual downloads — your hero number.

> **Two requirements before you start:**
> - You must be the **Account Holder** (or have an Admin enable API access). If
>   the Integrations menu is missing, that's why.
> - Create a **Team Key**, not an Individual key. Individual keys *cannot* read
>   Sales reports — which is exactly the data you want.

1. Go to **App Store Connect** → https://appstoreconnect.apple.com
2. **Users and Access** → **Integrations** tab → **App Store Connect API**.
3. Make sure **Team Keys** is selected. Press the **＋** button.
4. Name it (e.g. "marketing-readonly"), set access role to **App Manager**
   (enough for sales/analytics), and create it.
5. **Download the `.p8` file.** You can only download it **once** — if you lose
   it you must revoke and make a new one. Save it in the project root.
6. Note two IDs from that page:
   - **Key ID** — shown next to the key (e.g. `D383SF739`).
   - **Issuer ID** — shown above the keys table (a long UUID).
7. Get your **Vendor Number**: App Store Connect → **Payments and Financial
   Reports** (or Sales and Trends) → it's the number near your account name.

Put it in `.env`:
```
ASC_KEY_ID=D383SF739
ASC_ISSUER_ID=6053b7fe-68a8-4acb-89be-165aa6465141
ASC_VENDOR_NUMBER=12345678
ASC_PRIVATE_KEY_PATH=./AuthKey_D383SF739.p8
```

---

## 3) Install + run

```bash
pip install -r requirements.txt
cp .env.example .env        # then fill in your values

python scripts/fetch_youtube.py      # prints YouTube views per video
python scripts/fetch_appstore.py     # prints App Store downloads for the period
```

Both scripts just **print** the numbers so you can paste them into
`data/performance-log.csv`. Once you trust them, you can have the agent call them
and update the log itself.

## Security notes
- Add this to `.gitignore`: `.env` and `*.p8`.
- The `.p8` is a private key — treat it like a password.
- If a key leaks: YouTube → delete it in Credentials; Apple → revoke it under
  Team Keys. Both are instant.
