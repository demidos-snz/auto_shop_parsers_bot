from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.text_of_buttons import MAIN_MENU
from markups.markups import main_menu as mm
from utils import get_text

router: Router = Router()


@router.message(F.text == MAIN_MENU)
async def main_menu(message: Message, state: FSMContext):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=mm.as_markup(resize_keyboard=True),
    )

    await state.clear()
