from aiogram import F
from aiogram import Router
from aiogram.types import Message

from buttons.text_of_buttons import REPORTS, DOWNLOAD_REPORTS, GET_REPORTS, RUN_TASK_REPORT
from constants.reports_constants import ERROR_LATEST_REPORTS
from handlers.reports.utils import get_latest_reports, run_report_task
from handlers.utils import generate_custom_buttons_list
from markups.markups import reports_menu, download_reports_menu

router: Router = Router()


@router.message(F.text == REPORTS)
# fixme name
async def get_result_file(message: Message):
    await message.answer(
        text=f'Страница "{message.text}"',
        reply_markup=reports_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == DOWNLOAD_REPORTS)
# fixme name
async def get_result_file(message: Message):
    await message.answer(
        text=f'Страница "{message.text}"',
        reply_markup=download_reports_menu.as_markup(resize_keyboard=True),
    )


@router.message(F.text == GET_REPORTS)
# fixme name
async def needful_vendor_code(message: Message):
    response = await get_latest_reports()

    if response.ok:
        await generate_custom_buttons_list(
            message=message,
            list_objs=response.json(),
            answer_text=f'Страница "{message.text}"',
        )

    else:
        await message.answer(text=ERROR_LATEST_REPORTS)


@router.message(F.text == RUN_TASK_REPORT)
# fixme name
async def needful_vendor_code(message: Message):
    response = await run_report_task()

    if response.ok:
        await message.answer(
            text=response.json(),
            reply_markup=reports_menu.as_markup(resize_keyboard=True),
        )

    else:
        await message.answer(text=ERROR_LATEST_REPORTS)
