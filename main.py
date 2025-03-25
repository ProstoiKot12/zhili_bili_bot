import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties

from app.utils.commands import set_commands
from app.user.user_handler import router as us_h_router
from app.user.user_enroll_free_services import router as us_ef_services_router
from app.user.user_enroll_free_old import router as us_ef_old_router
from app.user.user_enroll_free import router as us_ef_router


async def start_bot(bot: Bot):
    load_dotenv()
    await set_commands(bot)
    try:
        await bot.send_message(getenv("ADMIN_IDS").split()[0], text='Бот запущен!')
    except Exception as e:
        print(e)


async def main() -> None:
    load_dotenv()
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.startup.register(start_bot)

    dp.include_router(us_h_router)
    dp.include_router(us_ef_router)
    dp.include_router(us_ef_services_router)
    dp.include_router(us_ef_old_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
