from unittest import TestCase, mock
import requests
from src.services.api_fetcher import InternalApiService

class TestInternalApiService(TestCase):

    @mock.patch("requests.get")
    def test_fetch_forecast_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "test_data"}

        data = InternalApiService.fetch_forecast()
        self.assertEqual(data, {"data": "test_data"})

    @mock.patch('requests.get')
    def test_fetch_forecast_error(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.HTTPError()
        mock_get.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            InternalApiService.fetch_forecast()

    @mock.patch("requests.get")
    def test_fetch_aqi_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "test_data"}

        data = InternalApiService.fetch_aqi()
        self.assertEqual(data, {"data": "test_data"})

    @mock.patch('requests.get')
    def test_fetch_aqi_error(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.HTTPError()
        mock_get.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            InternalApiService.fetch_aqi()