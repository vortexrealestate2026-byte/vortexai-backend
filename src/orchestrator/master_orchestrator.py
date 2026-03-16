import asyncio
from datetime import datetime

from src.tasks.agent_scheduler import run_property_agents
from src.tasks.agent_scheduler import run_vehicle_agents
from src.tasks.agent_scheduler import run_analysis_agents
from src.tasks.agent_scheduler import run_buyer_matching_agents
from src.tasks.agent_scheduler import run_outreach_agents


class VortexOrchestrator:

    def __init__(self):
        self.running = True

    async def start(self):

        print("🚀 Vortex AI Orchestrator Started")

        while self.running:

            print(f"🧠 Cycle started {datetime.utcnow()}")

            # Run agents
            await run_property_agents()
            await run_vehicle_agents()
            await run_analysis_agents()
            await run_buyer_matching_agents()
            await run_outreach_agents()

            print("✅ Cycle completed")

            await asyncio.sleep(60)


orchestrator = VortexOrchestrator()


async def start_orchestrator():
    await orchestrator.start()
