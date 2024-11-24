from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.text_of_buttons import (
    NEEDFUL_VENDOR_CODE, VENDOR_CODE_WITH_REPLACEMENTS,
)
from constants.constants import (
    CHOOSE_ONE_OF_VENDOR_CODES, ERROR_VENDOR_CODES_TEXT,
)
from handlers.utils import get_vendor_codes, generate_custom_buttons_list
from handlers.vendor_codes.mm_vendor_codes import VendorCodeState
from handlers.vendor_codes.vendor_codes import get_result_file

router: Router = Router()


# @router.message(F.text == GET_RESULTS_BY_VENDOR_CODE)
# async def results_by_vendor_code(message: Message, state: FSMContext):
#     await message.answer(
#         text=get_text(message_text=message.text),
#         reply_markup=results_by_parsers_menu.as_markup(resize_keyboard=True),
#     )
#
#     await state.set_state(VendorCodeState.results_by_vendor_code)


@router.message(
    VendorCodeState.results_by_vendor_code,
    F.text == NEEDFUL_VENDOR_CODE,
)
async def needful_vendor_code(message: Message, state: FSMContext):
    vendor_codes = await get_vendor_codes()

    if vendor_codes:
        await generate_custom_buttons_list(
            message=message,
            list_objs=vendor_codes,
            answer_text=CHOOSE_ONE_OF_VENDOR_CODES,
        )

        await state.set_state(VendorCodeState.needful_vendor_code)
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
        await generate_custom_buttons_list(
            message=message,
            list_objs=vendor_codes,
            answer_text=CHOOSE_ONE_OF_VENDOR_CODES,
        )

        await state.set_state(VendorCodeState.needful_vendor_code)
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
