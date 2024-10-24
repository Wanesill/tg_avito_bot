import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database import Profile
from bot.database.requests import get_profile

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

logger = logging.getLogger(__name__)
logger.level = logging.INFO

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message, session: AsyncSession, i18n: TranslatorRunner
) -> None:
    telegram_id = message.from_user.id
    profile: Profile = await get_profile(session, telegram_id)

    if profile.is_start:
        logger.info(i18n.logging.new_profile(telegram_id=str(telegram_id)))
        await message.answer(text=i18n.message.start.profile.new())
    else:
        await message.answer(text=i18n.message.start.profile.old())
