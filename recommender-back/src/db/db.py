import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.environ.get('DEVELOPMENT_DB_URI')
print(' * Connecting to MongoDB')

def get_db():
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database('poidata')
        return db
        
    except Exception as e:
        print(' * Error connecting to MongoDB:', str(e))
        return None
    
def get_collection():
    try:
        db = get_db()
        collection=db['pois']
        return collection          
    except Exception as e:
        print(' * Error getting collection in MongoDB:', str(e))
        return None

