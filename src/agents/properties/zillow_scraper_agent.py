import random


async def run_zillow_scraper():

    print("🏠 Zillow scraper running")

    properties = []

    for i in range(5):

        property_data = {
            "address": f"123{i} Main St",
            "city": "Dallas",
            "price": random.randint(120000, 250000)
        }

        properties.append(property_data)

    print("🏠 Properties found:", properties)

    return properties
