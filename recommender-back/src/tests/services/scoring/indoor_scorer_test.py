import unittest
from src.services.scoring.indoor_scorer import IndoorScorer

class TestIndoorScorer(unittest.TestCase):
    def setUp(self):
        self.scorer = IndoorScorer()

    def test_perfect_conditions(self):
        temperature = 22.5
        wind_speed = 2.0
        humidity = 0.5
        precipitation = 0.0
        clouds = 0.1
        air_quality = 5.0
        sunrise_time = "06:00"
        sunset_time = "18:00"
        current_time = "12:00"
        expected_score = 0.09
        score = self.scorer.score(temperature, wind_speed, humidity, precipitation, clouds, air_quality, sunrise_time, sunset_time, current_time)
        self.assertEqual(score, expected_score)

    def test_worst_conditions(self):
        temperature = 5.0
        wind_speed = 20.0
        humidity = 0.95
        precipitation = 10.0
        clouds = 1.0
        air_quality = 1.0
        sunrise_time = "06:00"
        sunset_time = "18:00"
        current_time = "12:00"
        expected_score = 0.94
        score = self.scorer.score(temperature, wind_speed, humidity, precipitation, clouds, air_quality, sunrise_time, sunset_time, current_time)
        self.assertEqual(score, expected_score)

    def test_daytime_weight(self):
        temperature = 22.5
        wind_speed = 2.0
        humidity = 0.5
        precipitation = 0.0
        clouds = 0.1
        air_quality = 1.0
        sunrise_time = "06:00"
        sunset_time = "18:00"
        current_time = "21:00"
        expected_score = 0.07
        score = self.scorer.score(temperature, wind_speed, humidity, precipitation, clouds, air_quality, sunrise_time, sunset_time, current_time)
        self.assertEqual(score, expected_score)
