import os
import copy
import json
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.environ.get('DEVELOPMENT_DB_URI')
print(' * Connecting to MongoDB')

def get_db(test_env=False):
    try:
        
        if test_env:
            client = MongoClient(mongo_uri)
            db = client.get_database('test')
        else:
            client = MongoClient(mongo_uri)
            db = client.get_database('development')
        return db
    except Exception as e:
        print('Error connecting to MongoDB:', str(e))
        return None
    
def get_collection(test_env=False):
    db = get_db()
    collection=db['pois']
    return collection
                  

def close_db(client):
    client.close()
    print(' * Connection closed to MongoDB')
