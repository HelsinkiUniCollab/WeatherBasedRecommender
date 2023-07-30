import math
from . import times


class PointOfInterest:
    def __init__(self, name=None, latitude=None, longitude=None, not_accessible_for=None, categories=None):
        self.sun = times.get_sun_data()
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.not_accessible_for = not_accessible_for
        self.categories = categories
        self.weather = {}
        self.categorytype = None

    def calculate_score(self):
        '''
        Chooses which algorithm to use in scoring.
        Must be manually handled to adjust when adding new points of interest.
        '''
        indoor_categories = ['Sport halls']
        outdoor_categories = ['Open air pools and beaches',
                              'Athletic fields and venues', 'Neighbourhood sports facilities and parks']
        sunrise = self.sun[0]
        sunset = self.sun[1]

        for category in self.categories:
            for timeinterval, data in enumerate(self.weather.values()):
                cur_time = times.get_current_time(timeinterval)
                wind_speed = float(data.get('Wind speed').split(' ')[0])
                precipitation = float(data.get('Precipitation').split(' ')[0])
                clouds = float(data.get('Cloud amount').split(' ')[0]) * 0.01
                temperature = float(data.get('Air temperature').split(' ')[0])
                humidity = float(data.get('Humidity').split(' ')[0]) * 0.01

                if category in outdoor_categories:
                    self.categorytype = "Outdoor"
                    data['Score'] = self._outdoor_score(temperature, wind_speed, humidity,
                                                        precipitation, clouds, sunrise, sunset, cur_time)
                elif category in indoor_categories:
                    self.categorytype = "Indoor"
                    data['Score'] = self._indoor_score(temperature, wind_speed, humidity,
                                                       precipitation, clouds, sunrise, sunset, cur_time)

    def _outdoor_score(self, temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time):
        '''
        Calculates the score for an outdoor point of interest based on weather conditions.

        Returns:
            float: The calculated score for the outdoor point of interest.
        '''
        precipitation_weight = 0.35
        temperature_weight = 0.3
        clouds_weight = 0.04
        wind_speed_weight = 0.04
        # Scoring
        score = precipitation_weight * math.exp(-precipitation)
        temperature_comp = 0
        if 20 <= temperature <= 25:
            temperature_comp = 1
        elif temperature < 20:
            temperature_comp = math.exp(-0.1 * (20 - temperature))
        else:
            temperature_comp = math.exp(0.1 * (25 - temperature))
        score += temperature_weight * temperature_comp
        if sunrise <= cur_time <= sunset:
            day_time_weight = 0.2
            score += day_time_weight
        # score += air_weight * math.exp(0.5 * 1- air)
        score += clouds_weight * math.exp(-clouds)
        score += wind_speed_weight * math.exp(-wind_speed)
        if 0.4 <= humidity <= 0.55:
            humidity_weight = 0.02

            score += humidity_weight
        return round(score, 2)

    def _indoor_score(self, temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time):
        # Weights
        precipitation_weight = 0.7
        temperature_weight = 0.1
        clouds_weight = 0.04
        wind_speed_weight = 0.03
        # Scoring
        score = precipitation_weight * (1 - math.exp(-10 * precipitation))
        temperature_comp = 0
        if 20 <= temperature <= 25:
            temperature_comp = 0
        elif temperature < 20:
            temperature_comp = 1 - math.exp(-0.04 * (20 - temperature))
        else:
            temperature_comp = 1 - math.exp(0.2 * (25 - temperature))
        score += temperature_weight * temperature_comp
        if sunrise > cur_time or cur_time > sunset:
            day_time_weight = 0.06
            score += day_time_weight
        # score += air_weight * (1 - math.exp(0.5 * 1- air))
        score += clouds_weight * (1 - math.exp(-3 * clouds))
        score += wind_speed_weight * (1 - math.exp(-0.3 * wind_speed))
        if humidity < 0.4 or humidity > 0.55:
            humidity_weight = 0.02

            score += humidity_weight
        return round(score, 2)

    def set_simulated_weather(self, air_temperature, wind_speed, humidity,
                              precipitation, cloud_amount, air_quality):
        '''
        Sets simulated weather data to test score calculations.
        '''
        self.weather = {"Weather": {
            "Air temperature": air_temperature,
            "Wind speed": wind_speed,
            "Humidity": humidity,
            "Precipitation": precipitation,
            "Cloud amount": cloud_amount,
            "Air quality": air_quality
        }}

    def get_json(self):
        '''
        Returns a JSON representation of the POI.
        '''
        return {'name': self.name, 'weather': self.weather,
                'latitude': self.latitude, 'longitude': self.longitude,
                'category': self.categories[-1], 'catetype': self.categorytype}
