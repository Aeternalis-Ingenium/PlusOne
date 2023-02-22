import abc

from passlib.context import CryptContext as PasslibCryptContext

from src.config.setup import settings


class HashingAlgorithm(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate_hash(self, salt: str, secret: str | None) -> str:
        """
        Returns a hashed string.
        """

    @abc.abstractmethod
    def is_hash_verified(self, secret: str, hashed_secret: str) -> bool:
        """
        Returns True the string is hashed with the chosen algorithm.
        """


class Argon2Algorithm(HashingAlgorithm):
    def __init__(self):
        self.algorithm: PasslibCryptContext = PasslibCryptContext(
            schemes=[settings.ARGON2_HASHING_ALGORITHM], deprecated="auto"
        )

    def generate_hash(self, salt: str, secret: str | None) -> str:
        if not secret:
            return self.algorithm.hash(secret=salt)
        return self.algorithm.hash(secret=salt + secret)

    def is_hash_verified(self, secret: str, hashed_secret: str) -> bool:
        return self.algorithm.verify(secret=secret, hash=hashed_secret)

    def __str__(self) -> str:
        return "Argon 2"


class BCryptAlgorithm(HashingAlgorithm):
    def __init__(self):
        self.algorithm: PasslibCryptContext = PasslibCryptContext(
            schemes=[settings.BCRYPT_HASHING_ALGORITHM], deprecated="auto"
        )

    def generate_hash(self, salt: str, secret: str | None) -> str:
        if not secret:
            return self.algorithm.hash(secret=salt)
        return self.algorithm.hash(secret=salt + secret)

    def is_hash_verified(self, secret: str, hashed_secret: str) -> bool:
        return self.algorithm.verify(secret=secret, hash=hashed_secret)

    def __str__(self) -> str:
        return "BCrypt"


class SHA256Algorithm(HashingAlgorithm):
    def __init__(self):
        self.algorithm: PasslibCryptContext = PasslibCryptContext(
            schemes=[settings.SHA256_HASHING_ALGORITHM], deprecated="auto"
        )

    def generate_hash(self, salt: str, secret: str | None) -> str:
        if not secret:
            return self.algorithm.hash(secret=salt)
        return self.algorithm.hash(secret=salt + secret)

    def is_hash_verified(self, secret: str, hashed_secret: str) -> bool:
        return self.algorithm.verify(secret=secret, hash=hashed_secret)

    def __str__(self) -> str:
        return "SHA 256"


class SHA512Algorithm(HashingAlgorithm):
    def __init__(self):
        self.algorithm: PasslibCryptContext = PasslibCryptContext(
            schemes=[settings.SHA512_HASHING_ALGORITHM], deprecated="auto"
        )

    def generate_hash(self, salt: str, secret: str | None) -> str:
        if not secret:
            return self.algorithm.hash(secret=salt)
        return self.algorithm.hash(secret=salt + secret)

    def is_hash_verified(self, secret: str, hashed_secret: str) -> bool:
        return self.algorithm.verify(secret=secret, hash=hashed_secret)

    def __str__(self) -> str:
        return "SHA 512"
