import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.config_data import BotConfig, DbConfig, get_config, NatsConfig
from bot.dialogs import start_dialog
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
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
        filemode="w",
        filename="info.log",
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

    dp.update.outer_middleware(DbSessionMiddleware(sessionmaker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())
    dp.update.outer_middleware(TranslatorRunnerMiddleware())

    dp.include_router(commands_router)
    dp.include_router(start_dialog)

    setup_dialogs(dp)

    try:
        await dp.start_polling(bot, _translator_hub=translator_hub)
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
