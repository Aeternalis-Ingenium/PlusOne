import unittest

from passlib.context import CryptContext as PasslibCryptContext

from src.security.hashing.algorithms import HashingAlgorithm
from src.utility.design_patterns.factory.hashing import get_hashing_function


class TestHashingFunction(unittest.TestCase):
    def setUp(self) -> None:
        self.argon2_context = get_hashing_function(algorithm="a2")
        self.argon2_salt = self.argon2_context.generate_hash(salt="argon2-salt", secret=None)  # type: ignore
        self.bcrypt_context = get_hashing_function(algorithm="bc")
        self.bcrypt_salt = self.bcrypt_context.generate_hash(salt="bcrypt-salt", secret=None)  # type: ignore
        self.sha256_context = get_hashing_function(algorithm="256")
        self.sha256_salt = self.sha256_context.generate_hash(salt="sha256-salt", secret=None)  # type: ignore
        self.sha512_context = get_hashing_function(algorithm="512")
        self.sha512_salt = self.sha512_context.generate_hash(salt="sha512-salt", secret=None)  # type: ignore

    async def test_hashing_function_with_argon2_algorithm(self):
        account_password = self.argon2_context.generate_hash(salt=self.argon2_salt, secret="fake-password")  # type: ignore
        assert isinstance(self.argon2_context, HashingAlgorithm)
        assert isinstance(self.argon2_context.algorithm, PasslibCryptContext)  # type: ignore
        assert str(self.argon2_context) == "Argon 2"
        assert (
            self.argon2_context.is_hash_verified(
                secret=self.argon2_salt + "fake-password", hashed_secret=account_password
            )
            is True
        )

    async def test_hashing_function_with_bcrypt_algorithm(self):
        account_password = self.bcrypt_context.generate_hash(salt=self.bcrypt_salt, secret="fake-password")  # type: ignore
        assert isinstance(self.bcrypt_context, HashingAlgorithm)
        assert isinstance(self.bcrypt_context.algorithm, PasslibCryptContext)  # type: ignore
        assert str(self.bcrypt_context) == "BCrypt"
        assert (
            self.bcrypt_context.is_hash_verified(
                secret=self.bcrypt_salt + "fake-password", hashed_secret=account_password
            )
            is True
        )

    async def test_hashing_function_with_sha256_algorithm(self):
        account_password = self.sha256_context.generate_hash(salt=self.sha256_salt, secret="fake-password")  # type: ignore
        assert isinstance(self.sha256_context, HashingAlgorithm)
        assert isinstance(self.sha256_context.algorithm, PasslibCryptContext)  # type: ignore
        assert str(self.sha256_context) == "SHA 256"
        assert (
            self.sha256_context.is_hash_verified(
                secret=self.sha256_salt + "fake-password", hashed_secret=account_password
            )
            is True
        )

    async def test_hashing_function_with_sha512_algorithm(self):
        account_password = self.sha512_context.generate_hash(salt=self.sha512_salt, secret="fake-password")  # type: ignore
        assert isinstance(self.sha512_context, HashingAlgorithm)
        assert isinstance(self.sha512_context.algorithm, PasslibCryptContext)  # type: ignore
        assert str(self.sha512_context) == "SHA 512"
        assert (
            self.sha512_context.is_hash_verified(
                secret=self.sha512_salt + "fake-password", hashed_secret=account_password
            )
            is True
        )

    async def test_hashing_function_with_argon2_and_bcrypt_algorithms(self):
        account_password = self.argon2_context.generate_hash(salt=self.bcrypt_salt, secret="fake-password")
        assert (
            self.argon2_context.is_hash_verified(
                secret=self.bcrypt_salt + "fake-password", hashed_secret=account_password
            )
            is True
        )

    def tearDown(self) -> None:
        pass
