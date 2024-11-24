import typing as t

import requests
from aiogram.types import (
    KeyboardButton, Message,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from buttons.buttons import main_menu_btn
from constants.size_constants import SIZE_ROW_CUSTOM_MENU
from handlers.urls import GET_VENDOR_CODES_URL, PARSERS_URL, POST_VENDOR_CODE_URL, DELETE_VENDOR_CODE_URL


async def get_vendor_codes() -> list[str]:
    # fixme redis
    # fixme asyncio
    return requests.get(url=GET_VENDOR_CODES_URL).json()


async def create_vendor_code(data: dict[str, list[tuple[str, t.Any]]]) -> int:
    # fixme redis
    # fixme asyncio
    return requests.post(url=POST_VENDOR_CODE_URL, json=data).status_code


async def delete_vendor_code(id_vc: int) -> int:
    # fixme redis
    # fixme asyncio
    return requests.delete(url=DELETE_VENDOR_CODE_URL.format(id_vc)).status_code


async def get_parsers() -> list[str]:
    # fixme asyncio
    return requests.get(url=PARSERS_URL).json()


async def generate_custom_buttons_list(
        message: Message,
        list_objs: list[str],
        answer_text: str,
        size_row: int = SIZE_ROW_CUSTOM_MENU,
):
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    _ = [builder.add(KeyboardButton(text=i)) for i in list_objs]
    builder.adjust(size_row)
    builder.row(main_menu_btn)
    await message.answer(
        text=answer_text,
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
