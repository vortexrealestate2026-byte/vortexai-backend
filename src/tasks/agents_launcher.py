from celery import shared_task
from src.services.data_service import save_property, save_vehicle


# -------------------------
# REAL ESTATE SCRAPER
# -------------------------

@shared_task
def zillow_scraper(city):

    print(f"Scraping Zillow in {city}")

    save_property(
        city=city,
        address="123 Main St",
        price=150000,
        source="zillow"
    )


@shared_task
def redfin_scraper(city):

    print(f"Scraping Redfin in {city}")

    save_property(
        city=city,
        address="45 Market St",
        price=180000,
        source="redfin"
    )


# -------------------------
# VEHICLE SCRAPER
# -------------------------

@shared_task
def autotrader_scraper(city):

    print(f"Scraping AutoTrader in {city}")

    save_vehicle(
        city=city,
        make="Toyota",
        model="Camry",
        price=12000,
        source="autotrader"
    )


@shared_task
def kijiji_vehicle_scraper(city):

    print(f"Scraping Kijiji in {city}")

    save_vehicle(
        city=city,
        make="Honda",
        model="Civic",
        price=9000,
        source="kijiji"
    )


# -------------------------
# DEAL ANALYZER
# -------------------------

@shared_task
def deal_analyzer():

    print("Analyzing deals...")
