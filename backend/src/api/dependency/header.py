import typing

import fastapi
import pydantic

from src.api.dependency.crud import get_crud
from src.config.setup import settings
from src.models.db.accounts.base import Account
from src.models.schema.accounts.base import CurrentAccountInRead
from src.repository.crud.account import AccountCRUDRepository
from src.security.authorizations.jwt import jwt_manager
from src.utility.design_patterns.factory.api_key import get_api_key
from src.utility.enums.api_key import APIKeyTypes
from src.utility.exceptions.custom import EntityDoesNotExist
from src.utility.exceptions.http.exc_403 import http_exc_403_forbidden_request


def get_auth_current_user(*, required: bool = True) -> typing.Callable:
    return _retrieve_current_user if required else _retrieve_optional_current_user


def _get_auth_header_retriever(*, required: bool = True) -> typing.Callable:
    return _retrieve_auth_header if required else _retrieve_optional_auth_header


async def _retrieve_auth_header(api_key: str = fastapi.Security(get_api_key(key_type=APIKeyTypes.HEADER))) -> str:
    try:
        token_prefix, token = api_key.split(" ")
    except ValueError as value_error:
        raise await http_exc_403_forbidden_request() from value_error

    if token_prefix != settings.JWT_TOKEN_PREFIX:
        raise await http_exc_403_forbidden_request()
    return token


async def _retrieve_optional_auth_header(
    api_key: typing.Optional[str] = fastapi.Security(get_api_key(key_type=APIKeyTypes.HEADER, is_auto_error=False))
) -> str:
    if api_key:
        return await _retrieve_auth_header(api_key)
    return ""


async def _retrieve_current_user(
    account_crud: AccountCRUDRepository = fastapi.Depends(get_crud(AccountCRUDRepository)),
    token: str = fastapi.Depends(_get_auth_header_retriever()),
) -> Account:
    try:
        username, email = jwt_manager.retrieve_details_from_jwt(token=token)

    except ValueError as value_error:
        raise await http_exc_403_forbidden_request() from value_error

    try:
        return await account_crud.read_account_by_username_and_email(
            account_retriever=CurrentAccountInRead(username=username, email=pydantic.EmailStr(email))
        )

    except EntityDoesNotExist as value_error:
        raise await http_exc_403_forbidden_request() from value_error


async def _retrieve_optional_current_user(
    account_crud: AccountCRUDRepository = fastapi.Depends(get_crud(AccountCRUDRepository)),
    token: str = fastapi.Depends(_get_auth_header_retriever(required=False)),
) -> Account | None:
    if token:
        return await _retrieve_current_user(account_crud=account_crud, token=token)
    return None
