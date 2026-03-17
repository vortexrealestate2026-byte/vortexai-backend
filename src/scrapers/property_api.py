from src.scrapers.web_scraper_engine import scrape_site
from src.scrapers.property_sources import PROPERTY_SITES
import logging

logger = logging.getLogger("vortex-ai")


def get_properties():

    properties = []

    for site in PROPERTY_SITES:

        results = scrape_site(site)

        properties.extend(results)

    logger.info(f"Collected {len(properties)} properties")

    return properties
