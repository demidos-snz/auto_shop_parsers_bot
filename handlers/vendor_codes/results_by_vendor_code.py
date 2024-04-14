from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton, Message,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from buttons.text_of_buttons import (
    NEEDFUL_VENDOR_CODE, VENDOR_CODE_WITH_REPLACEMENTS,
    GET_RESULTS_BY_VENDOR_CODE,
)
from constants import (
    CHOOSE_ONE_OF_VENDOR_CODES, SIZE_LIST_VENDOR_CODES_MENU,
    ERROR_VENDOR_CODES_TEXT,
)
from handlers.utils import get_vendor_codes
from handlers.vendor_codes.mm_vendor_codes import VendorCodeState
from handlers.vendor_codes.vendor_codes import get_result_file
from markups import (
    main_menu_btn, results_by_parsers_menu,
)
from utils import get_text

router: Router = Router()


@router.message(F.text == GET_RESULTS_BY_VENDOR_CODE)
async def results_by_vendor_code(message: Message, state: FSMContext):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=results_by_parsers_menu.as_markup(resize_keyboard=True),
    )

    await state.set_state(VendorCodeState.results_by_vendor_code)


@router.message(
    VendorCodeState.results_by_vendor_code,
    F.text == NEEDFUL_VENDOR_CODE,
)
async def needful_vendor_code(message: Message, state: FSMContext):
    vendor_codes = await get_vendor_codes()

    if vendor_codes:
        await vendor_codes_buttons_list(
            message=message,
            vendor_codes=vendor_codes,
            state=state,
        )
        await state.set_data(data={'only_needful_vendor_code': True})

    else:
        await message.answer(text=ERROR_VENDOR_CODES_TEXT)


@router.message(
    VendorCodeState.results_by_vendor_code,
    F.text == VENDOR_CODE_WITH_REPLACEMENTS,
)
async def vendor_code_with_replacements(message: Message, state: FSMContext):
    vendor_codes: list[str] = await get_vendor_codes()

    if vendor_codes:
        await vendor_codes_buttons_list(
            message=message,
            vendor_codes=vendor_codes,
            state=state,
        )
        await state.set_data(data={'only_needful_vendor_code': False})

    else:
        await message.answer(text=ERROR_VENDOR_CODES_TEXT)


@router.message(
    VendorCodeState.needful_vendor_code,
    F.text,
)
async def get_result_file_by_vendor_code(message: Message, state: FSMContext):
    data: dict[str, bool] = await state.get_data()
    only_needful_vendor_code: bool = data.get('only_needful_vendor_code', False)

    await get_result_file(
        message=message,
        only_needful_vendor_code=only_needful_vendor_code,
    )


async def vendor_codes_buttons_list(message: Message, vendor_codes: list[str], state: FSMContext):
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    _ = [builder.add(KeyboardButton(text=vendor_code)) for vendor_code in vendor_codes]
    builder.adjust(SIZE_LIST_VENDOR_CODES_MENU)
    builder.row(main_menu_btn)
    await message.answer(
        text=CHOOSE_ONE_OF_VENDOR_CODES,
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

    await state.set_state(VendorCodeState.needful_vendor_code)
