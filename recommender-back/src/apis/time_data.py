import datetime
from suntime import Sun

def get_sun_data():
    """
    Get info of sunrise and sunset based on date.

    Returns:
        Tuple: sunrise and sunset in formatted string.
    """
    date = datetime.date.today()
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
    time = datetime.datetime.now()

    return time.strftime('%H:%M')
