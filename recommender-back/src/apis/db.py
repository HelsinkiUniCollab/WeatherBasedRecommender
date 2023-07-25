import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.environ.get('DEVELOPMENT_DB_URI')

def get_db(test_env=False):
    try:
        print(' * Connecting to MongoDB')
        if test_env:
            client = MongoClient(mongo_uri)
            db = client.get_database('test_db')
        else:
            client = MongoClient(mongo_uri)
            db = client.get_database('development')
        db['pois'].create_index('name', unique=True)
        print(' * Connected to MongoDB')
        return db, client
    except Exception as e:
        print('Error connecting to MongoDB:', str(e))
        return None

def close_db(client):
    client.close()
    print(' * Connection closed to MongoDB')