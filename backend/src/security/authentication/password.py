from functools import lru_cache

from src.config.setup import settings
from src.utility.design_patterns.factory.hashing import get_hashing_function


class PasswordManager:
    @staticmethod
    def generate_double_layered_password(password: str) -> tuple[str, str]:
        hashed_salt = get_hashing_function(algorithm=settings.PWD_ALGORITHM_LAYER_1).generate_hash(
            salt=settings.HASHING_SALT, secret=None
        )
        hashed_password = get_hashing_function(algorithm=settings.PWD_ALGORITHM_LAYER_2).generate_hash(
            salt=hashed_salt, secret=password
        )
        return (hashed_salt, hashed_password)

    @staticmethod
    def is_hashed_password_verified(hashed_salt: str, password: str, hashed_password: str) -> bool:
        return get_hashing_function(algorithm=settings.PWD_ALGORITHM_LAYER_2).is_hash_verified(
            secret=hashed_salt + password, hashed_secret=hashed_password
        )


@lru_cache()
def get_password_manager() -> PasswordManager:
    return PasswordManager()


pwd_manager = get_password_manager()
