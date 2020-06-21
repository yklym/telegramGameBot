import requests

from db.dbController import dbController
from handlers.utils.admin_notify import notify_admin_chat
from loader import bot
from data.config import cat_api_url

@bot.message_handler(commands=['chat_info'])
def get_id(message):
    print("Hello")
    if not dbController.get_user(message.from_user):
        dbController.add_user(message.from_user)
        notify_admin_chat(bot, f"User @{message.from_user.username} was added to the db")

    bot.reply_to(message,
                 f'Hello, {message.from_user.first_name}\n'
                 f'Your id: {message.from_user.id}\n'
                 f'Chat type: {message.chat.type}\n'
                 f'Chat id: {message.chat.id}\n'
                 f'This is template for private chat')


@bot.message_handler(commands=['cat'])
def get_random_cat(message):
    response = requests.get(cat_api_url)
    bot.send_photo(message.from_user.id, response.json()[0]["url"])
