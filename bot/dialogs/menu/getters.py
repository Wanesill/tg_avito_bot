from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner


if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_information_for_menu(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
) -> dict[str, str]:
    count_account_slots = dialog_manager.start_data["count_account_slots"]
    count_activate_accounts = dialog_manager.start_data["count_activate_accounts"]

    return {
        "message_menu": i18n.message.menu(
            count_account_slots=count_account_slots,
            count_activate_accounts=count_activate_accounts,
        ),
        "button_accounts": i18n.button.accounts(),
        "button_add_account": i18n.button.add_account(),
        "button_information": i18n.button.information(),
        "button_buy_account_slot": i18n.button.buy_account_slot(),
        "button_chat_support": i18n.button.chat_support(),
    }
