import unittest

import pydantic
from jose import jwt as jose_jwt

from src.config.setup import settings
from src.models.schema.accounts.base import AccountInSignup
from src.security.authorizations.jwt import jwt_manager


class TestJWTManager(unittest.TestCase):
    def setUp(self) -> None:
        self.account = AccountInSignup(
            username="testaccount", email=pydantic.EmailStr("testaccount@unittest.com"), password="test-password"
        )

    async def test_generate_jwt_token(self):
        jwt_token = jwt_manager.generate_jwt(account=self.account)  # type: ignore

        assert isinstance(jwt_token, str)

        parsed_payload = jose_jwt.decode(
            token=jwt_token, key=settings.JWT_SECRET_KEY.get_secret_value(), algorithms=[settings.JWT_ALGORITHM]
        )

        assert parsed_payload["username"] == "testaccount"
        assert parsed_payload["email"] == "testaccount@pytest.com"
        assert parsed_payload["subject"] == "access"

    async def test_retrieve_details_from_jwt_token(self):
        jwt_token = jwt_manager.generate_jwt(account=self.account)  # type: ignore
        username, email = jwt_manager.retrieve_details_from_jwt(token=jwt_token)

        assert username == self.account.username
        assert email == self.account.email

    def tearDown(self) -> None:
        pass
