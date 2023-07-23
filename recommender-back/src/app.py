import os
from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv
from .models import Poi

load_dotenv()

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
CORS(app)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

# Testing database connection
Poi.save(Poi("Test Poi1", 100, 100))
Poi.save(Poi("Test Poi2", 120, 120))
Poi.get_all()

from src import routes
