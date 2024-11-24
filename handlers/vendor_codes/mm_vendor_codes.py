import io
import typing as t

import openpyxl
from aiogram import F
from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (
    Document,
)
from aiogram.types import Message
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from buttons.text_of_buttons import VENDOR_CODES
from handlers.utils import get_vendor_codes, create_vendor_code, delete_vendor_code
from markups.markups import list_vendor_codes_menu
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
        reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.document.file_name.endswith('.xlsx'))
async def get_list_parsers_menu_(message: Message):
    document: Document = message.document
    file_bytes: io.BytesIO = await message.document.bot.download(file=document)
    wb: Workbook = openpyxl.load_workbook(filename=file_bytes)

    # only first sheet
    sheet: Worksheet = wb.worksheets[0]
    # without header row
    min_row: int = 2
    # only first ... columns
    count_columns: int = 2
    excel_rows: list[tuple[str, t.Any]] = list(
        {
            row[:count_columns] for row in sheet.iter_rows(values_only=True, min_row=min_row)
        }
    )
    result: dict[str, list[tuple[str, str]]] = {
        'set_of_vendor_codes': excel_rows,
    }
    vendor_codes = await get_vendor_codes()
    data: list[int] | list = [set_of_vc.get('id', 0) for set_of_vc in vendor_codes]
    id_vc: int = data[0] if data else 0

    if id_vc:
        status_code = await delete_vendor_code(id_vc=id_vc)
    else:
        ...
        print('1')
        status_code = 400

    if status_code == 200:
        status_code = await create_vendor_code(data=result)
    else:
        ...
        print('2')

    if status_code == 201:
        await message.answer(text='Список артикулов обновлён')
    else:
        await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')
    #
    # # fixme
    # good_vendor_codes: list[str] = []
    # good_makers: list[str] = []
    # bad_vendor_codes: list[str] = []
    #
    # for maker, vendor_code in result['data']:
    #     if str(vendor_code) in vendor_codes:
    #         good_vendor_codes.append(str(vendor_code))
    #         good_makers.append(str(maker).lower())
    #     else:
    #         bad_vendor_codes.append(vendor_code)
    #
    # if bad_vendor_codes:
    #     # fixme text
    #     await message.answer(text=f'{bad_vendor_codes} not fount in global list')
    #
    # # fixme asyncio
    # response: requests.Response = requests.post(
    #     url=RUN_ALL_PAIR_DATA_URL,
    #     json={
    #         'vendor_codes': good_vendor_codes,
    #         'makers': good_makers,
    #         # fixme
    #         'only_needful_vendor_code': False,
    #     },
    # )
    #
    # if response.ok:
    #     response: list[str] = response.json()
    # else:
    #     await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')
    # if response:
    #     result_filepath: str = os.path.join(response[0])
    #     document: FSInputFile = FSInputFile(path=result_filepath)
    #
    #     await message.answer_document(document=document, caption='Результат выполнения запроса')
    # else:
    #     await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')
