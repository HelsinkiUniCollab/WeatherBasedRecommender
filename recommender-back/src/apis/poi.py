from . import times
from ..services.scoring.outdoor_scorer import OutdoorScorer
from ..services.scoring.indoor_scorer import IndoorScorer


class PointOfInterest:
    INDOOR_CATEGORIES = ['Sport halls']
    OUTDOOR_CATEGORIES = ['Open air pools and beaches',
                          'Athletic fields and venues',
                          'Neighbourhood sports facilities and parks']

    def __init__(self, name=None, latitude=None, longitude=None, not_accessible_for=None, categories=None):
        self.sun = times.get_sun_data()
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.not_accessible_for = not_accessible_for
        self.categories = []
        self.categories = categories
        self.weather = {}
        self.categorytype = None
        self.scorers = {
            "Indoor": IndoorScorer(),
            "Outdoor": OutdoorScorer()
        }

    def _extract_weather_data(self, data):
        extracted_weather = {'wind_speed': float(data.get('Wind speed').split(' ')[0]),
                            'precipitation': float(data.get('Precipitation').split(' ')[0]),
                            'clouds': float(data.get('Cloud amount').split(' ')[0]) * 0.01,
                            'temperature': float(data.get('Air temperature').split(' ')[0]),
                            'humidity': float(data.get('Humidity').split(' ')[0]) * 0.01}

        if data.get('Air quality'):
            extracted_weather['air_quality'] = float(data.get('Air quality').split(' ')[0])

        return extracted_weather

    def calculate_score(self, cur_time=None, sunrise=None, sunset=None):
        """
        Calculates a score for the Point of Interest based on weather and time.

        Args:
            cur_time (str, optional): Current time (HH:MM). Defaults to None.
            sunrise (str, optional): Sunrise time (HH:MM). Defaults to None.
            sunset (str, optional): Sunset time (HH:MM). Defaults to None.

        Returns:
            None

        Calculates scores based on weather and time for the POI's categories.
        The calculated scores are added to the POI's weather data.
        """
        if sunrise is None and sunset is None:
            sunrise, sunset = self.sun

        sunrise_time = times.time_from_string(sunrise)
        sunset_time = times.time_from_string(sunset)

        for category in self.categories:
            for timeinterval, data in enumerate(self.weather.values()):
                if cur_time is None:
                    cur_time = times.get_current_time(timeinterval)

                current_time = times.time_from_string(cur_time)
                weather_data = self._extract_weather_data(data)

                scorer = None
                if category in PointOfInterest.OUTDOOR_CATEGORIES:
                    self.categorytype = "Outdoor"
                    scorer = self.scorers["Outdoor"]
                elif category in PointOfInterest.INDOOR_CATEGORIES:
                    self.categorytype = "Indoor"
                    scorer = self.scorers["Indoor"]

                if scorer:
                    if weather_data.get('air_quality'):
                        data['Score'] = scorer.score(
                            weather_data['temperature'], weather_data['wind_speed'],
                            weather_data['humidity'], weather_data['precipitation'],
                            weather_data['clouds'], weather_data['air_quality'], 
                            sunrise_time, sunset_time, current_time
                        )
                    else:
                        data['Score'] = scorer.score(
                            weather_data['temperature'], weather_data['wind_speed'],
                            weather_data['humidity'], weather_data['precipitation'],
                            weather_data['clouds'], 0,
                            sunrise_time, sunset_time, current_time
                        )

    def set_simulated_weather(self, air_temperature, wind_speed, humidity,
                              precipitation, cloud_amount, air_quality):
        """
        Sets simulated weather data for testing score calculations.

        Args:
            air_temperature (float): Simulated air temperature in Celsius.
            wind_speed (float): Simulated wind speed in meters per second.
            humidity (float): Simulated humidity level in percentage.
            precipitation (float): Simulated precipitation amount in millimeters.
            cloud_amount (float): Simulated cloud coverage in percentage.
            air_quality (str): Simulated air quality information.

        This method sets simulated weather data for the Point of Interest (POI) to facilitate testing
        the score calculation functionality.
        """
        self.weather = {
            "Weather": {
                "Air temperature": f"{air_temperature} °C",
                "Wind speed": f"{wind_speed} m/s",
                "Humidity": f"{humidity} %",
                "Precipitation": f"{precipitation} mm",
                "Cloud amount": f"{cloud_amount} %",
                "Air quality": f"{air_quality} AQI",
            }
        }

    def get_json(self):
        """
        Returns a JSON representation of the Point of Interest.

        Returns:
            dict: A dictionary containing the POI's information in JSON format.
        """
        return {'name': self.name, 'weather': self.weather,
                'latitude': self.latitude, 'longitude': self.longitude,
                'category': self.categories[-1], 'catetype': self.categorytype,
                'not_accessible_for': self.not_accessible_for}
