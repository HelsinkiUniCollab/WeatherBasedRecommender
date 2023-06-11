from apis import time_data

class PointOfInterest:
    def __init__(self, time, **kwargs):
        self.sun = time_data.get_sun_data()
        self.time = time
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
        if self.time == None:
            self.time = time_data.get_current_time()
        sunrise = self.sun[0]
        sunset = self.sun[1]
        temperature_str = self.weather.get('Air temperature')
        humidity_str = self.weather.get('Humidity')

        try:
            temperature = float(temperature_str.split()[0])
            humidity = float(humidity_str.split('%')[0])
        except (AttributeError, ValueError):
            return -float('inf')

        suitable_temperature_range = (25, 35)
        suitable_humidity_range = (40, 60)

        if self.time >= sunrise and self.time <= sunset:
            if suitable_temperature_range[0] <= temperature <= suitable_temperature_range[1]:
                temperature_score = 1.0
            else:
                temperature_score = 0.0

            if suitable_humidity_range[0] <= humidity <= suitable_humidity_range[1]:
                humidity_score = 1.0
            else:
                humidity_score = 0.0

            score = (temperature_score + humidity_score) / 2
            return score
        else:
            score = 0
            return score

