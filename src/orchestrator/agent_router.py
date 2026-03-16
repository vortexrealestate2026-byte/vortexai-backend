import asyncio

from src.agents.properties.zillow_scraper_agent import run_zillow_scraper
from src.agents.properties.deal_scoring_agent import score_property

from src.agents.vehicles.vehicle_inventory_agent import run_vehicle_inventory

from src.agents.finance.loan_generation_agent import generate_loan
from src.agents.finance.bank_submission_agent import submit_to_bank

from src.agents.notifications.investor_alert_agent import send_investor_alert


async def run_property_agents():

    properties = await run_zillow_scraper()

    for p in properties:

        score = await score_property(p)

        await send_investor_alert(p, score)


async def run_vehicle_agents():

    vehicles = await run_vehicle_inventory()

    for v in vehicles:

        loan = await generate_loan(v)

        await submit_to_bank(loan)


async def run_all_agents():

    await asyncio.gather(

        run_property_agents(),
        run_vehicle_agents()

    )
