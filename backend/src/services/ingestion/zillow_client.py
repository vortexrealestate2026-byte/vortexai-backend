import requests
import os

ZILLOW_API_KEY = os.getenv("ZILLOW_API_KEY")

def fetch_zillow(zipcode="90210"):
    if not ZILLOW_API_KEY:
        print("[Zillow] Missing API key")
        return []

    url = f"https://api.zillow.com/v1/listings?zipcode={zipcode}"
    headers = {"Authorization": f"Bearer {ZILLOW_API_KEY}"}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            return res.json().get("listings", [])
    except Exception as e:
        print("[Zillow] Error:", e)

    return []
