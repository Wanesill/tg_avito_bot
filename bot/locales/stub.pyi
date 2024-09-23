from typing import Literal

class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...

    button: Button
    message: Message

class Button:
    @staticmethod
    def accounts() -> Literal["""Список аккаунтов"""]: ...
    @staticmethod
    def add_account() -> Literal["""Добавить аккаунт"""]: ...
    @staticmethod
    def information() -> Literal["""Информация"""]: ...
    @staticmethod
    def buy_account_slot() -> Literal["""Купить слот"""]: ...
    @staticmethod
    def chat_support() -> Literal["""👨‍🔧 Чат поддержки"""]: ...

class Message:
    start: MessageStart

    @staticmethod
    def menu(
        *, count_account_slots, count_activate_accounts
    ) -> Literal[
        """Количество слотов: { $count_account_slots }
Количество активированных аккаунтов: { $count_activate_accounts }"""
    ]: ...

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
