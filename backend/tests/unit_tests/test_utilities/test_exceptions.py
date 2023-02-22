import unittest

import pytest

from src.utility.exceptions.custom import (
    EmailAlreadyExists,
    EntityAlreadyExists,
    EntityDoesNotExist,
    UsernameAlreadyExists,
)
from src.utility.exceptions.http.exc_400 import (
    http_exc_400_bad_email_request,
    http_exc_400_bad_request,
    http_exc_400_bad_username_request,
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)
from src.utility.exceptions.http.exc_401 import http_exc_401_unauthorized_request
from src.utility.exceptions.http.exc_403 import http_exc_403_forbidden_request
from src.utility.exceptions.http.exc_404 import (
    http_exc_404_email_not_found_request,
    http_exc_404_id_not_found_request,
    http_exc_404_name_not_found_request,
    http_exc_404_username_not_found_request,
)
from src.utility.messages.exceptions.http.exc_details import (
    http_400_bad_request_details,
    http_400_email_details,
    http_400_signin_credentials_details,
    http_400_signup_credentials_details,
    http_400_username_details,
    http_401_unauthorized_details,
    http_403_forbidden_details,
    http_404_email_details,
    http_404_id_details,
    http_404_name_details,
    http_404_username_details,
)


class TestCustomExceptionClass(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_id = 1
        self.name = "testname"
        self.username = "cooltestusername"
        self.email = "cooltestemail@unittest.com"
        self.email_taken_message = "Email is taken! Please try a different email address."
        self.username_taken_message = "Username is taken! Please try a different username."
        self.entity_exists_message = "Database entity with id 1 already exist!"
        self.non_existing_entity_message = "Database entity with id 1 does not exist!"

    async def test_raise_custom_exception_class_for_taken_email(self) -> None:
        def email_taken_exception() -> EmailAlreadyExists:
            raise EmailAlreadyExists(self.email_taken_message)

        with pytest.raises(Exception, match=self.email_taken_message):
            email_taken_exception()

    async def test_raise_custom_exception_class_for_taken_username(self) -> None:
        def username_taken_exception() -> UsernameAlreadyExists:
            raise UsernameAlreadyExists(self.username_taken_message)

        with pytest.raises(Exception, match=self.username_taken_message):
            username_taken_exception()

    async def test_raise_custom_exception_class_for_existing_entity(self) -> None:
        def entity_existed_exception() -> EntityAlreadyExists:
            raise EntityAlreadyExists(self.entity_exists_message)

        with pytest.raises(Exception, match=self.entity_exists_message):
            entity_existed_exception()

    async def test_raise_custom_exception_class_for_non_existing_entity(self) -> None:
        def non_existing_entity_exception() -> EntityDoesNotExist:
            raise EntityDoesNotExist(self.non_existing_entity_message)

        with pytest.raises(Exception, match=self.non_existing_entity_message):
            non_existing_entity_exception()

    async def test_raise_http400_for_bad_request(self) -> None:
        with pytest.raises(Exception, match=http_400_bad_request_details()):
            await http_exc_400_bad_request()

    async def test_raise_http400_for_bad_signin_request(self) -> None:
        with pytest.raises(Exception, match=http_400_signin_credentials_details()):
            await http_exc_400_credentials_bad_signin_request()

    async def test_raise_http400_for_bad_signup_request(self) -> None:
        with pytest.raises(Exception, match=http_400_signup_credentials_details()):
            await http_exc_400_credentials_bad_signup_request()

    async def test_raise_http400_for_bad_email_request(self) -> None:
        with pytest.raises(Exception, match=http_400_email_details(email=self.email)):
            await http_exc_400_bad_email_request(email=self.email)

    async def test_raise_http400_for_bad_username_request(self) -> None:
        with pytest.raises(Exception, match=http_400_username_details(username=self.username)):
            await http_exc_400_bad_username_request(username=self.username)

    async def test_raise_http401_for_unauthorized_request(self) -> None:
        with pytest.raises(Exception, match=http_401_unauthorized_details()):
            await http_exc_401_unauthorized_request()

    async def test_raise_http403_for_forbidden_request(self) -> None:
        with pytest.raises(Exception, match=http_403_forbidden_details()):
            await http_exc_403_forbidden_request()

    async def test_raise_http404_for_email_not_found_request(self) -> None:
        with pytest.raises(Exception, match=http_404_email_details(email=self.email)):
            await http_exc_404_email_not_found_request(email=self.email)

    async def test_raise_http404_for_username_not_found_request(self) -> None:
        with pytest.raises(Exception, match=http_404_username_details(username=self.username)):
            await http_exc_404_username_not_found_request(username=self.username)

    async def test_raise_http404_for_id_not_found_request(self) -> None:
        with pytest.raises(Exception, match=http_404_id_details(id=self.fake_id)):
            await http_exc_404_id_not_found_request(id=self.fake_id)

    async def test_raise_http404_for_name_not_found_request(self) -> None:
        with pytest.raises(Exception, match=http_404_name_details(name=self.name)):
            await http_exc_404_name_not_found_request(name=self.name)

    def tearDown(self) -> None:
        pass
