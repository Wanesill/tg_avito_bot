from aiogram.fsm.state import State, StatesGroup


class MenuSG(StatesGroup):
    menu = State()
    information = State()
