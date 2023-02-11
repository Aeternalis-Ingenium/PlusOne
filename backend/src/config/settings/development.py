from src.config.settings.base import Settings
from src.config.settings.environment import Environment


class DevelopmentSettings(Settings):
    DESCRIPTION: str | None = (
        "Development Settings -- Backend application with FastAPI, PostgreSQL via SQLAlchemy with Alembic, and Docker."
    )
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
