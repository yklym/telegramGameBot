import json

import telebot
from telebot.apihelper import _make_request as make_request

from data.commands_list import commands_list
from data.config import BOT_TOKEN

telebot.apihelper.ENABLE_MIDDLEWARE = True

# Set bot's commands
make_request(BOT_TOKEN, r'setMyCommands', params={'commands': json.dumps(commands_list)}, method='post')
bot = telebot.TeleBot(BOT_TOKEN)
