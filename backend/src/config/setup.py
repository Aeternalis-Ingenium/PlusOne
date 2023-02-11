from functools import lru_cache

import decouple

from src.config.settings.base import Settings
from src.config.settings.development import DevelopmentSettings
from src.config.settings.environment import Environment
from src.config.settings.production import ProductionSettings
from src.config.settings.staging import StagingSettings


class SettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> Settings:
        if self.environment == Environment.DEVELOPMENT.value:
            return DevelopmentSettings()
        elif self.environment == Environment.STAGING.value:
            return StagingSettings()
        return ProductionSettings()


@lru_cache()
def get_settings() -> Settings:
    return SettingsFactory(environment=decouple.config("ENVIRONMENT", default="DEV", cast=str))()  # type: ignore


settings: Settings = get_settings()
