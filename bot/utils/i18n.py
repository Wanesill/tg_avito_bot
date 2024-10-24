from fluentogram import FluentTranslator, TranslatorHub
from fluent_compiler.bundle import FluentBundle


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        locales_map={
            "ru": "ru",
        },
        translators=[
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU", filenames=["bot/locales/ru/LC_MESSAGES/txt.ftl"]
                ),
            ),
        ],
        root_locale="ru",
    )
    return translator_hub
