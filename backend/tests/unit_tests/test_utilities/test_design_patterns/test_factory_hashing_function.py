import unittest

from src.security.hashing.algorithms import Argon2Algorithm, BCryptAlgorithm, SHA256Algorithm, SHA512Algorithm
from src.utility.design_patterns.factory.hashing import get_hashing_function


class TestHashingFunctionFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.argon2 = get_hashing_function(algorithm="a2")
        self.bcrypt = get_hashing_function(algorithm="bc")
        self.sha256 = get_hashing_function(algorithm="256")
        self.sha512 = get_hashing_function(algorithm="512")

    async def test_create_argon2_algorithm_from_hashing_function_factory(self) -> None:
        assert self.argon2 == Argon2Algorithm

    async def test_create_bcrypt_algorithm_from_hashing_function_factory(self) -> None:
        assert self.bcrypt == BCryptAlgorithm

    async def test_create_hsa256_algorithm_from_hashing_function_factory(self) -> None:
        assert self.sha256 == SHA256Algorithm

    async def test_create_hsa512_algorithm_from_hashing_function_factory(self) -> None:
        assert self.sha512 == SHA512Algorithm

    def tearDown(self):
        pass
