from flask import jsonify
from fmiopendata.wfs import download_stored_query


def get_weather():
    """
    Retrieves weather information.

    Returns:
        A JSON response containing the air temperature and air quality data.

    Raises:
        Exception: If an error occurs during the retrieval process.
    """
    try:
        obs = download_stored_query('fmi::observations::weather::multipointcoverage',
                                    args=['place=Kumpula,Helsinki'])
        airtemperature = query_handler(
            obs, 'Helsinki Kumpula', 'Air temperature')

        obs = download_stored_query('urban::observations::airquality::hourly::multipointcoverage',
                                    args=['place=Kumpula,Helsinki'])
        airquality = query_handler(
            obs, 'Helsinki Mäkelänkatu', 'Air Quality Index')

        data = {
            'airtemperature': airtemperature,
            'airquality': airquality
        }
        return jsonify(data)
    except Exception as error:
        error_data = {
            'message': 'An error occurred',
            'status': 500,
            'error': str(error)
        }
        return jsonify(error_data), 500


def query_handler(obs, station, value):
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
