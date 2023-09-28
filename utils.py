from constants import BASE_TEXT, PARAMS


def get_text(message_text: str) -> str:
    return f'Страница "{message_text}"\n\n{BASE_TEXT}'


# fixme delete
def add_history(user_id: int, data: str):
    if user_id not in PARAMS:
        PARAMS[user_id] = []
    PARAMS[user_id].append(data)
