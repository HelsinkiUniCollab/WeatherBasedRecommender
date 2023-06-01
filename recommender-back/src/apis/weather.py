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

    except Exception as error:
        error_data = {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error)
        }
        return jsonify(error_data), 500

def get_current_weather():
    obs = download_stored_query('fmi::observations::weather::multipointcoverage',
                                args=['place=Kumpula,Helsinki'])

    current_airtemperature = _current_query_handler(
            obs, 'Helsinki Kumpula', 'Air temperature')
    current_windpeed = _current_query_handler(
            obs, 'Helsinki Kumpula', 'Wind speed')
    current_pressure = _current_query_handler(
            obs, 'Helsinki Kumpula', 'Pressure (msl)')
    current_humidity = _current_query_handler(
            obs, 'Helsinki Kumpula', 'Relative humidity')

    obs = download_stored_query('urban::observations::airquality::hourly::multipointcoverage',
                                args=['place=Kumpula,Helsinki'])

    current_airquality = _current_query_handler(
        obs, 'Helsinki Mäkelänkatu', 'Air Quality Index')

    current = {
        'current': {
            'air temperature': current_airtemperature,
            'air pressure': current_pressure,
            'humidity': current_humidity,
            'wind': current_windpeed,
            'air quality': current_airquality
        }
    }

    return current

def get_forecast():
    current_time = dt.datetime.utcnow()
    start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = (current_time + dt.timedelta(days=1, hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')

    forecast_data = download_stored_query('fmi::forecast::harmonie::surface::point::multipointcoverage',
                                         args=['starttime=' + start_time,
                                         'endtime=' + end_time,
                                         'latlon=60.205,24.959'])

    forecast = _forecast_query_handler(forecast_data.data)

    return forecast

def _current_query_handler(obs, station, value):
    """
    Handles the retrieval of specific data from the provided observations.

    Args:
        obs: The observations data object.
        station: The name of the station.
        value: The specific value to retrieve.

    Returns:
        The retrieved data as a string.
    """
    while True:
        latest = max(obs.data.keys())
        data = obs.data[latest][station][value]
        data = str(data.get('value'))
        if data in {'nan', 'NaN'}:
            obs.data.pop(latest)
            continue
        break
    return data

def _forecast_query_handler(forecast_obj):
    forecast_data = {}

    for datetime_obj, weather_info in forecast_obj.items():
        datetime_obj_utc_plus_3 = datetime_obj + dt.timedelta(hours=3)
        formatted_datetime = datetime_obj_utc_plus_3.strftime('%d-%m-%Y %H:%M:%S')

        for _, station in weather_info.items():
            air_temperature = str(station['Air temperature']['value']) # C
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
