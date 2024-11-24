from aiogram.utils.keyboard import ReplyKeyboardBuilder

from buttons.buttons import *
from constants.size_constants import *
from markups.utils import generate_markup

main_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        vendor_codes_btn,
        # parsers_btn,
        reports_btn,
        # KeyboardButton(text='test_btn'),
    ],
    size=SIZE_MAIN_MENU_BUTTONS,
    add_mm_btn=False,
)


# results_by_vendor_codes_menu: ReplyKeyboardBuilder = generate_markup(
#     buttons=[
#         get_results_by_vendor_code_btn,
#         get_results_by_all_vendor_codes_btn,
#         list_vendor_codes_btn,
#     ],
#     size=SIZE_RESULTS_BY_VENDOR_CODES_BUTTONS,
# )


# results_by_parsers_menu: ReplyKeyboardBuilder = generate_markup(
#     buttons=[
#         get_results_by_parser_btn,
#         get_results_by_all_parsers_btn
#     ],
#     size=SIZE_RESULTS_BY_PARSER_MENU_BUTTONS,
# )


# needful_or_replacements_vendor_code_menu: ReplyKeyboardBuilder = generate_markup(
#     buttons=[
#         needful_vendor_code_btn,
#         vendor_code_with_replacements_btn,
#     ],
#     size=SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS,
# )


# needful_or_replacements_vendor_codes_menu: ReplyKeyboardBuilder = generate_markup(
#     buttons=[
#         needful_vendor_codes_btn,
#         vendor_codes_with_replacements_btn,
#     ],
#     size=SIZE_NEEDFUL_OR_REPLACEMENTS_MENU_BUTTONS,
# )


list_vendor_codes_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        get_list_vendor_codes_msg_btn,
        get_list_vendor_codes_file_btn,
        update_list_vendor_codes_btn,
    ],
    size=SIZE_LIST_VENDOR_CODES_MENU_BUTTONS,
)


# list_parsers_menu: ReplyKeyboardBuilder = generate_markup(
#     buttons=[
#         get_parsers_btn,
#         update_parsers_btn,
#     ],
#     size=SIZE_LIST_PARSERS_MENU_BUTTONS,
# )


reports_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        download_reports_btn,
        get_reports_btn,
        run_parser_btn,
    ],
    size=SIZE_REPORTS_MENU,
)


download_reports_menu: ReplyKeyboardBuilder = generate_markup(
    buttons=[
        download_all_reports_btn,
        download_latest_reports_btn,
    ],
    size=SIZE_DOWNLOAD_REPORTS_MENU,
)
