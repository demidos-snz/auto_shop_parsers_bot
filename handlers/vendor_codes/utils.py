import os
import typing as t

import requests
from aiogram.types import (
    Message, FSInputFile,
)

from constants.constants import (
    ERROR_FILE_TEXT, SUCCESS_FILE_TEXT,
)


async def send_file_or_error(
        message: Message,
        url: str,
        kwargs: t.Optional[dict[str, dict[str, t.Any]]] = None,
        method: str = 'get',
):
    kwargs: dict[str, dict[str, t.Any]] = kwargs or {}
    result: t.Optional[FSInputFile] = await get_result_file(url=url, kwargs=kwargs, method=method)

    if result is None:
        await message.answer(text=ERROR_FILE_TEXT)
    else:
        await message.answer_document(document=result, caption=SUCCESS_FILE_TEXT)


async def get_result_file(url: str, kwargs: dict[str, dict[str, t.Any]], method: str) -> t.Optional[FSInputFile]:
    # fixme asyncio
    run_method: t.Optional[t.Callable] = getattr(requests, method, None)
    if run_method is None:
        return None
    else:
        response: requests.Response = run_method(
            url=url,
            **kwargs,
        )
        kwargs = {}

    response: list[str] = response.json() if response.ok else []

    if response:
        # fixme
        result_filepath: str = os.path.join(response[0]) if kwargs else response
        return FSInputFile(path=result_filepath)
    else:
        return None


async def validate_vendor_codes(vendor_codes: list[dict[str, t.Any]]) -> str:
    data: list[list[list[str, t.Any]]] | list = [set_of_vc.get('set_of_vendor_codes', []) for set_of_vc in vendor_codes]
    data: list[list[str, t.Any]] | list = data[0] if data else []
    text: str = '\n'.join([str(row[0]) for row in data])
    return text
