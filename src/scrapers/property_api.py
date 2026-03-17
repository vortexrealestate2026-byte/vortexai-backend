import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("vortex-ai")

DATAFINITI_TOKEN = os.getenv("DATAFINITI_TOKEN")


def get_properties():

    url = "https://api.datafiniti.co/v4/properties/search"

    payload = {
        "query": "price:[50000 TO 300000]",
        "num_records": 20
    }

    headers = {
        "Authorization": f"Bearer {DATAFINITI_TOKEN}",
        "Content-Type": "application/json"
    }

    try:

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()

        properties = []

        for p in data.get("records", []):

            properties.append({
                "price": p.get("price", 0),
                "sqft": p.get("squareFootage", 1000),
                "address": p.get("address", "Unknown"),
                "city": p.get("city"),
                "state": p.get("province")
            })

        logger.info(f"Fetched {len(properties)} real properties")

        return properties

    except Exception as e:

        logger.error(f"Property API error: {e}")

        return []
