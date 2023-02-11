import datetime


def datetime_2_isoformat(date_time: datetime.datetime) -> str:
    return date_time.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")
