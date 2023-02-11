import datetime
import unittest

from src.utilities.formatters.date_time import datetime_2_isoformat
from src.utilities.formatters.name_case import any_2_snake, snake_2_camel, snake_2_pascal


class TestFormatters(unittest.TestCase):
    def setUp(self) -> None:
        self.nonisoformat_datetime = datetime.datetime(year=2023, month=2, day=10)
        self.isoformat_datetime = "2023-02-10T00:00:00Z"
        self.snake_case_var_1 = "test_name_case"
        self.snake_case_var_2 = "any_name_case"
        self.any_case_var_1 = "AnyCaseName"
        self.any_case_var_2 = "anyCaseName"
        self.any_case_var_3 = "any-case-name"
        self.camel_case = "testNameCase"
        self.pascal_case = "TestNameCase"

    async def test_datetime_2_isoformat_formatter(self) -> None:
        assert datetime_2_isoformat(date_time=self.nonisoformat_datetime) == self.isoformat_datetime

    async def test_snake_2_camel_formatter(self) -> None:
        assert snake_2_camel(var=self.snake_case_var_1) == self.camel_case

    async def test_snake_2_pascal_formatter(self) -> None:
        assert snake_2_pascal(var=self.snake_case_var_1) == self.pascal_case

    async def test_any_2_snake_formatter(self) -> None:
        assert any_2_snake(var=self.any_case_var_1) == self.snake_case_var_2
        assert any_2_snake(var=self.any_case_var_2) == self.snake_case_var_2
        assert any_2_snake(var=self.any_case_var_3) == self.snake_case_var_2

    def tearDown(self):
        pass
