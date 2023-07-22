from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv

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
