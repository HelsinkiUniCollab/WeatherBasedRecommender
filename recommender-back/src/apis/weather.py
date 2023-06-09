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


def forecast_grid(latitude, longitude):

    latitude = 60.17523
    longitude = 24.94459
    now = dt.datetime.utcnow()


    # Set start_time to 6 AM of the current day
    start_time = now.replace(hour=11, minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Set end_time to 6 AM of the next day
    end_time = (now + dt.timedelta(days=1)).replace(hour=11, minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ')


    model_data = download_stored_query("fmi::forecast::harmonie::surface::grid",
                                       args=["starttime=" + start_time,
                                             "endtime=" + end_time,
                                             "bbox=24.5,60,25.5,60.5"])

    latest_run = max(model_data.data.keys())
    data = model_data.data[latest_run]
    data.parse(delete=True)

    valid_times = data.data.keys()
    print(list(valid_times))
    return

    valid_times = data.data.keys()
    earliest_step = min(valid_times)
    data_levels = data.data[earliest_step].keys()

    lon_index, lat_index = np.unravel_index(np.abs(data.longitudes - longitude).argmin(), data.longitudes.shape)
    lat_index, lon_index = np.unravel_index(np.abs(data.latitudes - latitude).argmin(), data.latitudes.shape)

    for level in data_levels:
        datasets = data.data[earliest_step][level]
        for dset in datasets:
            unit = datasets[dset]["units"]
            data_array = datasets[dset]["data"]

            print("Level:", level)
            print("Dataset name:", dset)
            print("Data unit:", unit)
            print("Data array shape:", data_array.shape)
            specific_data = data_array[lon_index, lat_index]  # Corrected indexing
            print("Specific data:", specific_data)

forecast_grid(1,1)

