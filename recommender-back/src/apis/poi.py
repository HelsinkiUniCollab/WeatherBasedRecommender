import math as math
from apis import times


class PointOfInterest:
    def __init__(self, name=None, latitude=None, longitude=None, not_accessible_for=None, categories=None):
        self.sun = times.get_sun_data()
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.not_accessible_for = not_accessible_for
        self.categories = categories
        self.weather = {}

    def calculate_score(self):
        '''
        Chooses witch algorithm to use in scoring
        Must be manually handled to adjust when adding new pois
        '''

        # static for whole POI
        indoor_categories = ['Sport halls']
        outdoor_categories = ['Open air pools and beaches','Athletic fields and venues', 'Neighbourhood sports facilities and parks']
        sunrise = self.sun[0]
        sunset = self.sun[1]

        for category in self.categories:

            if category in outdoor_categories:
                for timeinterval, data in enumerate(self.weather.values()):
                    cur_time = times.get_current_time(timeinterval)
                    wind_speed = float(data.get('Wind speed').split(' ')[0])
                    precipitation = float(data.get('Precipitation').split(' ')[0])
                    clouds = float(data.get('Cloud amount').split(' ')[0]) * 0.01
                    temperature = float(data.get('Air temperature').split('°C')[0])
                    humidity = float(data.get('Humidity').split('%')[0]) * 0.01
                    data['Score'] = self._outdoor_score(temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time)
                return
            
            if category in indoor_categories:
                for timeinterval, data in enumerate(self.weather.values()):
                    cur_time = times.get_current_time(timeinterval)
                    wind_speed = float(data.get('Wind speed').split(' ')[0])
                    precipitation = float(data.get('Precipitation').split(' ')[0])
                    clouds = float(data.get('Cloud amount').split(' ')[0]) * 0.01
                    temperature = float(data.get('Air temperature').split('°C')[0])
                    humidity = float(data.get('Humidity').split('%')[0]) * 0.01
                    data['Score'] = self._indoor_score(temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time)
                return
            
    def _outdoor_score(self, temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time):
        # Weights
        precipitation_weight = 0.35
        temperature_weight = 0.3
        day_time_weight = 0.2
        clouds_weight = 0.04
        wind_speed_weight = 0.04
        humidity_weight = 0.02


        # Scoring
        score = precipitation_weight * math.exp(-precipitation)
        temperature_comp = 0
        if 20 <= temperature <= 25:
            temperature_comp = 1
        elif 20 > temperature:
            temperature_comp = math.exp(-0.1 * (20 - temperature))
        elif temperature > 25:
            temperature_comp = math.exp(0.1 * (25 - temperature))
        score += temperature_weight * temperature_comp
        if sunrise <= cur_time <= sunset:
            score += day_time_weight
        #score += air_weight * math.exp(0.5 * 1- air)
        score += clouds_weight * math.exp(-clouds)
        score += wind_speed_weight * math.exp(-wind_speed)
        if 0.4 <= humidity <= 0.55:
            score += humidity_weight
        return score
    
    def _indoor_score(self, temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time):
        # Weights
        precipitation_weight = 0.7
        temperature_weight = 0.1
        day_time_weight = 0.06
        clouds_weight = 0.04
        wind_speed_weight = 0.03
        humidity_weight = 0.02


        # Scoring
        score = precipitation_weight * (1 - math.exp(-10 * precipitation))
        temperature_comp = 0
        if 20 <= temperature <= 25:
            temperature_comp = 0
        elif 20 > temperature:
            temperature_comp = 1 - math.exp(-0.04 * (20 - temperature))
        elif temperature > 25:
            temperature_comp = 1 - math.exp(0.2 * (25 - temperature))
        score += temperature_weight * temperature_comp
        if sunrise > cur_time or cur_time > sunset:
            score += day_time_weight
        #score += air_weight * (1 - math.exp(0.5 * 1- air))
        score += clouds_weight * (1 - math.exp(-3 * clouds))
        score += wind_speed_weight * (1 - math.exp(-0.3 * wind_speed))
        if 0.4 > humidity or humidity > 0.55:
            score += humidity_weight
        return score



    def get_json(self):
        '''
        Returns a JSON representation of the POI.
        '''
        return {'name': self.name, 'weather': self.weather,
                'latitude': self.latitude, 'longitude': self.longitude}
    
