import datetime

def unix_to_utc(unix_time):
    """Konwertuje czas w formacie Unix na czas UTC."""
    utc_time = datetime.datetime.utcfromtimestamp(unix_time / 1000.0)
    return utc_time.strftime('%a, %d %b %Y %H:%M:%S GMT')


def utc_to_unix(utc_time):
    """Convert UTC time on format Unix time."""
    dt = datetime.datetime.strptime(utc_time, '%Y-%m-%d')
    unix_time = (dt - datetime.datetime(1970, 1, 1)).total_seconds() * 1000
    unix_time = int(unix_time)

    utc_time = datetime.datetime.utcfromtimestamp(unix_time / 1000.0)
    utc_str = utc_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
    return (unix_time,utc_str)

