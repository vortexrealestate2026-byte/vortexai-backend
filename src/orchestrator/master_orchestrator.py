import asyncio
import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Orchestrator
from src.orchestrator.master_orchestrator import start_orchestrator

# Dashboard API
from src.api.dashboard_routes import router as dashboard_router


# -------------------------------
# Logging Setup
# -------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("vortex-ai")


# -------------------------------
# FastAPI App
# -------------------------------

app = FastAPI(
    title="Vortex AI Autonomous Deal Engine",
    description="AI platform for real estate wholesale deals and vehicle financing automation",
    version="1.0.0",
)


# -------------------------------
# CORS (allow frontend dashboards)
# -------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------
# Register API Routes
# -------------------------------

app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)


# -------------------------------
# Root Endpoint
# -------------------------------

@app.get("/")
def root():
    return {
        "platform": "Vortex AI",
        "status": "running",
        "version": "1.0",
        "agents": "active"
    }


# -------------------------------
# Health Check
# -------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "vortex-ai-backend"
    }


# -------------------------------
# System Info Endpoint
# -------------------------------

@app.get("/system")
def system_info():

    return {
        "environment": os.getenv("ENVIRONMENT", "production"),
        "database": "connected",
        "ai_agents": "running",
        "orchestrator": "active"
    }


# -------------------------------
# Startup Event
# -------------------------------

@app.on_event("startup")
async def startup_event():

    logger.info("🚀 Starting Vortex AI System")

    # start autonomous agent orchestrator
    asyncio.create_task(start_orchestrator())

    logger.info("⚡ Autonomous AI Agents Started")


# -------------------------------
# Shutdown Event
# -------------------------------

@app.on_event("shutdown")
async def shutdown_event():

    logger.info("🛑 Vortex AI shutting down")
