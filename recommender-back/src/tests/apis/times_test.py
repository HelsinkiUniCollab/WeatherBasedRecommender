import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from datetime import datetime as dt 
from src.apis.times import get_current_time


class TimesTest(unittest.TestCase):
    @patch('src.apis.times.datetime')
    def test_current_time_is_returned_correctly_when_plus_is_not_set(self, mock_datetime):
        # Set the mocked return value for datetime.now()
        mock_datetime.now.return_value = datetime(2023, 7, 19, 10, 30)

        # Call the function being tested
        current_time = get_current_time()

        # Assert the result
        expected_time = '10:30'
        self.assertEqual(current_time, expected_time)
