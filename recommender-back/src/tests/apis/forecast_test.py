import unittest
import numpy as np
from unittest.mock import patch
from apis.weather import ForecastGrid, parse_forecast
from fmiopendata import grid

class ForecastTest(unittest.TestCase):
    def setUp(self):
        self.forecastgrid = ForecastGrid()

        self.mock_coords = np.array([
            [[60.1, 24.6]],
            [[60.2, 24.7]],
            [[60.3, 24.8]],
            [[60.4, 24.9]],
            [[60.5, 25.0]],
            ])

        self.forecastgrid.coordinates = self.mock_coords

    def test_forecast_data_is_parsed_correctly(self):
        forecast_data =  [{'Dataset': '2 metre temperature', 'Unit': 'K', 'Data': 280.0},
                          {'Dataset': '2 metre relative humidity', 'Unit': '%', 'Data': 64.013},
                          {'Dataset': '10 metre wind speed', 'Unit': 'm s**-1', 'Data': 1.6543},
                          {'Dataset': 'Mean sea level pressure', 'Unit': 'Pa', 'Data': 101500.2423}]

        expected_data = {'Air temperature': '6.9 °C',
                         'Wind': '1.7 m/s', 
                         'Air pressure': '1015.0 mbar',
                         'Humidity': '64.0 %'}
  
        parsed_data = parse_forecast(forecast_data)

        self.assertEqual(parsed_data, expected_data)

    def test_get_coordinates_returns_correct_pairs(self):
        self.latitudes = self.mock_coords[:, 0, 0].flatten()
        self.longitudes = self.mock_coords[:, 0, 1].flatten()

        coordinates = self.forecastgrid.get_coordinates()
        for lat, lon in zip(self.latitudes, self.longitudes):
            assert any(np.allclose([lat, lon], coord) for coord in coordinates)
