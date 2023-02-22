import typing
import unittest

from src.models.db.accounts.base import Account
from src.security.hashing.algorithms import Argon2Algorithm, BCryptAlgorithm, SHA256Algorithm, SHA512Algorithm
from src.utility.typing.account import Accounts
from src.utility.typing.algorithm import HashingAlgorithmSubClass


class TestHashingAlgorithmCustomType(unittest.TestCase):
    def setUp(self) -> None:
        self.argon2 = Argon2Algorithm()
        self.bcrypt = BCryptAlgorithm()
        self.sha256 = SHA256Algorithm()
        self.sha512 = SHA512Algorithm()

    async def test_acceptance_type_for_argon2(self) -> None:
        assert isinstance(self.argon2, HashingAlgorithmSubClass)  # type: ignore

    async def test_acceptance_type_for_bcrypt(self) -> None:
        assert isinstance(self.bcrypt, HashingAlgorithmSubClass)  # type: ignore

    async def test_acceptance_type_for_hsa256(self) -> None:
        assert isinstance(self.sha256, HashingAlgorithmSubClass)  # type: ignore

    async def test_acceptance_type_for_hsa512(self) -> None:
        assert isinstance(self.sha512, HashingAlgorithmSubClass)  # type: ignore

    def tearDown(self):
        pass


class TestAccountType(unittest.TestCase):
    def setUp(self) -> None:
        pass

    async def test_acceptance_type_accounts_for_sequence_of_account(self) -> None:
        assert isinstance(typing.Sequence[Account], type(Accounts))

    async def test_acceptance_type_accounts_for_list_of_account(self) -> None:
        assert isinstance(list[Account], type(Accounts))

    async def test_acceptance_type_accounts_for_set_of_account(self) -> None:
        assert isinstance(set[Account], type(Accounts))

    def tearDown(self):
        pass
