from celery import Celery
from celery.schedules import crontab

REDIS_URL = "redis://default:valEtDpprQzlMMnxnJQoNYthJIJQXIKJ@redis.railway.internal:6379/0"

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

    "run-real-estate-agents": {
        "task": "app.tasks.scheduler.launch_real_estate_agents",
        "schedule": crontab(minute=0, hour="*/3"),
    },

    "run-vehicle-agents": {
        "task": "app.tasks.scheduler.launch_vehicle_agents",
        "schedule": crontab(minute=0, hour="*/2"),
    },

    "run-deal-analyzers": {
        "task": "app.tasks.scheduler.launch_deal_analyzers",
        "schedule": crontab(minute=30, hour="*/2"),
    },
}

celery_app.autodiscover_tasks(["app.tasks"])
