from aiogram.types import KeyboardButton

from buttons.text_of_buttons import *

main_menu_btn: KeyboardButton = KeyboardButton(text=MAIN_MENU)
# -----------------------------
vendor_codes_btn: KeyboardButton = KeyboardButton(text=VENDOR_CODES)
# parsers_btn: KeyboardButton = KeyboardButton(text=PARSERS)
reports_btn: KeyboardButton = KeyboardButton(text=REPORTS)
# -----------------------------
# get_results_by_vendor_code_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_VENDOR_CODE)
# get_results_by_all_vendor_codes_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_ALL_VENDOR_CODES)
# list_vendor_codes_btn: KeyboardButton = KeyboardButton(text=LIST_VENDOR_CODES)
# -----------------------------
# get_results_by_parser_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_PARSER)
# get_results_by_all_parsers_btn: KeyboardButton = KeyboardButton(text=GET_RESULTS_BY_ALL_PARSERS)
# -----------------------------
# needful_vendor_code_btn: KeyboardButton = KeyboardButton(text=NEEDFUL_VENDOR_CODE)
# vendor_code_with_replacements_btn: KeyboardButton = KeyboardButton(text=VENDOR_CODE_WITH_REPLACEMENTS)
# -----------------------------
# needful_vendor_codes_btn: KeyboardButton = KeyboardButton(text=NEEDFUL_VENDOR_CODES)
# vendor_codes_with_replacements_btn: KeyboardButton = KeyboardButton(text=VENDOR_CODES_WITH_REPLACEMENTS)
# -----------------------------
get_list_vendor_codes_msg_btn: KeyboardButton = KeyboardButton(text=GET_LIST_VENDOR_CODES_MESSAGE)
get_list_vendor_codes_file_btn: KeyboardButton = KeyboardButton(text=GET_LIST_VENDOR_CODES_FILE)
update_list_vendor_codes_btn: KeyboardButton = KeyboardButton(text=UPDATE_LIST_VENDOR_CODES)
# -----------------------------
# get_parsers_btn: KeyboardButton = KeyboardButton(text=GET_PARSERS)
# update_parsers_btn: KeyboardButton = KeyboardButton(text=UPDATE_PARSERS)
# -----------------------------
download_reports_btn: KeyboardButton = KeyboardButton(text=DOWNLOAD_REPORTS)
get_reports_btn: KeyboardButton = KeyboardButton(text=GET_REPORTS)
run_parser_btn: KeyboardButton = KeyboardButton(text=RUN_TASK_REPORT)
# -----------------------------
download_all_reports_btn: KeyboardButton = KeyboardButton(text=DOWNLOAD_ALL_REPORTS)
download_latest_reports_btn: KeyboardButton = KeyboardButton(text=DOWNLOAD_LATEST_REPORTS)
# -----------------------------
