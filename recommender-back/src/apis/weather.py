import datetime as dt
import numpy as np
from flask import jsonify
from fmiopendata.wfs import download_stored_query



def get_full_weather_info():
    """
    Retrieves full weather information.

    Returns:
        A JSON response containing the current weather information and forecast.

    Raises:
        Exception: If an error occurs during the retrieval process.
    """
    try:
        current = get_current_weather()
        forecast = get_forecast()

        data = {**current, **forecast}

        return jsonify(data)

    except KeyError as error:
        error_data = {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error)
        }
        return jsonify(error_data), 500


def get_current_weather():
    """
    Retrieves the current weather data for various stations.

    Returns:
        dict: A dictionary containing the current weather data for each station.
    """

    obs = download_stored_query('fmi::observations::weather::multipointcoverage',
                                args=["bbox=24.5,60,25.5,60.5", "timeseries=True"])
    data = {}
    for station in obs.location_metadata.keys():
        weatherdata = {
            'Air temperature': str(obs.data[station]["t2m"]["values"][-1]) + " °C",
            'Wind': str(obs.data[station]["ws_10min"]["values"][-1]) + " m/s",
            'Air pressure': str(obs.data[station]["p_sea"]["values"][-1]) + " mbar",
            'Humidity': str(obs.data[station]["rh"]["values"][-1]) + " %"
        }
        for value in list(weatherdata):
            if 'nan' in str(weatherdata[value]):
                weatherdata.pop(value)
        if weatherdata:
            weatherdata["Latitude"] =  obs.location_metadata[station]["latitude"]
            weatherdata["Longitude"] = obs.location_metadata[station]["longitude"]
            data[station] = weatherdata
    return data

def get_forecast():
    """
    Retrieves the weather forecast data.

    Returns:
        dict: A dictionary containing the weather forecast for different time periods.
    """
    current_time = dt.datetime.now(dt.timezone.utc)
    start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = (current_time + dt.timedelta(days=1, hours=1)
                ).strftime('%Y-%m-%dT%H:%M:%SZ')

    forecast_data = download_stored_query(
        'fmi::forecast::harmonie::surface::grid',
        args=[
            f'starttime={start_time}',
            f'endtime={end_time}',
            "bbox=24.5,60,25.5,60.5"
        ],
    )

    return _forecast_query_handler(forecast_data)


def _forecast_query_handler(forecast_obj):
    """
    Handles the forecast data retrieved from the weather API.

    Args:
        forecast_obj (dict): The forecast data object.

    Returns:
        dict: A dictionary containing the formatted forecast data.
    """
    print(forecast_obj.data)
    print(forecast_obj.latitudes)
    return forecast_obj


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
        current_time = dt.datetime.now(dt.timezone.utc)
        start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_time = (current_time + dt.timedelta(days=1, hours=1)
                   ).strftime('%Y-%m-%dT%H:%M:%SZ')
        bbox = "24.5,60,25.5,60.5"
        timestep = 60 # minutes

        print(f"Query for new grind object at time: {current_time} UTC")

        forecast_data = download_stored_query("fmi::forecast::harmonie::surface::grid",
                                           args=[f"starttime={start_time}",
                                                 f"endtime={end_time}",
                                                 f"bbox={bbox}",
                                                 f"timestep={timestep}"])

        latest_forecast = max(forecast_data.data.keys())
        self.data = forecast_data.data[latest_forecast]
        self.data.parse(delete=True)

        self.valid_times = self.data.data.keys()
        earliest_step = min(self.valid_times)
        self.data_levels = self.data.data[earliest_step].keys()

        self.coordinates = np.dstack((self.data.latitudes, self.data.longitudes))

    def get_data(self):
        data = {}
        for date_time in self.valid_times:
            time_str = date_time.strftime('%Y-%m-%d %H:%M:%S')

            level_data = {}
            for level in self.data_levels:
                datasets = self.data.data[date_time][level]
                for dataset_name, dataset in datasets.items():
                    unit = dataset['units']
                    data_array = dataset['data']

                    coordinates_data = {}
                    for (lat_index, lon_index), data_value in np.ndenumerate(data_array):
                        latitude = self.coordinates[lat_index, lon_index, 0]
                        longitude = self.coordinates[lat_index, lon_index, 1]
                        key = str((latitude, longitude))

                        coordinates_data[key] = {'Unit': unit, 'Data': data_value}

                    level_data[dataset_name] = coordinates_data

            data[time_str] = level_data

        return data

    def find_nearest_index(self, lat, lon):
        target_coordinates = np.array([lat, lon])
        flattened_indices = np.argmin(np.linalg.norm(self.coordinates - target_coordinates, axis=-1), axis=None)
        return np.unravel_index(flattened_indices, self.coordinates.shape[:-1])


#if __name__ == "__main__":

    # Create an instance of the ForecastGrid class
#    forecast_grid = ForecastGrid()

    # Update the grid data initially
#    forecast_grid.update_data()

    # Example usage: Fetch data for a specific time in UTC
#    specific_time = dt.datetime.utcnow()

#    latitude = 60.44
#    longitude = 25.34

#    data = forecast_grid.get_data()
#    print("Latitude:", latitude)
#    print("Longitude:", longitude)
#    print("Data:", data)

    # Update the grid data hourly
    #while True:
    #    forecast_grid.update_data()
        # Perform any additional processing or analysis here
        # Sleep for an hour before fetching the new grid data
    #    time.sleep(3600)
