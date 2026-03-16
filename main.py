from fastapi import FastAPI
import asyncio
from src.tasks.agent_scheduler import launch_all_agents

app = FastAPI()

@app.on_event("startup")
async def start_agents():
    asyncio.create_task(launch_all_agents())

@app.get("/")
def root():
    return {"status":"Vortex AI running"}
