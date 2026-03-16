import asyncio

from src.leads.seller_finder import find_sellers
from src.leads.buyer_finder import find_investors
from src.leads.vehicle_buyer_finder import find_vehicle_buyers


async def run_lead_engine():

    print("🧲 Lead Engine Running")

    await find_sellers()
    await find_investors()
    await find_vehicle_buyers()

    print("✅ Lead Engine Completed")
