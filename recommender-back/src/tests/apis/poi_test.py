import unittest
from apis.poi import find_nearest_stations_weather_data


class POITest(unittest.TestCase):
    def test_find_nearest_stations_weather_data(self):
        weather_data = {
            'station1': {
                'Latitude': 60.1,
                'Longitude': 24.6,
                'Air temperature': '10.5 °C'
            },
            'station2': {
                'Latitude': 60.5,
                'Longitude': 26.0,
                'Air temperature': '11.2 °C'
            }
        }

        item = {
            'location': {
                'coordinates': [24.65, 60.15]
            }
        }

        expected_item = {
            'location': {
                'coordinates': [24.65, 60.15]
            },
            'weather': {'Current': {
                'Latitude': 60.1,
                'Longitude': 24.6,
                'Air temperature': '10.5 °C'
            }
        }
        }

        # Call the function to get the actual result
        actual_item = find_nearest_stations_weather_data(item, weather_data)

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_item, expected_item)
