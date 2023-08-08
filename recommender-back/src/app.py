import os
from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv
from .config import Config

load_dotenv()

if os.environ.get('CACHE_MODE') == 'simple':
    CACHE_TYPE = 'SimpleCache'
else:
    CACHE_TYPE = 'redis'

config = {
    "DEBUG": True,
    "CACHE_TYPE": CACHE_TYPE,
    "CACHE_REDIS_URL": Config.CACHE_REDIS_URL,
    "CACHE_DEFAULT_TIMEOUT": 3600
}

app = Flask(__name__)
app.config.from_mapping(config)
CORS(app)

cache = Cache(app)

from src import routes
