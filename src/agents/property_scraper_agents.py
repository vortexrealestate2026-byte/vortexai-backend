import requests
import logging

logger = logging.getLogger("vortex-ai")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_properties(city):

    logger.info(f"Scraping properties in {city}")

    url = f"https://api.example-realestate.com/search?city={city}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code != 200:
            return []

        data = response.json()

        properties = []

        for item in data["listings"]:
            properties.append({
                "address": item["address"],
                "price": item["price"],
                "beds": item["beds"],
                "baths": item["baths"],
                "sqft": item["sqft"]
            })

        logger.info(f"Found {len(properties)} properties")

        return properties

    except Exception as e:

        logger.error(f"Scraper error: {e}")
        return []
