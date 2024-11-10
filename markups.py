from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from buttons.buttons import (
    main_menu_btn, vendor_codes_btn, parsers_btn,
    get_results_by_vendor_code_btn, get_results_by_all_vendor_codes_btn, list_vendor_codes_btn,
    get_results_by_parser_btn, get_results_by_all_parsers_btn, needful_vendor_code_btn,
    vendor_code_with_replacements_btn, get_list_vendor_codes_msg_btn, get_list_vendor_codes_file_btn,
    update_list_vendor_codes_btn, get_parsers_btn, update_parsers_btn,
    needful_vendor_codes_btn, vendor_codes_with_replacements_btn,
)
from constants.constants import (
    SIZE_MAIN_MENU_BUTTONS, SIZE_RESULTS_BY_PARSER_MENU_BUTTONS,
    SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS, SIZE_LIST_VENDOR_CODES_MENU_BUTTONS,
    SIZE_LIST_PARSERS_MENU_BUTTONS, SIZE_RESULTS_BY_VENDOR_CODES_BUTTONS,
)


def generate_markup(
        buttons: list[KeyboardButton],
        size: int,
        add_mm_btn: bool = True,
) -> ReplyKeyboardBuilder:
    menu: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    _ = [menu.add(btn) for btn in buttons]
    menu.adjust(size)
    if add_mm_btn:
        menu.row(main_menu_btn)
    return menu


main_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        vendor_codes_btn,
        parsers_btn,
    ],
    size=SIZE_MAIN_MENU_BUTTONS,
    add_mm_btn=False,
)


results_by_vendor_codes_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        get_results_by_vendor_code_btn,
        get_results_by_all_vendor_codes_btn,
        list_vendor_codes_btn,
    ],
    size=SIZE_RESULTS_BY_VENDOR_CODES_BUTTONS,
)


results_by_parsers_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        get_results_by_parser_btn,
        get_results_by_all_parsers_btn
    ],
    size=SIZE_RESULTS_BY_PARSER_MENU_BUTTONS,
)


needful_or_replacements_vendor_code_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        needful_vendor_code_btn,
        vendor_code_with_replacements_btn,
    ],
    size=SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS,
)


needful_or_replacements_vendor_codes_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        needful_vendor_codes_btn,
        vendor_codes_with_replacements_btn,
    ],
    size=SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS,
)


list_vendor_codes_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        get_list_vendor_codes_msg_btn,
        get_list_vendor_codes_file_btn,
        update_list_vendor_codes_btn,
    ],
    size=SIZE_LIST_VENDOR_CODES_MENU_BUTTONS,
)


list_parsers_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        get_parsers_btn,
        update_parsers_btn,
    ],
    size=SIZE_LIST_PARSERS_MENU_BUTTONS,
)
