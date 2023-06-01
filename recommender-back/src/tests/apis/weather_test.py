from unittest import mock
import unittest
from app import app


class WeatherTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_weather_error(self):
        with mock.patch('apis.weather._current_query_handler', side_effect=Exception('Test exception')):
            error_response = self.client.get('/api/weather')
            error_data = error_response.get_json()
            self.assertEqual(error_response.status_code, 500)
            self.assertEqual(error_data['message'], 'An error occurred')
            self.assertEqual(error_data['status'], 500)
            self.assertIn('error', error_data)


if __name__ == '__main__':
    unittest.main()
