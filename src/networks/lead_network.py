import asyncio
import random


async def lead_agent(agent_id):

    print(f"🎯 Lead Agent {agent_id} finding buyers")

    await asyncio.sleep(random.uniform(0.5, 2))

    print(f"🎯 Agent {agent_id} captured new lead")


async def run_lead_network():

    tasks = []

    for i in range(100):

        tasks.append(lead_agent(i))

    await asyncio.gather(*tasks)
