import os
from celery import Celery

celery = Celery(
    "vortex_agents",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)
