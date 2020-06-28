import requests

from data.config import cat_api_url
from data.text.command import chat_info_text
from loader import bot


@bot.message_handler(commands=['chat_info'])
def chat_info(message):
    bot.reply_to(message, chat_info_text(message))


@bot.message_handler(commands=['cat'])
def get_random_cat(message):
    response = requests.get(cat_api_url)
    bot.send_photo(message.chat.id, response.json()[0]["url"])
