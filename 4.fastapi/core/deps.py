from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    seesion: AsyncSession = Session()

    try:
        yield seesion
    finally:
        await seesion.close()