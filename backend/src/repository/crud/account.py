import typing

import pydantic
import sqlalchemy
from sqlalchemy.orm import selectinload as sqlalchemy_selectinload
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.accounts.base import Account
from src.models.schema.accounts.base import (
    AccountInRead,
    AccountInSignin,
    AccountInSignout,
    AccountInSignup,
    AccountInUpdate,
)
from src.repository.crud.base import BaseCRUDRepository
from src.utility.exceptions.custom import EntityDoesNotExist, PasswordDoesNotMatch
from src.utility.typing.account import AccountForInput, AccountRetriever, Accounts


class AccountCRUDRepository(BaseCRUDRepository):
    async def create_account(self, account_signup: AccountInSignup) -> Account:
        new_account = Account(**account_signup.dict(exclude={"password"}))
        new_account.hashed_salt, new_account.hashed_password = new_account.set_password(
            password=account_signup.password
        )

        self.async_session.add(instance=new_account)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_account)
        await self.async_session.close()

        return new_account

    async def _is_username_available(self, username: str) -> bool:
        select_stmt = sqlalchemy.select(Account.username).select_from(Account).where(Account.username == username)
        query = await self.async_session.execute(select_stmt)
        db_username = query.scalar()
        if db_username:
            return False
        return True

    async def _is_email_available(self, email: str) -> bool:
        select_stmt = sqlalchemy.select(Account.email).select_from(Account).where(Account.email == email)
        query = await self.async_session.execute(select_stmt)
        db_email = query.scalar()
        if db_email:
            return False
        return True

    async def is_credentials_available(self, account_input: AccountForInput) -> bool:
        if account_input.email:
            is_email_available = await self._is_email_available(email=account_input.email)
            if not is_email_available:
                return False

        if account_input.username:
            is_username_taken = await self._is_username_available(username=account_input.username)
            if not is_username_taken:
                return False

        if not account_input.email and not account_input.username:
            return False
        return True

    async def read_accounts(self) -> Accounts:
        select_stmt = sqlalchemy.select(Account).options(sqlalchemy_selectinload("*"))
        query = await self.async_session.execute(statement=select_stmt)
        return query.scalars().all()

    async def _read_account_by_id(self, id: int) -> Account:
        select_stmt = sqlalchemy.select(Account).where(Account.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        if not query:
            raise EntityDoesNotExist(f"Account with id `{id}` does not exist!")
        return query.scalar()  # type: ignore

    async def _read_account_by_username(self, username: str) -> Account:
        select_stmt = sqlalchemy.select(Account).where(Account.username == username)
        query = await self.async_session.execute(statement=select_stmt)
        if not query:
            raise EntityDoesNotExist(f"Account with username `{username}` does not exist!")
        return query.scalar()  # type: ignore

    async def _read_account_by_email(self, email: pydantic.EmailStr) -> Account:
        select_stmt = sqlalchemy.select(Account).where(Account.email == email)
        query = await self.async_session.execute(statement=select_stmt)
        if not query:
            raise EntityDoesNotExist(f"Account with email `{email}` does not exist!")
        return query.scalar()  # type: ignore

    async def read_account_by_username_and_email(self, account_retriever: AccountRetriever) -> Account:
        select_stmt = (
            sqlalchemy.select(Account)
            .where(Account.username == account_retriever.username, Account.email == account_retriever.email)
            .options(sqlalchemy_selectinload("*"))
        )
        query = await self.async_session.execute(statement=select_stmt)
        if not query:
            raise EntityDoesNotExist(
                f"Account with username `{account_retriever.username}` and email {account_retriever.email} does not exist!"
            )
        return query.scalar()  # type: ignore

    async def read_specific_accounts(self, account_read: AccountInRead) -> Accounts:
        db_accounts: list[Account] = list()

        if account_read.id:
            db_account = await self._read_account_by_id(id=account_read.id)
            db_accounts.append(db_account)
        if account_read.email:
            db_account = await self._read_account_by_email(email=account_read.email)
            db_accounts.append(db_account)
        if account_read.username:
            db_account = await self._read_account_by_username(username=account_read.username)
            db_accounts.append(db_account)
        return set(db_accounts)

    async def update_account_by_id(self, id: int, account_update: AccountInUpdate) -> Account:
        update_data = account_update.dict(exclude_unset=True)
        db_account = await self._read_account_by_id(id=id)

        if not db_account:
            raise EntityDoesNotExist(f"Account with id `{id}` does not exist!")  # type: ignore

        update_stmt = sqlalchemy.update(table=Account).where(Account.id == db_account.id).values(updated_at=sqlalchemy_functions.now())  # type: ignore

        if update_data["username"]:
            update_stmt = update_stmt.values(username=update_data["username"])
        if update_data["email"]:
            update_stmt = update_stmt.values(email=update_data["email"])
        if update_data["password"]:
            salt, password = db_account.set_password(password=update_data["password"])
            update_stmt = update_stmt.values(hashed_salt=salt, hashed_password=password)

        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=db_account)
        return db_account

    async def delete_account_by_id(self, id: int) -> bool:
        db_account = await self._read_account_by_id(id=id)

        if not db_account:
            raise EntityDoesNotExist(f"Account with id `{id}` does not exist!")

        delete_stmt = sqlalchemy.delete(table=Account).where(Account.id == db_account.id)
        await self.async_session.execute(statement=delete_stmt)
        await self.async_session.commit()
        return True

    async def signin_account(self, account_signin: AccountInSignin) -> Account:
        db_account = await self.read_account_by_username_and_email(account_retriever=account_signin)

        if not db_account:
            raise EntityDoesNotExist("Wrong username or wrong email!")

        if not db_account.is_password_verified(password=account_signin.password):
            raise PasswordDoesNotMatch("Password does not match! Please try again.")

        update_stmt = sqlalchemy.update(table=Account).where(Account.id == db_account.id).values(is_logged_in=True)
        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=db_account)
        await self.async_session.close()
        return db_account

    async def signout_account(self, account_signout: AccountInSignout) -> Account:
        db_account = await self._read_account_by_id(id=account_signout.id)
        update_stmt = sqlalchemy.update(table=Account).where(Account.id == db_account.id).values(is_logged_in=False)
        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=db_account)
        return db_account
