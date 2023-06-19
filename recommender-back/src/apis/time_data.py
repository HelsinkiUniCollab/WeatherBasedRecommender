import datetime as dt
from suntime import Sun
from dateutil import tz

def get_sun_data():
    """
    Get info of sunrise and sunset based on date.

    Returns:
        Tuple: sunrise and sunset in formatted string.
    """
    date = dt.date.today()
    sun = Sun(60.192059,24.945831)
    sunrise = sun.get_local_sunrise_time(date)
    sunset = sun.get_local_sunset_time(date)
    str_sunrise = sunrise.strftime('%H:%M')
    str_sunset = sunset.strftime('%H:%M')
    return str_sunrise, str_sunset

def get_current_time(plus=None):
    """
    Retrieves the current time as a formatted string.
    
    plus; number of hours added to datetime.now()

    Returns:
        str: The current time in the formatted string.
    """
    if plus is None:
        time = dt.datetime.now()
        return time.strftime('%H:%M')
    else:
        time = dt.datetime.now() + dt.timedelta(hours=plus)
        return time.strftime('%H:%M')

def utc_to_finnish(datetime):
    """
    Converts a UTC datetime object to the corresponding time in the Finnish timezone.

    Args:
        datetime (datetime): The UTC datetime object to be converted.

    Returns:
        datetime: The datetime object converted to the Finnish timezone.
    """
    set_utc = datetime.replace(tzinfo=tz.UTC)
    get_timezone = tz.gettz('Europe/Helsinki')
    return set_utc.astimezone(get_timezone)

def get_forecast_times():
    """
    Retrieves the current time, start time, and end time for a forecast.

    Returns:
        Tuple: A tuple containing the current time, start time, and end time as formatted strings.
    """
    current_time = dt.datetime.now(dt.timezone.utc)
    start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = (current_time + dt.timedelta(days=1, hours=0)
                ).strftime('%Y-%m-%dT%H:%M:%SZ')
    return current_time, start_time, end_time
