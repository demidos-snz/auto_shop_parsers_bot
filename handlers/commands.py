from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from constants.constants import BASE_TEXT, WELCOME_TEXT
from markups.markups import main_menu

router: Router = Router()


@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(
        text=WELCOME_TEXT.format(message.from_user.first_name),
        reply_markup=main_menu.as_markup(resize_keyboard=True),
    )


@router.message(Command('help'))
async def start_command(message: Message):
    await message.answer(
        text=BASE_TEXT,
        reply_markup=main_menu.as_markup(resize_keyboard=True),
    )
