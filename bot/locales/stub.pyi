from typing import Literal

class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...

    logging: Logging
    message: Message

class Logging:
    @staticmethod
    def new_profile(
        *, telegram_id
    ) -> Literal["""Создан новый профиль: { $telegram_id }"""]: ...

class Message:
    start: MessageStart

class MessageStart:
    profile: MessageStartProfile

class MessageStartProfile:
    @staticmethod
    def new() -> (
        Literal[
            """Приветствую вас в боте AIX Avito Bot

Вам был выдан 1 слот под аккаунт c пробным периодом на 3 дня

Для перехода в главное меню бота введите: /menu"""
        ]
    ): ...
    @staticmethod
    def old() -> (
        Literal[
            """У вас уже есть/был пробный период на слот аккаунта

Для перехода в главное меню бота введите: /menu"""
        ]
    ): ...
