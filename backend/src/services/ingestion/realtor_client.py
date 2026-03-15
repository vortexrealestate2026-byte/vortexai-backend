import requests

API_URL = "https://api.realtor.com/listings"

def fetch_realtor():
    try:
        res = requests.get(API_URL, timeout=10)
        if res.status_code == 200:
            return res.json().get("listings", [])
    except Exception as e:
        print("[Realtor] Error:", e)

    return []
