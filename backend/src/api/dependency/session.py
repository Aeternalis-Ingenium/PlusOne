import typing

from sqlalchemy.ext.asyncio import (
    async_sessionmaker as sqlalchemy_async_sessionmaker,
    AsyncSession as SQLAlchemyAsyncSession,
)

from src.repository.database import db


async def get_async_session() -> typing.AsyncGenerator[sqlalchemy_async_sessionmaker[SQLAlchemyAsyncSession], None]:
    try:
        yield db.async_session
    except Exception as e:
        print(e)
        await db.async_session().rollback()
    finally:
        await db.async_session().close()
