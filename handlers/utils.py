import requests

from handlers.urls import VENDOR_CODES_URL, PARSERS_URL


async def get_vendor_codes() -> list[str]:
    # fixme redis
    # fixme asyncio
    return requests.get(url=VENDOR_CODES_URL).json()


async def get_parsers() -> list[str]:
    # fixme asyncio
    return requests.get(url=PARSERS_URL).json()
