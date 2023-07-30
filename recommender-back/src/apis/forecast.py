import math
import numpy as np
from .times import utc_to_finnish, get_forecast_times
from fmiopendata.wfs import download_stored_query

class Forecast:
    def __init__(self):
        self.data = None
        self.valid_times = None
        self.data_levels = None
        self.coordinates = None

    def update_data(self):
        '''
        Updates the forecast data by fetching the latest data from the API.
        '''
        current, start, end = get_forecast_times()
        bbox = '24.5,60,25.5,60.5'
        timestep = 60
        parameters = 'Temperature,Humidity,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover'
        args = [f'starttime={start}',
                                                    f'endtime={end}',
                                                    f'bbox={bbox}',
                                                    f'timestep={timestep}',
                                                    f'parameters={parameters}']
        print(f'Query for the new Grid object at time: {current} UTC')
        forecast_data = download_stored_query('fmi::forecast::harmonie::surface::grid',
                                            args=[f'starttime={start}',
                                                    f'endtime={end}',
                                                    f'bbox={bbox}',
                                                    f'timestep={timestep}',
                                                    f'parameters={parameters}']
                                                    )
        latest_forecast = max(forecast_data.data.keys())
        self.data = forecast_data.data[latest_forecast]
        self.data.parse(delete=True)
        self.valid_times = self.data.data.keys()
        earliest_step = min(self.valid_times)
        self.data_levels = self.data.data[earliest_step].keys()
        self.coordinates = np.dstack(
            (self.data.latitudes, self.data.longitudes))

    def get_data(self):
        '''
        Gets all the forecast data from the grid.

        Returns:
            dict: A dictionary containing all the forecast data.
        '''
        data = {}
        for date_time in self.valid_times:
            local_time = utc_to_finnish(date_time)
            time_str = local_time.strftime('%Y-%m-%d %H:%M:%S')
            coordinates_data = {}
            for level in self.data_levels:
                datasets = self.data.data[date_time][level]
                for dataset_name, dataset in datasets.items():
                    unit = dataset['units']
                    data_array = dataset['data']
                    for (lat_index, lon_index), data_value in np.ndenumerate(data_array):
                        latitude = self.coordinates[lat_index, lon_index, 0]
                        longitude = self.coordinates[lat_index, lon_index, 1]
                        key = str((latitude, longitude))
                        if key not in coordinates_data:
                            coordinates_data[key] = []
                        coordinates_data[key].append(
                            {'Dataset': dataset_name, 'Unit': unit, 'Data': data_value})
            data[time_str] = coordinates_data
        return data

    def get_coordinates(self):
        '''
        Returns all available coordinates within the bounding box area.

        Returns:
            list: List of coordinate pairs.
        '''
        unique_coords = set()

        flattened_coords = [tuple(coord) for sublist in self.coordinates for coord in sublist]

        for coord in flattened_coords:
            unique_coords.add(coord)

        return list(unique_coords)

    def get_closest_poi_coordinates_data(self, pois, aqi_data, aqi_coords):
        '''
        Finds the nearest coordinates forecast data for all of the POI's coordinates.

        Args:
            pois (list): List of POI objects.

        Returns:
            dict: A dictionary containing the nearest coordinates forecast data for each hour.
        '''
        data = self.get_data()
        coordinates = self.get_coordinates()
        returned_data = {hour: {} for hour in data}
        closest_coordinates_fore = {}
        closest_coodinates_aqi = {}

        for poi in pois:
            smallest = float('inf')
            nearest = []
            lat = poi.latitude
            lon = poi.longitude
            for coordinate in coordinates:
                dist = abs(coordinate[0] - lat) + abs(coordinate[1] - lon)
                if dist < smallest:
                    smallest = dist
                    nearest = [coordinate[0], coordinate[1]]
            closest_coordinates_fore[(lat, lon)] = nearest

        for poi in pois:
            smallest = float('inf')
            nearest = []
            lat = poi.latitude
            lon = poi.longitude
            for coordinate in aqi_coords:
                dist = abs(coordinate[0] - lat) + abs(coordinate[1] - lon)
                if dist < smallest:
                    smallest = dist
                    nearest = [coordinate[0], coordinate[1]]
            closest_coodinates_aqi[(lat, lon)] = nearest

        for hour, hour_data in data.items():
            print('hour fore:', hour)
            for poi_coord, nearest in closest_coordinates_fore.items():
                nearest_str = f'({nearest[0]}, {nearest[1]})'
                if nearest_str in hour_data:
                    forecast = hour_data[nearest_str]
                    returned_data[hour][f'{poi_coord[0]}, {poi_coord[1]}'] = self.parse_forecast(forecast)

        for hour, hour_data in aqi_data.items():
            print('hour aqi:', hour)
            for poi_coord, nearest in closest_coodinates_aqi.items():
                nearest_str = (nearest[0], nearest[1])
                if nearest_str in hour_data:
                    aqi_value = hour_data[nearest_str][0]['Air Quality Index']
                    if f'{poi_coord[0]}, {poi_coord[1]}' in returned_data[hour]:
                        returned_data[hour][f'{poi_coord[0]}, {poi_coord[1]}']['Air Quality Index'] = aqi_value

        return returned_data

    def parse_forecast(self, forecast):
        '''
        Parses the desired data from the forecast grid.

        Args:
            forecast (list): List of forecast data.

        Returns:
            dict: A dictionary containing the parsed forecast data.
        '''
        for value in forecast:

            if value['Dataset'] == '2 metre temperature':
                temperature = round(value['Data'] - 273.15, 1)
            elif value['Dataset'] == '2 metre relative humidity':
                humidity = round(value['Data'], 1)
            elif value['Dataset'] == '10 metre U wind component':
                u_wind = value['Data']
            elif value['Dataset'] == '10 metre V wind component':
                v_wind = value['Data']
            elif value['Dataset'] == 'surface precipitation amount, rain, convective':
                precipitation = round(value['Data'], 1)
            elif value['Dataset'] == 'Total Cloud Cover':
                cloudcoverage = round(value['Data'], 1)

        wind_speed = self.calculate_wind_speed_and_direction(
            u_wind, v_wind)
        return {
            'Air temperature': f'{str(temperature)} °C',
            'Humidity': f'{str(humidity)} %',
            'Wind speed': f'{wind_speed} m/s',
            'Precipitation': f'{precipitation} mm',
            'Cloud amount': f'{cloudcoverage} %',
        }

    def calculate_wind_speed_and_direction(self, u_wind, v_wind):
        '''
        Calculates the wind speed and direction based on the U and V components.

        Args:
            u_wind (float): U component of the wind.
            v_wind (float): V component of the wind.

        Returns:
            tuple: A tuple containing the wind speed and direction.
        '''
        wind_speed = math.sqrt(u_wind**2 + v_wind**2)
        wind_direction = math.atan2(u_wind, v_wind) * (180 / math.pi)
        wind_direction = (wind_direction + 360) % 360
        return round(wind_speed, 1)
