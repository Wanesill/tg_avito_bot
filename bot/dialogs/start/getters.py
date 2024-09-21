from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_start_bot_message(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
) -> dict[str, str]:
    return {
        "start-bot": (
            i18n.start.profile.new()
            if dialog_manager.start_data["is_new_profile"]
            else i18n.start.profile.old()
        )
    }
