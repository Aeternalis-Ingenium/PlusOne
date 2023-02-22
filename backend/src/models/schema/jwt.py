import pydantic

from src.models.schema.base import BaseSchemaModel


class JWToken(BaseSchemaModel):
    expired_at: str
    subject: str


class JWTAccount(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
