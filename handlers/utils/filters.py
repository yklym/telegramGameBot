def isPrivateChat(message):
    return message.chat.type == "private"


def isGroup(message):
    return message.chat.type == "group" or message.chat.type == "supergroup"
