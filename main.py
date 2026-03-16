from fastapi import FastAPI
from tasks.scheduler import launch_all_agents

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Vortex AI running"}


@app.get("/start-agents")
def start_agents():
    launch_all_agents.delay()
    return {"message": "Agents started"}
