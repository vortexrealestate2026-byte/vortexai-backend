from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

celery = Celery(
    "vortex",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery.autodiscover_tasks(["tasks"])
