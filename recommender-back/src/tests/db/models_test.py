import unittest
from src.db.db import get_db, get_collection
from src.db.models import Poi

class TestPoiInit(unittest.TestCase):
    def test_saving_pois(self):
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

        all_documents = test_collection.find()
        pois = list(all_documents)

        self.assertEqual(len(pois), 1)
        test_collection.delete_many({})
