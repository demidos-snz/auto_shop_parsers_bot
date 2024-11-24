from aiogram.types import FSInputFile

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
EXAMPLE_VENDOR_CODES: FSInputFile = FSInputFile(path=FILEPATH_EXAMPLE_VENDOR_CODES)
# -----------------------------
