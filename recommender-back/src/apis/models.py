from .db import get_db, close_db

class Poi:
    def __init__(self, name, latitude, longitude, accessibility, categories):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.accessibility = accessibility
        self.categories = categories

    def save(self):
        db, client = get_db()
        collection = db['pois']
        collection.insert_one({
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'not_accessible_for': self.accessibility,
            'categories': self.categories
        })
        close_db(client)

    @staticmethod
    def get_all():
        db, client = get_db()
        collection = db['pois']
        all_documents = collection.find()
        pois = list(all_documents)
        close_db(client)
        return pois