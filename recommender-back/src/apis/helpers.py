import datetime as dt
from apis import time_data

class Recommender:
    def __init__(self, time, **kwargs):
        self.sun = time_data.get_sun_data()
        self.id = kwargs.get('id')
        self.contract_type = kwargs.get('contract_type')
        self.name = kwargs.get('name')
        self.street_address = kwargs.get('street_address')
        self.municipality = kwargs.get('municipality')
        self.service_nodes = kwargs.get('service_nodes')
        self.location = kwargs.get('location')
        self.geometry = kwargs.get('geometry')
        self.accessibility_shortcoming_count = kwargs.get('accessibility_shortcoming_count')
        self.object_type = kwargs.get('object_type')
        self.weather = kwargs.get('weather')
        self.score = self.calculate_score()

    def calculate_score(self):

        sunrise = self.sun[0]
        sunset = self.sun[1]
        suitable_temperature_range = (20, 30)
        suitable_humidity_range = (40, 60)
        print(sunrise)
        print(sunset)
        for timeinterval, data in enumerate(self.weather.values()):
            time = time_data.get_current_time(timeinterval)
            temperature_str = data.get('Air temperature')
            humidity_str = data.get('Humidity')
            try:
                temperature = float(temperature_str.split('°C')[0])
                humidity = float(humidity_str.split('%')[0])
            except (TypeError, ValueError):
                data['score'] = -float('inf')
                continue
               
            if time >= sunrise and time <= sunset:
                if suitable_temperature_range[0] <= temperature <= suitable_temperature_range[1]:
                    temperature_score = 1.0
                else:
                    temperature_score = 0.0

                if suitable_humidity_range[0] <= humidity <= suitable_humidity_range[1]:
                    humidity_score = 1.0
                else:
                    humidity_score = 0.0

                score = (temperature_score + humidity_score) / 2
                data['score'] = score
            else:
                data['score'] = 0.0

        return self.weather
    