from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="VORTEX API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Health check ------------------------------------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}


# --- Stub endpoints to match your frontend -----------------------------------

@app.get("/properties")
def get_properties():
    return []  # replace with DB query


@app.get("/deals")
def get_deals(min_score: int | None = None, max_price: int | None = None):
    return []  # replace with filtered DB query


@app.get("/buyers")
def get_buyers():
    return []  # replace with DB query


@app.post("/buyers")
def create_buyer(buyer: dict):
    # replace with DB insert + return created buyer
    return {**buyer, "id": "temp-id"}
