import requests

from data.config import cat_api_url
from data.text.default_commands import chat_info_text
from ..utils.commands import update_rules_message
from loader import bot


@bot.message_handler(commands=['chat_info'])
def chat_info(message):
    bot.reply_to(message, chat_info_text(message))


@bot.message_handler(commands=['cat'])
def get_random_cat(message):
    response = requests.get(cat_api_url)
    bot.send_photo(message.chat.id, response.json()[0]["url"])

@bot.message_handler(commands=['rules'])
def show_rules(message):
    rules_message = bot.send_message(message.chat.id, "Init rules")
    update_rules_message(0,'right',bot, message.chat.id, rules_message.message_id)
