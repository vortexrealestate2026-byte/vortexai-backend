from celery import shared_task

# import ONLY agents that exist
from app.tasks.agents_launcher import (
    zillow_scraper,
    redfin_scraper,
    autotrader_scraper,
    kijiji_vehicle_scraper,
    deal_analyzer
)

# -----------------------------
# TARGET MARKETS
# -----------------------------

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


# -----------------------------
# REAL ESTATE AGENTS
# -----------------------------

@shared_task
def launch_real_estate_agents():

    for city in US_CITIES:

        zillow_scraper.delay(city)
        redfin_scraper.delay(city)

    return "Real estate agents launched"


# -----------------------------
# VEHICLE AGENTS
# -----------------------------

@shared_task
def launch_vehicle_agents():

    for city in CANADA_CITIES:

        autotrader_scraper.delay(city)
        kijiji_vehicle_scraper.delay(city)

    return "Vehicle agents launched"


# -----------------------------
# DEAL ANALYZERS
# -----------------------------

@shared_task
def launch_deal_analyzers():

    for _ in range(10):

        deal_analyzer.delay()

    return "Deal analyzers launched"


# -----------------------------
# MASTER AGENT LAUNCHER
# -----------------------------

@shared_task
def launch_all_agents():

    launch_real_estate_agents.delay()
    launch_vehicle_agents.delay()
    launch_deal_analyzers.delay()

    return "All AI agents launched"
