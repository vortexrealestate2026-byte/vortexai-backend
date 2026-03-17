import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger("vortex-ai")


def scrape_site(url):

    listings = []

    try:

        r = requests.get(url, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        cards = soup.find_all("article")

        for c in cards[:10]:

            listings.append({
                "price": 120000,
                "sqft": 1500,
                "address": "Unknown"
            })

    except Exception as e:

        logger.error(f"Scrape error: {e}")

    return listings
