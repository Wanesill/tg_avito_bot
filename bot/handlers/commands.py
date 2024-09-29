import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode, StartMode
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database import Profile
from bot.database.requests import get_profile, insert_account_slots
from bot.states import MenuSG

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

logger = logging.getLogger(__name__)
logger.level = logging.INFO

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message,
    session: AsyncSession,
    i18n: TranslatorRunner,
) -> None:
    profile: Profile = await get_profile(session, message.from_user.id)

    if profile.is_start and not profile.account_slots:
        await insert_account_slots(session, profile, 1)
        logger.info(f"Создан новый профиль: {message.from_user.id}")
        await message.answer(text=i18n.message.start.profile.new())
    else:
        await message.answer(text=i18n.message.start.profile.old())


@commands_router.message(Command("menu"))
async def process_menu_command(
    message: Message,
    dialog_manager: DialogManager,
    session: AsyncSession,
) -> None:
    profile: Profile = await get_profile(session, message.from_user.id)
    count_account_slots = len(profile.account_slots)
    count_activate_accounts = len(
        [account_slot for account_slot in profile.account_slots if account_slot.account]
    )

    await dialog_manager.start(
        state=MenuSG.menu,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND,
        data={
            "count_account_slots": count_account_slots,
            "count_activate_accounts": count_activate_accounts,
        },
    )


@commands_router.message(Command("cancel"))
async def process_cancel_command(
    message: Message,
    dialog_manager: DialogManager,
) -> None:
    await dialog_manager.done(show_mode=ShowMode.DELETE_AND_SEND)
