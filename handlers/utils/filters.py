def is_private_chat(message):
    return message.chat.type == "private"


def is_group(message):
    return message.chat.type == "group" or message.chat.type == "supergroup"


def is_authorized(message):
    return message.db_user
