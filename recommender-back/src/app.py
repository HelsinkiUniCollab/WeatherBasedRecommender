from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv
from .config import Config

load_dotenv()

config = {
    "DEBUG": True,
    "CACHE_TYPE": Config.CACHE_TYPE,
    "CACHE_REDIS_URL": Config.CACHE_REDIS_URL,
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
CORS(app)

cache = Cache(app, config=config)

from src import routes
