from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.text_of_buttons import (
    NEEDFUL_VENDOR_CODES, VENDOR_CODES_WITH_REPLACEMENTS,
    GET_RESULTS_BY_ALL_VENDOR_CODES,
)
from handlers.urls import RUN_ALL_URL
from handlers.vendor_codes.mm_vendor_codes import VendorCodeState
from handlers.vendor_codes.utils import send_file_or_error
from markups import results_by_parsers_menu
from utils import get_text

router: Router = Router()


@router.message(
    F.text == GET_RESULTS_BY_ALL_VENDOR_CODES,
)
async def results_by_all_vendor_codes(message: Message, state: FSMContext):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=results_by_parsers_menu.as_markup(resize_keyboard=True),
    )

    await state.set_state(VendorCodeState.results_by_all_vendor_codes)


@router.message(
    VendorCodeState.results_by_all_vendor_codes,
    F.text == NEEDFUL_VENDOR_CODES,
)
async def result_file_needful_vendor_codes(message: Message):
    await send_file_or_error(
        message=message,
        url=RUN_ALL_URL,
        data={'only_needful_vendor_code': True},
    )


@router.message(
    VendorCodeState.results_by_all_vendor_codes,
    F.text == VENDOR_CODES_WITH_REPLACEMENTS,
)
async def result_file_vendor_codes_with_replacements(message: Message):
    await send_file_or_error(
        message=message,
        url=RUN_ALL_URL,
        data={'only_needful_vendor_code': False},
    )
