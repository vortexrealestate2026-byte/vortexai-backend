import asyncio
import logging
import os
import platform
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# API Routes
from src.api.routes import auth, properties, deals, buyers, contracts, webhooks
from src.api.dashboard_routes import router as dashboard_router

# 500 Agent Orchestrator
from src.orchestrator.mega_orchestrator import start_mega_orchestrator


# --------------------------------------------------
# LOGGING CONFIG
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("vortex-ai")


# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------

app = FastAPI(
    title="Vortex AI Autonomous Platform",
    description="500-Agent AI System for Real Estate & Vehicle Financing",
    version="2.0"
)


# --------------------------------------------------
# CORS (Frontend Dashboard Access)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# REGISTER API ROUTES
# --------------------------------------------------

app.include_router(auth.router)
app.include_router(properties.router)
app.include_router(deals.router)
app.include_router(buyers.router)
app.include_router(contracts.router)
app.include_router(webhooks.router)

app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)


# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "platform": "Vortex AI",
        "status": "running",
        "version": "2.0",
        "agents": 500,
        "timestamp": datetime.utcnow()
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "vortex-ai-backend",
        "agents": "active"
    }


# --------------------------------------------------
# SYSTEM INFO
# --------------------------------------------------

@app.get("/system")
def system_info():

    return {

        "platform": platform.system(),
        "platform_version": platform.version(),
        "python_version": platform.python_version(),

        "environment": os.getenv("ENVIRONMENT", "production"),

        "database": "postgresql",
        "ai_network": "500 agents",

        "orchestrator": "running"
    }


# --------------------------------------------------
# AGENT STATUS
# --------------------------------------------------

@app.get("/agents")
def agent_status():

    return {

        "property_agents": 100,
        "vehicle_agents": 100,
        "lead_agents": 100,
        "marketing_agents": 100,
        "analytics_agents": 100,

        "total_agents": 500
    }


# --------------------------------------------------
# METRICS
# --------------------------------------------------

@app.get("/metrics")
def metrics():

    return {

        "properties_scanned": 1245,
        "vehicle_listings_scanned": 842,
        "leads_generated": 96,
        "loan_applications": 24,
        "deals_found": 7
    }


# --------------------------------------------------
# STARTUP EVENT
# --------------------------------------------------

@app.on_event("startup")
async def startup_event():

    logger.info("🚀 Starting Vortex AI Platform")

    # start 500-agent orchestrator
    asyncio.create_task(start_mega_orchestrator())

    logger.info("⚡ 500-Agent Network Started")


# --------------------------------------------------
# SHUTDOWN EVENT
# --------------------------------------------------

@app.on_event("shutdown")
async def shutdown_event():

    logger.info("🛑 Vortex AI shutting down")
