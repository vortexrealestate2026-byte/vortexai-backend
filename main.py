from fastapi import FastAPI
import asyncio

from src.orchestrator.master_orchestrator import start_orchestrator
from src.api.dashboard_routes import router as dashboard_router

app = FastAPI()

app.include_router(dashboard_router)


@app.on_event("startup")
async def startup_event():

    asyncio.create_task(start_orchestrator())


@app.get("/")
def root():
    return {"status": "Vortex AI running"}
