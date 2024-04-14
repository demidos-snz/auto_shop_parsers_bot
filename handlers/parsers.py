from aiogram import F
from aiogram import Router
from aiogram.types import Message

from buttons.text_of_buttons import (
    GET_RESULTS_BY_PARSER, GET_RESULTS_BY_ALL_PARSERS,
    PARSERS, GET_PARSERS,
    UPDATE_PARSERS,
)
from constants import IN_DEVELOPING, PARSES_LIST_IS_EMPTY
from handlers.utils import get_parsers
from handlers.vendor_codes.mm_vendor_codes import VendorCodeState
from markups import (
    list_parsers_menu, needful_or_replacements_vendor_code_menu,
    needful_or_replacements_vendor_codes_menu,
)
from utils import get_text

router: Router = Router()


@router.message(F.text == PARSERS)
async def mm_parsers(message: Message):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=list_parsers_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == GET_RESULTS_BY_PARSER)
async def results_by_parser(message: Message):
    await message.answer(text=IN_DEVELOPING)


@router.message(
    VendorCodeState.results_by_vendor_code,
    F.text == GET_RESULTS_BY_ALL_PARSERS,
)
async def results_for_all_parsers_by_vendor_code(message: Message):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=needful_or_replacements_vendor_code_menu.as_markup(resize_keyboard=True),
    )


@router.message(
    VendorCodeState.results_by_all_vendor_codes,
    F.text == GET_RESULTS_BY_ALL_PARSERS,
)
async def results_for_all_parsers_by_all_vendor_codes(message: Message):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=needful_or_replacements_vendor_codes_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == GET_PARSERS)
async def parsers_list(message: Message):
    parsers = await get_parsers()

    text: str = '\n'.join(parsers)

    await message.answer(
        text=text or PARSES_LIST_IS_EMPTY,
        reply_markup=list_parsers_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == UPDATE_PARSERS)
async def update_parsers(message: Message):
    await message.answer(text=IN_DEVELOPING)
