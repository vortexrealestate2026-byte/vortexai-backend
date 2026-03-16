import asyncio


async def run_property_agent():
    while True:
        print("🔎 Scanning properties...")
        await asyncio.sleep(60)
