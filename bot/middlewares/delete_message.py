from typing import Any, Awaitable, Callable, cast, Dict, Optional

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from aiogram_dialog.api.entities import Context

from bot.states import AccountAdditionSG


class DeleteMessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        event = cast(Message, event)

        if event.text in ["/menu", "/start"]:
            await event.bot.delete_message(
                chat_id=event.chat.id, message_id=event.message_id
            )
            return await handler(event, data)

        dialog_context: Optional[Context] = data.get("aiogd_context")

        if event.text == "/cancel":
            if dialog_context and dialog_context.state.group == AccountAdditionSG:
                await event.bot.delete_message(
                    chat_id=event.chat.id, message_id=event.message_id
                )
                return await handler(event, data)

        if dialog_context and dialog_context.state.group == AccountAdditionSG:
            return await handler(event, data)

        await event.bot.delete_message(
            chat_id=event.chat.id, message_id=event.message_id
        )
