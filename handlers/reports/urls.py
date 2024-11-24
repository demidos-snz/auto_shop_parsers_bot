from settings import SERVER_ADDRESS

LATEST_REPORTS_URL: str = f'{SERVER_ADDRESS}/api/file'
RUN_REPORT_TASK_URL: str = f'{SERVER_ADDRESS}/api/run_parser_task'
ZIP_FILEPATH_LATEST_REPORTS_URL: str = f'{SERVER_ADDRESS}/api/zip_latest_reports'
ZIP_FILEPATH_ALL_REPORTS_URL: str = f'{SERVER_ADDRESS}/api/zip_all_reports'
FILEPATH_REPORT_URL: str = f'{SERVER_ADDRESS}/api/filepath_report'
