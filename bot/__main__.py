import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.config_data import BotConfig, DbConfig, get_config, LoggingConfig, NatsConfig
from bot.dialogs import menu_dialog
from bot.database.requests import test_connection
from bot.handlers import commands_router
from bot.middlewares import (
    DbSessionMiddleware,
    TrackAllUsersMiddleware,
    TranslatorRunnerMiddleware,
)
from bot.storage import NatsStorage
from bot.utils import connect_to_nats, create_translator_hub


logger = logging.getLogger(__name__)


async def main() -> None:
    logging_config = get_config(LoggingConfig, "logging")
    file_log = logging.FileHandler(
        mode=logging_config.filemode, filename=logging_config.filename
    )
    console_out = logging.StreamHandler()
    logging.basicConfig(
        handlers=(console_out,) if logging_config.is_console else (file_log,),
        level=logging_config.level,
        format=logging_config.format,
    )

    bot_config = get_config(BotConfig, "bot")
    bot = Bot(
        token=bot_config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    nats_config = get_config(NatsConfig, "nats")
    nc, js = await connect_to_nats(server=str(nats_config.dsn))
    storage: NatsStorage = await NatsStorage(nc=nc, js=js).create_storage()

    translator_hub: TranslatorHub = create_translator_hub()

    dp = Dispatcher(storage=storage)

    db_config = get_config(DbConfig, "db")
    engine = create_async_engine(
        url=str(db_config.dsn),
        echo=db_config.is_echo,
    )
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    async with sessionmaker() as session:
        await test_connection(session)

    dp.update.outer_middleware(DbSessionMiddleware(sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())
    dp.update.outer_middleware(TranslatorRunnerMiddleware())

    dp.include_router(commands_router)
    dp.include_router(menu_dialog)

    setup_dialogs(dp)

    try:
        await dp.start_polling(bot, _translator_hub=translator_hub)
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
