from src.config.settings.base import Settings
from src.config.settings.environment import Environment


class ProductionSettings(Settings):
    DESCRIPTION: str | None = (
        "Production Settings -- Backend application with FastAPI, PostgreSQL via SQLAlchemy with Alembic, and Docker."
    )
    ENVIRONMENT: Environment = Environment.PRODUCTION
