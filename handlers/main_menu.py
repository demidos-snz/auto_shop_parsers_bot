from aiogram import Router, F
from aiogram.types import Message

from constants import BASE_TEXT, PARAMS
from markups import main_menu
from text_of_buttons import MAIN_MENU


router: Router = Router()


@router.message(F.text == MAIN_MENU)
async def get_main_menu(message: Message):
    # fixme delete Params
    user_id: int = message.from_user.id

    if user_id in PARAMS:
        PARAMS[user_id].clear()
    else:
        PARAMS[user_id] = []

    await message.answer(text=BASE_TEXT, reply_markup=main_menu.as_markup(resize_keyboard=True))
