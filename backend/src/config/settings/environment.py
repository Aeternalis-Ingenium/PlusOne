import enum


class Environment(str, enum.Enum):
    PRODUCTION = "PROD"
    DEVELOPMENT = "DEV"
    STAGING = "STAGE"
