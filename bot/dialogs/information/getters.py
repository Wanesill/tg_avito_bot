from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner


if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def information_getter(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
) -> dict[str, str]:
    return {
        "message_information": i18n.message.information(),
        "button_menu": i18n.button.menu(),
    }
