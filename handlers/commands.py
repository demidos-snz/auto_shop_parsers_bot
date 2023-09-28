from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from constants import PARAMS
from markups import main_menu

router: Router = Router()


# fixme help new def
@router.message(Command('start', 'help'))
async def example_bot_operation(message: Message):
    # fixme delete Params
    PARAMS[message.from_user.id] = []
    text: str = f'Привет, {message.from_user.first_name}!'
    await message.answer(text=text, reply_markup=main_menu.as_markup(resize_keyboard=True))
