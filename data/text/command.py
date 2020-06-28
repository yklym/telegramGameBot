def chat_info_text(message):
    return ('Hello, {m.from_user.first_name}\n'
            'Your id: {m.from_user.id}\n'
            'Chat type: {m.chat.type}\n'
            'Chat id: {m.chat.id}\n').format(m=message)
