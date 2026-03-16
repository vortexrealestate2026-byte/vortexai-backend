import requests
import logging

logger = logging.getLogger("vortex-ai")

def scrape_vehicle_listings(city):

    logger.info(f"Scraping vehicle listings in {city}")

    url = f"https://api.example-vehicles.com/search?city={city}"

    try:
        r = requests.get(url, timeout=10)

        vehicles = []

        if r.status_code == 200:

            data = r.json()

            for car in data["results"]:
                vehicles.append({
                    "make": car["make"],
                    "model": car["model"],
                    "price": car["price"],
                    "year": car["year"]
                })

        logger.info(f"{len(vehicles)} vehicles found")

        return vehicles

    except Exception as e:
        logger.error(e)
        return []
