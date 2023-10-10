import io
import os
import tempfile
import typing as t

import requests
from aiogram import F
from aiogram import Router
from aiogram.types import (
    KeyboardButton, Message,
    Document, BufferedInputFile,
    FSInputFile,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from constants import PARAMS, EXAMPLE_VENDOR_CODES
from markups import main_menu, results_by_parser_menu, list_vendor_codes_menu, main_menu_btn
from settings import SERVER_ADDRESS
from text_of_buttons import (
    GET_RESULTS_BY_VENDOR_CODE, GET_RESULTS_BY_ALL_VENDOR_CODES, NEEDFUL_VENDOR_CODE,
    VENDOR_CODE_WITH_REPLACEMENTS, LIST_VENDOR_CODES, GET_LIST_VENDOR_CODES_MESSAGE,
    GET_LIST_VENDOR_CODES_FILE, UPDATE_LIST_VENDOR_CODES,
)
from utils import get_text, add_history


router: Router = Router()


@router.message(F.text == LIST_VENDOR_CODES)
async def get_list_vendor_codes_menu(message: Message):
    # fixme delete Params
    add_history(user_id=message.from_user.id, data=message.text)

    text: str = get_text(message_text=message.text)
    await message.answer(text=text, reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True))


@router.message(F.text.regexp('^Пробить( [а-я]+ | )артику(л|лов)$'))
async def get_results_by_parser_menu(message: Message):
    # fixme delete Params
    add_history(user_id=message.from_user.id, data=message.text)

    text: str = get_text(message_text=message.text)
    await message.answer(text=text, reply_markup=results_by_parser_menu.as_markup(resize_keyboard=True))


@router.message(F.text == NEEDFUL_VENDOR_CODE)
async def get_list_parsers_menu(message: Message):
    # fixme delete Params
    add_history(user_id=message.from_user.id, data=message.text)

    if GET_RESULTS_BY_VENDOR_CODE in PARAMS[message.from_user.id]:
        # fixme
        SIZE: int = 3
        vendor_codes = await get_vendor_codes(message=message)

        if vendor_codes:
            builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
            _ = [builder.add(KeyboardButton(text=vendor_code)) for vendor_code in vendor_codes]
            builder.adjust(SIZE)
            builder.row(main_menu_btn)

            await message.answer(text='Выбери один из артикулов', reply_markup=builder.as_markup(resize_keyboard=True))

    elif GET_RESULTS_BY_ALL_VENDOR_CODES in PARAMS[message.from_user.id]:
        # fixme url, double
        response: requests.Response = requests.post(
            url=f'{SERVER_ADDRESS}/run_all',
            json={'only_needful_vendor_code': True},
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
        # fixme error
        pass


@router.message(F.text == VENDOR_CODE_WITH_REPLACEMENTS)
async def get_list_parsers_menu(message: Message):
    # fixme delete Params
    add_history(user_id=message.from_user.id, data=message.text)

    if GET_RESULTS_BY_VENDOR_CODE in PARAMS[message.from_user.id]:
        # fixme
        SIZE: int = 3
        vendor_codes = await get_vendor_codes(message=message)

        if vendor_codes:
            builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
            _ = [builder.add(KeyboardButton(text=vendor_code)) for vendor_code in vendor_codes]
            builder.adjust(SIZE)
            builder.row(main_menu_btn)

            await message.answer(text='Выбери один из артикулов', reply_markup=builder.as_markup(resize_keyboard=True))

    elif GET_RESULTS_BY_ALL_VENDOR_CODES in PARAMS[message.from_user.id]:
        # fixme url, double
        response: requests.Response = requests.post(
            url=f'{SERVER_ADDRESS}/run_all',
            json={'only_needful_vendor_code': False},
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
        # fixme error
        await message.answer(text='Повтори запрос', reply_markup=main_menu.as_markup(resize_keyboard=True))


@router.message(F.text == GET_LIST_VENDOR_CODES_MESSAGE)
async def get_list_parsers_menu(message: Message):
    vendor_codes = await get_vendor_codes(message=message)

    text: str = '\n'.join(vendor_codes)
    if text:
        await message.answer(text=text, reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True))
#     fixme else


@router.message(F.text == GET_LIST_VENDOR_CODES_FILE)
async def get_list_parsers_menu(message: Message):
    vendor_codes = await get_vendor_codes(message=message)

    text: str = '\n'.join(vendor_codes)
    if text:
        with tempfile.TemporaryFile() as f:
            f.write(bytes(text, encoding='cp1251'))
            f.seek(0)
            vendor_codes_list: BufferedInputFile = BufferedInputFile(file=f.read(), filename=f'{LIST_VENDOR_CODES}.txt')

            await message.answer_document(document=vendor_codes_list)
#     fixme else


async def get_vendor_codes(message: Message) -> list[str]:
    # fixme url
    vendor_codes: list[str] = requests.get(url=f'{SERVER_ADDRESS}/vendor_codes').json()

    if not vendor_codes:
        await message.answer(
            text=f'{LIST_VENDOR_CODES} пуст',
            reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
        )
        vendor_codes: list[str] = []

    return vendor_codes


@router.message(F.document)
async def get_list_parsers_menu_(message: Message):
    document: Document = message.document
    file_bytes: io.BytesIO = await message.document.bot.download(file=document)
    result: str = file_bytes.getvalue().decode()

    result: dict[str, list[str]] = {'data': [row.strip() for row in result.split('\n') if row]}

    # fixme url
    response: requests.Response = requests.post(
        url=f'{SERVER_ADDRESS}/vendor_codes',
        json=result,
    )

    if response.ok:
        await message.answer(
            text=f'{LIST_VENDOR_CODES} обновлён',
            reply_markup=list_vendor_codes_menu.as_markup(resize_keyboard=True),
        )
    else:
        # fixme error
        pass


@router.message(F.text == UPDATE_LIST_VENDOR_CODES)
async def get_list_parsers_menu(message: Message):
    text: str = 'Для обновления списка артикулов необходимо загрузить файл следующего формата'
    await message.answer_document(document=EXAMPLE_VENDOR_CODES, caption=text)


@router.message(F.text)
async def get_weather_forecast(message: Message):
    # fixme delete Params
    add_history(user_id=message.from_user.id, data=message.text)

    vendor_codes = await get_vendor_codes(message=message)
    if message.text in vendor_codes:
        data: dict[str, t.Any] = {
            'vendor_code': message.text,
            'only_needful_vendor_code': NEEDFUL_VENDOR_CODE in PARAMS[message.from_user.id],
        }

        # fixme url
        response: requests.Response = requests.post(
            url=f'{SERVER_ADDRESS}/run',
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
        await message.answer(text='Этого артикула нет в списке артикулов')
