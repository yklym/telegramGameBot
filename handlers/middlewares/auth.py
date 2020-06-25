from data.commands_list import commands_str_list
from db.dbController import dbController
from loader import bot


@bot.middleware_handler(update_types=['message'])
def set_db_user(bot_instance, message):
    message.db_user = None
    if message.text and message.text in commands_str_list:
        message.db_user = dbController.get_user(message.from_user)
