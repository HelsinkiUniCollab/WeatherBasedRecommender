import datetime as dt
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
        'fmi::forecast::harmonie::surface::point::multipointcoverage',
        args=[
            f'starttime={start_time}',
            f'endtime={end_time}',
            'latlon=60.205,24.959',
        ],
    )

    return _forecast_query_handler(forecast_data.data)


def _forecast_query_handler(forecast_obj):
    """
    Handles the forecast data retrieved from the weather API.

    Args:
        forecast_obj (dict): The forecast data object.

    Returns:
        dict: A dictionary containing the formatted forecast data.
    """
    forecast_data = {}

    for datetime_obj, weather_info in forecast_obj.items():
        datetime_obj_utc_plus_3 = datetime_obj + dt.timedelta(hours=3)
        formatted_datetime = datetime_obj_utc_plus_3.strftime(
            '%d-%m-%Y %H:%M:%S')

        for _, station in weather_info.items():
            air_temperature = str(station['Air temperature']['value'])  # C
            air_pressure = str(station['Air pressure']['value'])  # hPa
            humidity = str(station['Humidity']['value'])  # %
            wind_speed = str(station['Wind speed']['value'])  # m/s

            forecast_data.setdefault('forecast', {})[formatted_datetime] = {
                'air temperature': air_temperature,
                'air pressure': air_pressure,
                'humidity': humidity,
                'wind': wind_speed
            }

    return forecast_data
