from .db import get_db

db = get_db()
pois_collection = db['pois']  

class Poi:
    def __init__(self, name, latitude, longitude, accessibility, categories):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.accessibility = accessibility
        self.categories = categories

    def save(self):
        pois_collection.insert_one({
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'not_accessible_for': self.accessibility,
            'categories': self.categories
        })

    def get_all(test=False):
        all_documents = pois_collection.find()
        pois = list(all_documents)
        return pois
