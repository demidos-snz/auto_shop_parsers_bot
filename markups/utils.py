from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from buttons.buttons import main_menu_btn


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
