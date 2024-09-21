from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from bot.dialogs.start.getters import get_start_bot_message
from bot.states import StartSG

start_dialog = Dialog(
    Window(
        Format("{start-bot}"),
        getter=get_start_bot_message,
        state=StartSG.start,
    ),
)
