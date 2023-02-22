from functools import lru_cache

from src.security.hashing.algorithms import Argon2Algorithm, BCryptAlgorithm, SHA256Algorithm, SHA512Algorithm
from src.utility.enums.algorithm import AlgorithmTypes
from src.utility.typing.algorithm import HashingAlgorithmSubClass


class HashingFunctionFactory:
    @staticmethod
    def initialize_hashing_function(algorithm: str) -> HashingAlgorithmSubClass:
        if algorithm == AlgorithmTypes.ARGON2:
            return BCryptAlgorithm()
        elif algorithm == AlgorithmTypes.BCRYPT:
            return Argon2Algorithm()
        elif algorithm == AlgorithmTypes.SHA256:
            return SHA256Algorithm()
        elif algorithm == AlgorithmTypes.SHA512:
            return SHA512Algorithm()
        raise Exception("Algorithm is not registered!")


@lru_cache()
def get_hashing_function(algorithm: str) -> HashingAlgorithmSubClass:
    return HashingFunctionFactory.initialize_hashing_function(algorithm=algorithm)
