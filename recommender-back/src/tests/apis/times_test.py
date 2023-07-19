import unittest
from unittest.mock import patch
from datetime import datetime
from src.apis.times import get_current_time


class TimesTest(unittest.TestCase):
    @patch('src.apis.times.dt.datetime')
    def test_current_time_is_returned_correctly_when_plus_is_not_set(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 7, 19, 15, 30)

        current_time = get_current_time()
        expected_time = '15:30'

        self.assertEqual(current_time, expected_time)

    @patch('src.apis.times.dt.datetime')
    def test_current_time_is_returned_correctly_when_plus_is_set(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 7, 19, 15, 30)

        current_time = get_current_time(plus=3)
        expected_time = '18:30'

        self.assertEqual(current_time, expected_time)
