import io
import os
import tempfile
import typing as t

import openpyxl
import requests
from aiogram import F
from aiogram import Router
from aiogram.types import (
    Message, FSInputFile,
    Document, BufferedInputFile,
)
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from buttons.text_of_buttons import (
    LIST_VENDOR_CODES, GET_LIST_VENDOR_CODES_MESSAGE,
    GET_LIST_VENDOR_CODES_FILE, UPDATE_LIST_VENDOR_CODES,
)
from constants.constants import (
    EXAMPLE_VENDOR_CODES, VENDOR_CODE_NOT_EXISTS_IN_LIST_VENDOR_CODES, LIST_VENDOR_CODES_IS_EMPTY_TEXT,
    LIST_VENDOR_CODES_FILENAME, LIST_VENDOR_CODES_UPDATED_TEXT, ERROR_UPDATE_LIST_VENDOR_CODES_TEXT,
    UPDATE_LIST_VENDOR_CODES_TEXT, ERROR_OF_ANOTHER_DOCUMENT_TYPE,
)
from handlers.urls import VENDOR_CODES_URL, RUN_URL, RUN_ALL_PAIR_DATA_URL
from handlers.utils import get_vendor_codes
from markups import list_vendor_codes_menu
from utils import get_text

router: Router = Router()


@router.message(F.text == LIST_VENDOR_CODES)
async def list_vendor_codes(message: Message):
    await message.answer(
        text=get_text(message_text=message.text),
        reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == GET_LIST_VENDOR_CODES_MESSAGE)
async def list_vendor_codes_message(message: Message):
    vendor_codes = await get_vendor_codes()

    text: str = '\n'.join(vendor_codes)

    await message.answer(
        text=text or LIST_VENDOR_CODES_IS_EMPTY_TEXT,
        reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == GET_LIST_VENDOR_CODES_FILE)
async def list_vendor_codes_file(message: Message):
    vendor_codes = await get_vendor_codes()

    text: str = '\n'.join(vendor_codes)

    if text:
        with tempfile.TemporaryFile() as f:
            f.write(bytes(text, encoding='cp1251'))
            f.seek(0)
            vendor_codes_list: BufferedInputFile = BufferedInputFile(
                file=f.read(),
                filename=LIST_VENDOR_CODES_FILENAME,
            )

            await message.answer_document(document=vendor_codes_list)

    else:
        await message.answer(
            text=LIST_VENDOR_CODES_IS_EMPTY_TEXT,
            reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
        )


@router.message(F.document.file_name.endswith('.txt'))
async def update_list_vendor_code(message: Message):
    document: Document = message.document
    file_bytes: io.BytesIO = await message.document.bot.download(file=document)
    result: str = file_bytes.getvalue().decode()

    result: dict[str, list[str]] = {'data': [row.strip() for row in result.split('\n') if row]}

    # fixme asyncio
    response: requests.Response = requests.post(
        url=VENDOR_CODES_URL,
        json=result,
    )

    if response.ok:
        await message.answer(
            text=LIST_VENDOR_CODES_UPDATED_TEXT,
            reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
        )
    else:
        await message.answer(text=ERROR_UPDATE_LIST_VENDOR_CODES_TEXT)


@router.message(F.text == UPDATE_LIST_VENDOR_CODES)
async def update_list_vendor_code_answer(message: Message):
    await message.answer_document(
        document=EXAMPLE_VENDOR_CODES,
        caption=UPDATE_LIST_VENDOR_CODES_TEXT,
    )


@router.message(F.document)
async def error_another_document_type(message: Message):
    await message.answer(text=ERROR_OF_ANOTHER_DOCUMENT_TYPE)


# fixme name, unused???
@router.message(F.document.file_name.endswith('.xlsx'))
async def get_list_parsers_menu_(message: Message):
    document: Document = message.document
    file_bytes: io.BytesIO = await message.document.bot.download(file=document)
    wb: Workbook = openpyxl.load_workbook(filename=file_bytes)

    # only first sheet
    sheet: Worksheet = wb.worksheets[0]
    # without header row
    min_row: int = 2
    result: dict[str, list[tuple[str, str]]] = {
        'data': [row for row in sheet.iter_rows(values_only=True, min_row=min_row) if all(row)],
    }

    vendor_codes = await get_vendor_codes()

    # fixme
    good_vendor_codes: list[str] = []
    good_makers: list[str] = []
    bad_vendor_codes: list[str] = []

    for maker, vendor_code in result['data']:
        if str(vendor_code) in vendor_codes:
            good_vendor_codes.append(str(vendor_code))
            good_makers.append(str(maker).lower())
        else:
            bad_vendor_codes.append(vendor_code)

    if bad_vendor_codes:
        # fixme text
        await message.answer(text=f'{bad_vendor_codes} not fount in global list')

    # fixme asyncio
    response: requests.Response = requests.post(
        url=RUN_ALL_PAIR_DATA_URL,
        json={
            'vendor_codes': good_vendor_codes,
            'makers': good_makers,
            # fixme
            'only_needful_vendor_code': False,
        },
    )

    if response.ok:
        response: list[str] = response.json()
    else:
        await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')
    if response:
        result_filepath: str = os.path.join(response[0])
        document: FSInputFile = FSInputFile(path=result_filepath)

        await message.answer_document(document=document, caption='Результат выполнения запроса')
    else:
        await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')


# fixme name, unused???
@router.message(F.text.split(',').len() == 2)
async def get_weather_forecast(message: Message):
    vendor_codes = await get_vendor_codes()

    maker, vendor_code = message.text.split(',')

    if vendor_code in vendor_codes:
        data: dict[str, t.Any] = {
            'vendor_code': vendor_code,
            'maker': maker,
            # fixme True or False hz? need help
            'only_needful_vendor_code': True,
        }

        # fixme asyncio
        response: requests.Response = requests.post(
            url=RUN_URL,
            json=data,
        )

        if response.ok:
            response: list[str] = response.json()
        else:
            await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')
        if response:
            result_filepath: str = os.path.join(response[0])
            document: FSInputFile = FSInputFile(path=result_filepath)

            await message.answer_document(document=document, caption='Результат выполнения запроса')
        else:
            await message.answer(text='Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку')
    else:
        await message.answer(text=VENDOR_CODE_NOT_EXISTS_IN_LIST_VENDOR_CODES)
