import os
import typing as t

import requests
from aiogram.types import (
    Message, FSInputFile,
)

from constants.constants import (
    ERROR_FILE_TEXT, SUCCESS_FILE_TEXT,
)


async def send_file_or_error(message: Message, url: str, data: dict[str, t.Any]):
    result: t.Optional[FSInputFile] = await result_file(url=url, data=data)

    if result is None:
        await message.answer(text=ERROR_FILE_TEXT)
    else:
        await message.answer_document(document=result, caption=SUCCESS_FILE_TEXT)


async def result_file(url: str, data: dict[str, t.Any]) -> t.Optional[FSInputFile]:
    # fixme asyncio
    response: requests.Response = requests.post(
        url=url,
        json=data,
    )

    response: list[str] = response.json() if response.ok else []

    if response:
        result_filepath: str = os.path.join(response[0])
        return FSInputFile(path=result_filepath)
    else:
        return None
