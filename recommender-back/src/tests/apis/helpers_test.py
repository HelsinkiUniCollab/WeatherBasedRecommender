import unittest
from apis.helpers import PointOfInterest


class PointOfInterestTest(unittest.TestCase):
    def test_calculate_score_with_valid_data(self):
        poi_data = {
            'id': 1,
            'name': 'POI 1',
            'weather': {'Air temperature': '30 °C', 'Humidity': '50%'}
        }
        poi = PointOfInterest(**poi_data)
        self.assertAlmostEqual(poi.score, 1.0)

    def test_calculate_score_with_invalid_data(self):
        poi_data = {
            'id': 2,
            'name': 'POI 2',
            'weather': {'Air temperature': None, 'Humidity': '50%'}
        }
        poi = PointOfInterest(**poi_data)
        self.assertEqual(poi.score, -float('inf'))

    def test_point_of_interest_initialization(self):
        poi_data = {
            'id': 3,
            'name': 'POI 3',
            'weather': {'Air temperature': '25 °C', 'Humidity': '45%'}
        }
        poi = PointOfInterest(**poi_data)
        self.assertEqual(poi.id, 3)
        self.assertEqual(poi.name, 'POI 3')
        self.assertEqual(poi.score, 1.0)


if __name__ == '__main__':
    unittest.main()
