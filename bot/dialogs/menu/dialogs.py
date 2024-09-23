from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group, SwitchTo, Url
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.menu.getters import information_getter, menu_getter
from bot.dialogs.menu.handlers import (
    process_accounts_press,
    process_add_account_press,
    process_buy_account_slot_press,
)
from bot.states import MenuSG

menu_dialog = Dialog(
    Window(
        Format("{message_menu}"),
        Group(
            Button(
                text=Format("{button_accounts}"),
                id="accounts",
                on_click=process_accounts_press,
            ),
            Button(
                text=Format("{button_add_account}"),
                id="add_account",
                on_click=process_add_account_press,
            ),
            SwitchTo(
                text=Format("{button_information}"),
                id="information",
                state=MenuSG.information,
            ),
            Button(
                text=Format("{button_buy_account_slot}"),
                id="buy_account_slot",
                on_click=process_buy_account_slot_press,
            ),
            Url(
                text=Format("{button_chat_support}"),
                url=Const("https://t.me/lev_yalovega"),
                id="chat_support",
            ),
            width=2,
        ),
        getter=menu_getter,
        state=MenuSG.menu,
    ),
    Window(
        Format("{message_information}"),
        SwitchTo(text=Format("{button_menu}"), id="menu", state=MenuSG.menu),
        getter=information_getter,
        state=MenuSG.information,
    ),
)
