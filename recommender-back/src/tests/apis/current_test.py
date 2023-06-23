from unittest import mock
from unittest.mock import MagicMock
import unittest
from app import app
from apis.poi import PointOfInterest
from apis.current import Current


class CurrentTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_current_weather(self):
        with mock.patch('apis.current.download_stored_query') as mock_download:
            mock_response = MagicMock()
            mock_response.location_metadata = {
                'station1': {'latitude': 60.1, 'longitude': 24.6},
                'station2': {'latitude': 60.2, 'longitude': 24.7}
            }
            mock_response.data = {
                'station1': {
                    't2m': {'values': [10.5]},
                    'ws_10min': {'values': ['nan']},
                    'ri_10min': {'values': ['nan']},
                    'n_man': {'values': ['nan']},
                    'rh': {'values': ['nan']}
                },
                'station2': {
                    't2m': {'values': [11.2]},
                    'ws_10min': {'values': ['nan']},
                    'ri_10min': {'values': ['nan']},
                    'n_man': {'values': ['nan']},
                    'rh': {'values': ['nan']}
                }
            }
            mock_download.return_value = mock_response
            self.current = Current()
            expected_data = {
                'station1': {
                    'Air temperature': '10.5 °C',
                    'Latitude': 60.1,
                    'Longitude': 24.6
                },
                'station2': {
                    'Air temperature': '11.2 °C',
                    'Latitude': 60.2,
                    'Longitude': 24.7
                }
            }
            self.assertEqual(self.current.weather, expected_data)

    def test_find_nearest_stations_weather_data(self):
        self.current = Current()
        missing_fields = ['Air temperature', 'Wind speed',
                          'Precipitation', 'Cloud amount', 'Humidity']
        self.current.weather = {
            'station1': {
                'Latitude': 60.1,
                'Longitude': 24.6,
                'Air temperature': '10.5 °C',
                'Wind speed': '10.0 m/s',
                'Precipitation': '10.0 %',
                'Cloud amount': '5.0 %',
                'Humidity': '60.0 %'
            },
            'station2': {
                'Latitude': 60.5,
                'Longitude': 26.0,
                'Air temperature': '11.2 °C',
                'Wind speed': '10.0 m/s',
                'Precipitation': '10.0 %',
                'Cloud amount': '5.0 %',
                'Humidity': '60.0 %'
            }
        }

        item = PointOfInterest(longitude=24.65, latitude=60.15)

        expected_item = {
            'Air temperature': '10.5 °C',
            'Wind speed': '10.0 m/s',
            'Precipitation': '10.0 %',
            'Cloud amount': '5.0 %',
            'Humidity': '60.0 %'
        }
        self.current.find_nearest_stations_weather_data(item)
        self.assertEqual(item.weather['Current'], expected_item)


if __name__ == '__main__':
    unittest.main()
