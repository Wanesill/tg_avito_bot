from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

commands_router = Router()

@commands_router.message(CommandStart())
async def process_start_command(message: Message, i18n: TranslatorRunner) -> None:
    await message.answer(i18n.message.start.profile.new())
