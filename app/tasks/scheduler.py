from app.tasks.agents_launcher import (
    zillow_scraper,
    redfin_scraper,
    facebook_property_scraper,
    foreclosure_scraper,
    autotrader_scraper,
    kijiji_vehicle_scraper,
    facebook_vehicle_scraper,
    deal_analyzer
)

US_CITIES = [
    "Atlanta",
    "Houston",
    "Dallas",
    "Phoenix",
    "Tampa",
    "Orlando",
    "Charlotte",
    "Indianapolis",
    "Cleveland",
    "Detroit"
]

CANADA_CITIES = [
    "Winnipeg",
    "Steinbach",
    "Regina",
    "Saskatoon",
    "Calgary",
    "Edmonton"
]

def launch_agents():

    for city in US_CITIES:
        zillow_scraper.delay(city)
        redfin_scraper.delay(city)
        facebook_property_scraper.delay(city)
        foreclosure_scraper.delay(city)

    for city in CANADA_CITIES:
        autotrader_scraper.delay(city)
        kijiji_vehicle_scraper.delay(city)
        facebook_vehicle_scraper.delay(city)

    for _ in range(10):
        deal_analyzer.delay()
