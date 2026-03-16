from app.celery_worker import celery
from agents.property_scraper import scrape_properties

@celery.task
def run_property_agent():

    properties = scrape_properties()

    return properties
