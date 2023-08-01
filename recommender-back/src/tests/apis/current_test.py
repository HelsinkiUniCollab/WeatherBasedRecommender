import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.app import app
from src.apis.poi import PointOfInterest
from src.apis.current import Current
from src.services.forecastdatafetcher import DataFetcher
import json


class CurrentTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.item = PointOfInterest(longitude=24.65, latitude=60.15)
        self.fetcher = DataFetcher()

    def test_get_current_weather(self):
        with mock.patch(
            'src.services.forecastdatafetcher.DataFetcher.get_current_weather_data'
        ) as mock_download:
            mock_response = MagicMock()
            mock_response.location_metadata = {
                'station1': {'latitude': 60.1, 'longitude': 24.6},
                'station2': {'latitude': 60.2, 'longitude': 24.7},
            }
            mock_response.data = {
                'station1': {
                    't2m': {'values': [10.5]},
                    'ws_10min': {'values': ['nan']},
                    'ri_10min': {'values': ['nan']},
                    'n_man': {'values': ['nan']},
                    'rh': {'values': ['nan']},
                    'AQINDEX_PT1H_avg': {'values': ['nan']}
                },
                'station2': {
                    't2m': {'values': [11.2]},
                    'ws_10min': {'values': ['nan']},
                    'ri_10min': {'values': ['nan']},
                    'n_man': {'values': ['nan']},
                    'rh': {'values': ['nan']},
                    'AQINDEX_PT1H_avg': {'values': ['nan']}
                }
            }
            mock_download.return_value = mock_response
            self.current = Current(self.fetcher)
            expected_data = {
                'station1': {
                    'Air temperature': '10.5 °C',
                    'Latitude': 60.1,
                    'Longitude': 24.6,
                },
                'station2': {
                    'Air temperature': '11.2 °C',
                    'Latitude': 60.2,
                    'Longitude': 24.7,
                },
            }
            self.assertEqual(self.current.weather, expected_data)

    def test_find_nearest_stations_weather_data(self):
        self.current = Current(self.fetcher)
        self.current.weather = {
            'station1': {
                'Latitude': 60.1,
                'Longitude': 24.6,
                'Air temperature': '10.5 °C',
                'Wind speed': '10.0 m/s',
                'Precipitation': '10.0 %',
                'Cloud amount': '5.0 %',
                'Humidity': '60.0 %',
                'Air quality': '1.0 AQI'
            },
            'station2': {
                'Latitude': 60.5,
                'Longitude': 26.0,
                'Air temperature': '11.2 °C',
                'Wind speed': '10.0 m/s',
                'Precipitation': '10.0 %',
                'Cloud amount': '5.0 %',
                'Humidity': '60.0 %',
                'Air quality': '1.0 AQI'
            }
        }

        expected_item = {
            'Air temperature': '10.5 °C',
            'Wind speed': '10.0 m/s',
            'Precipitation': '10.0 %',
            'Cloud amount': '5.0 %',
            'Humidity': '60.0 %',
            'Air quality': '1.0 AQI'
        }
        self.current.find_nearest_stations_weather_data(self.item)
        self.assertEqual(self.item.weather['Current'], expected_item)

    def test_find_nearest_stations_weather_data_with_missing_fields(self):
        self.current = Current(self.fetcher)

        self.current.weather = {
            'station1': {
                'Latitude': 60.1,
                'Longitude': 24.6,
                'Air temperature': '10.5 °C',
                'Precipitation': '10.0 %',
                'Cloud amount': '5.0 %',
                'Humidity': '60.0 %',
                'Air quality': '1.0 AQI'
            },
            'station2': {
                'Latitude': 60.5,
                'Longitude': 26.0,
                'Wind speed': '10.0 m/s',
                'Precipitation': '10.0 %',
                'Cloud amount': '5.0 %',
                'Humidity': '60.0 %',
                'Air quality': '1.0 AQI'
            }
        }

        expected_item = {
            'Air temperature': '10.5 °C',
            'Wind speed': '10.0 m/s',
            'Precipitation': '10.0 %',
            'Cloud amount': '5.0 %',
            'Humidity': '60.0 %',
            'Air quality': '1.0 AQI'
        }

        self.current.find_nearest_stations_weather_data(self.item)
        self.assertEqual(self.item.weather['Current'], expected_item)
