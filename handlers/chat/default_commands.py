from db.dbController import dbController
from handlers.utils.admin_notify import notify_admin_chat
from loader import bot
from ..utils.filters import isGroup


@bot.message_handler(func=isGroup, commands=['start'])
def start(message):
    if not message.db_user:
        dbController.add_user(message.from_user)
        notify_admin_chat(bot, f"User @{message.from_user.username} was added to the db")

    bot.reply_to(message,
                 f'Hello, {message.from_user.first_name}\n'
                 f'Your id: {message.from_user.id}\n'
                 f'Chat type: {message.chat.type}\n'
                 f'Chat id: {message.chat.id}\n'
                 f'This is template for group or supergroup')
