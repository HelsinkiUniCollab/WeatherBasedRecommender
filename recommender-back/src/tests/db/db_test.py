import unittest
from src.db.db import get_db
from src.db.models import Poi

class TestDb(unittest.TestCase):
    def test_getting_db(self):
        db = get_db()
        self.assertEqual(db.name, "poidata") 

    def test_getting_collection(self):
        db = get_db()
        test_collection = db['pois_test']
        poi = Poi("Test POI", "21", "61", [], [{"category": "test"}])

        test_collection.insert_one({
            'name': poi.name,
            'latitude': poi.latitude,
            'longitude': poi.longitude,
            'not_accessible_for': poi.accessibility,
            'category': poi.categories
        })

        test_collection.delete_many({})
        self.assertEqual(test_collection.count_documents({}), 0)
