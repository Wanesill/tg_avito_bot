from typing import Literal

class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...

    button: Button
    message: Message

class Button:
    @staticmethod
    def menu() -> Literal["""Главное меню"""]: ...
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
    @staticmethod
    def information() -> (
        Literal[
            """❓ Что умеет этот бот:
⁃ Автоответ по определенным триггерным словам которые вы назначите
⁃ Либо отвечать на все сообщения (без триггерного слова)
⁃ Отвечать только на первое сообщение или на все
⁃ Под каждый аккаунт вы создаёте отдельный чат/группу и назначаете приход сообщений в конкретный чат от конкретного аккаунта (это позволит не смешивать чаты из разных аккаунтов и не путаться)
⁃ Неограниченное количество текста в автоответе (в 1 сообщении можно поместить до 1000 символов, но если вам нужно использовать более 1000 символов можно создать цепочку из нескольких сообщений в неограниченном количестве)
⁃ История прошлых сообщений чата вглубь до 5 прошлых сообщений (системные сообщения от авито не учитываются)
⁃ Отправка сообщений через чат телеграмм смахиванием влево в чат Авито"""
        ]
    ): ...

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
