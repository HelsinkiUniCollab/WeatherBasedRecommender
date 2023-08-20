import datetime as dt
import pytz
from datetime import datetime
from suntime import Sun
from dateutil import tz


def get_sun_data():
    '''
    Get info of sunrise and sunset based on the date.

    Returns:
        Tuple: sunrise and sunset in formatted string.
    '''
    date = dt.date.today()
    sun = Sun(60.192059, 24.945831)
    sunrise = sun.get_local_sunrise_time(date)
    sunset = sun.get_local_sunset_time(date)
    str_sunrise = sunrise.strftime('%H:%M')
    str_sunset = sunset.strftime('%H:%M')
    return str_sunrise, str_sunset


def get_current_time(plus=None):
    '''
    Retrieves the current time as a formatted String.

    Returns:
        str: The current time in the formatted String.
    '''
    if plus is None:
        time = dt.datetime.now()
    else:
        time = dt.datetime.now() + dt.timedelta(hours=plus)

    return time.strftime('%H:%M')


def utc_to_finnish(datetime_object):
    '''
    Converts a UTC datetime object to the corresponding time in the Finnish timezone.

    Args:
        datetime (datetime): The UTC datetime object to be converted.

    Returns:
        datetime: The datetime object converted to the Finnish timezone.
    '''
    set_utc = datetime_object.replace(tzinfo=tz.UTC)
    get_timezone = tz.gettz('Europe/Helsinki')
    return set_utc.astimezone(get_timezone)


def forecast_q_time_to_finnish(fore_q_time):
    '''
    Converts forecast query time into Finnish time format.

    Returns:
        String: converted time in Finnish timezone format
    '''
    finland_tz = pytz.timezone('Europe/Helsinki')
    fore_q_time_datetime = datetime.strptime(fore_q_time, '%Y-%m-%d %H:%M:%S')
    return fore_q_time_datetime.replace(tzinfo=pytz.utc).astimezone(finland_tz)

def server_time_to_finnish():
    """Converts server datetime object time to match finnish timezone

    Returns:
        datetime: New datetime object with times converted to finnish time.
    """
    server_time = datetime.now()
    finland_tz = pytz.timezone('Europe/Helsinki')
    return server_time.astimezone(finland_tz)


def get_forecast_times():
    '''
    Retrieves the current time, start time, and end time for a forecast.

    Returns:
        Tuple: A tuple containing the current time, start time, and end time as formatted strings.
    '''
    current_time = dt.datetime.now(dt.timezone.utc)
    start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = (current_time + dt.timedelta(days=1, hours=1)
                ).strftime('%Y-%m-%dT%H:%M:%SZ')
    return current_time, start_time, end_time


def time_from_string(time_str):
    '''
    Converts a given time string or datetime object.

    Args:
        time_str (Union[str, datetime.datetime]): The time representation, either as a string formatted as "%H:%M" or as a datetime.datetime object.

    Returns:
        datetime.time: The time extracted from the input.

    Raises:
        ValueError: If the provided string is not formatted correctly.
    '''
    if isinstance(time_str, dt.datetime):
        return time_str.time()
    return dt.datetime.strptime(time_str, "%H:%M").time()
