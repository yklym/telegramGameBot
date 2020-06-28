import requests

from data.config import cat_api_url
from data.text import command
from loader import bot


@bot.message_handler(commands=['chat_info'])
def get_id(message):
    bot.reply_to(message,
                 command["chat_info"].format(message.from_user.username, message.from_user.id, message.chat.type,
                                             message.chat.id))


@bot.message_handler(commands=['cat'])
def get_random_cat(message):
    response = requests.get(cat_api_url)
    bot.send_photo(message.chat.id, response.json()[0]["url"])
