import datetime
import typing

import pydantic

from src.utility.formatters.date_time import datetime_2_isoformat
from src.utility.formatters.name_case import snake_2_camel


class BaseSchemaModel(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        orm_mode: bool = True
        validate_assignment: bool = True
        allow_population_by_field_name: bool = True
        json_encoders: typing.Dict[type, typing.Callable] = {datetime.datetime: datetime_2_isoformat}
        alias_generator: typing.Callable[[str], str] = snake_2_camel
