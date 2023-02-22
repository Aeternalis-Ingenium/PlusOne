import unittest

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


class TestHTTPExceptionDetails(unittest.TestCase):
    def setUp(self) -> None:
        self.http_400_bad_request_details = http_400_bad_request_details()
        self.http_400_email_details = http_400_email_details(email="test.email1@exception.com")
        self.http_400_sigin_credentials_details = http_400_signin_credentials_details()
        self.http_400_signup_credentials_details = http_400_signup_credentials_details()
        self.http_400_username_details = http_400_username_details(username="testusername1")
        self.http_401_unauthorized_details = http_401_unauthorized_details()
        self.http_403_forbidden_details = http_403_forbidden_details()
        self.http_404_email_details = http_404_email_details(email="test.email2@exception.com")
        self.http_404_id_details = http_404_id_details(id=1)
        self.http_404_name_details = http_404_name_details(name="testusername2")
        self.http_404_username_details = http_404_username_details(username="testusername3")

    async def test_http_400_exc_bad_request_message(self) -> None:
        assert self.http_400_bad_request_details == "Bad request!"

    async def test_http400_exc_for_taken_email_message(self) -> None:
        assert "test.email1@exception.com" in self.http_400_email_details

    async def test_http_400_exc_for_taken_username_message(self) -> None:
        assert "testusername1" in self.http_400_username_details

    async def test_http_404_exc_for_not_found_email_message(self) -> None:
        assert "test.email2@exception.com" in self.http_404_email_details

    async def test_http_404_exc_for_not_found_username_message(self) -> None:
        assert "testusername3" in self.http_404_username_details

    async def test_http_400_exc_failed_signup_message(self) -> None:
        assert "Signup failed!" in self.http_400_signup_credentials_details

    async def test_http_400_exc_failed_signin_message(self) -> None:
        assert "Signin failed!" in self.http_400_sigin_credentials_details

    async def test_http_401_exc_unauthorized_request_message(self) -> None:
        assert "Refused to complete request" in self.http_401_unauthorized_details

    async def test_http_403_exc_forbidden_request_message(self) -> None:
        assert "Refused access" in self.http_403_forbidden_details

    async def test_http_404_exc_for_not_found_id_message(self) -> None:
        assert "1" in self.http_404_id_details

    async def test_http_404_exc_for_not_found_entity_name_message(self) -> None:
        assert "testusername2" in self.http_404_name_details

    def tearDown(self):
        pass
