import asyncio
import logging

from src.scrapers.property_api import get_properties
from src.scrapers.vehicle_api import get_vehicles

from src.ai.deal_analyzer import analyze_property
from src.ai.vehicle_analyzer import analyze_vehicle

logger = logging.getLogger("vortex-ai")


async def run_agent(agent_id):

    logger.info(f"Agent {agent_id} started")

    while True:

        try:

            # -------------------------
            # PROPERTY DEAL SCAN
            # -------------------------

            properties = get_properties()

            for p in properties:

                analysis = analyze_property(p)

                if analysis["deal_score"] >= 6:

                    logger.info(
                        f"🔥 PROPERTY DEAL FOUND | "
                        f"Agent {agent_id} | "
                        f"Price: {analysis['price']} | "
                        f"Margin: {analysis['wholesale_margin']}"
                    )

            # -------------------------
            # VEHICLE DEAL SCAN
            # -------------------------

            vehicles = get_vehicles()

            for v in vehicles:

                vehicle_analysis = analyze_vehicle(v)

                if vehicle_analysis["deal_score"] >= 5:

                    logger.info(
                        f"🚗 VEHICLE LEAD FOUND | "
                        f"Agent {agent_id} | "
                        f"Price: {vehicle_analysis['price']} | "
                        f"Year: {vehicle_analysis['year']}"
                    )

        except Exception as e:

            logger.error(f"Agent {agent_id} error: {str(e)}")

        await asyncio.sleep(30)


async def start_mega_orchestrator():

    logger.info("🧠 Mega Orchestrator Booting")

    tasks = []

    for i in range(500):

        tasks.append(asyncio.create_task(run_agent(i)))

    logger.info("⚡ 500 agents launched")

    await asyncio.gather(*tasks)
