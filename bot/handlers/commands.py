import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database import Profile
from bot.database.requests import get_profile, insert_account_slots
from bot.states import StartSG

logger = logging.getLogger(__name__)

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message, dialog_manager: DialogManager, session: AsyncSession
) -> None:
    profile: Profile = await get_profile(session, message.from_user.id)

    if profile.is_start and not profile.account_slots:
        await insert_account_slots(session, profile, 1)

        logger.info(f"Создан новый профиль: {message.from_user.id}")

        is_new_profile = True
    else:
        is_new_profile = False

    await dialog_manager.start(
        state=StartSG.start,
        mode=StartMode.RESET_STACK,
        data={"is_new_profile": is_new_profile},
    )
