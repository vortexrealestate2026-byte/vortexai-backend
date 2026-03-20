import logging
from src.celery_app import celery_app

logger = logging.getLogger("vortex-ai-celery")


# --------------------------------------------------
# EXAMPLE TASK (TEST)
# --------------------------------------------------

@celery_app.task(name="tasks.test_task")
def test_task():
    logger.info("Celery test task executed")
    return {"status": "success", "message": "Celery is working"}


# --------------------------------------------------
# PROPERTY SCRAPER TASK
# --------------------------------------------------

@celery_app.task(name="tasks.scrape_properties")
def scrape_properties(city: str):

    logger.info(f"Starting property scrape for {city}")

    # Placeholder logic
    properties_found = 25

    return {
        "city": city,
        "properties_found": properties_found
    }


# --------------------------------------------------
# VEHICLE SCRAPER TASK
# --------------------------------------------------

@celery_app.task(name="tasks.scrape_vehicles")
def scrape_vehicles():

    logger.info("Starting vehicle scrape")

    vehicles_found = 12

    return {
        "vehicles_found": vehicles_found
    }


# --------------------------------------------------
# DEAL ANALYSIS TASK
# --------------------------------------------------

@celery_app.task(name="tasks.analyze_deal")
def analyze_deal(price: float, arv: float, rehab: float):

    mao = (arv * 0.7) - rehab
    profit = mao - price

    return {
        "price": price,
        "arv": arv,
        "rehab": rehab,
        "mao": mao,
        "estimated_profit": profit
    }
