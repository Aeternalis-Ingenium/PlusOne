import enum

from src.config.setup import settings


class APIKeyTypes(str, enum.Enum):
    HEADER = "header"
    COOKIE = "cookie"
    QUERY = "query"


class APIKeyTitles(str, enum.Enum):
    API_KEY_COOKIE = settings.API_COOKIE_KEY_TITLE.get_secret_value()
    API_KEY_HEADER = settings.API_HEADER_KEY_TITLE.get_secret_value()
    API_KEY_QUERY = settings.API_QUERY_KEY_TITLE.get_secret_value()
