from functools import lru_cache

from src.config.setup import settings
from src.security.authentication.api_key import CustomAPIKeyCookie, CustomAPIKeyHeader, CustomAPIKeyQuery
from src.utility.enums.api_key import APIKeyTitles, APIKeyTypes
from src.utility.typing.api_key import CustomAPIKey


class APIKeyFactory:
    @staticmethod
    def initialize_api_key(key_type: str, is_auto_error: bool) -> CustomAPIKey:
        if key_type == APIKeyTypes.COOKIE:
            return CustomAPIKeyCookie(name=APIKeyTitles.API_KEY_COOKIE, auto_error=is_auto_error)
        elif key_type == APIKeyTypes.HEADER:
            return CustomAPIKeyHeader(name=APIKeyTitles.API_KEY_HEADER, auto_error=is_auto_error)
        elif key_type == APIKeyTypes.QUERY:
            return CustomAPIKeyQuery(name=APIKeyTitles.API_KEY_QUERY, auto_error=is_auto_error)
        raise Exception("Invalid method for API Key initialization!")


@lru_cache()
def get_api_key(key_type: str, is_auto_error: bool = True) -> CustomAPIKey:
    return APIKeyFactory.initialize_api_key(key_type=key_type, is_auto_error=is_auto_error)
