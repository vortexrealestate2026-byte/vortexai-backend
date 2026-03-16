import requests

BASE_URL = "https://www.trulia.com"

def fetch_trulia(zipcode: str = "90210", limit: int = 50):
    """
    Placeholder/API-style client for Trulia.
    In production, back this with a scraper or proxy API.
    """
    print(f"[Trulia] Fetching listings for {zipcode} (limit={limit})")
    # TODO: implement real integration
    return []
