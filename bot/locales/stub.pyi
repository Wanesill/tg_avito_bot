from typing import Literal

class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...

    start: Start

class Start:
    profile: StartProfile

class StartProfile:
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
