from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv
from .celery_worker import celery
from .config import Config
from .services.tasks import fetch_data

load_dotenv()

config = {
    "DEBUG": True,
    "CACHE_TYPE": Config.CACHE_TYPE,
    "CACHE_REDIS_URL": Config.CACHE_REDIS_URL,
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CELERY_BROKER_URL": Config.CELERY_URL,
    "CELERY_RESULT_BACKEND": Config.CELERY_URL,
}

app = Flask(__name__)
app.config.from_mapping(config)
CORS(app)

cache = Cache(app)

from src import routes
