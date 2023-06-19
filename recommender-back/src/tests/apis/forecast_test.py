import unittest
import numpy as np
from datetime import datetime
from unittest.mock import MagicMock, PropertyMock, patch
from apis.weather import ForecastGrid, parse_forecast

class ForecastTest(unittest.TestCase):
    def setUp(self):
        self.forecastgrid = ForecastGrid()
        self.grid_by_datetime = MagicMock()
        self.mock_grid = MagicMock()

        self.grid_by_datetime.data = {
            datetime(2023, 6, 19, 5, 0): self.mock_grid
        }

        self.mock_grid_data = PropertyMock(return_value={
            datetime(2023, 6, 19, 5, 0): {
                0: {
                    'Mean sea level pressure': {
                        'units': 'Pa',
                        'data': np.array([[10300, 10500, 10600, 10700, 10800]])
                    }
                },
                2: {
                    '2 metre temperature': {
                        'units': 'K',
                        'data': np.array([[288.2, 287.3, 283.5, 291.4, 287.7]])
                    }
                },
                10: {
                    '10 metre wind speed': {
                        'units': 'm s**-1',
                        'data': np.array([[1.23, 1.7, 1.43, 1.42, 1.77]])
                    }
                }
            }
        })

        type(self.mock_grid).data = self.mock_grid_data
        type(self.mock_grid).latitudes = PropertyMock(return_value=np.array([[60.1, 60.2, 60.3, 60.4, 60.5]]))
        type(self.mock_grid).longitudes = PropertyMock(return_value=np.array([[24.6, 24.7, 24.8, 24.9, 25.0]]))

    @patch('apis.weather.download_stored_query')
    def test_data_is_updated_correctly(self, mock_download_stored_query):
        mock_download_stored_query.return_value = self.grid_by_datetime

        self.forecastgrid.update_data()

        # Check that data contains a grid object
        self.assertIsInstance(self.forecastgrid.data, type(self.mock_grid))

        # Check that coordinates are now pairs
        np.testing.assert_array_equal(
            self.forecastgrid.coordinates,
            np.array([((60.1, 24.6), (60.2, 24.7), (60.3, 24.8), (60.4, 24.9), (60.5, 25.0))])
        )

        # Check that valid_times returns datetime dict_keys
        expected_valid_times = self.grid_by_datetime.data.keys()
        self.assertEqual(self.forecastgrid.valid_times, expected_valid_times)

        # Check that all data levels match
        expected_data_levels = []
        for datetime_data in self.mock_grid.data.values():
            data_levels = datetime_data.keys()
            expected_data_levels.extend(data_levels)
        self.assertListEqual(list(self.forecastgrid.data_levels), expected_data_levels)

    def test_get_coordinates_returns_correct_list_of_pairs(self):
        self.forecastgrid.coordinates = np.dstack((self.mock_grid.latitudes, self.mock_grid.longitudes))
        coordinates = self.forecastgrid.get_coordinates()
        for lat, lon in zip(self.mock_grid.latitudes.flatten(), self.mock_grid.longitudes.flatten()):
            assert any(np.allclose([lat, lon], coord) for coord in coordinates)

    def test_forecast_data_is_parsed_correctly(self):
            data = [{'Dataset': '2 metre temperature', 'Unit': 'K', 'Data': 280.0},
                    {'Dataset': '2 metre relative humidity', 'Unit': '%', 'Data': 64.013},
                    {'Dataset': '10 metre wind speed', 'Unit': 'm s**-1', 'Data': 1.6543},
                    {'Dataset': 'Mean sea level pressure', 'Unit': 'Pa', 'Data': 101500.2423}]

            expected_parsed_data = {'Air temperature': '6.9 °C',
                                    'Wind': '1.7 m/s', 
                                    'Air pressure': '1015.0 mbar',
                                    'Humidity': '64.0 %'}

            parsed_data = parse_forecast(data)

            self.assertEqual(parsed_data, expected_parsed_data)
