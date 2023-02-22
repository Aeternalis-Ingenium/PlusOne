import enum


class AlgorithmTypes(str, enum.Enum):
    ARGON2 = "a2"
    BCRYPT = "bc"
    SHA256 = "256"
    SHA512 = "512"
