from constants import BASE_TEXT


def get_text(message_text: str) -> str:
    return f'Страница "{message_text}"\n\n{BASE_TEXT}'
