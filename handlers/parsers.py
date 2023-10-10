import requests
from aiogram import F
from aiogram import Router
from aiogram.types import Message

from markups import list_parsers_menu, needful_or_replacements_menu
from settings import SERVER_ADDRESS
from text_of_buttons import GET_RESULTS_BY_PARSER, GET_RESULTS_BY_ALL_PARSERS, LIST_PARSERS, GET_LIST_PARSERS, \
    UPDATE_LIST_PARSERS
from utils import get_text, add_history


router: Router = Router()


@router.message(F.text == LIST_PARSERS)
async def get_list_parsers_menu(message: Message):
    # fixme delete Params
    add_history(user_id=message.from_user.id, data=message.text)

    text: str = get_text(message_text=message.text)
    await message.answer(text=text, reply_markup=list_parsers_menu.as_markup(resize_keyboard=True))


@router.message(F.text == GET_RESULTS_BY_PARSER)
async def get_list_parsers_menu(message: Message):
    # fixme В разработке...
    text: str = 'В разработке...'
    await message.answer(text=text)


@router.message(F.text == GET_RESULTS_BY_ALL_PARSERS)
async def get_list_parsers_menu(message: Message):
    text: str = get_text(message_text=message.text)
    await message.answer(text=text, reply_markup=needful_or_replacements_menu.as_markup(resize_keyboard=True))


@router.message(F.text == GET_LIST_PARSERS)
async def get_list_parsers_menu(message: Message):
    parsers = await get_parsers()
    text: str = '\n'.join(parsers)
    if text:
        await message.answer(text=text, reply_markup=list_parsers_menu.as_markup(resize_keyboard=True))
    else:
        await message.answer(text='Список parsers пуст', reply_markup=list_parsers_menu.as_markup(resize_keyboard=True))


async def get_parsers() -> list[str]:
    # fixme url
    return requests.get(url=f'{SERVER_ADDRESS}/parsers').json()


@router.message(F.text == UPDATE_LIST_PARSERS)
async def get_list_parsers_menu(message: Message):
    # fixme В разработке...
    text: str = 'В разработке...'
    await message.answer(text=text)
