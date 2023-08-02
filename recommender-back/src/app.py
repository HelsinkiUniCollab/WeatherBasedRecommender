from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv
from celery import Celery
from .config import Config

def create_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"]
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
            
    celery.Task = ContextTask
    return celery

load_dotenv()

config = {
    "DEBUG": True,
    "CACHE_TYPE": Config.CACHE_TYPE,
    "CACHE_REDIS_URL": Config.CACHE_REDIS_URL,
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CELERY_BROKER_URL": Config.CELERY_URL,
    "CELERY_RESULT_BACKEND": Config.CELERY_URL
}

app = Flask(__name__)
app.config.from_mapping(config)
celery = create_celery(app)
CORS(app)

cache = Cache(app)

from src import routes
