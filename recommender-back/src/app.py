import os
from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient

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

def get_db():
    try:
        mongo_uri = os.environ.get('DEVELOPMENT_DB_URI')
        print(' * Connecting to', mongo_uri)
        client = MongoClient(mongo_uri)
        db = client.get_database('development') 
        print(' * Connected to MongoDB')
        collection = db['pois']
        test = collection.find_one()
        print(test)
        client.close()
        return db
    except Exception as e:
        print('Error connecting to MongoDB:', str(e))
        return None
    
db = get_db()

from src import routes
