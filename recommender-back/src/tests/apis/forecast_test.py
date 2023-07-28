import unittest
import numpy as np
from datetime import datetime
from unittest.mock import MagicMock, PropertyMock, patch
from src.apis.forecast import Forecast
from src.apis.poi import PointOfInterest
from src.services.forecastdatafetcher import DataFetcher



class ForecastTest(unittest.TestCase):
    def setUp(self):
        self.forecast = Forecast(DataFetcher())
        self.grid_by_datetime = MagicMock()
        self.mock_grid = MagicMock()

        self.grid_by_datetime.data = {datetime(2023, 6, 19, 5, 0): self.mock_grid}

        self.mock_grid_data = PropertyMock(
            return_value={
                datetime(2023, 6, 19, 5, 0): {
                    0: {
                        "Mean sea level pressure": {
                            "units": "Pa",
                            "data": np.array([[10300, 10500, 10600, 10700, 10800]]),
                        }
                    },
                    2: {
                        "2 metre temperature": {
                            "units": "K",
                            "data": np.array([[288.2, 287.3, 283.5, 291.4, 287.7]]),
                        },
                        "2 metre relative humidity": {
                            "units": "%",
                            "data": np.array([[51, 52, 53, 54, 55]]),
                        },
                    },
                    10: {
                        "10 metre U wind component": {
                            "units": "m s**-1",
                            "data": np.array([[7, 9, 3, 2, 5]]),
                        },
                        "10 metre V wind component": {
                            "units": "m s**-1",
                            "data": np.array([[-1, -2, -3, 3, -2]]),
                        },
                        "surface precipitation amount, rain, convective": {
                            "units": "kg m**-2",
                            "data": np.array([[2, 3, 4, 5, 6]]),
                        },
                        "Total Cloud Cover": {
                            "units": "%",
                            "data": np.array([[23, 24, 25, 26, 27]]),
                        },
                    },
                }
            }
        )

        type(self.mock_grid).data = self.mock_grid_data
        type(self.mock_grid).latitudes = PropertyMock(
            return_value=np.array([[60.1, 60.2, 60.3, 60.4, 60.5]])
        )
        type(self.mock_grid).longitudes = PropertyMock(
            return_value=np.array([[24.6, 24.7, 24.8, 24.9, 25.0]])
        )

    @patch("src.services.forecastdatafetcher.DataFetcher.get_forecast_data")
    def test_data_is_updated_correctly(self, mock_download_stored_query):
        mock_download_stored_query.return_value = self.grid_by_datetime

        self.forecast.update_data()

        # Check that data contains a grid object
        self.assertIsInstance(self.forecast.data, type(self.mock_grid))

        # Check that coordinates are now pairs
        np.testing.assert_array_equal(
            self.forecast.coordinates,
            np.array(
                [((60.1, 24.6), (60.2, 24.7), (60.3, 24.8), (60.4, 24.9), (60.5, 25.0))]
            ),
        )

        # Check that valid_times returns datetime dict_keys
        expected_valid_times = self.grid_by_datetime.data.keys()
        self.assertEqual(self.forecast.valid_times, expected_valid_times)

        # Check that all data levels match
        expected_data_levels = []
        for datetime_data in self.mock_grid.data.values():
            data_levels = datetime_data.keys()
            expected_data_levels.extend(data_levels)
        self.assertListEqual(list(self.forecast.data_levels), expected_data_levels)

    @patch("src.services.forecastdatafetcher.DataFetcher.get_forecast_data")
    def test_get_data_returns_data_correctly(self, mock_download_stored_query):
        mock_download_stored_query.return_value = self.grid_by_datetime
        self.forecast.update_data()
        data = self.forecast.get_data()

        expected_data = {
            "2023-06-19 08:00:00": {
                "(60.1, 24.6)": [
                    {"Dataset": "Mean sea level pressure", "Unit": "Pa", "Data": 10300},
                    {"Dataset": "2 metre temperature", "Unit": "K", "Data": 288.2},
                    {"Dataset": "2 metre relative humidity", "Unit": "%", "Data": 51},
                    {
                        "Dataset": "10 metre U wind component",
                        "Unit": "m s**-1",
                        "Data": 7,
                    },
                    {
                        "Dataset": "10 metre V wind component",
                        "Unit": "m s**-1",
                        "Data": -1,
                    },
                    {
                        "Dataset": "surface precipitation amount, rain, convective",
                        "Unit": "kg m**-2",
                        "Data": 2,
                    },
                    {"Dataset": "Total Cloud Cover", "Unit": "%", "Data": 23},
                ],
                "(60.2, 24.7)": [
                    {"Dataset": "Mean sea level pressure", "Unit": "Pa", "Data": 10500},
                    {"Dataset": "2 metre temperature", "Unit": "K", "Data": 287.3},
                    {"Dataset": "2 metre relative humidity", "Unit": "%", "Data": 52},
                    {
                        "Dataset": "10 metre U wind component",
                        "Unit": "m s**-1",
                        "Data": 9,
                    },
                    {
                        "Dataset": "10 metre V wind component",
                        "Unit": "m s**-1",
                        "Data": -2,
                    },
                    {
                        "Dataset": "surface precipitation amount, rain, convective",
                        "Unit": "kg m**-2",
                        "Data": 3,
                    },
                    {"Dataset": "Total Cloud Cover", "Unit": "%", "Data": 24},
                ],
                "(60.3, 24.8)": [
                    {"Dataset": "Mean sea level pressure", "Unit": "Pa", "Data": 10600},
                    {"Dataset": "2 metre temperature", "Unit": "K", "Data": 283.5},
                    {"Dataset": "2 metre relative humidity", "Unit": "%", "Data": 53},
                    {
                        "Dataset": "10 metre U wind component",
                        "Unit": "m s**-1",
                        "Data": 3,
                    },
                    {
                        "Dataset": "10 metre V wind component",
                        "Unit": "m s**-1",
                        "Data": -3,
                    },
                    {
                        "Dataset": "surface precipitation amount, rain, convective",
                        "Unit": "kg m**-2",
                        "Data": 4,
                    },
                    {"Dataset": "Total Cloud Cover", "Unit": "%", "Data": 25},
                ],
                "(60.4, 24.9)": [
                    {"Dataset": "Mean sea level pressure", "Unit": "Pa", "Data": 10700},
                    {"Dataset": "2 metre temperature", "Unit": "K", "Data": 291.4},
                    {"Dataset": "2 metre relative humidity", "Unit": "%", "Data": 54},
                    {
                        "Dataset": "10 metre U wind component",
                        "Unit": "m s**-1",
                        "Data": 2,
                    },
                    {
                        "Dataset": "10 metre V wind component",
                        "Unit": "m s**-1",
                        "Data": 3,
                    },
                    {
                        "Dataset": "surface precipitation amount, rain, convective",
                        "Unit": "kg m**-2",
                        "Data": 5,
                    },
                    {"Dataset": "Total Cloud Cover", "Unit": "%", "Data": 26},
                ],
                "(60.5, 25.0)": [
                    {"Dataset": "Mean sea level pressure", "Unit": "Pa", "Data": 10800},
                    {"Dataset": "2 metre temperature", "Unit": "K", "Data": 287.7},
                    {"Dataset": "2 metre relative humidity", "Unit": "%", "Data": 55},
                    {
                        "Dataset": "10 metre U wind component",
                        "Unit": "m s**-1",
                        "Data": 5,
                    },
                    {
                        "Dataset": "10 metre V wind component",
                        "Unit": "m s**-1",
                        "Data": -2,
                    },
                    {
                        "Dataset": "surface precipitation amount, rain, convective",
                        "Unit": "kg m**-2",
                        "Data": 6,
                    },
                    {"Dataset": "Total Cloud Cover", "Unit": "%", "Data": 27},
                ],
            }
        }

        self.assertEqual(data, expected_data)

    @patch("src.services.forecastdatafetcher.DataFetcher.get_forecast_data")
    def test_closest_poi_coordinate_data_is_fetched_correctly(
        self, mock_download_stored_query
    ):
        mock_download_stored_query.return_value = self.grid_by_datetime
        self.forecast.update_data()

        poi = PointOfInterest()
        poi.latitude = 60.15
        poi.longitude = 24.65

        data = self.forecast.get_closest_poi_coordinates_data([poi])

        expected_data = {
            "2023-06-19 08:00:00": {
                "60.15, 24.65": {
                    "Air temperature": "15.1 °C",
                    "Cloud amount": "23 %",
                    "Humidity": "51 %",
                    "Precipitation": "2 mm",
                    "Wind speed": "7.1 m/s",
                }
            }
        }

        self.assertEqual(data, expected_data)

    def test_get_coordinates_returns_correct_list_of_pairs(self):
        self.forecast.coordinates = np.dstack(
            (self.mock_grid.latitudes, self.mock_grid.longitudes)
        )
        coordinates = self.forecast.get_coordinates()
        for lat, lon in zip(
            self.mock_grid.latitudes.flatten(), self.mock_grid.longitudes.flatten()
        ):
            assert any(np.allclose([lat, lon], coord) for coord in coordinates)

    def test_forecast_data_is_parsed_correctly(self):
        data = [
            {"Dataset": "2 metre temperature", "Unit": "K", "Data": 280.0},
            {"Dataset": "2 metre relative humidity", "Unit": "%", "Data": 64.013},
            {"Dataset": "10 metre U wind component", "Unit": "m s**-1", "Data": 1.223},
            {"Dataset": "10 metre V wind component", "Unit": "m s**-1", "Data": -4.7},
            {
                "Dataset": "surface precipitation amount, rain, convective",
                "Unit": "kg m**-2",
                "Data": 0.0231,
            },
            {"Dataset": "Total Cloud Cover", "Unit": "%", "Data": 23.2},
        ]

        expected_parsed_data = {
            "Air temperature": "6.9 °C",
            "Humidity": "64.0 %",
            "Wind speed": "4.9 m/s",
            "Precipitation": "0.0 mm",
            "Cloud amount": "23.2 %",
        }

        parsed_data = self.forecast.parse_forecast(data)

        self.assertEqual(parsed_data, expected_parsed_data)
