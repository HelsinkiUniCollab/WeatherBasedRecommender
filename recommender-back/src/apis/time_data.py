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

def get_current_time():
    """
    Returns:
        Sring: Time in formatted string
    """
    time = dt.datetime.now()

    return time.strftime('%H:%M')

def utc_to_finnish(datetime):
    set_utc = datetime.replace(tzinfo=tz.UTC)
    get_timezone = tz.gettz('Europe/Helsinki')
    finnish_time = set_utc.astimezone(get_timezone)
    return finnish_time

def get_forecast_times():
    current_time = dt.datetime.now(dt.timezone.utc)
    start_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = (current_time + dt.timedelta(days=1, hours=1)
                ).strftime('%Y-%m-%dT%H:%M:%SZ')
    return current_time, start_time, end_time
