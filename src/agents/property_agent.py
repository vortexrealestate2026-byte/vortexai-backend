from src.scrapers.datafiniti_property_scraper import get_properties

def run_property_agent():

    cities = [
        ("Phoenix","AZ"),
        ("Atlanta","GA"),
        ("Dallas","TX")
    ]

    for city, state in cities:

        properties = get_properties(city, state)

        for p in properties:

            print("PROPERTY FOUND:", p["address"])
