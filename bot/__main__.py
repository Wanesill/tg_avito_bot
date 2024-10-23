import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from bot.config_data import BotConfig, get_config


logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    bot_config = get_config(BotConfig, "bot")
    bot = Bot(token=bot_config.token.get_secret_value())

    dp = Dispatcher()

    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
