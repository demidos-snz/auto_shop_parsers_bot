from aiogram.types import FSInputFile

from buttons.text_of_buttons import LIST_VENDOR_CODES
from settings import FILEPATH_EXAMPLE_VENDOR_CODES

BASE_TEXT: str = (
    'Выбери одно из действий или '
    'напиши номер артикула(например, VKD35002), '
    'его пробьют по всем доступным парсерам'
)
WELCOME_TEXT: str = 'Привет, {}!'
# -----------------------------
IN_DEVELOPING: str = 'В разработке...'
PARSES_LIST_IS_EMPTY: str = 'Список парсеров пуст'
# -----------------------------
VENDOR_CODE_NOT_EXISTS_IN_LIST_VENDOR_CODES: str = 'Этого артикула нет в списке артикулов'
# -----------------------------
CHOOSE_ONE_OF_VENDOR_CODES: str = 'Выбери один из артикулов'
ERROR_VENDOR_CODES_TEXT: str = 'Не удалось получить список артикулов, просьба написать в поддержку'
# -----------------------------
ERROR_FILE_TEXT: str = 'Файл не сформировался, наверное произошла ошибка, просьба написать в поддержку'
SUCCESS_FILE_TEXT: str = 'Результат выполнения запроса'
# -----------------------------
LIST_VENDOR_CODES_IS_EMPTY_TEXT: str = f'{LIST_VENDOR_CODES} пуст'
LIST_VENDOR_CODES_FILENAME: str = f'{LIST_VENDOR_CODES}.txt'
LIST_VENDOR_CODES_UPDATED_TEXT: str = f'{LIST_VENDOR_CODES} обновлён'
ERROR_UPDATE_LIST_VENDOR_CODES_TEXT: str = 'Не удалось обновить список артикулов, просьба написать в поддержку'
UPDATE_LIST_VENDOR_CODES_TEXT: str = 'Для обновления списка артикулов необходимо загрузить файл следующего формата'
ERROR_OF_ANOTHER_DOCUMENT_TYPE: str = 'Данный тип файла не поддерживается'
# -----------------------------
EXAMPLE_VENDOR_CODES: FSInputFile = FSInputFile(path=FILEPATH_EXAMPLE_VENDOR_CODES)
# -----------------------------
SIZE_MAIN_MENU_BUTTONS: int = 2
SIZE_RESULTS_BY_VENDOR_CODES_BUTTONS: int = 2
SIZE_RESULTS_BY_PARSER_MENU_BUTTONS: int = 2
SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS: int = 2
SIZE_LIST_VENDOR_CODES_MENU_BUTTONS: int = 2
SIZE_LIST_PARSERS_MENU_BUTTONS: int = 2
SIZE_LIST_VENDOR_CODES_MENU: int = 3
# -----------------------------
SIZE_REPORTS_MENU: int = 3
# -----------------------------
SIZE_DOWNLOAD_REPORTS_MENU: int = 2
# -----------------------------
