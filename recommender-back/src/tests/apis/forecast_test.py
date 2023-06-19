import unittest
import numpy as np
from datetime import datetime, timedelta 
from fmiopendata import grid
from unittest.mock import MagicMock, PropertyMock, patch
from apis.weather import ForecastGrid, parse_forecast

class ForecastTest(unittest.TestCase):
    def setUp(self):
        self.datetime_mock = MagicMock()
        self.mock_grid = MagicMock(spec=grid.Grid)
        self.forecastgrid = ForecastGrid()

        mock_grid_data = {
            0: {
                'Mean sea level pressure': {
                    'units': 'Pa',
                    'data': np.array([[1000, 1000, 1000, 1000, 1000]])
                },
            },
            2: {
                '2 metre temperature': {
                    'units': 'K',
                    'data': np.array([[280, 280, 280, 280, 280]])
                }
            },
            10: {
                'Mean wind direction': {
                    'units': 'degrees',
                    'data': np.array([[180, 180, 180, 180, 180]])
                }
            }
        }

        mock_datetimes = {
            datetime.now(): self.mock_grid,
            datetime.now() - timedelta(hours=3): self.mock_grid,
            datetime.now() - timedelta(hours=6): self.mock_grid
        }

        self.datetime_mock.data = mock_datetimes
        type(self.mock_grid).latitudes = PropertyMock(return_value=np.array([[60.1, 60.2, 60.3, 60.4, 60.5]]))
        type(self.mock_grid).longitudes = PropertyMock(return_value=np.array([[24.6, 24.7, 24.8, 24.9, 25.0]]))
        type(self.mock_grid).data = PropertyMock(return_value=mock_grid_data)

    @patch('apis.weather.download_stored_query')
    def test_data_is_updated_correctly(self, mock_download_stored_query):
        mock_download_stored_query.return_value = self.datetime_mock

        self.forecastgrid.update_data()

        #check that data contains a grid object
        self.assertEqual(self.forecastgrid.data, self.mock_grid)

        #check coordinates
        np.testing.assert_array_equal(
            self.forecastgrid.coordinates, 
            np.array([((60.1, 24.6), (60.2, 24.7), (60.3, 24.8), (60.4, 24.9), (60.5, 25.0))]))

        #check valid_times
        self.assertEqual(self.forecastgrid.valid_times, self.mock_grid.data.keys())

        #check data levels
        self.assertEqual(self.forecastgrid.data_levels, [0, 2, 10])

    def test_get_coordinates_returns_correct_pairs(self):
        self.forecastgrid.coordinates = np.dstack((self.mock_grid.latitudes, self.mock_grid.longitudes))
        coordinates = self.forecastgrid.get_coordinates()
        for lat, lon in zip(self.mock_grid.latitudes.flatten(), self.mock_grid.longitudes.flatten()):
            assert any(np.allclose([lat, lon], coord) for coord in coordinates)

    def test_forecast_data_is_parsed_correctly(self):
            datasets = [{'Dataset': '2 metre temperature', 'Unit': 'K', 'Data': 280.0},
                        {'Dataset': '2 metre relative humidity', 'Unit': '%', 'Data': 64.013},
                        {'Dataset': '10 metre wind speed', 'Unit': 'm s**-1', 'Data': 1.6543},
                        {'Dataset': 'Mean sea level pressure', 'Unit': 'Pa', 'Data': 101500.2423}]

            expected_parsed_data = {'Air temperature': '6.9 °C',
                                    'Wind': '1.7 m/s', 
                                    'Air pressure': '1015.0 mbar',
                                    'Humidity': '64.0 %'}

            parsed_data = parse_forecast(datasets)

            self.assertEqual(parsed_data, expected_parsed_data)
