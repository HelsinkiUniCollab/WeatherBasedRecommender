import unittest
from unittest.mock import patch
from src.apis.poi import PointOfInterest

class TestPointOfInterest(unittest.TestCase):
    def setUp(self):
        self.poi = PointOfInterest()

    def test_calculate_score_chooses_indoor(self):
        with patch('src.apis.times.get_current_time') as mock_get_current_time:
            weather = {'20:00':{'Wind speed':'2.0 m/s','Precipitation':'200 mm','Cloud amount':'0.6 %',
                    'Air temperature':'22.0 *C','Humidity':'0.45 %', 'Air quality': '5.0 AQI'}}

            sun = ('06:00','18:00')
            mock_get_current_time.return_value = '20:00'
            categories = ['Sport halls']

            test_poi = PointOfInterest(categories=categories)
            test_poi.weather = weather
            test_poi.sun = sun

            expected_score = 0.74

            test_poi.calculate_score()
            score = test_poi.weather['20:00']['Score']

            self.assertAlmostEqual(score, expected_score, places=6)

    def test_calculate_score_chooses_outdoor(self):
        with patch('src.apis.times.get_current_time') as mock_get_current_time:
            weather = {'12:00':{'Wind speed':'5.0 m/s','Precipitation':'20 mm','Cloud amount':'0.6 %',
                    'Air temperature':'23.0 *C','Humidity':'0.5 %', 'Air quality': '1.0 AQI'}}

            sun = ('06:00','18:00')
            mock_get_current_time.return_value = '12:00'
            categories = ['Open air pools and beaches']

            test_poi = PointOfInterest(categories=categories)
            test_poi.weather = weather
            test_poi.sun = sun

            expected_score = 0.59

            test_poi.calculate_score()
            score = test_poi.weather['12:00']['Score']

            self.assertAlmostEqual(score, expected_score, places=6)
      
    def test_json_in_correct_form(self):
        weather = {'12:00':{'Wind speed':'5.0 m/s','Precipitation':'20 mm','Cloud amount':'0.6 %',
                'Air temperature':'23.0 *C','Humidity':'0.5 %'}}

        sun = ('06:00','18:00')
        categories = ['Open air pools and beaches']
        not_accessible_for = ['wheelchair']

        test_poi = PointOfInterest(name= 'Test POI', latitude=21, longitude=61, categories=categories)
        test_poi.weather = weather
        test_poi.sun = sun
        test_poi.not_accessible_for = not_accessible_for
        expected_json = {
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
            "not_accessible_for": not_accessible_for
        }

        test_json = test_poi.get_json()
        
        self.assertEqual(test_json, expected_json)


    def test_extract_weather_data_with_dash(self):
        test_data = {
            'Wind speed': '5.0 m/s',
            'Precipitation': '20 mm',
            'Cloud amount': '0.6 %',
            'Air temperature': '-',
            'Humidity': '0.5 %',
            'Air quality': '1.0 AQI'
        }

        expected_data = {
            'wind_speed': 5.0,
            'precipitation': 20.0,
            'clouds': 0.006,
            'temperature': 0.0,
            'humidity': 0.005,
            'air_quality': 1.0
        }

        extracted_data = self.poi._extract_weather_data(test_data)

        self.assertEqual(extracted_data, expected_data)

if __name__ == '__main__':
    unittest.main()


