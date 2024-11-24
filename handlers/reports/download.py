from aiogram import F
from aiogram import Router
from aiogram.types import Message

from buttons.text_of_buttons import DOWNLOAD_ALL_REPORTS, DOWNLOAD_LATEST_REPORTS
from handlers.reports.urls import ZIP_FILEPATH_LATEST_REPORTS_URL, ZIP_FILEPATH_ALL_REPORTS_URL, FILEPATH_REPORT_URL
from handlers.vendor_codes.utils import send_file_or_error

router: Router = Router()


@router.message(F.text == DOWNLOAD_ALL_REPORTS)
# fixme name
async def get_result_file(message: Message):
    await send_file_or_error(
        message=message,
        url=ZIP_FILEPATH_ALL_REPORTS_URL,
    )


@router.message(F.text == DOWNLOAD_LATEST_REPORTS)
# fixme name
async def get_result_file(message: Message):
    await send_file_or_error(
        message=message,
        url=ZIP_FILEPATH_LATEST_REPORTS_URL,
    )


@router.message((F.text.len() == 23) & F.text.endswith('.csv'))
# fixme name, len == 2024-11-10 17:40:54.csv
async def get_result_file(message: Message):
    await send_file_or_error(
        message=message,
        url=FILEPATH_REPORT_URL,
        kwargs={'params': {'filename': message.text}},
    )
