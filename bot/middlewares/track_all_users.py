from typing import Any, Awaitable, Callable, cast, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from cachetools import TTLCache
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.requests import upsert_user


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 6,
        )

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        event = cast(Message, event)
        user_id = event.from_user.id

        if user_id not in self.cache:
            session: AsyncSession = data["session"]

            await upsert_user(
                session=session,
                telegram_id=user_id,
                telegram_username=event.from_user.username,
            )

            self.cache[user_id] = None

        return await handler(event, data)
