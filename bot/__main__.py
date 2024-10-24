import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.config_data import BotConfig, get_config
from bot.handlers import commands_router
from bot.middlewares import TranslatorRunnerMiddleware
from bot.utils import create_translator_hub

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
           "[%(asctime)s] - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    bot_config = get_config(BotConfig, "bot")
    bot = Bot(token=bot_config.token.get_secret_value())

    dp = Dispatcher()

    translator_hub: TranslatorHub = create_translator_hub()

    dp.update.middleware(TranslatorRunnerMiddleware())

    dp.include_router(commands_router)

    setup_dialogs(dp)

    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == "__main__":
    asyncio.run(main())
