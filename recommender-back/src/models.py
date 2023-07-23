from .db import get_db, close_db

class Poi:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def save(self):
        db, client = get_db()
        collection = db['pois']
        collection.insert_one({
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        })
        close_db(client)

    @staticmethod
    def get_all():
        db, client = get_db()
        collection = db['pois']
        all_documents = collection.find()
        for document in all_documents:
           print(document)
        close_db(client)