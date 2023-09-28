from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from constants import (
    SIZE_MAIN_MENU_BUTTONS, SIZE_RESULTS_BY_PARSER_MENU_BUTTONS,
    SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS, SIZE_LIST_VENDOR_CODES_MENU_BUTTONS,
    SIZE_LIST_PARSERS_MENU_BUTTONS,
)
from text_of_buttons import (
    MAIN_MENU, GET_RESULTS_BY_VENDOR_CODE, GET_RESULTS_BY_ALL_VENDOR_CODES,
    GET_RESULTS_BY_PARSER, GET_RESULTS_BY_ALL_PARSERS, LIST_VENDOR_CODES,
    GET_LIST_VENDOR_CODES_MESSAGE, GET_LIST_VENDOR_CODES_FILE, UPDATE_LIST_VENDOR_CODES,
    LIST_PARSERS, NEEDFUL_VENDOR_CODE, VENDOR_CODE_WITH_REPLACEMENTS,
    GET_LIST_PARSERS, UPDATE_LIST_PARSERS,
)


main_menu_btn: KeyboardButton = KeyboardButton(text=MAIN_MENU)


get_results_by_vendor_code_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_VENDOR_CODE)
get_results_by_all_vendor_codes_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_ALL_VENDOR_CODES)

get_results_by_parser_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_PARSER)
get_results_by_all_parsers_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_ALL_PARSERS)

needful_vendor_code_btn: KeyboardButton = KeyboardButton(text=NEEDFUL_VENDOR_CODE)
vendor_code_with_replacements_btn: KeyboardButton = KeyboardButton(text=VENDOR_CODE_WITH_REPLACEMENTS)

list_vendor_codes_btn: KeyboardButton = KeyboardButton(text=LIST_VENDOR_CODES)

get_list_vendor_codes_msg_btn: KeyboardButton = KeyboardButton(text=GET_LIST_VENDOR_CODES_MESSAGE)
get_list_vendor_codes_file_btn: KeyboardButton = KeyboardButton(text=GET_LIST_VENDOR_CODES_FILE)
update_list_vendor_codes_btn: KeyboardButton = KeyboardButton(text=UPDATE_LIST_VENDOR_CODES)


list_parsers_btn: KeyboardButton = KeyboardButton(text=LIST_PARSERS)

get_list_parsers_btn: KeyboardButton = KeyboardButton(text=GET_LIST_PARSERS)
update_list_parsers_btn: KeyboardButton = KeyboardButton(text=UPDATE_LIST_PARSERS)


main_menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
main_menu_buttons: list[KeyboardButton] = [
    get_results_by_vendor_code_btn,
    get_results_by_all_vendor_codes_btn,
    list_vendor_codes_btn,
    list_parsers_btn,
]
_ = [main_menu.add(btn) for btn in main_menu_buttons]
main_menu.adjust(SIZE_MAIN_MENU_BUTTONS)


results_by_parser_menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
results_by_parser_menu_buttons: list[KeyboardButton] = [
    get_results_by_parser_btn,
    get_results_by_all_parsers_btn,
]
_ = [results_by_parser_menu.add(btn) for btn in results_by_parser_menu_buttons]
results_by_parser_menu.adjust(SIZE_RESULTS_BY_PARSER_MENU_BUTTONS)
results_by_parser_menu.row(main_menu_btn)


needful_or_replacements_menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
needful_or_replacements_menu_buttons: list[KeyboardButton] = [
    needful_vendor_code_btn,
    vendor_code_with_replacements_btn,
]
_ = [needful_or_replacements_menu.add(btn) for btn in needful_or_replacements_menu_buttons]
needful_or_replacements_menu.adjust(SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS)
needful_or_replacements_menu.row(main_menu_btn)


list_vendor_codes_menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
list_vendor_codes_menu_buttons: list[KeyboardButton] = [
    get_list_vendor_codes_msg_btn,
    get_list_vendor_codes_file_btn,
    update_list_vendor_codes_btn,
]
_ = [list_vendor_codes_menu.add(btn) for btn in list_vendor_codes_menu_buttons]
list_vendor_codes_menu.adjust(SIZE_LIST_VENDOR_CODES_MENU_BUTTONS)
list_vendor_codes_menu.row(main_menu_btn)


list_parsers_menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
list_parsers_menu_buttons: list[KeyboardButton] = [
    get_list_parsers_btn,
    update_list_parsers_btn,
]
_ = [list_parsers_menu.add(btn) for btn in list_parsers_menu_buttons]
list_parsers_menu.adjust(SIZE_LIST_PARSERS_MENU_BUTTONS)
list_parsers_menu.row(main_menu_btn)
