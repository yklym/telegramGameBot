import json

import telebot

from data.commands_list import commands_list
from data.config import BOT_TOKEN
from telebot.apihelper import _make_request as make_request
bot = telebot.TeleBot(BOT_TOKEN)



# Set bot's commands
make_request(BOT_TOKEN, r'setMyCommands', params={'commands': json.dumps(commands_list)}, method='post')
