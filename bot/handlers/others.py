from aiogram import Bot, Router
from aiogram.types import Message


others_router = Router()


@others_router.message()
async def process_delete_other_message(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)