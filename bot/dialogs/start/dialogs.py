from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group
from aiogram_dialog.widgets.text import Format

from bot.dialogs.start.getters import get_information_for_menu
from bot.states import MenuSG

menu_dialog = Dialog(
    Window(
        Format("{message_menu}"),
        Group(
            Button(Format("{button_accounts}"), id="accounts"),
            Button(Format("{button_add_account}"), id="add_account"),
            Button(Format("{button_information}"), id="information"),
            Button(Format("{button_buy_account_slot}"), id="buy_account_slot"),
            Button(Format("{button_chat_support}"), id="chat_support"),
            width=2,
        ),
        getter=get_information_for_menu,
        state=MenuSG.main_menu,
    ),
)
