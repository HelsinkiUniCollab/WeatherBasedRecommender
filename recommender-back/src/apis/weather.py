import datetime as dt
import numpy as np
from fmiopendata.wfs import download_stored_query
import eccodes

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
        elif value['Dataset'] == 'Mean sea level pressure':
            pressure = round(value['Data'], 1)
        elif value['Dataset'] == '10 metre wind speed':
            windspeed = round(value['Data'], 1)
    return {
        'Air temperature': f'{str(temperature)} °C',
        'Wind': f'{str(windspeed)} m/s',
        'Air pressure': f'{str(pressure/100)} mbar',
        'Humidity': f'{str(humidity)} %'
    }


class ForecastGrid:
    def __init__(self):
        self.data = None
        self.valid_times = None
        self.data_levels = None
        self.coordinates = None

    def update_data(self):
        # Query format needs to be in UTC, which is three hours behind of Finnish time.
        # The starting point for the datetime objects is the next hour from the current time, rounded up.
        # For example, if the current time in Finland is 9:10, you would round up to 10:00, substract 3 hours and get first datetime object at 7:00 UTC.

        current_time = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=3)
        start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_time = (current_time + dt.timedelta(days=1, hours=1)
                   ).strftime('%Y-%m-%dT%H:%M:%SZ')
        bbox = '24.5,60,25.5,60.5'
        timestep = 60 # minutes

        print(f'Query for new grind object at time: {current_time} UTC')

        forecast_data = download_stored_query('fmi::forecast::harmonie::surface::grid',
                                           args=[f'starttime={start_time}',
                                                 f'endtime={end_time}',
                                                 f'bbox={bbox}',
                                                 f'timestep={timestep}'])

        latest_forecast = max(forecast_data.data.keys())
        self.data = forecast_data.data[latest_forecast]
        self.data.parse(delete=True)

        self.valid_times = self.data.data.keys()
        earliest_step = min(self.valid_times)
        self.data_levels = self.data.data[earliest_step].keys()

        self.coordinates = np.dstack((self.data.latitudes, self.data.longitudes))


    def get_data(self):
        '''Gets all the data from grid
        Returns:
            dict containing all the data
        '''
        data = {}
        for date_time in self.valid_times:
            time_str = date_time.strftime('%Y-%m-%d %H:%M:%S')
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
