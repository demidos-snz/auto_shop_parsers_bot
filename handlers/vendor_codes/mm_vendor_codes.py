from aiogram import F
from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from buttons.text_of_buttons import VENDOR_CODES
from markups import results_by_vendor_codes_menu
from utils import get_text

router: Router = Router()


class VendorCodeState(StatesGroup):
    results_by_vendor_code: State = State()
    results_by_all_vendor_codes: State = State()
    needful_vendor_code: State = State()


@router.message(F.text == VENDOR_CODES)
async def mm_vendor_codes(message: Message):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=results_by_vendor_codes_menu.as_markup(resize_keyboard=True),
    )
