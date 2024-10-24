from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    message: Message


class Message:
    start: MessageStart


class MessageStart:
    profile: MessageStartProfile


class MessageStartProfile:
    @staticmethod
    def new() -> Literal["""Приветствую вас в боте AIX Avito Bot

Вам был выдан 1 слот под аккаунт c пробным периодом на 3 дня

Для перехода в главное меню бота введите: /menu"""]: ...

