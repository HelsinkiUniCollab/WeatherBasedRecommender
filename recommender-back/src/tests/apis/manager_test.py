import unittest
from src.apis.manager import get_pois
from src.apis.poi import PointOfInterest


class TestGetPOIs(unittest.TestCase):
    def test_get_pois_returns_list(self):
        result = get_pois()
        self.assertIsInstance(result, list)

    def test_get_pois_contains_items(self):
        result = get_pois()
        self.assertTrue(len(result) > 0)

    def test_get_pois_all_items_are_point_of_interest_objects(self):
        result = get_pois()
        for poi in result:
            self.assertIsInstance(poi, PointOfInterest)

    def test_get_pois_structure(self):
        result = get_pois()
        for poi in result:
            self.assertTrue(hasattr(poi, 'name'))
            self.assertTrue(hasattr(poi, 'latitude'))
            self.assertTrue(hasattr(poi, 'longitude'))
            self.assertTrue(hasattr(poi, 'not_accessible_for'))
            self.assertTrue(hasattr(poi, 'categories'))

    def test_get_pois_coordinates_valid(self):
        result = get_pois()
        for poi in result:
            self.assertIsInstance(poi.latitude, float)
            self.assertIsInstance(poi.longitude, float)

if __name__ == '__main__':
    unittest.main()
