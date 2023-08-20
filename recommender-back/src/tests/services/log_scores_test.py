import json
import unittest 
from src.services.log_scores import save_score_history

class LogScoresTestCase(unittest.TestCase):
    def test_save_score_history(self):
        data = [{
            "name": 'Test POI',
            "weather": {
                "12:00": {
                    "Wind speed": "5.0 m/s",
                    "Precipitation": "20 mm",
                    "Cloud amount": "0.6 %",
                    "Air temperature": "23.0 *C",
                    "Humidity": "0.5 %"
                    }
                },
            "latitude": 21,
            "longitude": 61,
            "category": "Open air pools and beaches",
            "catetype": None,
            "not_accessible_for": {} 
        },
        {
            "name": 'Test POI2"',
            "weather": {
                "12:00": {
                    "Wind speed": "5.0 m/s",
                    "Precipitation": "20 mm",
                    "Cloud amount": "0.6 %",
                    "Air temperature": "23.0 *C",
                    "Humidity": "0.5 %"
                    }
                },
            "latitude": 21,
            "longitude": 61,
            "category": "Open air pools and beaches",
            "catetype": None,
            "not_accessible_for": {} 
        }]
        response = save_score_history(json.dumps(data), 'scorehistory_test')
        self.assertEqual(response['status'], 200) 