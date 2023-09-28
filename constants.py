from aiogram.types import FSInputFile
from settings import FILEPATH_EXAMPLE_VENDOR_CODES

PARAMS: dict[int, list[str]] = {}

BASE_TEXT: str = (
    'Выбери одно из действий или '
    'напиши номер артикула(например, VKD35002), его пробьют по всем доступным парсерам'
)

EXAMPLE_VENDOR_CODES: FSInputFile = FSInputFile(path=FILEPATH_EXAMPLE_VENDOR_CODES)

SIZE_MAIN_MENU_BUTTONS: int = 2
SIZE_RESULTS_BY_PARSER_MENU_BUTTONS: int = 2
SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS: int = 2
SIZE_LIST_VENDOR_CODES_MENU_BUTTONS: int = 2
SIZE_LIST_PARSERS_MENU_BUTTONS: int = 2
