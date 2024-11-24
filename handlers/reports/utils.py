import requests
from requests import Response

from handlers.reports.urls import LATEST_REPORTS_URL, RUN_REPORT_TASK_URL


async def get_latest_reports() -> Response:
    # fixme redis
    # fixme asyncio
    return requests.get(url=LATEST_REPORTS_URL)


async def run_report_task() -> Response:
    # fixme asyncio
    return requests.post(url=RUN_REPORT_TASK_URL)
