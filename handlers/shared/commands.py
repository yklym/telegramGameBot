import requests

from data.config import cat_api_url
from loader import bot


@bot.message_handler(commands=['chat_info'])
def get_id(message):
    bot.reply_to(message,
                 f'Hello, {message.from_user.first_name}\n'
                 f'Your id: {message.from_user.id}\n'
                 f'Chat type: {message.chat.type}\n'
                 f'Chat id: {message.chat.id}\n'
                 f'This is template for private chat')


@bot.message_handler(commands=['cat'])
def get_random_cat(message):
    response = requests.get(cat_api_url)
    bot.send_photo(message.chat.id, response.json()[0]["url"])
