import unittest
from src.db.db import get_db
from src.db.models import Poi

class TestManger(unittest.TestCase):
    def test_saving_pois(self):
        db = get_db()
        collection = db['pois']
        collection.delete_many({})
        poi = Poi("Test POI", "21", "61", [], [{"category": "test"}])
        poi.save()
        self.assertEqual(len(poi.get_all()), 1)
        collection.delete_many({})

if __name__ == '__main__':
    unittest.main()
