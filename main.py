import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import (
    commands,
    main_menu as mm_handler,
    # parsers,
    vendor_codes,
    reports,
)

try:
    from settings import TELEGRAM_TOKEN
except ImportError:
    exit('copy settings.py.default settings.py and set TELEGRAM_TOKEN')


logging.basicConfig(level=logging.INFO)


async def main() -> None:
    bot: Bot = Bot(
        token=TELEGRAM_TOKEN,
    )
    dp: Dispatcher = Dispatcher(
        storage=MemoryStorage(),
    )

    dp.include_routers(
        commands.router,
        mm_handler.router,
        # parsers.router,
        reports.reports.router,
        reports.download.router,
        vendor_codes.mm_vendor_codes.router,
        vendor_codes.list_vendor_codes.router,
        # vendor_codes.results_by_vendor_code.router,
        # vendor_codes.results_by_all_vendor_codes.router,
        # vendor_codes.vendor_codes.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
