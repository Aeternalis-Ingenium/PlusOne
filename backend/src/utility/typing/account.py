import typing

from src.models.db.accounts.base import Account
from src.models.schema.accounts.base import AccountInSignin, AccountInSignup, AccountInUpdate, CurrentAccountInRead

Accounts = typing.Sequence[Account] | list[Account] | set[Account]
AccountRetriever = AccountInSignin | CurrentAccountInRead
AccountForInput = AccountInSignup | AccountInUpdate
