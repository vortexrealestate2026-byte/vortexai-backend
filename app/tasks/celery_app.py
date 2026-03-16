import os
from celery import Celery
from celery.schedules import crontab

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://default:valEtDpprQzlMMnxnJQoNYthJIJQXIKJ@redis.railway.internal:6379/0"
)

celery_app = Celery(
    "vortex_ai",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.update(
    broker_url=REDIS_URL,
    result_backend=REDIS_URL,
    accept_content=["json"],
    task_serializer="json",
    result_serializer="json",
    timezone="UTC",
    enable_utc=True
)

celery_app.conf.beat_schedule = {

    "real-estate-agents": {
        "task": "app.tasks.scheduler.launch_real_estate_agents",
        "schedule": crontab(minute=0, hour="*/3"),
    },

    "vehicle-agents": {
        "task": "app.tasks.scheduler.launch_vehicle_agents",
        "schedule": crontab(minute=0, hour="*/2"),
    },

    "deal-analyzers": {
        "task": "app.tasks.scheduler.launch_deal_analyzers",
        "schedule": crontab(minute=30, hour="*/2"),
    },
}

celery_app.autodiscover_tasks(["app.tasks"])
