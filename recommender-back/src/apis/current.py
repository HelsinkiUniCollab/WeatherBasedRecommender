import copy
from .poi import PointOfInterest
from ..services.forecastdatafetcher import DataFetcher
from ..config import Config


class Current:
    def __init__(self, fetcher: DataFetcher):
        self.fetcher = fetcher
        self.weather = None
        self.aqi = None
        self.get_current_weather()
        self.get_current_air_quality()

    def get_current_weather(self):
        '''
        Retrieves the current weather data for various stations.

        Returns:
            dict: A dictionary containing the current weather data for each station.
        '''

        obs = self.fetcher.get_current_weather_data(Config.BBOX, True)
        data = {}
        for station, metadata in obs.location_metadata.items():
            weatherdata = {
                'Air temperature': str(obs.data[station]['t2m']['values'][-1]) + ' °C',
                'Wind speed': str(obs.data[station]['ws_10min']['values'][-1]) + ' m/s',
                'Humidity': str(obs.data[station]['rh']['values'][-1]) + ' %',
                'Precipitation': str(obs.data[station]['ri_10min']['values'][-1])
                + ' mm',
                'Cloud amount': str(obs.data[station]['n_man']['values'][-1]) + ' %',
            }
            for value in list(weatherdata):
                if 'nan' in str(weatherdata[value]):
                    weatherdata.pop(value)
            if weatherdata:
                weatherdata['Latitude'] = metadata['latitude']
                weatherdata['Longitude'] = metadata['longitude']
                data[station] = weatherdata
        self.weather = data

    def get_current_air_quality(self):
        '''
        Retrieves the current AQI data for various stations.

        Returns:
            dict: A dictionary containing the current weather data for each station.
        '''
        obs = self.fetcher.get_current_air_quality_data(Config.BBOX, True)
        data = {}
        for station, metadata in obs.location_metadata.items():
            aqi = {
                'Air quality': str(obs.data[station]['AQINDEX_PT1H_avg']['values'][-1]) + ' AQI'
            }
            if 'nan' in str(aqi['Air quality']):
                continue
            aqi['Latitude'] = metadata['latitude']
            aqi['Longitude'] = metadata['longitude']
            data[station] = aqi
        self.aqi = data

    def find_nearest_stations_weather_data(self, poi: PointOfInterest):
        '''
        Finds the nearest weather station to a given point of interest (POI) and adds its weather data to the POI,
        also adds the Air Quality Index data.

        Args:
            poi (PointOfInterest): The POI for which weather data needs to be added.

        Returns:
            PointOfInterest: The modified POI with weather information.

        '''
        lat = poi.latitude
        lon = poi.longitude
        weather = copy.deepcopy(self.weather)
        missing_fields = [
            'Air temperature',
            'Wind speed',
            'Precipitation',
            'Cloud amount',
            'Humidity',
        ]
        returned = {}
        aqi = copy.deepcopy(self.aqi)
        while True:
            smallest, nearest = float('inf'), ''
            for station in weather:
                dist = abs(weather[station]['Latitude'] - lat) + abs(
                    weather[station]['Longitude'] - lon
                )
                if dist < smallest:
                    smallest, nearest = dist, station
            for key, value in weather[nearest].items():
                if key not in ['Latitude', 'Longitude']:
                    returned.setdefault(key, value)
                    if key in missing_fields:
                        missing_fields.remove(key)
            if not missing_fields or not weather:
                smallest, nearest = float('inf'), ''
                if len(aqi) > 0:
                    for station in aqi:
                        dist = abs(aqi[station]['Latitude'] - lat)\
                            + abs(aqi[station]['Longitude'] - lon)
                        if dist < smallest:
                            smallest, nearest = dist, station
                    returned.setdefault(
                        'Air quality', aqi[nearest]['Air quality'])
                break
            del weather[nearest]
        poi.weather['Current'] = returned
        return poi
