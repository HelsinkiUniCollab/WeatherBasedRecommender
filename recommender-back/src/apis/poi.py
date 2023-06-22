from apis import times


class PointOfInterest:
    def __init__(self, name=None, longitude=None, latitude=None, not_accessible_for=None, categories=None):
        self.sun = times.get_sun_data()
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.not_accessible_for = not_accessible_for
        self.categories = categories
        self.weather = {}

    def calculate_score(self):
        '''
        Calculates a score for the POI based on weather data and time constraints..
        '''

        sunrise = self.sun[0]
        sunset = self.sun[1]
        suitable_temperature_range = (20, 30)
        suitable_humidity_range = (40, 60)
        for timeinterval, data in enumerate(self.weather.values()):
            time = times.get_current_time(timeinterval)
            temperature_str = data.get('Air temperature')
            humidity_str = data.get('Humidity')
            try:
                temperature = float(temperature_str.split('°C')[0])
                humidity = float(humidity_str.split('%')[0])
            except (TypeError, ValueError):
                data['Score'] = -float('inf')
                continue
            except (AttributeError):
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
                data['Score'] = score
            else:
                data['Score'] = 0.0

    def get_json(self):
        '''
        Returns a JSON representation of the POI.

        Returns:
            dict: JSON representation of the POI.
        '''
        return {'name': self.name, 'weather': self.weather,
                'latitude': self.latitude, 'longitude': self.longitude}
