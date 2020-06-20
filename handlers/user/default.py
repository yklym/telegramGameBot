from loader import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Hello, {message.from_user.first_name}\n'
                     f'Your id: {message.from_user.id}\n'
                     f'Chat type: {message.chat.type}\n'
                     f'Chat id: {message.chat.id}')
