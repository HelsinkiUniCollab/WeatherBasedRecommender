import unittest
from unittest.mock import patch
from apis.helpers import Recommender
from apis.time_data import get_sun_data , get_current_time

class RecommenderTests(unittest.TestCase):
    def setUp(self):
        self.sun = get_sun_data()
        self.sunrise = self.sun[0]
        self.sunset = self.sun[1]
        print(self.sunrise)
        print(self.sunset)
        self.weather = {
            "0": {
                "Air temperature": "25",
                "Humidity": "60"
            },
            "1": {
                "Air temperature": "30",
                "Humidity": "80"
            },
            "2": {
                "Air temperature": "22",
                "Humidity": "50"
            }
        }
        
    @patch('apis.time_data.get_current_time', return_value='12:00')
    def test_calculate_score_with_invalid_humidity(self, mocked_time):
        self.weather["0"]["Humidity"] = "invalid"
        recommender = Recommender(weather=self.weather)
        expected_scores = {
            "0": -float('inf'),
            "1": 0.5,
            "2": 1.0
        }

        for data_key, expected_score in expected_scores.items():
            self.assertEqual(recommender.weather[data_key]['score'], expected_score)

    @patch('apis.time_data.get_current_time', return_value='12:00')
    def test_calculate_score_with_invalid_temperature(self, mocked_time):
        self.weather["0"]["Air temperature"] = "invalid"
        recommender = Recommender(weather=self.weather)
        expected_scores = {
            "0": -float('inf'),
            "1": 0.5,
            "2": 1.0
        }

        for data_key, expected_score in expected_scores.items():
            if get_current_time(int(data_key)) > self.sunset and get_current_time(int(data_key)) < self.sunrise:
                self.assertEqual(recommender[data_key]['score'], 0)
            self.assertEqual(recommender.weather[data_key]['score'], expected_score)

    @patch('apis.time_data.get_current_time', return_value='12:00')
    def test_calculate_score_within_suitable_time_range(self, mocked_time):
        recommender = Recommender(weather=self.weather)
        expected_scores = {
            "0": 1.0,
            "1": 0.5,
            "2": 1.0
        }

        for data_key, expected_score in expected_scores.items():
            self.assertEqual(recommender.weather[data_key]['score'], expected_score)

if __name__ == '__main__':
    unittest.main()
