import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
if 'MONGO_URI' in os.environ:
        mongo_uri = os.environ['MONGO_URI']
else:
    mongo_uri = os.environ.get('DEVELOPMENT_DB_URI')

def get_db():
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database('poidata')
        return db
        
    except Exception as e:
        print(' * Error connecting to MongoDB:', str(e))
        return None
    
def get_collection(name):
    try:
        db = get_db()
        collection=db[name]
        return collection          
    except Exception as e:
        print(' * Error getting collection from MongoDB:', str(e))
        return None

