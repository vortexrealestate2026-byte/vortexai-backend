import os
from celery import Celery
from celery.schedules import crontab

REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "vortex_agents",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.update(
    timezone="UTC",
    enable_utc=True
)

celery_app.conf.beat_schedule = {

    # real estate scrapers every 3 hours
    "run-real-estate-agents": {
        "task": "app.tasks.scheduler.launch_real_estate_agents",
        "schedule": crontab(minute=0, hour="*/3"),
    },

    # vehicle scrapers every 2 hours
    "run-vehicle-agents": {
        "task": "app.tasks.scheduler.launch_vehicle_agents",
        "schedule": crontab(minute=0, hour="*/2"),
    },

    # deal analyzers every 2 hours
    "run-deal-analyzers": {
        "task": "app.tasks.scheduler.launch_deal_analyzers",
        "schedule": crontab(minute=30, hour="*/2"),
    },
}

celery_app.autodiscover_tasks(["app.tasks"])
