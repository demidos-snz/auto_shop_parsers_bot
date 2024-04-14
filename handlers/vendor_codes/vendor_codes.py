import typing as t

from aiogram import F
from aiogram import Router
from aiogram.types import Message

from constants import VENDOR_CODE_NOT_EXISTS_IN_LIST_VENDOR_CODES
from handlers.urls import RUN_URL
from handlers.utils import get_vendor_codes
from handlers.vendor_codes.utils import send_file_or_error

router: Router = Router()


@router.message(F.text)
async def get_result_file(message: Message, url: str = RUN_URL, only_needful_vendor_code: bool = False):
    data: dict[str, t.Any] = {
        'vendor_code': message.text,
        'only_needful_vendor_code': only_needful_vendor_code,
    }

    vendor_codes = await get_vendor_codes()

    if message.text in vendor_codes:
        await send_file_or_error(message=message, url=url, data=data)
    else:
        await message.answer(text=VENDOR_CODE_NOT_EXISTS_IN_LIST_VENDOR_CODES)
