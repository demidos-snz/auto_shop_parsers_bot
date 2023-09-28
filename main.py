import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import (
    commands,
    main_menu as main_menu_handler,
    parsers,
    vendor_codes,
)

try:
    from settings import TELEGRAM_TOKEN, FILEPATH_EXAMPLE_VENDOR_CODES
except ImportError:
    exit('copy settings.py.default settings.py and set TELEGRAM_TOKEN')


logging.basicConfig(level=logging.INFO)


async def main() -> None:
    bot: Bot = Bot(token=TELEGRAM_TOKEN)
    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        commands.router,
        main_menu_handler.router,
        parsers.router,
        vendor_codes.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
