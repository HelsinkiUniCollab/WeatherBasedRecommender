import datetime as dt
import math as math
import numpy as np
from apis.time_data import utc_to_finnish, get_forecast_times
from fmiopendata.wfs import download_stored_query

def get_current_weather():
    '''
    Retrieves the current weather data for various stations.

    Returns:
        dict: A dictionary containing the current weather data for each station.
    '''

    obs = download_stored_query('fmi::observations::weather::multipointcoverage',
                                args=['bbox=24.5,60,25.5,60.5', 'timeseries=True'])
    data = {}
    for station in obs.location_metadata.keys():
        weatherdata = {
            'Air temperature': str(obs.data[station]['t2m']['values'][-1]) + ' °C',
            'Wind': str(obs.data[station]['ws_10min']['values'][-1]) + ' m/s',
            'Air pressure': str(obs.data[station]['p_sea']['values'][-1]) + ' mbar',
            'Humidity': str(obs.data[station]['rh']['values'][-1]) + ' %'
        }
        for value in list(weatherdata):
            if 'nan' in str(weatherdata[value]):
                weatherdata.pop(value)
        if weatherdata:
            weatherdata['Latitude'] =  obs.location_metadata[station]['latitude']
            weatherdata['Longitude'] = obs.location_metadata[station]['longitude']
            data[station] = weatherdata
    return data

def parse_forecast(forecast):
    '''
    Parses the wanted data from the grid 
    Some adjustments are made to change units to match obs station data
    '''
    for value in forecast:
        if value['Dataset'] == '2 metre temperature':
            temperature = round(value['Data'] - 273.15, 1)

        elif value['Dataset'] == '2 metre relative humidity':
            humidity = round(value['Data'], 1)

        elif value['Dataset'] == '10 metre U wind component':
            windU = value['Data']

        elif value['Dataset'] == '10 metre V wind component':
            windV = value['Data']
        
        elif value['Dataset'] == 'surface precipitation amount, rain, convective':
            precipitation = round(value['Data'], 1)

        elif value['Dataset'] == 'Total Cloud Cover':
            cloudcoverage = round(value['Data'], 1)

    wind_speed, wind_direction = calculate_wind_speed_and_direction(windU,windV)

    return {
        'Air temperature': f'{str(temperature)} °C',
        'Humidity': f'{str(humidity)} %',
        'Wind speed': f'{wind_speed} m/s',
        'Wind direction': f'{wind_direction} °',
        'Precipication': f'{precipitation}',
        'Total Cloud Cover': f'{cloudcoverage}',
    }


def calculate_wind_speed_and_direction(WindU, WindV):
    wind_speed = math.sqrt(WindU**2 + WindV**2)
    wind_direction = math.atan2(WindU, WindV) * (180 / math.pi)
    wind_direction = (wind_direction + 360) % 360 
    return (round(wind_speed, 1), round(wind_direction, 1))

class ForecastGrid:
    def __init__(self):
        self.data = None
        self.valid_times = None
        self.data_levels = None
        self.coordinates = None

    def update_data(self):
        current, start, end = get_forecast_times()
        bbox = '24.5,60,25.5,60.5'
        timestep = 60

        print(f'Query for new grind object at time: {current} UTC')

        forecast_data = download_stored_query('fmi::forecast::harmonie::surface::grid',
                                           args=[f'starttime={start}',
                                                 f'endtime={end}',
                                                 f'bbox={bbox}',
                                                 f'timestep={timestep}'])

        latest_forecast = max(forecast_data.data.keys())
        self.data = forecast_data.data[latest_forecast]
        self.data.parse(delete=True)

        self.valid_times = self.data.data.keys()
        earliest_step = min(self.valid_times)
        self.data_levels = self.data.data[earliest_step].keys()

        self.coordinates = np.dstack((self.data.latitudes, self.data.longitudes))
        print('got it')

    def get_data(self):
        '''Gets all the data from grid
        Returns:
            dict containing all the data
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
                        coordinates_data[key].append({'Dataset': dataset_name, 'Unit': unit, 'Data': data_value})
            data[time_str] = coordinates_data
        return data

    def get_coordinates(self):
        '''All avaible coords in bbox area
        Returns:
            List of list where each sublist is coord pair
        '''
        unique_coords = []

        flattened_coords = [coord for sublist in self.coordinates for coord in sublist]

        for coord in flattened_coords:
            if list(coord) not in unique_coords:
                unique_coords.append(list(coord))

        return unique_coords
