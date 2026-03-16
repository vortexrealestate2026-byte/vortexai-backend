import asyncio
import random


async def property_agent(agent_id):

    print(f"🏠 Property Agent {agent_id} scanning")

    await asyncio.sleep(random.uniform(0.5, 2))

    print(f"🏠 Agent {agent_id} found property deal")


async def run_property_network():

    tasks = []

    for i in range(100):

        tasks.append(property_agent(i))

    await asyncio.gather(*tasks)
