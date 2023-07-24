import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.environ.get('DEVELOPMENT_DB_URI')

def get_db():
    try:
        print(' * Connecting to', mongo_uri)
        client = MongoClient(mongo_uri)
        db = client.get_database('development') 
        collection_name = 'pois'
        db['pois'].create_index('name', unique=True)
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
        print(' * Connected to MongoDB')
        return db, client
    except Exception as e:
        print('Error connecting to MongoDB:', str(e))
        return None

def close_db(client):
    client.close()
    print(' * Connection closed to MongoDB')