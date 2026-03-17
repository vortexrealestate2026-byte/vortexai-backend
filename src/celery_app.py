
import os
from celery import Celery
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Redis connection
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Create Celery app
celery_app = Celery(
    "vortex_ai",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    broker_connection_retry_on_startup=True
)

# Auto-discover tasks
celery_app.autodiscover_tasks(
    [
        "src.tasks",
        "src.scrapers",
        "src.agents"
    ]
)
