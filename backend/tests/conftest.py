import typing

import asgi_lifespan
import fastapi
import httpx
import pytest

from src.config.setup import settings
from src.main import initialize_application
from src.models.db.accounts.base import Account
from src.security.authorizations.jwt import jwt_manager


@pytest.fixture(name="test_app")
def test_app() -> fastapi.FastAPI:
    """
    A fixture to initialize FastAPI instance as test application.
    """

    return initialize_application()


@pytest.fixture(name="initialize_test_application")
async def initialize_test_application(test_app: fastapi.FastAPI) -> typing.AsyncGenerator[fastapi.FastAPI, None]:
    async with asgi_lifespan.LifespanManager(test_app):
        yield test_app


@pytest.fixture(name="async_client")
async def async_client(initialize_test_application: fastapi.FastAPI) -> typing.AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(
        app=initialize_test_application,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client


@pytest.fixture(name="test_jwt_token")
def test_jwt_token(test_account: Account) -> str:
    return jwt_manager.generate_jwt(account=test_account)


@pytest.fixture(name="authorized_token_prefix")
def authorized_token_prefix() -> str:
    jwt_token_prefix = settings.JWT_TOKEN_PREFIX
    return jwt_token_prefix


@pytest.fixture(name="authorized_async_client")
def authorized_async_client(async_client: httpx.AsyncClient) -> httpx.AsyncClient:
    async_client.headers = {
        "Authorization": f"{authorized_token_prefix}-{test_jwt_token}",
        **async_client.headers,
    }

    return async_client
