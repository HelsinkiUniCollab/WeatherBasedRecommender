import unittest
from src.db.db import get_db, get_collection

class TestManger(unittest.TestCase):
    def test_getting_db(self):
        db = get_db()
        self.assertEqual(db.name, "poidata") 


    def test_getting_collection(self):
        collection = get_collection()
        collection.delete_many({})
        self.assertEqual(collection.count_documents({}), 0)

if __name__ == '__main__':
    unittest.main()
