from fastapi import FastAPI
import asyncio

from src.orchestrator.master_orchestrator import start_orchestrator

app = FastAPI()


@app.on_event("startup")
async def startup_event():

    asyncio.create_task(start_orchestrator())


@app.get("/")
def root():
    return {"message": "Vortex AI Running"}
