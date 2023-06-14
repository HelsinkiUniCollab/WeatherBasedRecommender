import unittest
from unittest.mock import patch
from apis import time_data
from apis.helpers import Recommender

class RecommenderTests(unittest.TestCase):
    def setUp(self):
        self.time = "12:00"
        self.weather = {
            "data1": {
                "Air temperature": "25",
                "Humidity": "60"
            },
            "data2": {
                "Air temperature": "30",
                "Humidity": "80"
            },
            "data3": {
                "Air temperature": "22",
                "Humidity": "50"
            }
        }
        
    def test_calculate_score_with_invalid_humidity(self):
        self.weather["data1"]["Humidity"] = "invalid"
        recommender = Recommender(self.time, weather=self.weather)
        expected_scores = {
            "data1": -float('inf'),
            "data2": 0.5,
            "data3": 1.0
        }
        scores = recommender.calculate_score()
        for data_key, expected_score in expected_scores.items():
            self.assertEqual(scores[data_key]['score'], expected_score)

    def test_calculate_score_with_invalid_temperature(self):
        self.weather["data1"]["Air temperature"] = "invalid"
        recommender = Recommender(self.time, weather=self.weather)
        expected_scores = {
            "data1": -float('inf'),
            "data2": 0.5,
            "data3": 1.0
        }
        scores = recommender.calculate_score()
        for data_key, expected_score in expected_scores.items():
            self.assertEqual(scores[data_key]['score'], expected_score)

    def test_calculate_score_within_suitable_time_range(self):
        recommender = Recommender(self.time, weather=self.weather)
        expected_scores = {
            "data1": 1.0,
            "data2": 0.5,
            "data3": 1.0
        }
        scores = recommender.calculate_score()
        for data_key, expected_score in expected_scores.items():
            self.assertEqual(scores[data_key]['score'], expected_score)

if __name__ == '__main__':
    unittest.main()
