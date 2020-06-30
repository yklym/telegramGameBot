from data.text.game import game_info_text, no_game_info_text
from data.text.warnings import warnings
from db.dbController import dbController
from loader import bot
from ..utils.game import update_main_message


# function=isGroup
@bot.message_handler(commands=['game_create'])
def create_game(message):
    if message.db_user.curr_game:
        bot.reply_to(message, warnings["cant_create_game"])
        return
    # notify_admin_chat(bot, f"User @{message.from_user.username} created new game")
    game_main_message = bot.send_message(message.chat.id, f"Creating game ...")
    new_game = dbController.create_game(message.db_user, message.chat.id, game_main_message.message_id)
    update_main_message(bot, new_game)


@bot.message_handler(commands=['game_info'])
def game_info(message):
    game = message.db_user.curr_game
    if not game:
        bot.reply_to(message, no_game_info_text())
        return
    bot.send_message(message.chat.id, game_info_text(game), parse_mode="HTML")


@bot.message_handler(commands=['game_start'])
def start_game(message):
    game = message.db_user.creator_to
    if not message.db_user.creator_to:
        bot.reply_to(message, warnings["no_game_created"])
        return

    if not game.state == "lobby":
        bot.reply_to(message, warnings["game_started_already"])
        return
    # notify_admin_chat(bot, f"User @{message.from_user.username} created new game")


    dbController.init_game()
    update_main_message(bot, new_game)
