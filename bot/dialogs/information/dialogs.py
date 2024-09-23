from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Format

from bot.dialogs.information.getters import information_getter
from bot.states import InformationSG

information_dialog = Dialog(
    Window(
        Format("{message_information}"),
        Cancel(text=Format("{button_menu}"), id="menu"),
        getter=information_getter,
        state=InformationSG.information,
    ),
)
