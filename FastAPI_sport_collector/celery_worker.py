import tasks
from celery_app import celery_app


celery_app.conf.beat_schedule = {
    "scrape-every-10-minutes": {
        "task": "scrape_data",
        "schedule": 300  # Every 5 minits
    }
}
