from unittest import mock
from unittest.mock import MagicMock
import unittest
from app import app
import apis.weather as weather

class WeatherTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_current_weather(self):
        with mock.patch('apis.weather.download_stored_query') as mock_download:
            mock_response = MagicMock()
            mock_response.location_metadata = {
                'station1': {'latitude': 60.1, 'longitude': 24.6},
                'station2': {'latitude': 60.2, 'longitude': 24.7}
            }
            mock_response.data = {
                'station1': {
                    't2m': {'values': [10.5]},
                    'ws_10min': {'values': [5.2]},
                    'p_sea': {'values': [1013.2]},
                    'rh': {'values': [70.5]}
                },
                'station2': {
                    't2m': {'values': [11.2]},
                    'ws_10min': {'values': [4.8]},
                    'p_sea': {'values': [1012.8]},
                    'rh': {'values': [75.2]}
                }
            }
            mock_download.return_value = mock_response
            expected_data = {
                'station1': {
                    'Air temperature': '10.5 °C',
                    'Wind': '5.2 m/s',
                    'Air pressure': '1013.2 mbar',
                    'Humidity': '70.5 %',
                    'Latitude': 60.1,
                    'Longitude': 24.6
                },
                'station2': {
                    'Air temperature': '11.2 °C',
                    'Wind': '4.8 m/s',
                    'Air pressure': '1012.8 mbar',
                    'Humidity': '75.2 %',
                    'Latitude': 60.2,
                    'Longitude': 24.7
                }
            }
            actual_data = weather.get_current_weather()
            self.assertEqual(actual_data, expected_data)


if __name__ == '__main__':
    unittest.main()
