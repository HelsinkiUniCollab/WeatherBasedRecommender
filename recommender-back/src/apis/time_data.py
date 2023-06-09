import datetime
from suntime import Sun

class Time:
    """
    A class to fetch time, sunrise and sunset info.
    """
    def __init__(self):
        self.date = datetime.date.today()
        self.sun = Sun(60.192059,24.945831)

    def get_sun_data(self):
        """
        Get info of sunrise and sunset based on date.

        Returns:
            Tuple: sunrise and sunset in formatted string.
        """
        sunrise = self.sun.get_local_sunrise_time(self.date)
        sunset = self.sun.get_local_sunset_time(self.date)

        str_sunrise = sunrise.strftime('%H:%M')
        str_sunset = sunset.strftime('%H:%M')

        return str_sunrise, str_sunset

    def get_current_time(self):
        """
        Returns:
            Sring: Time in formatted string
        """
        time = datetime.datetime.now()

        str_time = time.strftime('%H:%M')

        return str_time
