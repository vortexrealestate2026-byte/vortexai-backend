from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.tasks.scheduler import launch_all_agents
from app.database import engine, SessionLocal
from app.models import Base, Property, Vehicle

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="VORTEX API")

# -----------------------
# CORS
# -----------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# HEALTH CHECK
# -----------------------

@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------
# START AI AGENTS
# -----------------------

@app.get("/start-agents")
def start_agents():
    launch_all_agents.delay()
    return {"status": "AI agents launched"}


# -----------------------
# PROPERTIES
# -----------------------

@app.get("/properties")
def get_properties():

    db = SessionLocal()

    properties = db.query(Property).all()

    result = []

    for p in properties:
        result.append({
            "id": p.id,
            "city": p.city,
            "address": p.address,
            "price": p.price,
            "source": p.source
        })

    db.close()

    return result


# -----------------------
# VEHICLES
# -----------------------

@app.get("/vehicles")
def get_vehicles():

    db = SessionLocal()

    vehicles = db.query(Vehicle).all()

    result = []

    for v in vehicles:
        result.append({
            "id": v.id,
            "city": v.city,
            "make": v.make,
            "model": v.model,
            "price": v.price,
            "source": v.source
        })

    db.close()

    return result


# -----------------------
# DEALS (placeholder)
# -----------------------

@app.get("/deals")
def get_deals(min_score: int | None = None, max_price: int | None = None):
    return []


# -----------------------
# BUYERS
# -----------------------

@app.get("/buyers")
def get_buyers():
    return []


@app.post("/buyers")
def create_buyer(buyer: dict):
    return {**buyer, "id": "temp-id"}


# -----------------------
# LEADS
# -----------------------

@app.get("/leads")
def get_leads():
    return []


# -----------------------
# FINANCING APPROVALS
# -----------------------

@app.get("/approvals")
def get_approvals():
    return []
