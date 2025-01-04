from datetime import datetime


def date_validator(value: str):
    datetime.strptime(value, "%Y-%m-%d")
    return value
