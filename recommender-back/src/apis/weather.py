import datetime as dt
import numpy as np
import time
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

    def update_data(self):
        # Limit the time to the next 24 hours
        now = dt.datetime.utcnow()
        start_time = now.strftime('%Y-%m-%dT00:00:00Z')
        end_time = (now + dt.timedelta(hours=24)).strftime('%Y-%m-%dT00:00:00Z')
        bbox = "24.5,60,25.5,60.5"

        model_data = download_stored_query("fmi::forecast::harmonie::surface::grid",
                                           args=["starttime=" + start_time,
                                                 "endtime=" + end_time,
                                                 "bbox=" + bbox])

        latest_run = max(model_data.data.keys())
        self.data = model_data.data[latest_run]
        self.data.parse(delete=True)

        self.valid_times = self.data.data.keys()
        earliest_step = min(self.valid_times)
        self.data_levels = self.data.data[earliest_step].keys()

    def get_data(self, valid_time, lat, lon):
        # Find the closest valid time to the specified time
        closest_valid_time = min(self.valid_times, key=lambda x: abs(x - valid_time))
        datasets = self.data.data[closest_valid_time]

        # Retrieve the data at the specified location
        lat_index = self.find_nearest_index(self.data.latitudes, lat)
        lon_index = self.find_nearest_index(self.data.longitudes, lon)

        data = {}
        for level in self.data_levels:
            level_data = {}
            for dataset_name, dataset in datasets[level].items():
                unit = dataset["units"]
                data_array = dataset["data"][lat_index, lon_index]
                level_data[dataset_name] = {"unit": unit, "data": data_array}
            data[level] = level_data

        return data

    @staticmethod
    def find_nearest_index(array, value):
        return int((np.abs(array - value)).argmin())

# Create an instance of the ForecastGrid class
#forecast_grid = ForecastGrid()

# Update the grid data initially
#forecast_grid.update_data()

# Example usage: Fetch data for a specific time and location
specific_time = dt.datetime.utcnow() + dt.timedelta(hours=12)
latitude = 60.5
longitude = 25.0

data = forecast_grid.get_data(specific_time, latitude, longitude)
print("Forecast data for time:", specific_time)
print("Latitude:", latitude)
print("Longitude:", longitude)
print("Data:", data)

# Update the grid data hourly
#while True:
#    forecast_grid.update_data()
    # Perform any additional processing or analysis here
    # Sleep for an hour before fetching the new grid data
#    time.sleep(3600)


