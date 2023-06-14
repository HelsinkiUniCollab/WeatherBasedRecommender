from dateutil import tz

def utc_to_finnish(datetime):
    set_utc = datetime.replace(tzinfo=tz.UTC)
    get_timezone = tz.gettz('Europe/Helsinki')
    finnish_time = set_utc.astimezone(get_timezone)
    return finnish_time
