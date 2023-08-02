from celery import Celery
from celery.schedules import crontab

def make_celery(app_name=__name__):
    backend = 'redis://redis:6379/0'
    broker = 'redis://redis:6379/0'
    celery = Celery(app_name, backend=backend, broker=broker)

    celery.conf.beat_schedule = {
        'fetch_data': {
            'task': 'src.services.tasks.fetch_data',  # import path for the task
            'schedule': crontab(minute='*/10'),  # execute every 10 minutes
            'args': (),  # arguments passed to the task function
        },
    }

    return celery
