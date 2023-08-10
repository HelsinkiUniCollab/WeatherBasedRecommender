import unittest
from src.db.db import get_collection
from src.apis.manager import get_pois, find_nearest_coordinate_forecast_data
from src.apis.poi import PointOfInterest
from src.app import app
import json

class TestManger(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.fore = {
            "2023-07-20 12:00:00": {
                "60.201231, 24.973478": {
                    "Air temperature": "20.5 °C",
                    "Humidity": "58.2 %",
                    "Wind speed": "3.8 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "20.3 %"
                },
                "60.1998, 24.968672": {
                    "Air temperature": "19.8 °C",
                    "Humidity": "61.4 %",
                    "Wind speed": "4.1 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "15.7 %"
                },
                "60.189543, 24.921326": {
                    "Air temperature": "21.2 °C",
                    "Humidity": "54.6 %",
                    "Wind speed": "3.4 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "24.9 %"
                }
            },
            "2023-07-20 13:30:00": {
                "60.201231, 24.973478": {
                    "Air temperature": "21.8 °C",
                    "Humidity": "52.9 %",
                    "Wind speed": "4.5 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "12.1 %"
                },
                "60.1998, 24.968672": {
                    "Air temperature": "20.3 °C",
                    "Humidity": "59.0 %",
                    "Wind speed": "4.0 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "18.5 %"
                },
                "60.189543, 24.921326": {
                    "Air temperature": "22.0 °C",
                    "Humidity": "50.3 %",
                    "Wind speed": "3.2 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "29.4 %"
                }
            },
            "2023-07-20 15:15:00": {
                "60.201231, 24.973478": {
                    "Air temperature": "22.5 °C",
                    "Humidity": "49.1 %",
                    "Wind speed": "4.8 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "8.6 %"
                },
                "60.1998, 24.968672": {
                    "Air temperature": "20.8 °C",
                    "Humidity": "56.7 %",
                    "Wind speed": "3.9 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "16.9 %"
                },
                "60.189543, 24.921326": {
                    "Air temperature": "22.8 °C",
                    "Humidity": "47.6 %",
                    "Wind speed": "3.7 m/s",
                    "Precipitation": "0.0 mm",
                    "Cloud amount": "34.2 %"
                }
            }
        }

    '''def test_get_simulated_pois_as_json(self):
        response = self.client.get(
            '/api/simulator?air_temperature=10&wind_speed=5&humidity=10&precipitation=5&cloud_amount=10&air_quality=2')
        data = json.loads(response.text)
        tested = data[0]['weather']['Weather']
        del tested['Score']
        equals = {'Air temperature': '10 °C',
                  'Wind speed': '5 m/s',
                  'Humidity': '10 %',
                  'Precipitation': '5 mm',
                  'Cloud amount': '10 %',
                  'Air quality': '2'}
        self.assertEqual(tested, equals)'''
    def test_get_simulated_pois_as_json(self):
        # Define parameters
        params = {
            "air_temperature": 10,
            "wind_speed": 5,
            "humidity": 10,
            "precipitation": 5,
            "cloud_amount": 10,
            "air_quality": 2,
            "current_time": '16:00',
            'sunrise': '6:00',
            'sunset': '22:00',
        }

        # Make POST request and get response
        response = self.client.post(
            '/api/simulator', 
            json=params,
        )

        data = json.loads(response.text)
        tested = data[0]['weather']['Weather']
        del tested['Score']
        equals = {'Air temperature': '10 °C',
                'Wind speed': '5 m/s',
                'Humidity': '10 %',
                'Precipitation': '5 mm',
                'Cloud amount': '10 %',
                'Air quality': 2}
        self.assertEqual(tested, equals)

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

    def test_find_nearest_coordinates(self):
        pois = get_pois()
        for onepoi in pois:
            res = find_nearest_coordinate_forecast_data(onepoi, self.fore)
            self.assertEqual(len(res.weather), 3)
            break


if __name__ == '__main__':
    unittest.main()
