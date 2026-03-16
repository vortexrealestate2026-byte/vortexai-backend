from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.tasks.scheduler import launch_all_agents
app = FastAPI(title="VORTEX API")

# -------------------------------
# CORS
# -------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Health Check
# -------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------------
# Start AI Agents
# -------------------------------

@app.get("/start-agents")
def start_agents():
    launch_agents()
    return {"status": "AI agents launched"}

# -------------------------------
# Real Estate API
# -------------------------------

@app.get("/properties")
def get_properties():
    # TODO: replace with PostgreSQL query
    return []

@app.get("/deals")
def get_deals(min_score: int | None = None, max_price: int | None = None):
    # TODO: replace with PostgreSQL query
    return []

# -------------------------------
# Buyers
# -------------------------------

@app.get("/buyers")
def get_buyers():
    return []

@app.post("/buyers")
def create_buyer(buyer: dict):
    return {**buyer, "id": "temp-id"}

# -------------------------------
# Vehicle System
# -------------------------------

@app.get("/vehicles")
def get_vehicles():
    return []

@app.get("/leads")
def get_leads():
    return []

@app.get("/approvals")
def get_approvals():
    return []
